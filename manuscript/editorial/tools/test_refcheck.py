#!/usr/bin/env python3
"""Regression checks for the manuscript's source-closure gate."""
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

CHECKER = Path(__file__).with_name('refcheck.py')


class ReferenceGateTests(unittest.TestCase):
    def check(self, files):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            for name, text in files.items():
                target = root / name
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_text(text, encoding='utf-8')
            return subprocess.run(
                [sys.executable, str(CHECKER)], cwd=root,
                capture_output=True, text=True, check=False,
            )

    def test_missing_input_fails_even_without_references(self):
        result = self.check({'book.tex': r'\input{missing}'})
        self.assertEqual(result.returncode, 1)
        self.assertIn('MISSING book.tex -> missing', result.stdout)

    def test_missing_root_fails(self):
        result = self.check({})
        self.assertEqual(result.returncode, 1)
        self.assertIn('MISSING <root> -> book.tex', result.stdout)

    def test_lowercase_multireference_is_checked(self):
        result = self.check({'book.tex': r'\label{ok}\cref{ok,missing}'})
        self.assertEqual(result.returncode, 1)
        self.assertIn("['missing']", result.stdout)

    def test_nested_includes_comments_and_escaped_percent(self):
        result = self.check({
            'book.tex': '\\draftinclude{chapter}\n% \\input{missing}\n'
                        '\\label{ok}\\cref{ok, nested}\\Cref*{nested}\n',
            'chapter.tex': '\\input{parts/nested.tex}\n'
                           '\\% visible percent % \\label{ok}\n',
            'parts/nested.tex': '\\label{nested}\n% \\begin{proof}\n',
        })
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn('files in build closure: 3', result.stdout)

    def test_duplicate_labels_fail(self):
        result = self.check({'book.tex': r'\label{same}\label{same}'})
        self.assertEqual(result.returncode, 1)
        self.assertIn('multiply defined:      1', result.stdout)

    def test_unbalanced_environment_fails(self):
        result = self.check({'book.tex': r'\begin{proof}'})
        self.assertEqual(result.returncode, 1)
        self.assertIn("'proof': 1", result.stdout)


if __name__ == '__main__':
    unittest.main()
