+++
author = "Wang Chaohua"
title = "Mathematical Analysis | 4 The Continuity of Functions"
subtitle = "The Continuity of Functions"
date = "2021-04-04T10:52:59+02:00"

tags = [
    "markdown",
]
categories = [
    "analysis"
]
series = ["math analysis"]
aliases = ["migrate-from-jekyl"]
math = true

+++


## 1. Definitions 
Definition 1 (**Continuity at $x_0$**)
: Given a function $f$ defined on $U(x_0,\delta)$. If $\lim_{x\to x_0} = f(x_0)$, $f$ is said to be *continuous at $x_0$*.

That $f$ is continuous at $x_0$ implies that we can interchange the order of $\lim$ and $f$, 
$$ 
 \lim_{x\to x_0} = f(\lim{x\to x_0} x).
$$


We introduce a new terminology "increment", which is defined by $\Delta x = x - x_0$ and $\Delta y = y- y_0 = f(x_0 + \Delta x) - f(x_0)$. Now the continuity of function $f$ at $x_0$ is equivalent to 
$$ 
 \lim_{\Delta x\to 0} \Delta y = 0.
$$

Definition 2 (**Discontinuity at $x_0$**)
: Given a function $f$ defined on $U^o(x_0,\delta)$. If $f$ is not defined at $x_0$ or $f$ is well defined at $x_0$ but not continuous at $x_0$, $f$ is said to be *discontinuous at $x_0$* and $x_0$ is called a discontinuity of $f$.

According to the definition, if $x_0$ is a discontinuity of $f$, then one of the following cases must happen:

1. $f$ is not defined at $x_0$.
2. $f$ is defined at $x_0$, but the limit of $f$ at $x_0$ does not exist.
3. $f$ is defined at $x_0$ and the limit $\lim_{x\to x_0}f(x)$ exists, but $\lim_{x\to x_0}f(x) \neq f(x_0)$.

Therefore, a discontinuity of $f$ can be classified into one of the three types:

1. removable discontinuity. Suppose $\lim_{x\to x_0}f(x) = A$, then $x_0$ is called a removable discontinuity of $f$ if $f$ is not defined on $x_0$ or $f(x_0)\neq A$. 
2. jump discontinuity. The two one-sided limits of $f$ at $x_0$ exist but they are not equal. 
3. essential discontinuity. At least one of the two one-sided limits does not exist.


Definition 3 (**Continuity on an interval**)
: Given a interval $I$, if function $f$ is continuous at every point in $I$,then $f$ is said to be continuous on $I$.


## 2. Properties
Proposition 4 (**Continuous at $x_0$**)
:  
1. locally bounded. If $f$ is continuous at $x_0$, then $f$ is bouned in some neighbourhood $U(x_0,\delta)$.

2. locally signed. If $f$ is continuous at $x_0$, and $f(x_0)>0$, then for any $0<c<f(x_0)$, there exists a neighbourhood $U(x_0,\delta)$ s.t. for all $x\in U(x_0,\delta)$, $f(x)>r$.

3. closed on plus and multiplication.

4. compound. If $f$ is continuous at $x_0$ and $g$ continuous at $u_0$, $u_0 = f(x_0)$, then $f\circ g$ is continuous at $x_0$.

Proposition 5 (Continuous on $[a,b]$)
: 
1. boundedness. If $f$ is continuous on an interval $[a,b]$, then $f$ has its maximum and minimum on $[a,b]$ (bounded).

2. mean-value. If $f$ is continuous on an interval $[a,b]$ and $f(a)\neq f(b)$, then for any $u\in(f(a),f(b))$ there exists $\xi\in(a,b)$ s.t. $f(\xi)=u$.

3. inverse function. If $f$ is continuous and strictly monotone on an interval $[a,b]$, then $f^{-1}$ is continuous ot its domain.

## 3. Uniformly Continuous
Definition 6 (**Uniformly continuous**)
: Given a function $f$ defined on an interval $I$, $f$ is said to be *uniformly continuous* on $I$ if for any $\epsilon>0$, there exists $\delta$ s.t. for all $|x_1 - x_2|<\delta$ we have $|f(x_1) - f(x_2)|<\epsilon$.

Uniform continuity is stronger than the ordinary continuity.

Theorem 7 (**Uniformly continuous**)
: If $f$ is continuous on $[a,b]$, then $f$ is uniformly continuous on $[a,b]$

proof
: By contradiction. If not, there exists $\epsilon_0$ s.t. for any $\delta>0$ we can find sequences $\{x_n\},\{y_n\}$ with $\lim_{n\to\infty}(x_n - y_n) = 0$ but $|f(x_n) - f(y_n)|\geq \epsilon_0$. By the boundedness, we can find subsequences  $\{x_{nk}\},\{y_{nk}\}$ convergent to $x_0$.

Now we obtain a contradiction, $\epsilon_0\leq |f(x_{nk}) - f(y_{nk})|\to 0$.

$\Box$