---
author : "Wang Chaohua"
title : "Functional Analysis | 1 Normed Spaces"
date : "2021-04-21T10:52:59+02:00"

tags : [
    "markdown",
]
categories : [
    "analysis"
]
series : ["functional analysis"]
# aliases : ["migrate-from-jekyl"]
math : true
---



## 1. Finite-dimensional Normed Spaces

Definition 1 (Norm)
: Let $X$ be a vector space over $\mathbb{F}$. A `norm` on $X$ is a function $||\cdot||:X\to\R$ s.t. for all $x,y\in X$ and $\alpha\in\mathbb{F}$,
    1. $|| x||\geq 0$ ,
    2. $||x||=0$ iff $x=0$,
    3. $|| \alpha x|| = |\alpha| || x||$,
    4. $||x+y||\leq ||x|| + ||y||$.

    A vector $X$ equipped with a norm is called a `normed vector space` or just a `normed space`. In particular, a `unit vector` in $X$ is a vector $x$ s.t. $||x||=1$.

Example 2 (**Norms on $\mathbb{F}^n$**)
: Let $x=(x_1,...,x_n)$, $||x || = \left(\sum_{i=1}^n |x_i|^2\right)^{1/2}$ is a norm.

Example 3 (**Norms on $C(M)$**)
: Let $M$ be a compact metric space and let $C(M)$ be the vector space of functions defined on $M$. Then the function $||\cdot||:C(M)\to\R$ given by 
$$ 
 ||f|| = \sup_{x\in M} |f(x)|
$$
is a norm on $C(M)$.

Example 4 (**Norms on $L^p$**)
: Let $(X,\Sigma,\mu)$ be a measure space. 
  1. If $1\leq p <\infty$, then $||f||_p = \left(\int |f|^p \;d\mu\right)^{1/p}$ is a norm on $L^p(X)$.
  2. If $p=\infty$, then $||f||_\infty = \mathrm{ess}\sup |f|$ is a norm on $L^\infty(X)$, where the `essential supremum` $\mathrm{ess}\sup$ of a measurable function $f$ is defined by 
$$ 
 \mathrm{ess}\sup f = \inf \{b: f(x)\leq b \; a.e.\}  .
$$


Lemma 5 (Norm and metric)
: Let $X$ be a vector space equipped with norm $||\cdot||$. If $d: X\times X\to\R$ is defined by $d(x,y) = ||x-y||$, then $(X,d)$ is a metric space.

Notice that there can be many different norms on each finite-dimensional space.

Definition 6 (Equivalence)
: Let $X$ be a vector space and let $||\cdot||_1$ and $||\cdot||_2$ be two norms on $X$. We say the norm $||\cdot||_2$ is `equivalent` to the norm $||\cdot||_1$ if there exists $M,m>0$ s.t. for all $x\in X$
$$ 
m||x||_1 \leq ||x||_2 \leq M||x||_1.
$$

Theorem 7
: Let $X$ be finite-dimensional vector space with norm $||\cdot||$ and let $\{e_1,...,e_n\}$ be a basis for $X$. We define another norm $||\cdot||_1$ on $X$ by 
$$
\begin{equation}
 || \sum\_{j=1}^n \lambda_j e_j||_1 =   \left(\sum\_{i=1}^n |\lambda_i|^2\right)^{1/2}.
\end{equation}
$$
Then norms $||\cdot||$ and $||\cdot||_1$ are equivalent.

proof
: Let $M = \left(\sum_{i=1}^n ||e_i||^2\right)^{1/2}$. Then we have 
$$
 \begin{align*}
    || \sum_{i=1}^n \lambda_i e_i|| &\leq  \sum_{i=1}^n ||\lambda_i e_i|| \cr
        &=\sum_{i=1}^n |\lambda_i | ||e_i|| \cr
        &\leq \left(\sum\_{i=1}^n |\lambda_i|^2\right)^{1/2} \left(\sum\_{i=1}^n ||e_i||^2\right)^{1/2} \cr
        &= M|| \sum\_{j=1}^n \lambda_j e_j||_1
 \end{align*}
$$
Next, we define a function $f$ by 
$$ 
 f(\lambda_1,...,\lambda_n) =   || \sum\_{i=1}^n \lambda_i e_i||.
$$
The function $f$ is continuous w.r.t. the standard metric. Now we define $S$ be the unit circle, i.e. 
$$ 
 S = \{(\lambda_1,...,\lambda_n): \sum\_{i=1}^n |\lambda_i|^2 = 1\}.
$$
Since $S$ is compact, there exists $(u_1,...,u_n)\in S $s.t. $f(u_1,...,u_n)\leq f(\lambda_1,...,\lambda_n)$ for all $(\lambda_1,...,\lambda_n)\in S$. Let $m = f(u_1,...,u_n)$. Notice that $m>0$.

    By the definition of $||\cdot||_1$, if $||x||_1=1$ then $||x||\geq m$. Therefore $y\in X\setminus\{0\}$, we have $|| \frac{y}{||y||_1}||\geq m$ since $|| \frac{y}{||y||_1}||_1 = 1$. It follows that 
    $$
     ||y||\geq m ||y||_1.
    $$
For $y=0$, it still holds.

$\Box$

Corollary 8 (**Equivalent norms & finite-dimensional**)
: If $||\cdot||$ and $||\cdot||_2$ are any two norms on a finite-dimensional vector space $X$, then they are equivalent

proof
: By Theorem 1.7, we can see that both $||\cdot||$  and $||\cdot||_2$ are equivalent to $||\cdot||_1$.

$\Box$

Lemma 9 (**Complete metric space & finite-dimensional**)
: Let $X$ be finite-dimensional vector space with norm $||\cdot||_1$ that is defined as (1) and let $\{e_1,...,e_n\}$ be a basis for $X$. Then $X$ is a complete metric space.

proof
: Let $\{x_m\}$ be a Cauchy sequence. It implies when $k,m\geq N$,
$$ 
 \sum_{j=1}^n |\lambda_{j,k} - \lambda_{j,m}|^2 = ||x_k - x_m ||_1^2 <\epsilon.
$$
Hence $\{\lambda_{j,m}\}$ is a Cauchy sequence for $j\leq n$. And since $\mathbb{F}$ is complete, there exists $\lambda_j\in\mathbb{F}$ s.t. $\lambda_{j,m}\to \lambda$. Define $x = \sum_{j=1}^n \lambda_je_j$, we have $||x_m - x ||_1^2\to 0$.

$\Box$

This lemma means that for any norm on a finite-dimensional space $X$, $X$ is a complete metric space.

Corollary 10
: If $Y$ is a finite-dimensional subspace of a normed vector space $X$, then $Y$ is closed.

proof
: Y is a complete metric space by Lemma 1.10. Hence $Y$ is closed since any complete subset of a metric space $X$ is closed.

$\Box$

## 2. Banach Spaces
In this Section we turn to infinite-dimensional vector spaces.

Lemma 11
: If $X$ is a normed vector space and $S$ is a linear subspace of $X$ then $\bar{S}$ is also a linear subspace of $X$.

proof
: Let $x,y \in\bar{S}$, so we can find sequences $\{x_n\},\{y_n\}$ in $S$ s.t. 
$$ 
 x_n\to x, y_n\to y.
$$
Then $x+y\in\bar{S}$ and $\alpha x \in\bar{S}$.

$\Box$

Let $X$ be a normed vector space and $E\subset X,E\neq \empty$. The `closed linear span` of $E$, denoted by $\overline{sp}(E)$, is the intersection of all closed linear subspaces of $x$ which contain $E$.


Theorem 12 (**Riesz's**) <span id = "c1_Riesz">
: Let $X$ is a normed vector space, $Y$ is closed linear subspace of $X$ s.t. $Y\neq X$, and $\alpha\in(0,1)$. Then there exists $x_\alpha\in X$ s.t. 
$$ 
 ||x_\alpha|| = 1, \quad ||x_\alpha - y||>\alpha, \;\forall y\in Y.
$$

proof
: Let $x\in X\setminus Y$. Also, since $Y$ is closed, 
$$ 
 d = \inf\{||x-z||: z\in Y\}  >0.
$$
Thus there exists $z\in Y$ s.t. $||x-z||< d \alpha^{-1}$. Let $x_\alpha = \frac{x-z}{||x-z||}$. Then for any $y\in Y$
$$
 \begin{align*}
 ||x_\alpha - y|| &= \frac{1}{||x-z||} || x - (z - ||x-z||y)||\cr
    &>\alpha d^{-1} d.
 \end{align*}
$$

$\Box$

Theorem 13 (**Compactness & infinite-dimensional**)
: Let $X$ be an infinite-dimensional normed vector space, then neither $D =\{x\in X: ||x||\leq 1\}$ nor $K =\{x\in X: ||x||= 1\}$ is compact.

proof
: Let $x_1\in K$, then $sp(x_1)$ is closed. By Riesz's, there exists $x_2\in K$ s.t. 
$$ 
 || x_2 - a x_1|| \geq 3/4, \;\forall a\in\mathbb{F}.
$$
Go on with $sp(x_1,x_2)$, we have $x_3\in K$ s.t. 
$$ 
 || x_3 - a x_1 - b x_2||\geq 3/4,\; \forall a,b\in\mathbb{F}.
$$
Continuing this way, we obtain a sequence $\{x_n\}$ in $K$ s.t. $||x_n - x_m||\geq 3/4$ when $n\neq m$. This cannot have a convergent subsequence.

$\Box$

Recall that in a finite-dimensional normed space, any closed bounded set is compact, but this is not true for infinite-dimensional spaces.


Definition 14 (**Banach space**)
: A `Banach space` is a normed vector space which is complete relative to the metric associated with the norm.

Theorem 15
: 1. Any finite-dimensional normed vector space is a Banach space.
    2. if $X$ is a compact metric space then $C(X)$ is a Banach space.
    3. if $(X,\Sigma,\mu)$ is a measure space, then $L^p(X)$ is a Banach space for $1\leq p\leq \infty$.
    4. $\ell^p$ is a Banach space for $1\leq p\leq \infty$.
    5. If $X$ is a Banach space and $Y$ is a linear subspace of $X$, then $Y$ is a Banach space $\Leftrightarrow$ $Y$ is closed in $X$.


proof
: 1. Any finite-dimensional normed vector space is complete.
    2. $C(M)$ is complete.
    3. $L^p(X)$ is complete.
    4. $\ell^p$ is a special case of $L^p$ by taking counting measure on $\N$.
    5. A subset of a complete metric space is complete iff it is closed.
$\Box$