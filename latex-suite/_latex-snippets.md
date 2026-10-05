# LaTeX Suite Snippet Reference

> All snippets fire automatically in math mode unless marked **Tab**.  
> Open with Hover Editor as a floating window for quick reference while editing.

---

## Bracket Conventions

Four classes, applied consistently across every snippet:

| Class | Shape | Examples |
| ----- | ----- | -------- |
| **Named function** — argument is a value | `\name\!\left( … \right)` | `sin`, `log`, `exp`, `det`, `dim`, `ker`, `gcd`, `tr`, `rank`, `span`, `arg`, `max`, `min`, `sig`, `fn` |
| **Large operator** — argument is a body of arbitrary extent | `\op\limits_{…}^{…}\,` | `Sum`, `Prd`, `Lim`, `BigU`, `BigI`, `BigW`, `BigV`, `Max`, `Min`, `Sup`, `Inf`, `amax`, `amin` |
| **Probability functional** | `\name\left[ … \right]` | `Ex`, `Egv`, `Pr`, `Pgv`, `Vr`, `Cv`, `ind` |
| **Fence** | `\left\lvert … \right\rvert` etc. | `abs`, `Norm`, `ceil`, `floor` |

> The `\!` cancels the thin space TeX inserts between an operator name and `\left(`. It is **not** used before `\left[` — a bracket already sits close enough.

Function names use `\operatorname{…}`, which supplies the surrounding spacing that `\mathrm{…}` does not. `\mathrm{…}` is reserved for *names that are not operators*: distributions (`\mathrm{Ber}`, `\mathrm{Bin}`, `\mathrm{Poi}`), groups (`\mathrm{SO}`), and constants (`\mathrm{e}`, `\mathrm{i}`).

Deliberate exceptions, all with small fixed arguments where autosizing buys nothing: `SO` / `so` (`\mathrm{SO}(3)`), and the proof-annotation labels `res` / `MP` (`\text{Res}(1, 2)`).

---

## Mode Entry

| Trigger | Expands to |
| ------- | ---------- |
| `mk` | inline math `$ $` |
| `dm` | display math `$$ $$` |
| `cbl` **Tab** | fenced code block — first stop = language, Tab = body |

> `cbl` fires in **text mode**.

---

## Greek Letters

| Trigger | Name | | Trigger | Name | | Trigger | Name |
| ------- | ---- |-| ------- | ---- |-| ------- | ---- |
| `@a` | $\alpha$ | | `@k` | $\kappa$ | | `@f` | $\phi$ |
| `@b` | $\beta$ | | `@l` | $\lambda$ | | `@F` | $\Phi$ |
| `@g` | $\gamma$ | | `@L` | $\Lambda$ | | `@c` | $\chi$ |
| `@G` | $\Gamma$ | | `@m` | $\mu$ | | `@q` | $\psi$ |
| `@d` | $\delta$ | | `@n` | $\nu$ | | `@Q` | $\Psi$ |
| `@D` | $\Delta$ | | `@x` | $\xi$ | | `@o` | $\omega$ |
| `@e` | $\epsilon$ | | `@X` | $\Xi$ | | `@O` | $\Omega$ |
| `:e` | $\varepsilon$ | | `@p` | $\pi$ | | `@j` | $\tau$ |
| `@z` | $\zeta$ | | `@P` | $\Pi$ | | `@u` | $\upsilon$ |
| `@h` | $\eta$ | | `@r` | $\rho$ | | `@U` | $\Upsilon$ |
| `@t` | $\theta$ | | `@s` | $\sigma$ | | `:t` | $\vartheta$ |
| `:f` | $\varphi$ | | | | | | |
| `@T` | $\Theta$ | | `@S` | $\Sigma$ | | `@i` | $\iota$ |

> `@j` = $\tau$ (since `t` is taken by $\theta$). Variants: `:e` → $\varepsilon$, `:t` → $\vartheta$.  
> Full names also work (backslash auto-prepended): `phi`, `psi`, `mu`, `nu`, `xi`, `pi`, `rho`, `chi`, `eta`, `tau`.

---

## Font Styles

| Trigger | Style | Renders as |
| ------- | ----- | ---------- |
| `bf` | bold | $\mathbf{x}$ |
| `rm` | roman (upright) | $\mathrm{x}$ |
| `mbb` | blackboard bold | $\mathbb{x}$ |
| `mcal` | calligraphic | $\mathcal{x}$ |
| `mfrak` | Fraktur | $\mathfrak{x}$ |
| `msf` | sans-serif | $\mathsf{x}$ |
| `mtt` | typewriter / monospace | $\mathtt{x}$ |
| `mit` | italic | $\mathit{x}$ |
| `mbs` | bold symbol | $\boldsymbol{x}$ |
| `text` or `"` | upright text in math | $\text{words}$ |

---

## Subscripts, Superscripts & Powers

| Trigger | Name | Renders as |
| ------- | ---- | ---------- |
| `sr` | square | $x^{2}$ |
| `cb` | cube | $x^{3}$ |
| `rd` | power (tabstop) | $x^{n}$ |
| `_` | subscript | $x_{n}$ |
| `^` | superscript | $x^{n}$ |
| `ee` | exponential | $\mathrm{e}^{x}$ |
| `eul` | Euler's number (constant) | $\mathrm{e}$ |
| `iu` | imaginary unit (constant) | $\mathrm{i}$ |
| `eip` | complex exponential | $\mathrm{e}^{- \mathrm{i} \theta}$ |
| `cis` | cis — θ is a shared tabstop | $\cos\!\left(\theta\right) + \mathrm{i}\sin\!\left(\theta\right)$ |
| `invs` | inverse | $x^{-1}$ |
| `conj` | conjugate / adjoint | $x^{*}$ |
| `sq` | square root | $\sqrt{x}$ |
| `crt` | cube root | $\sqrt[3]{x}$ |
| `nrt` | nth root — Tab: n (mirrored) → radicand | $\sqrt[n]{x}$ |
| `//` | fraction | $\frac{a}{b}$ |
| `tf` | text-size fraction | $\tfrac{a}{b}$ |
| `pmod` | parenthesized modulo | $x \pmod{n}$ |
| `binom` | binomial coefficient | $\binom{n}{k}$ |
| `x10` | scientific notation — Tab out of the exponent | $3\times 10^{8}$ |

**Auto subscript** — fires after a letter immediately followed by the given characters:

| Trigger | Subscript | Example |
| ------- | --------- | ------- |
| `x3` | digit 0–9 | $x_{3}$ |
| `x_{3}4` | extend existing subscript | $x_{34}$ |
| `xnn` | `n` | $x_{n}$ |
| `\xii` | `i` | $x_{i}$ |
| `xjj` | `j` | $x_{j}$ |
| `xkk` | `k` | $x_{k}$ |
| `xp1` | `n+1` | $x_{n+1}$ |
| `xk1` | `k+1` | $x_{k+1}$ |

> `\xii` requires the backslash prefix to avoid conflicting with `\xi`.

> `x10` outranks the auto subscript, so it wins over $x_{10}$; type `x_10` when you
> really want the subscript.

---

## Decorators & Accents

Attach after a letter (`xhat`) or use standalone (`hat`). Also works on Greek: `\alpha hat` → $\hat{\alpha}$.

| Trigger | Decorator | Renders as |
| ------- | --------- | ---------- |
| `hat` / `xhat` | hat | $\hat{x}$ |
| `bar` / `xbar` | bar | $\bar{x}$ |
| `dot` / `xdot` | dot | $\dot{x}$ |
| `ddot` / `xddot` | double dot | $\ddot{x}$ |
| `tilde` / `xtilde` | tilde | $\tilde{x}$ |
| `what` | wide hat (use for multi-char) | $\widehat{ABC}$ |
| `wbar` | wide bar / closure / conjugate | $\overline{ABC}$ |
| `wtld` | wide tilde (use for multi-char) | $\widetilde{ABC}$ |
| `wvec` | wide vector arrow (directed segment) | $\overrightarrow{AB}$ |
| `vec` / `xvec` | vector arrow | $\vec{x}$ |
| `und` / `xund` | underline | $\underline{x}$ |
| `cdot` | centered dot | $\cdot$ |
| `x.,` or `x,.` | bold vector | $\mathbf{x}$ |
| `0.,` | zero vector | $\mathbf{0}$ |
| `1.,` | ones vector | $\mathbf{1}$ |
| `\alpha.,` | bold Greek | $\boldsymbol{\alpha}$ |

---

## Operators & Symbols

| Trigger | Name | Renders as |
| ------- | ---- | ---------- |
| `+-` | plus-minus | $\pm$ |
| `-+` | minus-plus | $\mp$ |
| `xx` | times / cross product | $\times$ |
| `**` | centered dot | $\cdot$ |
| `circ` | composition | $\circ$ |
| `para` | parallel | $\parallel$ |
| `perp` | perpendicular | $\perp$ |
| `cperp` | conditional independence | $\perp\!\!\!\perp$ |
| `ooo` | infinity | $\infty$ |
| `...` | ellipsis | $\dots$ |
| `cds` | centered dots | $\cdots$ |
| `vds` | vertical dots | $\vdots$ |
| `dds` | diagonal dots | $\ddots$ |
| `sum` | sum symbol (bare) | $\sum$ |
| `prod` | product symbol (bare) | $\prod$ |
| `lim` | limit symbol (bare) | $\lim$ |

> For `sum` / `prod` / `lim` with full limit tabstops, use `Sum` / `Prd` / `Lim` in the Big Operators section.

---

## Relations & Arrows

| Trigger | Name | Renders as |
| ------- | ---- | ---------- |
| `===` | equivalent / congruent | $\equiv$ |
| `:=` | defined as | $\coloneqq$ |
| `cong` | congruent to | $\cong$ |
| `!=` | not equal | $\neq$ |
| `>=` | greater or equal | $\geq$ |
| `<=` | less or equal | $\leq$ |
| `>>` | much greater than | $\gg$ |
| `<<` | much less than | $\ll$ |
| `simm` | similar to / distributed as | $\sim$ |
| `sim=` | approximately equal | $\simeq$ |
| `approx` | approximate equality | $\approx$ |
| `prop` | proportional to | $\propto$ |
| `prec` | precedes | $\prec$ |
| `preq` | precedes or equal | $\preceq$ |
| `succ` | succeeds | $\succ$ |
| `sucq` | succeeds or equal | $\succeq$ |
| `->` | right arrow / to | $\to$ |
| `<-` **Tab** | left arrow | $\leftarrow$ |
| `<->` | left-right arrow | $\leftrightarrow$ |
| `=>` | implies | $\implies$ |
| `=<` | implied by | $\impliedby$ |
| `iff` | if and only if | $\iff$ |
| `==>` | long implies | $\Longrightarrow$ |
| `<=>` | long iff | $\Longleftrightarrow$ |
| `!>` / `mapsto` | maps to | $\mapsto$ |
| `smap` | stacked-C mapsto (implied assignment) | $\overset{C}{\mapsto}$ |
| `mid` | divides / such that bar | $\mid$ |
| `giv` | given / conditional bar — Tab 0 = A, Tab 1 = B | $A\mid B$ |

---

## Set Theory & Number Systems

**Set operations:**

| Trigger | Name | Renders as |
| ------- | ---- | ---------- |
| `inn` | element of | $\in$ |
| `nni` | contains | $\ni$ |
| `notin` | not element of | $\notin$ |
| `cmp` | set complement (append) | $A^{c}$ |
| `sub=` | subset or equal | $\subseteq$ |
| `sup=` | superset or equal | $\supseteq$ |
| `ssub` | proper subset | $\subset$ |
| `ssup` | proper superset | $\supset$ |
| `and` | intersection | $\cap$ |
| `orr` | union | $\cup$ |
| `eset` | empty set | $\emptyset$ |
| `set` | autosizing set braces | $\left\{ x \right\}$ |
| `\\\` | set minus | $\setminus$ |
| `sbd` | set-builder notation | $\left\{ x \mid P(x) \right\}$ |
| `quot` | quotient structure — Tab 0 = set (`A`), Tab 1 = relation (`\sim`) | $\mathcal{A}/_{\sim}$ |
| `eqc` | equivalence class — Tab 0 = element (`x`), Tab 1 = relation (`\sim`) | $\left[ x \right]_{\sim}$ |

> `and`/`orr` = set-theoretic $\cap$/$\cup$. For logical $\land$/$\lor$ see Logic section.

**Number systems:**

| Trigger | Set | Renders as |
| ------- | --- | ---------- |
| `RR` | reals | $\mathbb{R}$ |
| `RR` then `n` | $n$-dim reals | $\mathbb{R}^{n}$ |
| `Rnn` | non-negative reals | $\mathbb{R}_{\ge 0}$ |
| `Rp` | positive reals | $\mathbb{R}^{+}$ |
| `Rm` | negative reals | $\mathbb{R}^{-}$ |
| `CC` | complex numbers | $\mathbb{C}$ |
| `ZZ` | integers | $\mathbb{Z}$ |
| `Zp` | positive integers | $\mathbb{Z}^{+}$ |
| `Zm` | negative integers | $\mathbb{Z}^{-}$ |
| `NN` | natural numbers | $\mathbb{N}$ |
| `QQ` | rationals | $\mathbb{Q}$ |
| `FF` | field | $\mathbb{F}$ |

---

## Brackets, Braces & Visual

**Delimiters** — all produce autosizing `\left…\right` pairs:

| Trigger | Name | Renders as |
| ------- | ---- | ---------- |
| `(` | parentheses | $\left( x \right)$ |
| `[` | square brackets | $\left[ x \right]$ |
| `{` | curly braces | $\left\{ x \right\}$ |
| `lr(` | left-right parentheses (explicit) | $\left( x \right)$ |
| `lr[` | left-right square brackets (explicit) | $\left[ x \right]$ |
| `lr{` | left-right curly braces (explicit) | $\left\{ x \right\}$ |
| `lr\|` | absolute value bars | $\left\| x \right\|$ |
| `lra` | angle brackets | $\left\langle x \right\rangle$ |
| `avg` | angle brackets / inner product | $\left\langle x \right\rangle$ |
| `abs` | absolute value | $\left\lvert x \right\rvert$ |
| `Norm` | double norm | $\left\lVert x \right\rVert$ |
| `snorm` | spectral norm | $\left\lVert x \right\rVert_2$ |
| `fnorm` | Frobenius norm | $\left\lVert x \right\rVert_F$ |
| `floor` | floor | $\left\lfloor x \right\rfloor$ |
| `ceil` | ceiling | $\left\lceil x \right\rceil$ |
| `mod` | binary modulo operator | $a \bmod n$ |
| `subst` | substitution $F[G/A]$ | $F\left[G/A\right]$ |
| `subn` | simultaneous substitution $F[t_1/x_1,\ldots,t_n/x_n]$ | $F\left[t_1/x_1, \ldots, t_n/x_n\right]$ — Tab 0 = t, Tab 1 = x, Tab 2 = n (each mirrored) |

**Braces:**

| Trigger | Name | Renders as |
| ------- | ---- | ---------- |
| `ub` | underbrace | $\underbrace{expr}_{label}$ |
| `ob` | overbrace | $\overbrace{expr}^{label}$ |

> Tabstops: cursor on expression, Tab to label.

**Dirac notation:**

| Trigger | Name | Renders as |
| ------- | ---- | ---------- |
| `bra` | bra vector | $\langle \psi \rvert$ |
| `ket` | ket vector | $\lvert \psi \rangle$ |
| `brk` | braket / inner product | $\langle \phi \mid \psi \rangle$ |

**Visual operations** *(requires text selection; Vim mode only)*:

| Trigger | Wraps selection in |
| ------- | ------------------ |
| `S` | $\sqrt{\square}$ |
| `U` | $\underbrace{\square}_{}$ |
| `O` | $\overbrace{\square}^{}$ |
| `B` | $\underset{}{\square}$ |
| `C` | $\cancel{\square}$ |
| `K` | $\cancelto{}{\square}$ |

---

## Big Operators

All use `\limits` so bounds stack above/below. Tabstops: lower bound → upper bound → operand.

| Trigger | Name | Renders as |
| ------- | ---- | ---------- |
| `Sum` | sum with limits | $\sum\limits_{i=1}^{n} a_i$ |
| `Prd` | product with limits | $\prod\limits_{i=1}^{n} a_i$ |
| `Lim` | limit (stacked) | $\lim\limits_{n \to \infty} a_n$ |
| `BigU` | big union with limits | $\bigcup\limits_{i=1}^{n} A_i$ |
| `BigI` | big intersection with limits | $\bigcap\limits_{i=1}^{n} A_i$ |
| `BigW` | big conjunction with limits | $\bigwedge\limits_{i=1}^{n} F_i$ |
| `BigV` | big disjunction with limits | $\bigvee\limits_{i=1}^{n} F_i$ |
| `bwdg` | bare big conjunction | $\bigwedge$ |
| `bvdg` | bare big disjunction | $\bigvee$ |
| `stk` | stacked conditions (`\substack`) | $\sum\limits_{\substack{u,v \in V \\ u \neq v}}$ |

> `stk` is used inside `_{}` to stack multiple limit conditions. Tabstops: first line, Tab to second. Add more with `\\`.

---

## Math Functions

All expand to `\func\!\left(\cdot\right)` with the argument as a tabstop.

**General:**

| Trigger | Function | Renders as |
| ------- | -------- | ---------- |
| `exp` | exponential | $\exp\!\left(x\right)$ |
| `log` | logarithm (base 2 by CS convention) | $\log\!\left(x\right)$ |
| `lgb` | logarithm with specified base | $\log_{b}\!\left(x\right)$ |
| `ln` | natural log | $\ln\!\left(x\right)$ |
| `det` | determinant | $\det\!\left(A\right)$ |
| `Re` | real part | $\operatorname{Re}\!\left(z\right)$ |
| `Im` | imaginary part | $\operatorname{Im}\!\left(z\right)$ |
| `arg` | argument of complex number | $\arg\!\left(z\right)$ |

**Linear algebra:**

| Trigger | Function | Renders as |
| ------- | -------- | ---------- |
| `tr` | trace | $\operatorname{tr}\!\left(A\right)$ |
| `span` | span | $\operatorname{span}\!\left(S\right)$ |
| `vcz` | vectorisation | $\operatorname{vec}\!\left(A\right)$ |
| `dom` | domain | $\operatorname{dom}\!\left(A\right)$ |
| `range` | range | $\operatorname{range}\!\left(A\right)$ |
| `nul` | null space | $\operatorname{null}\!\left(A\right)$ |
| `nlty` | nullity | $\operatorname{nullity}\!\left(A\right)$ |
| `col` | column space | $\operatorname{col}\!\left(A\right)$ |
| `row` | row space | $\operatorname{row}\!\left(A\right)$ |
| `dim` | dimension | $\dim\!\left(V\right)$ |
| `cnum` | condition number | $\kappa\!\left(A\right)$ |
| `ker` | kernel | $\ker\!\left(A\right)$ |
| `gcd` | greatest common divisor | $\gcd\!\left(a,b\right)$ |
| `lcm` | least common multiple | $\operatorname{lcm}\!\left(a,b\right)$ |
| `img` | image | $\operatorname{im}\!\left(A\right)$ |
| `rank` / `rnk` | rank | $\operatorname{rank}\!\left(A\right)$ |
| `dg` | diagonal | $\operatorname{diag}\!\left(A\right)$ |
| `proj` | projection | $\operatorname{proj}_{u}\!\left(v\right)$ |
| `jac` | Jacobian | $J_{f}$ |

**Custom:**

| Trigger | Expands to |
| ------- | ---------- |
| `fn` | `\operatorname{name}\!\left(x\right)` — Tab 0 = name, Tab 1 = argument |
| `opn` | `\operatorname{name}` — bare operator, no brackets — Tab 0 = name, Tab 1 = exit |

---

## Trigonometry

Type the full name: backslash auto-prepended and autosizing brackets added automatically.

| Trigger | | Trigger | | Trigger |
| ------- |-| ------- |-| ------- |
| `sin` | | `arcsin` | | `sinh` |
| `cos` | | `arccos` | | `cosh` |
| `tan` | | `arctan` | | `tanh` |
| `csc` | | `arccsc` | | `coth` |
| `sec` | | `arcsec` | | `sech` |
| `cot` | | `arccot` | | `csch` |

All expand to e.g. $\sin\!\left(x\right)$ with autosizing brackets.

> There is no bracketless form — every function always takes autosizing brackets. To write $\sin x$, type `sin` and let the brackets appear.

> **Hyperbolics:** `sin` expands the moment it is typed, so the `h` of `sinh` lands inside the brackets and is promoted: `\sin\!\left(h` rewrites to `\sinh\!\left(`. Typing `sinh`, `cosh`, `tanh`, `coth`, `sech`, `csch` therefore works as expected — the last two render through `\operatorname{…}`, as MathJax has no `\sech`. The cost is that an argument of literally `h` — $\cos\!\left(h\right)$ for a step size — promotes too; undo once to keep it.

**Powered forms** — capitalise first letter, then a digit or suffix:

| Pattern | Example trigger | Renders as |
| ------- | --------------- | ---------- |
| `Func2`…`Func9` | `Sin2` | $\sin^{2}\!\left(x\right)$ |
| `FuncN` | `SinN` | $\sin^{n}\!\left(x\right)$ — `n` is a tabstop |

Applies to: `Sin`, `Cos`, `Tan`, `Csc`, `Sec`, `Cot`, `Sinh`, `Cosh`, `Tanh`, `Coth`, `Log`, `Ln`.

**Cardinal functions** — capital first letter, `c` suffix:

| Trigger | Renders as |
| ------- | ---------- |
| `Sinc` | $\operatorname{sinc}\!\left(x\right)$ |
| `Cosc` | $\operatorname{cosc}\!\left(x\right)$ |
| `Tanc` | $\operatorname{tanc}\!\left(x\right)$ |
| `Sinhc` | $\operatorname{sinhc}\!\left(x\right)$ |
| `Coshc` | $\operatorname{coshc}\!\left(x\right)$ |
| `Tanhc` | $\operatorname{tanhc}\!\left(x\right)$ |

> Use `arcsin`, `arccos`, `arctan` etc. for inverse trig — not `\sin^{-1}` (ambiguous).

| `atan2` | two-argument arctangent | $\operatorname{atan2}\!\left(y, x\right)$ |

---

## Calculus

**Nabla:**

| Trigger | Name | Renders as |
| ------- | ---- | ---------- |
| `nabl` | nabla (bare) | $\nabla$ |
| `grad` | gradient | $\nabla f$ |
| `hess` | Hessian | $\nabla^2 f$ |

**Partial derivatives:**

| Trigger | Name                                                    | Renders as                                                 |
| ------- | ------------------------------------------------------- | ---------------------------------------------------------- |
| `par`   | $\partial y / \partial x$ (tabstops)                    | $\frac{\partial y}{\partial x}$                            |
| `paxy`  | regex — type two letters, e.g. `pafx`                   | $\frac{\partial f}{\partial x}$                            |
| `pa2`   | 2nd-order (tabstops)                                    | $\frac{\partial^2 f}{\partial x^2}$                        |
| `pa3`   | 3rd-order (tabstops)                                    | $\frac{\partial^3 f}{\partial x^3}$                        |
| `pan`   | nth-order — n mirrored, Tab: n → f → x                 | $\frac{\partial^{n} f}{\partial x^{n}}$                    |
| `pam`   | mixed 2nd partial (tabstops)                            | $\frac{\partial^2 f}{\partial x \partial y}$               |
| `ppax`  | $\partial/\partial x$ operator — regex, type one letter | $\frac{\partial}{\partial x}\!\left(f\right)$              |
| `ppa2x` | 2nd-order operator — regex, type one letter, e.g. `ppa2t` | $\frac{\partial^2}{\partial x^2}\!\left(f\right)$        |
| `ppa3x` | 3rd-order operator — regex, type one letter             | $\frac{\partial^3}{\partial x^3}\!\left(f\right)$          |
| `ppa?`  | $\partial/\partial x$ operator — regex, type one letter | $\frac{ \partial }{ \partial \cdot } \left( \cdot \right)$ |

**Ordinary derivatives:**

| Trigger | Name | Renders as |
| ------- | ---- | ---------- |
| `der` | $\mathrm{d}y/\mathrm{d}x$ — tabstops, Tab: y → x | $\frac{\mathrm{d}y}{\mathrm{d}x}$ |
| `de2` | 2nd-order — tabstops, Tab: y → x | $\frac{\mathrm{d}^2 y}{\mathrm{d}x^2}$ |
| `de3` | 3rd-order — tabstops, Tab: y → x | $\frac{\mathrm{d}^3 y}{\mathrm{d}x^3}$ |
| `dydx` | $\mathrm{d}y/\mathrm{d}x$ — regex, type e.g. `dydx`, `dfdt` | $\frac{\mathrm{d}y}{\mathrm{d}x}$ |
| `d2ydx` | 2nd-order — regex, e.g. `d2ydx`, `d2fdt` | $\frac{\mathrm{d}^2 y}{\mathrm{d}x^2}$ |
| `d3ydx` | 3rd-order — regex, e.g. `d3ydx`, `d3fdt` | $\frac{\mathrm{d}^3 y}{\mathrm{d}x^3}$ |
| `nthd` | nth-order — n mirrored, Tab: n → f → x | $\frac{\mathrm{d}^{n} f}{\mathrm{d}x^{n}}$ |
| `ddt` | $\mathrm{d}/\mathrm{d}t$ operator | $\frac{\mathrm{d}}{\mathrm{d}t} f$ |
| `ddx` | $\mathrm{d}/\mathrm{d}x$ operator — regex, type e.g. `ddx`, `ddy` | $\frac{\mathrm{d}}{\mathrm{d}x} f$ |
| `dd2x` | 2nd-order operator — regex, type one letter, e.g. `dd2t` | $\frac{\mathrm{d}^2}{\mathrm{d}x^2} f$ |
| `dd3x` | 3rd-order operator — regex, type one letter | $\frac{\mathrm{d}^3}{\mathrm{d}x^3} f$ |

> `ddt` has higher priority than the `ddx` regex, so typing `ddt` always gives the d/dt operator.  
> **Tabstop forms** (`der`, `de2`, `de3`) leave the variable as a tabstop — Tab to it and type `t` for $\mathrm{d}/\mathrm{d}t$. **Regex forms** (`dydx`, `d2ydx`, `d3ydx`) take the variable directly: `d2fdt` → $\frac{\mathrm{d}^2 f}{\mathrm{d}t^2}$.

**Differentials** (word-boundary auto):

`dt` `dx` `dy` `dz` `ds` `du` → $\mathrm{d}t$, $\mathrm{d}x$, $\mathrm{d}y$, $\mathrm{d}z$, $\mathrm{d}s$, $\mathrm{d}u$

**Integrals:**

| Trigger        | Name                     | Renders as                                        |
| -------------- | ------------------------ | ------------------------------------------------- |
| `int`          | indefinite integral      | $\int f\,\mathrm{d}x$                             |
| `\int` **Tab** | same, manually triggered | $\int f\,\mathrm{d}x$                             |
| `dint`         | definite integral        | $\int_{0}^{1} f\,\mathrm{d}x$                     |
| `oint`         | contour integral         | $\oint_{\gamma} f\,\mathrm{d}x$                   |
| `iint`         | double integral          | $\iint f\,\mathrm{d}x\,\mathrm{d}y$               |
| `tint`         | triple integral          | $\iiint f\,\mathrm{d}x\,\mathrm{d}y\,\mathrm{d}z$ |
| `oinf`         | integral $0$ to $\infty$ | $\int_{0}^{\infty} f\,\mathrm{d}x$                |
| `infi`         | integral over all reals  | $\int_{-\infty}^{\infty} f\,\mathrm{d}x$          |
| `eval`         | evaluation bar           | $\Big\|_{a}^{b}$                                  |
| `evb`          | evaluation brackets      | $\left[ F \right]_{a}^{b}$                        |

> The differential variable is a tabstop — Tab to change it. The $\mathrm{d}$ is upright (math roman).
> `eval` tabstops: lower bound → upper bound → exit.
> `evb` tabstops: integrand → lower bound → upper bound → exit.

**Taylor expansion:**

| Trigger | Renders as |
| ------- | ---------- |
| `tayl` | $f(x+h) = f(x) + f'(x)h + \tfrac{h^2}{2!}f''(x) + \dots$ |

---

## Linear Algebra & Matrices

### Operations & Notation

| Trigger | Name | Renders as |
| ------- | ---- | ---------- |
| `tp` / `trp` | transpose | $A^{\top}$ |
| `dag` | dagger / Moore-Penrose pseudo-inverse | $A^{\dagger}$ |
| `sk` | skew-symmetric representation | $\left[v\right]_{\times}$ |
| `kron` | Kronecker product | $\otimes$ |
| `conv` | convolution | $f \ast g$ |
| `had` | Hadamard (elementwise) product | $A \odot B$ |
| `o+` | direct sum | $\oplus$ |
| `dprd` | dot product / inner product | $\left\langle \cdot,\cdot \right\rangle$ |
| `lb` | Lie bracket | $\left[\cdot,\cdot\right]$ |
| `rvec` | row vector template | $\begin{pmatrix} v_1 & \cdots & v_n \end{pmatrix}$ |
| `cvec` | column vector template | $\begin{pmatrix} v_1 \\ \vdots \\ v_n \end{pmatrix}$ |

> `trp` is identical to `tp` — use either.

### Matrix Environments

Auto-expand in `$$ $$`; Tab-expand in `$ $`. Tab = next cell, Enter = new row.

| Trigger | Name | Renders as |
| ------- | ---- | ---------- |
| `pmat` | parenthesis matrix | $\begin{pmatrix} a & b \\ c & d \end{pmatrix}$ |
| `bmat` | bracket matrix | $\begin{bmatrix} a & b \\ c & d \end{bmatrix}$ |
| `Bmat` | curly brace matrix | $\begin{Bmatrix} a & b \\ c & d \end{Bmatrix}$ |
| `vmat` | determinant matrix | $\begin{vmatrix} a & b \\ c & d \end{vmatrix}$ |
| `Vmat` | double bar matrix | $\begin{Vmatrix} a & b \\ c & d \end{Vmatrix}$ |
| `matrix` | plain matrix (no delimiters) | — |
| `casb` | bare cases (2 rows, tabstops) | $\begin{cases} \cdot & \cdot \\ \cdot & \cdot \end{cases}$ |
| `cases` | cases with `\text{if }` + comma/period | $\begin{cases} F & \text{if }cond, \\ \neg F & \text{if }cond. \end{cases}$ |
| `idenN` | identity matrix (`iden3` = $3\times3$) | diagonal ones |
| `rvN` | row vector with $N$ tabstops (`rv3`) | $\begin{pmatrix} \$0 & \$1 & \$2 \end{pmatrix}$ |
| `cvN` | column vector with $N$ tabstops (`cv3`) | $N \times 1$ pmatrix |
| `matNxM` | $N\times M$ matrix, all entries as tabstops | `mat2x3` → $2\times3$ pmatrix |
| `m_{N}M` | short rectangular pmatrix — type `m_{2}3` | $2\times3$ pmatrix |
| `pmN` | square $N\times N$ pmatrix, all entries as tabstops | `pm3` → $3\times3$ pmatrix |
| `bmN` | square $N\times N$ bmatrix, all entries as tabstops | `bm3` → $3\times3$ bmatrix |
| `DiagN` | $N\times N$ diagonal, diagonal entries as tabstops | `Diag3` → zeros off-diagonal |
| `gmat` | general $m\times n$ template | $\begin{pmatrix} a_{1,1} & \cdots & a_{1,n} \\ \vdots & \ddots & \vdots \\ a_{m,1} & \cdots & a_{m,n} \end{pmatrix}$ |
| `smat` | square $n\times n$ template | $\begin{pmatrix} a_{1,1} & \cdots & a_{1,n} \\ \vdots & \ddots & \vdots \\ a_{n,1} & \cdots & a_{n,n} \end{pmatrix}$ |
| `blmat` | 2×2 block matrix — Tab: A → B → C → D | $\begin{pmatrix} A & B \\ C & D \end{pmatrix}$ |
| `utri3` | upper triangular 3×3 (camera intrinsic K pattern) | $\begin{pmatrix} a & b & c \\ 0 & d & e \\ 0 & 0 & f \end{pmatrix}$ |
| `ltri3` | lower triangular 3×3 (Cholesky L pattern) | $\begin{pmatrix} a & 0 & 0 \\ b & c & 0 \\ d & e & f \end{pmatrix}$ |
| `sym2` | symmetric 2×2 — b mirrored | $\begin{pmatrix} a & b \\ b & c \end{pmatrix}$ |
| `sym3` | symmetric 3×3 — off-diagonals mirrored | $\begin{pmatrix} a & b & c \\ b & d & e \\ c & e & f \end{pmatrix}$ |
| `Skew3` | 3×3 skew-symmetric (hat op.) — type vector name once | $\begin{pmatrix} 0 & -w_3 & w_2 \\ w_3 & 0 & -w_1 \\ -w_2 & w_1 & 0 \end{pmatrix}$ |
| `Tmat` | SE(3) rigid body transform — Tab: R → T | $\begin{pmatrix} R & T \\ 0 & 1 \end{pmatrix}$ |
| `twmat` | se(3) twist matrix — Tab: $\hat{w}$ → v | $\begin{pmatrix} \hat{w} & v \\ 0 & 0 \end{pmatrix}$ |
| `outp` | outer product | $\mathbf{u}\mathbf{v}^\top$ |
| `svd` | SVD — Tab: A → U → V | $A = U\Sigma V^\top$ |
| `QR` | QR decomposition | $A = QR$ |
| `LU` | LU decomposition | $A = LU$ |
| `chol` | Cholesky — L mirrored | $A = LL^\top$ |
| `eigd` | eigendecomposition (general) — Q mirrored | $A = Q\Lambda Q^{-1}$ |
| `eigs` | eigendecomposition (symmetric) — Q mirrored | $A = Q\Lambda Q^\top$ |
| `gram` | Gram matrix — X mirrored | $X^\top X$ |
| `augmat` | augmented matrix — Tab: col-spec → A → b | $\left[A \mid b\right]$ |

> `gmat` tabstops: letter → rows (`m`) → cols (`n`). `smat` tabstops: letter → dimension (`n`) — all four corner subscripts update together.

### Equation Environments

| Trigger | Name |
| ------- | ---- |
| `align` / `ali` | aligned equations (no numbering) |
| `aln` | aligned equations (numbered) |
| `gather` / `gat` | gathered equations (no numbering) |
| `gtn` | gathered equations (numbered) |
| `array` | array — column spec `{rcl}` as first tabstop |
| `tg` | `\tag{label}` — annotate equation line (label in parens) |
| `Tg` | `\tag*{label}` — annotate equation line (no parens) |

Inside `align` / `align*`, typing `=`, `<`, or `>` as the **first operator on a new line** auto-prepends `&`:

| Trigger (at line start) | Expands to |
| ----------------------- | ---------- |
| `=` | `&=` |
| `<` | `&<` |
| `>` | `&>` |
| `:=` | `&\coloneqq` — `&` auto-forms before the relation |
| `->` | `\to` — chords normally (no spurious `&`) |

### Lie Groups

| Trigger | Group | | Trigger | Algebra |
| ------- | ----- |-| ------- | ------- |
| `SO` | $\mathrm{SO}(3)$ — rotations | | `so` | $\mathfrak{so}(3)$ |
| `SE` | $\mathrm{SE}(3)$ — rigid motions | | `seL` | $\mathfrak{se}(3)$ |
| `GL` | $\mathrm{GL}(n)$ — general linear | | `gl` | $\mathfrak{gl}(n)$ |
| `SL` | $\mathrm{SL}(n)$ — special linear | | `sl` | $\mathfrak{sl}(n)$ |
| `Sim` | $\mathrm{Sim}(3)$ — similarity | | `quat` | $w + x\mathrm{i} + y\mathrm{j} + z\mathrm{k}$ |

---

## Sequences & Tuples

Four container types × five index ranges. Tabstops: Tab 0 = letter (`a`), Tab 1 = upper index (shared).

| Range | Sequence | Set | Tuple | String (space-sep) |
| ----- | -------- | --- | ----- | ------------------ |
| **1…n** | `seq` | `sset` | `sarr` | `str` |
| **0…n** | `zseq` | `zsset` | `zsarr` | `zstr` |
| **compact 1…n** | `cseq` | `csset` | `csarr` | `cstr` |
| **compact 0…n** | `czseq` | `czsset` | `czsarr` | `czstr` |
| **i…j** | `ijseq` | `ijsset` | `ijsarr` | `ijstr` |
| **infinite** | `iseq` | `infset` | — | `istr` |
| **index-defined** | — | `iset` | — | — |

> **1…n**: `a_1, a_2, …, a_n`. **Compact**: omits the second element (`a_1, …, a_n`). **i…j**: Tab 0 = letter, Tab 1 = start index `i` (also auto-inserted as `i+1`), Tab 2 = end `j`. **Infinite**: letter tabstop only.  
> `infset` name avoids the `ssetI` collision (`sset` is auto-firing). `iset` = $\left\{a_i\right\}_{i=1}^{n}$.

---

## Logic

### Quantifiers

| Trigger | Name | Renders as |
| ------- | ---- | ---------- |
| `AA` | for all | $\forall\,$ |
| `EX` | there exists | $\exists\,$ |
| `EU` | there exists unique | $\exists!\,$ |
| `EN` | there does not exist | $\nexists\,$ |
| `Af` | for all x, F (FOL formula form) | $\forall x\, F$ |
| `Ef` | there exists x, F (FOL formula form) | $\exists x\, F$ |
| `Qe` | close quantifier chain | $\;\left(\cdot\right)$ |

> Each quantifier emits the symbol + thin space for chaining. Close with `Qe`: e.g. `AA` `x` `EX` `y` `Qe` → $\forall\, x\;\exists\, y\;\left(\phi\right)$.  
> `Af`/`Ef` are the FOL formula form: tab 0 = variable (default `x`), tab 1 = formula (default `F`), tab 2 = exit.

### Constants & Connectives

| Trigger | Name | Renders as |
| ------- | ---- | ---------- |
| `top` | tautology / true | $\top$ |
| `bot` | contradiction / false | $\bot$ |
| `qed` | end of proof | $\blacksquare$ |
| `thus` | therefore | $\therefore$ |
| `bcs` | because | $\because$ |
| `land` | conjunction | $\land$ |
| `lor` | disjunction | $\lor$ |
| `neg` | negation | $\neg$ |
| `nand` | NAND | $\barwedge$ |
| `norr` | NOR | $\downarrow$ |
| `xor` | exclusive or | $\oplus$ |
| `box` | box / necessity | $\Box$ |
| `dia` | diamond / possibility | $\Diamond$ |
| `ecl` | empty clause (resolution) | $\Box$ |

### Entailment & Provability

| Trigger | Name | Renders as |
| ------- | ---- | ---------- |
| `\|-` | syntactic entailment | $\vdash$ |
| `nvdash` | not provable | $\nvdash$ |
| `\|=` | semantic entailment / models | $\models$ |
| `nvmod` | does not model | $\not\models$ |
| `vres` | provable by resolution | $\vdash_{\text{Res}}$ |
| `vdG` | provable in system $G$ | $\vdash_G$ |
| `vdH` | provable in Hilbert system | $\vdash_H$ |
| `vdN` | provable in natural deduction | $\vdash_N$ |
| `IH` | induction hypothesis | $\text{IH}$ |
| `=IH` | equals by induction hypothesis | $\overset{\text{IH}}{=}$ |
| `oveq` | something over equals | $\overset{\cdot}{=}$ |

> `\|=` auto-inserts a space when followed by a letter (e.g. `|=A` → $\models A$).

### Assignment & Models

| Trigger | Name | Renders as |
| ------- | ---- | ---------- |
| `cA` | assignment $\mathcal{A}$ | $\mathcal{A}$ |
| `^cA` | superscript $^{\mathcal{A}}$ | $^{\mathcal{A}}$ |
| `cAf` | assignment applied to formula | $\mathcal{A}\!\left(\cdot\right)$ |
| `cS` | set of formulae $\mathcal{S}$ | $\mathcal{S}$ |
| `cM` | model / interpretation $\mathcal{M}$ | $\mathcal{M}$ |
| `cP` | property $\mathcal{P}$ | $\mathcal{P}$ |
| `cPf` | property applied | $\mathcal{P}\!\left(\cdot\right)$ |
| `fmid` | formula restricted by assignment | $F\mid_{\mathcal{A}}$ |
| `LL` | Lagrangian / $\mathcal{L}$ | $\mathcal{L}$ |
| `HH` | Hilbert space / $\mathcal{H}$ | $\mathcal{H}$ |

---

## Proof Theory & Sequent Calculus

Uses MathJax's `bussproofs` extension. Formulas inside bussproofs args must be wrapped in inner `$...$` (Obsidian quirk).

### Primitives

| Trigger | Name | Expands to |
| ------- | ---- | ---------- |
| `pft` **text/math** | proof tree skeleton | `$$\begin{prooftree}…\end{prooftree}$$` |
| `axc` | axiom / open hypothesis | `\AxiomC{$formula$}` |
| `axl` | axiom line (no label) | `\AxiomC{}` + `\UnaryInfC{$formula$}` |
| `axrl` | axiom line with label | `\AxiomC{}` + `\RightLabel{\;$name$}` + `\UnaryInfC{$formula$}` |
| `uic` | unary inference | `\UnaryInfC{$formula$}` |
| `bic` | binary inference | `\BinaryInfC{$formula$}` |
| `tic` | ternary inference | `\TrinaryInfC{$formula$}` |
| `rlab` | right rule label | `\RightLabel{\;$name$}` |
| `casm` | closed assumption leaf | `\AxiomC{$[A]^{n}$}` |
| `Seq` | sequent template | $\Gamma \Rightarrow \Delta$ |
| `Rr` | sequent arrow (bare) | $\Rightarrow$ |

> `rlab` goes immediately **before** the corresponding `\*InfC`.  
> `casm` superscript `n` should match the `: n` step number of the rule that closes the assumption.  
> `pft` fires in text mode (wraps in `$$ $$`) and math mode (bare `\begin{prooftree}`).

### Sequent Calculus Rule Chords

Two variants per rule: **`mv`** (Vim visual-select conclusion inside `\AxiomC{$…$}`, fire trigger) and **`xRULE`** (cursor at end of `\AxiomC{$formula$}`, type e.g. `xnL`). Both pre-fill the conclusion from the leaf. Mirrored tabstops: shared variables (F, Γ, Δ) update together.

| Trigger | Rule | Arity | Conclusion | Premise(s) |
| ------- | ---- | ----- | ---------- | ---------- |
| `Ax` | Identity | 0 | `A,Γ ⇒ A,Δ` | — (label plain text) |
| `rax` | Named axiom | 0 | `A,Γ ⇒ A,Δ` | — (label is a tabstop) |
| `btL` | ⊥L | 0 | `⊥,Γ ⇒ Δ` | — |
| `nL` | ¬L | 1 | `¬F,Γ ⇒ Δ` | `Γ ⇒ F,Δ` |
| `nR` | ¬R | 1 | `Γ ⇒ ¬F,Δ` | `F,Γ ⇒ Δ` |
| `anL` | ∧L | 1 | `F∧G,Γ ⇒ Δ` | `F,G,Γ ⇒ Δ` |
| `anR` | ∧R | 2 | `Γ ⇒ F∧G,Δ` | `Γ ⇒ F,Δ` / `Γ ⇒ G,Δ` |
| `orL` | ∨L | 2 | `F∨G,Γ ⇒ Δ` | `F,Γ ⇒ Δ` / `G,Γ ⇒ Δ` |
| `orR` | ∨R | 1 | `Γ ⇒ F∨G,Δ` | `Γ ⇒ F,G,Δ` |
| `toL` | →L | 2 | `F→G,Γ ⇒ Δ` | `Γ ⇒ F,Δ` / `G,Γ ⇒ Δ` |
| `toR` | →R | 1 | `Γ ⇒ F→G,Δ` | `F,Γ ⇒ G,Δ` |
| `cut` | Cut | 2 | `Γ ⇒ Δ` | `Γ ⇒ F,Δ` / `Γ,F ⇒ Δ` |

### Natural Deduction Rule Chords

Same two variants (`mv` / `xRULE`) as sequent calculus. Tabstop order: conclusion → premises left-to-right → **step number** (last). Labels render as `$\text{rule}: k$`. Closed assumptions `[A]^n` use `casm`; the `n` should match the rule's `: k` step number.

| Trigger | Rule | Arity | Conclusion | Premise(s) |
| ------- | ---- | ----- | ---------- | ---------- |
| `anI` | ∧I | 2 | `A ∧ B` | `A` / `B` |
| `anE1` | ∧E₁ | 1 | `A` | `A ∧ B` |
| `anE2` | ∧E₂ | 1 | `B` | `A ∧ B` |
| `orI1` | ∨I₁ | 1 | `A ∨ B` | `A` |
| `orI2` | ∨I₂ | 1 | `A ∨ B` | `B` |
| `orE` | ∨E | 3 | `C` | `A ∨ B` / `C` (from `[A]`) / `C` (from `[B]`) |
| `toI` | →I | 1 | `A → B` | `B` (closes `[A]`) |
| `toE` | →E | 2 | `B` | `A → B` / `A` |
| `nI` | ¬I | 1 | `¬A` | `⊥` (closes `[A]`) |
| `nE` | ¬E | 2 | `⊥` | `¬A` / `A` |
| `btE` | ⊥ (ex falso) | 1 | `A` | `⊥` |
| `mpE` | MP (Hilbert →E) | 2 | `B` | `A → B` / `A` |


> `mpE` is the Hilbert-system →E rule — same bussproofs structure as `toE` but the label has no step number. Tab order (mA mode): B (shared conclusion + premise consequent) → A (shared premise antecedent + minor premise).
> `nE` is the one rule whose conclusion is fixed (⊥), so its `mv` variant pre-fills the **negated premise** rather than the conclusion: select A, and `¬A` is filled while the minor premise stays as tabstop $0.
### Axiom-Expand Chords (normal mode, no Vim required)

Place cursor at end of `\AxiomC{$formula$}` and type the chord. The axiom is replaced; the formula pre-fills as the conclusion.

**Generic (rule label is a tabstop):**

| Trigger | Arity |
| ------- | ----- |
| `xun` | Unary |
| `xbi` | Binary |
| `xtr` | Ternary |
| `xrax` | Unary (tab label) |

**Sequent calculus (rule pre-filled):**

| Trigger | Rule | Trigger | Rule | Trigger | Rule |
| ------- | ---- | ------- | ---- | ------- | ---- |
| `xAx` | Ax | `xanR` | ∧R | `xtoL` | →L |
| `xbtL` | ⊥L | `xorL` | ∨L | `xtoR` | →R |
| `xnL` | ¬L | `xorR` | ∨R | `xcut` | Cut |
| `xnR` | ¬R | `xanL` | ∧L | | |

**Natural deduction (conclusion auto-filled into premises where it appears; remaining unknowns are multicursor tabstops; step number is second-to-last tabstop):**
> **Intro rules** (`xanI`, `xorI1`, `xorI2`, `xtoI`): trigger regex matches the connective in the conclusion (e.g. `A \lor B` or `A\lorB`), so both operands are captured and pre-filled — the cursor formula must be in `X \op Y` form (any whitespace around the connective is accepted).
> **Elim/other rules**: generic capture of the whole conclusion formula — `[[0]]` is substituted wherever the conclusion appears verbatim in the premises.

| Trigger | Rule | Trigger | Rule | Trigger | Rule |
| ------- | ---- | ------- | ---- | ------- | ---- |
| `xanI` | ∧I | `xorE` | ∨E | `xnI` | ¬I |
| `xanE1` | ∧E₁ | `xtoI` | →I | `xnE` | ¬E |
| `xanE2` | ∧E₂ | `xtoE` | →E | `xbtE` | ⊥ |
| `xorI1` | ∨I₁ | `xmpE` | MP (Hilbert) | | |
| `xorI2` | ∨I₂ | | | | |

---

## Proof Tables

Use `ptab` outside math to create a full proof table block.

| Trigger | Mode | Expands to |
| ------- | ---- | ---------- |
| `ptab` | text | `$$\begin{array}{r l l}…\end{array}$$` with first row |
| `harr` | text | `$$\begin{array}{r@{\quad}l@{\quad}l}…\end{array}$$` — Hilbert proof layout (with `$$` wrapper) |
| `harr` | block math | `\begin{array}{r@{\quad}l@{\quad}l}…\end{array}` — bare array (inside existing `$$`) |
| `tbl` | math | `\begin{array}{col_spec}…\end{array}` scaffold |
| `res` | math | `\text{Res}(`$0`,`$1`)` — resolution justification |
| `prem` | math | `\text{Premise}` |
| `MP` | math | `\text{MP}($0, $1)` — Hilbert MP justification |
| `mpA` | math (auto) | 3-row MP block: `n: & B \to A &`, `n+1: & A &`, `n+2: & B & \text{MP}(n, n+1)` |
| `mpA` | math (visual) | same block with selected B pre-filled; select existing conclusion before firing |

> **`ptab`** tabstops: $0 = step → $1 = clause cell → $2 = justification (default `Premise`) → $3 = next row body.  
> **`harr`** tabstops: $0 = line number → $1 = formula (default `\phi`) → $2 = justification (default `\text{Hyp}`) → $3 = next row body.  
> **`tbl`** tabstops: $1 = column spec → $2 = body → $0 = exit.  
> **`res`** (word-boundary): $0 = first clause index, $1 = second index. Note: `Res` (capital) can't be used in math — `Re` fires first.
> **`MP`** (word-boundary): $0 = first line index, $1 = second line index — for Hilbert sequential proofs.
> **`mpA`** (auto, word-boundary): tab order: $0=A (shared in both premises) → $1=B (shared in first premise + conclusion) → $2=n (shared with MP first arg) → $3=n+1 (shared with MP second arg) → $4=n+2 → $5=just₁ → $6=just₂ → exit. **Note:** subsequent lines must be manually renumbered (+2 each); LaTeX Suite cannot update line numbers outside the matched text.
> **`mpA`** (visual): select existing B first — it fills the first premise only; the conclusion's B is a tabstop, because LaTeX Suite substitutes just the first `${VISUAL}` in a template. Tab order: $0=A → $1=n (shared) → $2=n+1 (shared) → $3=n+2 → $4=just₁ → $5=just₂ → $6=B → exit.

**Typical resolution proof workflow:**

1. `ptab` → full `array` block; cursor on step number `1`
2. Tab to clause cell → type e.g. `\{P,Q\}`, Tab to justification → `prem` or type freely
3. Type `\\` to end the row, continue next row manually
4. For derived steps: type `res` in the justification cell → fill clause indices with Tab
5. Add `\hline` between premises and derived rows

---

## Probability & Statistics

| Trigger | Name | Renders as |
| ------- | ---- | ---------- |
| `Ex` | expectation | $\mathbb{E}\left[X\right]$ |
| `Egv` | conditional expectation ("E given") | $\mathbb{E}\left[X \mid Y\right]$ |
| `ND` | normal / Gaussian | $\mathcal{N}\!\left(\mu, \sigma^2\right)$ |
| `Ber` | Bernoulli | $\mathrm{Ber}\!\left(p\right)$ |
| `Bin` | binomial | $\mathrm{Bin}\!\left(n, p\right)$ |
| `Cat` | categorical | $\mathrm{Cat}\!\left(\mathbf{p}\right)$ |
| `Multi` | multinomial | $\mathrm{Multi}\!\left(n, \mathbf{p}\right)$ |
| `Poi` | Poisson | $\mathrm{Poi}\!\left(\lambda\right)$ |
| `Unif` | uniform | $\mathrm{Unif}\!\left(a, b\right)$ |
| `Beta` | beta | $\mathrm{Beta}\!\left(\alpha, \beta\right)$ |
| `Gam` | gamma | $\mathrm{Gamma}\!\left(\alpha, \beta\right)$ |
| `Dir` | Dirichlet | $\mathrm{Dir}\!\left(\boldsymbol{\alpha}\right)$ |
| `MSE` | mean squared error | $\mathrm{MSE}$ |
| `MAE` | mean absolute error | $\mathrm{MAE}$ |
| `NLL` | negative log-likelihood | $\mathrm{NLL}$ |
| `xent` | cross-entropy | $H\!\left(p, q\right)$ |
| `Pr` | probability | $\Pr\left[A\right]$ |
| `Pgv` | conditional probability ("P given") | $\Pr\left[A \mid B\right]$ |
| `Vr` | variance | $\operatorname{Var}\left[X\right]$ |
| `Vgv` | conditional variance ("Var given") | $\operatorname{Var}\left[X \mid Y\right]$ |
| `Cv` | covariance | $\operatorname{Cov}\left[X,\,Y\right]$ |
| `Cgv` | conditional covariance ("Cov given") | $\operatorname{Cov}\left[X, Y \mid Z\right]$ |
| `KL` | KL divergence | $D_{\mathrm{KL}}\!\left(P\,\Vert\,Q\right)$ |
| `iid` | i.i.d. | $\overset{\mathrm{iid}}{\sim}$ |
| `ind` | indicator function | $\mathbf{1}\!\left[A\right]$ |
| `sig` | sigmoid | $\sigma\!\left(x\right)$ |
| `smax` | softmax | $\operatorname{softmax}\!\left(x\right)$ |
| `max` | max (bare) | $\max$ |
| `max` | max of arguments / set | $\max\!\left(\cdot\right)$ |
| `min` | min of arguments / set | $\min\!\left(\cdot\right)$ |
| `Max` | max over bound (optimization) | $\max\limits_{x} f(x)$ |
| `Min` | min over bound (optimization) | $\min\limits_{x} f(x)$ |
| `amax` | argmax over bound | $\operatorname*{argmax}\limits_{x} f(x)$ |
| `amin` | argmin over bound | $\operatorname*{argmin}\limits_{x} f(x)$ |
| `Sup` | supremum over bound | $\sup\limits_{x} f(x)$ |
| `Inf` | infimum over bound | $\inf\limits_{x} f(x)$ |

---

## Miscellaneous

| Trigger | Name | Renders as / Expands to |
| ------- | ---- | ----------------------- |
| `beg` | begin/end environment | `\begin{}\end{}` |
| `NP` | NP complexity class | $\mathbf{NP}$ |
| `aleph` | aleph (infinite cardinality) | $\aleph$ |
| `PP` | P complexity class | $\mathbf{P}$ |
| `ft` | function type signature | $f : A \to B$ |
| `lam` | lambda abstraction | $\lambda x.\; M$ |
| `hoare` | Floyd-Hoare triple | $\{P\}\; C \;\{Q\}$ |
| `hlt` | RMP halts / converges — Tab 0 = program (`P`), Tab 1 = input (`0`) | $P\left( 0 \right)\downarrow$ |
| `boo` | Cantor space $\{0,1\}^\omega$ | $\left\{0,1\right\}^{\omega}$ |
| `un` **Tab** | physical unit — thin space + upright roman | $9.8\,\mathrm{m\,s^{-2}}$ |

**Asymptotic complexity:**

| Trigger | Name | Renders as |
| ------- | ---- | ---------- |
| `asO` | Big-O | $O\!\left(n\right)$ |
| `softO` | soft-O (O-tilde) | $\widetilde{O}\!\left(n\right)$ |
| `aso` | little-o | $o\!\left(n\right)$ |
| `asTh` | Big-Theta | $\Theta\!\left(n\right)$ |
| `asW` | Big-Omega | $\Omega\!\left(n\right)$ |
| `asw` | little-omega | $\omega\!\left(n\right)$ |
