ID: n3

SUMMARY:
Nodal obstruction and remaining gaps: raw mass plus standard finite dual energy does not suffice on all singular curves. A mass-V divisorial atom forces unequal normalization endpoint values over a node. Higher-dimensional unibranch envelopes and the discretely valued singular equation package remain unproved; status is partial and candidate=false.

DETAILED SUMMARY:
On an integral projective nodal curve over algebraically closed trivially valued characteristic-zero k, μ=Vδ_ord(q1) has finite actual-X dual energy at most V/2 but no actual-X finite-energy solution. The unique normalization solution drops by V at one preimage of the node and by zero at the other, contradicting fiber constancy. The draft leaves higher-dimensional PL/psh/conductor descent, unibranch envelopes, the nontrivially discretely valued singular finite-energy package, and a corrected branched-measure range unresolved. Required inputs, proof files, source extracts and twice-run TeX diagnostics are retained.

SUPPORT:
["n1", "n2"]

TEXT:
Let k be algebraically closed, trivially valued and characteristic zero. Let X be an integral projective curve with an ordinary node p, L ample of raw degree V, and q1,q2 its normalization preimages. Put μ=Vδ_v, where v=ord_q1 viewed on X^an. This has the exact required raw mass. Every actual-X psh potential pulls back to Y, and model projection followed by decreasing extension preserves its energy without asserting surjectivity of pullback. Therefore E*_X(δ_v)≤E*_Y(δ_ord_q1)=V/2, by n2's smooth-curve tail calculation at t=1. Thus μ has finite dual energy on actual X.

Suppose μ=MA_raw,X(φ) for φ∈E¹(X,L). Normalization pushforward identifies its upstairs MA. Normalization is injective at finite generic-support ray points, and finite-energy MA has no endpoint mass, so the upstairs measure is exactly Vδ_ord_q1. By n2's slope uniqueness, its potential is a−V min(t,1) on the q1-ray and constant a on the q2-ray. Endpoint values are a−V and a. Both endpoints map to p, whereas a pulled-back function must be constant on that fiber. This contradiction proves failure of surjectivity. No arbitrary restriction of a measure was normalized and no potential descent was assumed. This is the raw-mass obstruction of BJ Example 12.11, with the descent checked.

The positive theorem consequently retains unibranchness and integrality. On disconnected spaces, polarization masses must be fixed componentwise and uniqueness has a constant per component. On branched singular spaces, standard mass and finite energy are insufficient; a corrected measure range requires an explicit conductor-compatible theory.

The whole original atom remains unresolved in this draft. The curve generator argument does not prove higher-dimensional PL or psh descent. Topological normalization homeomorphism alone supplies none of semipositivity, approximation, energy preservation for arbitrary upstairs potentials, or envelopes. In the inspected trivial-field source, unibranch envelopes remain Conjecture 5.14, and Theorem 12.8 makes their proof the missing general existence input. This concerns the exact inspected version, not every later theorem outside the authorized caches. Pullback of an ample class to a resolution may be nonample, so no smooth ample-class theorem was silently applied there.

No singular-space finite-energy equation package is established here over the nontrivially discretely valued residue-characteristic-zero endpoint. The saved BFJ v1 algebraizability and SNC-support assumptions cannot be erased. Higher-dimensional conductor descents and a corrected admissible-measure range for non-unibranch varieties remain unsupplied.

P16.1-argument.md contains the complete partial proof and remaining obligations. P16.1-paper.tex is standalone, and build/P16.1-paper.pdf has 11 pages. input-original.json is byte-identical to input.json; assignment-original.txt retains the exact assignment string; task-original.json retains the task object. status.json has exactly id,status,exact_result,proof_file,concrete_gaps, with status partial. source-extracts/source-provenance.json retains literal primary-source proofs and application checks. Both builds using the existing pdflatex returned 0, with actual diagnostic streams and logs retained. Exact-rational checks passed but do not verify the theorem. Environment and commands are in environment.json and commands.txt; rerun with bash rerun.sh.

No other campaigns, models, workers, external messaging, installation or heavy computation were used. The requested native model and effort cannot be independently queried or changed through the available runtime tools; no substitute model was invoked. These are unverified drafts. The original P16.1 is not completely proved.

Artifacts: /workspace/research/campaigns/round-45/P16.1-public-source-singular-finite-energy-equations/artifacts/codex-ZDgZTo
