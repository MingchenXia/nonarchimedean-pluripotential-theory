#!/bin/zsh
set -eu

record_dir=$(cd "$(dirname "$0")" && pwd)
candidate_dir="$record_dir/../../solver_dossiers_20260901/p148_zero_mass_reconstruction_candidate_v2_20260901"
chapter_file="$record_dir/../../../parts/part5/ch51_complex_prerequisites.tex"

cd "$candidate_dir"
shasum -a 256 -c SHA256SUMS

test "$(shasum -a 256 ../p148_zero_mass_reconstruction_triage_20260901/PROPOSED_STATEMENT.tex | awk '{print $1}')" = \
  d4324b026beef06f5314ddd43c7dda6e921c622fe700ce718db76341e3989bc4
test "$(shasum -a 256 ../p148_zero_mass_reconstruction_triage_20260901/PROOF.tex | awk '{print $1}')" = \
  6e7d264863efe29ca7b589ddc7c1a30ab9337a8f113b8bed2fd081958786c897
test "$(shasum -a 256 ../p148_zero_mass_reconstruction_triage_hostile_audit_20260901/AUDIT.md | awk '{print $1}')" = \
  cba92db90daa448a667a27111fe133fe86791732d28687b285d777242531db48
test "$(shasum -a 256 ../p148_zero_mass_reconstruction_triage_hostile_audit_20260901/MINIMAL_REPAIRS.md | awk '{print $1}')" = \
  40dd2c743d4359bf32ffe0ca3f140b28360ea9a622c69c19e95f76aad6e41066

cmp -s LIVE_I_PROJECTION_EXACT.tex <(sed -n '3291,3339p' "$chapter_file")
cmp -s LIVE_P1_CANTOR_CONSTRUCTION_EXACT.tex <(sed -n '3758,3880p' "$chapter_file")
cmp -s LIVE_P1_ZERO_MASS_FAMILY_EXACT.tex <(sed -n '3949,3968p' "$chapter_file")
cmp -s LIVE_I_PROJECTION_EXACT.tex \
  "$record_dir/../../rethlas_packets_20260824/ch55_xia8_8_premise_i_projection_exact.tex"

cmp -s V1_TO_V2.patch <(
  diff -u --label v1/PROPOSED_STATEMENT.tex --label v2/PROPOSED_STATEMENT.tex \
    ../p148_zero_mass_reconstruction_triage_20260901/PROPOSED_STATEMENT.tex \
    PROPOSED_STATEMENT.tex || true
  diff -u --label v1/PROOF.tex --label v2/PROOF.tex \
    ../p148_zero_mass_reconstruction_triage_20260901/PROOF.tex \
    PROOF.tex || true
)

rg -Fq 'it charges no' PROOF.tex
rg -Fq 'pluripolar set.' PROOF.tex
rg -q '\\one_\{X\\setminus F\}' PROOF.tex
rg -q 'Any different reconstruction problem must first' PROPOSED_STATEMENT.tex
rg -q 'smooth projective variety' PROPOSED_STATEMENT.tex
rg -Fq "pseudoeffective real N\\'eron--Severi class" PROPOSED_STATEMENT.tex
rg -Fq '\mathbf Q\)-line-bundle class' PROPOSED_STATEMENT.tex

if rg -n 'no remaining third interpretation|Full realized DXZ/Boucksom--Jonsson objects already' PROPOSED_STATEMENT.tex; then
  print -u2 'rejected scope language found'
  exit 1
fi
if rg -n '\\begin\{(theorem|lemma|proposition|corollary)\}\[' PROPOSED_STATEMENT.tex PROOF.tex main.tex; then
  print -u2 'optional theorem name found'
  exit 1
fi
if rg -ni 'exercise|acknowledg' PROPOSED_STATEMENT.tex PROOF.tex main.tex; then
  print -u2 'forbidden exercise or acknowledgments text found'
  exit 1
fi
if rg -n '\\ref\{' PROPOSED_STATEMENT.tex PROOF.tex main.tex; then
  print -u2 'raw ref command found'
  exit 1
fi
rg -q '^\\author\{\}$' main.tex
rg -q '\\newcommand\{\\one\}' main.tex
rg -q '\\mathrm d\\mu' PROOF.tex
rg -q '\\mathrm e' PROOF.tex

if rg -n 'Warning|undefined|Overfull|Underfull|Error' main.log; then
  print -u2 'build diagnostic found'
  exit 1
fi

print 'P14.8 v2 rebased current-input checks: PASS_NOT_PRODUCTION_ACCEPTED'
