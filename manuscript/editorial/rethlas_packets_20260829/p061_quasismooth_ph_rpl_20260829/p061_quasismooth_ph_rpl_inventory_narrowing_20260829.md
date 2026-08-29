# P06.1 inventory narrowing record

**Promotion record.** The exact frozen statement and proof received a
production Rethlas `gpt-5.6-sol`/`xhigh` verdict of `correct`, with zero
critical errors and zero gaps, and this narrowing was promoted on 29 August
2026.

Replace the P06.1 bullet by:

> - **P06.1** `[T2; open after the quasi-smooth and all strict-curve cases]`
>   On a good, separated, strict, boundaryless analytic space, decide whether
>   every classically pluriharmonic function is \(\mathbf R\)-PL near a
>   non-quasi-smooth point of analytic dimension at least two.

Insert the following paragraph before the existing P06.2 audit paragraph:

> The quasi-smooth scope of P06.1 is settled by
> `thm:p061-quasismooth-ph-rpl`: every classically pluriharmonic function on a
> good strict quasi-smooth analytic space is \(\mathbf R\)-PL and GJR
> harmonic, without global quasicompactness, separatedness, or
> boundarylessness. The proof combines Temkin's altered local uniformization
> with rigid étale sheaf descent. The published curve comparison already
> covers all strict analytic curves, including singular and nonreduced ones
> (`GR25Classical`, §4.1.2 and Proposition 3.15).
> The coefficient cannot be strengthened: `prop:p061-integral-pl-counterexample`
> gives \(\sqrt2\log|T|\) on a strict semistable annulus, which is not
> \(\mathbf Q\)-PL. The controlling run is
> `20260829T043457Z_0b1b4d161e3b`, item
> `pi_7cd35ebd843cf80a7cd696bb`. P06.1 remains one active T2 atom,
> now confined to non-quasi-smooth points in dimension at least two. No atom count,
> tier count, or queue position changes.

The queue line listing `P06.1` is unchanged. The environment still has two
active atoms, P06.1 and P06.2.
