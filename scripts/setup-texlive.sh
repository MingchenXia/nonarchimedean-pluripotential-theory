#!/usr/bin/env bash
set -euo pipefail

source "$(dirname -- "${BASH_SOURCE[0]}")/tex-env.sh"

for tool in tlmgr kpsewhich pdflatex latexmk bibtex makeindex python3 pdfinfo gpg curl; do
  if ! command -v "$tool" >/dev/null 2>&1; then
    printf 'Missing prerequisite: %s\n' "$tool" >&2
    exit 1
  fi
done

texlive_year="$(tlmgr --version | sed -n 's/.*TeX Live.*version \(20[0-9][0-9]\).*/\1/p' | head -n 1)"
if [[ "$texlive_year" != 2025 ]]; then
  printf 'TeX Live 2025 is required; found: %s\n' "${texlive_year:-unknown}" >&2
  exit 1
fi

mkdir -p "$TEXMFHOME" "$TEXMFCONFIG" "$TEXMFVAR"
if [[ ! -f "$TEXMFHOME/tlpkg/texlive.tlpdb" ]]; then
  tlmgr --usertree "$TEXMFHOME" init-usertree
fi

# The TeX Live 2025 archive's signing key is renewed periodically. Fetch the
# current official key and pin its fingerprint before importing it locally.
export TL_GNUPGHOME="$TEXMFHOME/tlpkg/gpg"
mkdir -p "$TL_GNUPGHOME"
key_file="$(mktemp "$TEXMFHOME/texlive-key.XXXXXX")"
trap 'rm -f "$key_file"' EXIT
curl --fail --location --silent --show-error \
  https://www.tug.org/texlive/files/texlive.asc -o "$key_file"
key_fingerprint="$(gpg --homedir "$TL_GNUPGHOME" --show-keys --with-colons "$key_file" \
  | awk -F: '$1 == "fpr" { print $10; exit }')"
if [[ "$key_fingerprint" != C78B82D8C79512F79CC0D7C80D5E5D9106BAB6BC ]]; then
  printf 'The TeX Live signing key fingerprint did not match the pinned key\n' >&2
  exit 1
fi
gpg --batch --yes --homedir "$TL_GNUPGHOME" --import "$key_file"

repository=https://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2025/tlnet-final
repository_status="$(tlmgr --usertree "$TEXMFHOME" --verify-repo=all \
  --repository "$repository" repository status)"
if ! grep -Eq '^main .* verified$' <<< "$repository_status"; then
  printf 'TeX Live repository signature could not be verified:\n%s\n' "$repository_status" >&2
  exit 1
fi
tlmgr --usertree "$TEXMFHOME" --verify-repo=all --repository "$repository" install newtx doublestroke kastrup tex-gyre

for package_file in newtxtext.sty newtxmath.sty dsfont.sty binhex.tex ts1-qtmb.tfm; do
  kpsewhich "$package_file" >/dev/null || {
    printf 'TeX package file still missing: %s\n' "$package_file" >&2
    exit 1
  }
done
printf 'TeX Live 2025 dependencies are ready in %s\n' "$TEXMFHOME"
