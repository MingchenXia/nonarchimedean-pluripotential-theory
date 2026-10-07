from pathlib import Path
from datetime import datetime,timezone
import hashlib,json

R=Path('/workspace/research');K=R/'root-checks'
p=K/'P05.2-continuation277-actual-reference-height-through-genuine-cap-completion-working-proof-20261007.json'
assert not p.exists()
D=K/'public-P05.2-continuation272-arbitrary-real-reference-completion-and-flat-jet-contact'
J=next(K.glob('P05.2-continuation276-*.json'))
sha=lambda q:hashlib.sha256(q.read_bytes()).hexdigest()
steps=[
('H1','Explicit pending dependencies and correct original-reference cutoff.',r'''This is a NEW UNREVIEWED application with TWO pending reconstruction obligations: (i) the genuine SAMEactualgamma mixed extension/weak C_b continuity from currently unaccepted272, with its prior rational-component height estimate; (ii) joint rational-cone/domain max closure and cap calculus from unreviewedROOT276. These are DATA, not grants. Reconstruct them in a future author paper before using this implication. Let gamma be the actual real PA PC positive-growth reference, d the raw dimension, M its raw mass, and choose rational c> -min gamma. Define H_gamma=gamma+c>=0 and q_j=max(gamma-j,-c), j positive rational. Its gap is EXACTLY h_j=gamma-q_j=min(H_gamma,j), not min(H_gamma,j+c). Irrational equality walls mean q_j need not be finite rational-geometry PA. ROOT276 supplies its genuine uniform/decreasing domain antecedent BEFORE any operator below is applied.'''),
('H2','Actual finite approximants are exact on the tails.',r'''For fixed j use arbitrarily close rational gamma_i with gamma=sum t_i gamma_i, all t_i>0,sum t_i=1, and all gamma_i>-c; closeness and a common coercivity bound ensure the last strict inequality globally. Put q_delta=sum t_i max(gamma_i-j,-c). Every entry is rational-affine on rational geometry since j,c are rational. Thus q_delta is ACTUAL relative REAL PA PC. On a common compact set it approximates q_j by one-Lipschitzness; outside that set every summand equals gamma_i-j, so q_delta=gamma-j EXACTLY. Also q_delta<=gamma termwise and q_delta>=q_j by convexity of max, so 0<=gamma-q_delta<=h_j<=j. Every finite q_delta receives the primitive operator only after its actual finite PA antecedent is established. The existing rational-component continuity theorem applies to this FIXEDj/fixed relative-bound family. Its operator identification at q_j then follows by uniform convergence; no pre-extension primitive divisor of the irrational-wall q_j is used.'''),
('H3','Bounded mixed IBP extends to this actual completed cutoff.',r'''For finite actual relative PA a_1,...,a_d the raw finite identity from272 is
 integral(gamma-q_delta)MA(a_1,...,a_d)
 =integral(gamma-a_1)MA(q_delta,a_2,...,a_d)
  +integral(a_1-q_delta)MA(gamma,a_2,...,a_d).
All tests are bounded continuous and all raw positive measures have massM. The functions gamma-q_delta and a_1-q_delta converge UNIFORMLY to the corresponding q_j tests, with bounds uniform in delta. The genuine fixed-C weak C_b convergence of every mixed tuple containing q_delta permits passage to the exact SAMEidentity with q_j, whose measure is already defined on the true completion. This is not IBP for an unbounded test and does not assume gamma-height tightness: weak convergence here was previously proved using the rational gamma0 height. Rearranging gives
 integral h_j MA(a_1,...,a_d)
 =integral h_j MA(gamma,a_2,...,a_d)
  +integral(a_1-gamma)[MA(gamma,a_2,...,a_d)-MA(q_j,a_2,...,a_d)].
If every ||a_i-gamma||<=C, the last absolute contribution is at most2CM, since both positive mixed measures have the genuine raw massM.'''),
('H4','Direct raw intrinsic height bound for EVERY completed mixed tuple.',r'''Repeat H3 over all d factors, retaining the actual gamma and massM at every step. Then
 integral min(H_gamma,j) MA(a_1,...,a_d)
 <=2dCM +integral min(H_gamma,j) MA(gamma).
The finite reference raw measure MA(gamma) is supported at finitely many rational vertices, so J_gamma=integral H_gamma MA(gamma)<infinity. Monotone convergence j->infinity gives
 integral H_gamma MA(a_1,...,a_d)<=2dCM+J_gamma.
For arbitrary actual completed tuple f_l with ||f_l-gamma||<=C, choose genuine uniform PA approximants with relative bounds C+epsilon_n. For each fixed T>0, min(H_gamma,T) is bounded continuous, so the PREVIOUSLY established genuine weak C_b convergence passes the bound with C+epsilon_n to the completed tuple. Increase T and use monotone convergence. This proves the SAME exact constant2dCM+J_gamma for EVERY member of each ENTIRE fixed-C completed mixed family. MassM=0 gives zero outputs by positivity. No factor1/epsilon from a chosen rational component remains in this stronger intrinsic bound; no extra factorial or probability normalization appears. Its noncircular order is prior gamma0-height -> genuine weak mixed completion -> cap-domain proof -> bounded cutoff IBP -> intrinsic gamma-height.'''),
('H5','Scope and immutable audits.',r'''The implication and its actual cutoff construction need a NEW independently reconstructed source and whole review; neither272nor276 is presently accepted. The new intrinsic bound strengthens the existing rational-component estimate after those genuine antecedents are proved. It DOES NOT assert ALLcontinuousPC or ALLobstacle envelopes are regularizable, and it does not supply full non-PA contact sufficiency. OriginalP05.2 remains open. Active209curve269 and210reference272 local-source audits receive no new proof/hot feedback or source changes. Their independent verdicts and all earlier207/208INCONCLUSIVE histories remain immutable. No new accepted paper, grant or original closure.''')]
d=dict(recorded_utc=datetime.now(timezone.utc).isoformat(),atom='P05.2',continuation=277,
kind='UNREVIEWED conditional application with explicit genuine cap-domain and completed-operator dependencies',
data_sources=[dict(path=str(D/'P05.2-paper.tex'),sha256=sha(D/'P05.2-paper.tex'),new_grant=False),dict(path=str(J),sha256=sha(J),new_grant=False)],
steps=[dict(id=i,statement=s,proof=t) for i,s,t in steps],
new_mathematical_grant=False,new_accepted_paper=False,original_closed=False,
all_obstacle_regularization_proved=False,no_primitive_operator_at_irrational_nonPA_cutoff_before_completion=True,
no_private_active_output_read=True,no_hot_feedback=True,not_frozen_in_active209210=True,protected_editor_unchanged_open=True)
p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(path=str(p),sha256=sha(p),bytes=p.stat().st_size,new_mathematical_grant=False,original_closed=False),indent=2))

