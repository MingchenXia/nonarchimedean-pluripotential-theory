# P03.1 v59 source ledger

Date: 2026-09-20

## External source

Jérôme Poineau, *Les espaces de Berkovich sont angéliques*, *Bulletin de la
Société mathématique de France* **141** (2013), no. 2, 267--297,
DOI `10.24033/bsmf.2648`; final preprint arXiv:1105.0250v5,
14 December 2012.

- Official PDF: `https://arxiv.org/pdf/1105.0250`
- Audited local copy: `/private/tmp/poineau_universal_1105.0250v5.pdf`
- SHA-256:
  `e42644373d072080990bc5ff9baebcbc62580ec4daa9377fa4ab6f592c6520ef`
- Published metadata was independently checked against the Crossref record
  for DOI `10.24033/bsmf.2648`.
- Definition 3.2 defines universal points and their canonical scalar lifts by
  the multiplicative tensor norm.
- Corollary 3.7 proves continuity of the canonical lift on the universal
  locus of a Banach spectrum.
- Remark 3.13 extends the notions and the continuity result to analytic
  spaces by restriction to affinoid domains.
- Corollary 3.14 proves that every point of an analytic space over an
  algebraically closed field is universal.

The live corollary imports only existence and continuity of the canonical
section.  It does not import analyticity of that section, preservation of psh
functions by the associated retraction, or any Shilov-boundary claim.

## Internal dependencies

- `thm:p031-rational-defect-terminal-boundary-core` supplies the connected,
  nested carrier closures containing the root and every chosen terminal
  endpoint.
- `thm:p031-proper-open-persistent-component-anchor` is the complementary
  v58 result for arbitrary lifted endpoints under properness and global
  openness.  The v59 section-selected result neither uses nor supersedes that
  theorem.

## Self-contained deductions

The statement and proof establish directly that a continuous section gives
pointwise openness along its image, exact usc regularization there, component
surjectivity for the section-selected component, and an explicit common
section anchor for every decreasing connected family.
