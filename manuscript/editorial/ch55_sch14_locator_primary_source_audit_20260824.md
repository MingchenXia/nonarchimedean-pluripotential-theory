# Chapter 55 Schneider locator audit

**Audit date:** 2026-08-24 (Asia/Shanghai)  
**Verdict:** **PASS after two locator corrections.**  In the 2014 second
expanded edition cited as `Sch14`, the John ellipsoid normalization is
Theorem 10.12.2 on page 588, and Blaschke selection is Theorem 1.8.7 on
page 63.  The former Chapter 55 locator Theorem 4.1.8 was unsupported, and
Theorem 1.8.6 is not Blaschke selection.

## Edition identity

The bibliography entry `Sch14` identifies Rolf Schneider,
*Convex Bodies: The Brunn--Minkowski Theory*, second expanded edition,
Cambridge University Press, Encyclopedia of Mathematics and its
Applications 151, 2014, ISBN 978-1-107-60101-7, xxii+736 pages.

- Live bibliography:
  `manuscript/bibliography/ComplexGeometry.bib`, 219,568 bytes,
  SHA-256
  `e4d69e071636bf447210c6000a704f2bd1cc6a1e0b0c03f6f4dd418cfbf39383`;
  entry `Sch14` is at lines 5865--5878.
- Supplied author bibliography:
  `/Users/mingchen/Downloads/Mixed_volumes_of_partial_Okounkov_bodies/ComplexGeometry.bib`,
  182,223 bytes, SHA-256
  `e3e48c5c503cd6cdaa7bb2e02bdbc02767031e3084c52eff7415258d9483813e`;
  entry `Sch14` is at lines 4918--4927 and explicitly says “Second
  expanded”.
- The publisher's official front matter and contents are available at
  <https://assets.cambridge.org/97811076/01017/frontmatter/9781107601017_frontmatter.pdf>.

No complete Schneider PDF is stored in the workspace, so this audit does not
invent a book-PDF SHA-256.  The controlling theorem-level evidence is the
publisher-authorized Google Books page preview for volume
`VfbXAAAAQBAJ`, matched to the edition above by title, author, publisher,
year, pagination, and ISBN.

## Locator evidence

### John ellipsoid normalization

The page-588 preview search for
[Theorem 10.12.2](https://books.google.com/books?id=VfbXAAAAQBAJ&pg=PA588&dq=%22Theorem+10.12.2%22)
returns the theorem on page 588.  It takes a convex body and its John
ellipsoid and gives the affine containment with factor (n); in the
centrally symmetric case it gives the sharper square-root factor.  This is
exactly the input used at Chapter 55 lines 955--962 after sending the John
ellipsoid to the unit ball.

### Blaschke selection

The page-63 preview search for
[Theorem 1.8.7](https://books.google.com/books?id=VfbXAAAAQBAJ&pg=PA63&dq=%22Theorem+1.8.7%22)
identifies that numbered result as the Blaschke selection theorem and states
the bounded-sequence subsequential compactness used at Chapter 55 lines
963--973.

The companion page-63 preview search for
[Theorem 1.8.6](https://books.google.com/books?id=VfbXAAAAQBAJ&pg=PA63&dq=%22Theorem+1.8.6%22)
instead identifies a closedness statement for the space of convex bodies.
It therefore cannot support the subsequence extraction.

### Rejection of Theorem 4.1.8

The former John citation `Theorem 4.1.8` is not supported by the second
edition's section 4.1 or by the book preview's theorem search.  Since the
exact John statement is positively located at Theorem 10.12.2, retaining a
generic citation merely to avoid correcting the invalid pinpoint would be
unnecessarily imprecise.

## Cross-check with the supplied author source

The supplied source
`/Users/mingchen/Downloads/Mixed_volumes_of_partial_Okounkov_bodies/main.tex`
has 41,905 bytes and SHA-256
`5746eb011417caecfa876c05c6c74fb548e2ae9d086c1441189bbcad02a96594`.
Line 625 gives only a generic `\cite{Sch14}` for both John's theorem and
Blaschke selection; lines 637--649 use the same John normalization and
subsequence argument.  This cross-check confirms the mathematical source
but supplies no pinpoint locator of its own.  The page-preview evidence above
is what justifies upgrading the live book to precise theorem numbers.

## Live-source conclusion

The current Chapter 55 source has 64,938 bytes and SHA-256
`b2134d6b59f7687f8f5f296023a7d80703122210909032856b965f12f61619ab`.
It now cites:

- `\cite[Theorem~10.12.2]{Sch14}` at live line 957 for the John ellipsoid
  containment; and
- `\cite[Theorem~1.8.7]{Sch14}` at live line 965 for Blaschke selection.

Both locators are exact for the identified second edition.  The mathematical
argument is unchanged.  No file under Downloads was modified in this audit.
