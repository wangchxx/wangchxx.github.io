+++
author = "Wang Chaohua"
title = "Mathematical Analysis | 9 Riemann Integrals"
date = "2021-04-09T10:52:59+02:00"

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

Definition 1 (**Partition**)
: Let $[a,b]$ be a given interval, by a `partition` $T$ of $[a,b]$, we mean a finite set of points $x_0,x_1,...,x_n$, where
$$ 
 a = x_0\leq x_1\leq \cdots\leq x_n = b
$$
We write $\Delta x_i = x_i  - x_{i-1}$, and denote $|T| = \max_i \Delta x_i$ as the `mesh` of the partition $T$.

Definition 2 (**Riemann sum**)
: Let $f$ be a given function defined on $[a,b]$, and $T$ be a partition of $[a,b]$. For any points $x_{i-1}\leq\xi\leq x_i$, $i=1,2,...,n$, the summation 
$$ 
 \sum_{i=1}^n f(\xi_i)\Delta x_i,
$$
is called the `Riemaan sum` of $f$ on $[a,b]$.


Definition 3 (**Riemann integrable**)
: Let $f$ be a given function defined on $[a,b]$, and $J$ be a fixed number. If for any $\epsilon>0$, there exists $\delta>0$, s.t. for every partition $T$ of $[a,b]$ with $|T|<\delta$ and for any choice of $\{\xi_i\}$ we have 
$$ 
 |\sum_{i=1}^n f(\xi_i)\Delta x_i - J|  <\epsilon,\tag{1}
$$
we say that the function $f$ is `Riemann integrable` on the interval $[a,b]$, we write $f\in\mathcal{R}$ and we denote the $J$ by $J = \int_a^b f(x) dx$.


Definition 4 (Stieltjes integral)
: Let $\alpha$ be an increasing and bounded function on $[a,b]$, $f:[a,b]\to \mathbb{R}$. For each partition $T$ of $[a,b]$, we write $\Delta \alpha_i = \alpha(x_i) - \alpha(x_{i-1})$. If for any $\epsilon>0$, there exists $\delta>0$, s.t. for every partition $T$ of $[a,b]$ with $|T|<\delta$ and for any choice of $\{\xi_i\}$ we have 
$$ 
 |\sum_{i=1}^n f(\xi_i)\Delta \alpha_i - J|  <\epsilon,\tag{2}
$$
we say that the function $f$ is `Stieltjes integrable` w.r.t. $\alpha$ on the interval $[a,b]$, and write $f\in \mathcal{R}(\alpha)$, denoted by $J = \int_a^b f(x) d\alpha(x)$.

By taking $\alpha(x) = x$, the Riemann integral can be viewed as a special case of the Stieltjes integral.

## 2. Existence

Theorem 5 (**Necessary condition**)
: If $f\in \mathcal{R}$ on $[a,b]$, then $f$ is bounded on $[a,b]$.

proof
: By contradiction. If $f$ is unbounded on $[a,b]$, then for any partition $T$ of $[a,b]$, there exists an interval $[x_{k-1},x_k]$ where $f$ is unbounded. Let $G = |\sum_{i\neq k} f(\xi_i) \Delta x_i|$, then for any $M>0$, there exists $\xi_k\in [x_{k-1},x_k]$ s.t. 
$$ 
 |f(\xi_k)\Delta x_k|> \frac{M+ G}{\Delta x_k}.
$$
So $|\sum_{i=1}^n f(\xi_i) \Delta x_i| \geq |f(\xi_k)\Delta x_k| - G > M$.

$\Box$

Suppose $T$ is a partition of $[a,b]$, and $f$ is bounded on $[a,b]$. Then we define $m_i,M_i$ as the lower bound and upper bound of $f$ on $[x_{i-1},x_i]$, respectively. Also we make summations,
$$ 
 L(T,f) = \sum_{i=1}^n M_i \Delta x_i, \quad U(T,f)  \sum_{i=1}^n m_i \Delta x_i.
$$
They are called the `upper sum` and `lower sum` of $f$ on $[a,b]$ with partition $T$, respectively. Similarly, we can define 
$$ 
   L(T,f,\alpha) = \sum_{i=1}^n M_i \Delta \alpha_i, \quad U(T,f,\alpha)  \sum_{i=1}^n m_i \Delta \alpha_i.
$$


Theorem 6
: $f\in\mathcal{R}(\alpha)$ on $[a,b]$ iff for any $\epsilon>0$, there exists a partition $T$ s.t. 
$$ 
 U(T,f,\alpha)  - L(T,f,\alpha)< \epsilon.\tag{3}
$$

proof
: For every $T$, we have that 
$$ 
   L(T,f,\alpha) \leq \underline{\int} f d\alpha \leq \overline{\int}fd\alpha\leq U(T,f,\alpha),
$$
where $\underline{\int} f d\alpha = \sup_T  L(T,f,\alpha)$ and $\overline{\int}fd\alpha =\inf_T U(T,f,\alpha)$. Then the assumption (3) implies that 
$$ 
 0\leq \overline{\int}fd\alpha - \underline{\int} f d\alpha <\epsilon,
$$
and hence $\overline{\int}fd\alpha = \underline{\int} f d\alpha$.

Conversely, if $f\in\mathcal{R}(\alpha)$, then for every $\epsilon>0$, there exist partitions $T_1,T_2$ s.t. 
$$ 
   U(T_2,f,\alpha) - \int_a^b f d\alpha<\epsilon/2, \quad \int_a^b f d\alpha - L(T_1,f,\alpha)<\epsilon/2.\tag{4}
$$
We choose $T = T_1\cup T_2$, then we have 
$$ 
   U(T,f,\alpha)\leq U(T_2,f,\alpha) < \int_a^b f d\alpha + \epsilon/2 < L(T_1,f,\alpha) + \epsilon \leq L(T,f,\alpha) + \epsilon.
$$

$\Box$

Corollary 7
: If $f$ is continuous on $[a,b]$, then $f\in\mathcal{R}(\alpha)$ on $[a,b]$.

proof
: For any $\epsilon>0$, we can choose $\eta>0$ s.t. 
$$ 
 |\alpha(b)  -\alpha(a)|\eta <\epsilon.
$$
Since $f$ is continuous on the closed interval $[a,b]$, it is uniformly continuous on $[a,b]$. There exists $\delta>0$ s.t. for any $x_1,x_2\in[a,b]$ satisfying $|x_1 - x_2|<\delta$,
$$ 
 |f(x_1) - f(x_2)|<\eta .
$$

Given a partition $T$ s.t. $|T|<\delta$, we have that $U(T,f,\alpha) - L(T,f,\alpha)<\epsilon$.

$\Box$


Theorem 8
: If $f$ is monotonic on $[a,b]$, and $\alpha$ is continuous on $[a,b]$,then $f\in\mathcal{R}(\alpha)$ on $[a,b]$.

proof
: For any $\epsilon>0,n$, we choose a partition $T$ s.t. 
$$ 
 \Delta \alpha_i = \frac{\alpha(b)- \alpha(a)}{n}.
$$
W.l.o.g. we assume that $f$ is increasing, then $M_i = f(x_i), m_i = f(x_{i-1})$, and thus $U(T,f,\alpha) - L(T,f,\alpha) = \frac{\alpha(b)- \alpha(a)}{n} (f(b) - f(a))<\epsilon$, by letting $n$ large enough.

$\Box$

Theorem 9
: Suppose $f$ is bounded on $[a,b]$, and has only finitely many points of  discontinuity, and $\alpha$ is continuous at each point where $f$ is discontinuous. Then $f\in\mathcal{R}(\alpha)$ on $[a,b]$.

proof
: Given any $\epsilon>0$, put $M = \sup_x |f(x)|$, and let $E$ be the set of points of discontinuity. Then we can cover $E$ by finitely many disjoint intervals $[u_i,v_i]\subset [a,b]$ s.t. $\sum |\alpha(v_i) - \alpha(u_i)|<\epsilon$. 

Let $K:= [a,b]\setminus \cup_i (u_i,v_i)$, we can see $K$ is a union of finitely many closed intervals, thus we can find a partition $T_K$ of $K$ s.t.
$$ 
   U(T_K,f,\alpha) - L(T_K,f,\alpha)<\epsilon.
$$
Consider intervals $(u_i,v_i)$, we can defined a partition $T$ of $[a,b]$ by $T = T_K\cup\{u_1,v_1,...,u_k,v_k\}$. It follows that 
$$ 
 U(T,f,\alpha) - L(T,f,\alpha)\leq  U(T_K,f,\alpha) - L(T_K,f,\alpha) + 2M\epsilon<\epsilon + 2M\epsilon.
$$

$\Box$

Theorem 10 (**Fundamental theorem of calculus**)
: If $f\in\mathcal{R}$ on $[a,b]$ and if $f$ possesses a primary function $F$, then 
$$ 
 \int_a^b f(x)dx = F(b) - F(a).
$$

proof
: For any $\epsilon>0$, choose a partition $T$ s.t. $U(T,f) - L(T,f)<\epsilon$. Then by the mean value theorem, we have $\eta_i\in[x_{i-1},x_i]$
$$ 
 F(x_i)  - F(x_{i-1}) = f(\eta_i)\Delta x_i.
$$
Thus $\sum_{i}^n f(\eta_i)\Delta x_i = F(b) - F(a)$. Because $\sum_{i}^n f(\xi_i)\Delta x_i \in [L,U]$, we obtain that for any $\xi_i \in[x_{i-1},x_i]$
$$ 
 |F(b) - F(a) - \sum_{i}^n f(\xi_i)\Delta x_i|<\epsilon  .
$$

$\Box$


## 3. Properties

Theorem 11 (**Integral mean value I**)
: If $f$ is continuous on $[a,b]$, then there exists $\xi\in[a,b]$ s.t. 
$$ 
 \int_a^b f(x) dx = f(\xi)(b-a).
$$

proof
: $m(b-a)\leq \int_a^b f(x) dx \leq M(b-a)$. It follows that 
$$ 
 m\leq \frac{1}{b-a}  \int_a^b f(x) dx \leq M.
$$
By the continuity of $f$, we can find $\xi\in[a,b]$ s.t. $f(\xi) = \frac{1}{b-a}  \int_a^b f(x) dx$.

$\Box$

Theorem 12
: If $f\in\mathcal{R}$ on $[a,b]$. For $x\in[a,b]$, put 
$$ 
 F(x) = \int_a^x f(t)dt.
$$
Then $F$ is continuous on $[a,b]$. Furthermore, if $f$ is continuous at $x_0$, then $F$ is differentiable at $x_0$, with 
$$ 
 F'(x_0) = f(x_0) .
$$

proof
: We know that $f$ is bounded $|f|\leq M$. Then $|F(y) - F(x)|\leq M |y-x|$. Given $\epsilon>0$, we see $|F(y) - F(x)|<\epsilon$, provided $|y - x|<\epsilon/M$. This shows the continuity of $F$.

Now suppose that $f$ is continuous at $x_0$. We can choose $\delta>0$ s.t. $|f(t) - f(x_0)|<\epsilon$ if $|t-x_0|<\delta$. Hence for any $s,t\in [a,b]$ s.t. $x_0\in [s,t]\subset U(x_0,\delta)$, we have that $F(t) - F(s) = (t-s) f(\xi)$ for some $\xi\in[s,t]$ by the Integral mean value theorem I. Then,
$$ 
 \bigg|\frac{F(t) - F(s)}{t-s} - f(x_0)\bigg| = |f(\xi) - f(x_0)|  <\epsilon.
$$

$\Box$

Theorem 13 (**Integral mean value II**)
: Suppose that $f\in\mathcal{R}$ on $[a,b]$.

1. If $g$ is decreasing on $[a,b]$ and $g\geq 0$, then there exists $\xi\in [a,b]$ s.t. 
$$ 
   \int_a^b f(x)g(x) dx = g(a)\int_a^\xi f(x)dx.
$$
2.  If $g$ is increasing on $[a,b]$ and $g\geq 0$, then there exists $\eta\in [a,b]$ s.t. 
$$ 
   \int_a^b f(x)g(x) dx = g(b)\int_\eta^b f(x)dx.
$$

proof
: We have shown that $F(x) = \int_a^x f(t)dt$ is continuous on $[a,b]$, and thus bounded. $g(a) = 0$ is trivial so we show the case $g(a)>0$ only. We shall find $\xi\in[a,b]$ s.t.
$$ 
 F(\xi) = \frac{1}{g(a)} \int_a^b f(x)g(x) dx.
$$

Now, by the intermediate value theorem, it suffices to show that
$$ 
   m\leq \frac{1}{g(a)} \int_a^b f(x)g(x) dx \leq M.
$$

