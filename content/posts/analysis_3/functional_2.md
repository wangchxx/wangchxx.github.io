---
author : "Wang Chaohua"
title : "Functional Analysis | 2 Hilbert Spaces"
date : "2021-04-22T10:52:59+02:00"

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



## 1. Inner Product spaces

Definition 1 (**Inner product**)
: Let $X$ be a vector space. An inner product on $X$ is a function $<\cdot,\cdot>:X\times X\to \mathbb{F}$, s.t. for all $x,y,z\in X$, $\alpha,\beta\in\mathbb{F}$,
   1. $< x,x >\geq 0$,
   2. $< x,x > = 0 \Leftrightarrow x = 0$ ,
   3. $< \alpha x + \beta y ,z> = \alpha < x,z > + \beta < y,z >$,
   4. $ < x,y > = \overline{< y,x >}$.

   A vector space $X$ with an inner product $< >$ is called an `inner product space`.

With an inner product, we can define a norm by $|| x|| = \sqrt{< x, x>}$, and hence we can define a metric $d$.

Lemma 2 (**Continuity of inner product**)
: let $X$ be an inner product space, and suppose that $\{x_n\}, \{y_n\}$ are convergent sequences $X$ with $x_n \to x, y_n\to y$. Then 
$$ 
 < x_n, y_n > \to < x, y>.
$$

proof
: 
$$
\begin{align*}
    | < x_n , y_n> - < x , y> | &\leq | < x_n , y_n> - < x_n , y> | + | < x_n , y> - < x , y> | \cr
    &\leq ||x_n|| ||y_n - y|| + ||y|| ||x_n - x||\to 0 
\end{align*}
$$


## 2. Hilbert Spaces

Definition 3 (Hilbert space)
: An inner product space is called a `Hilbert space` if it is complete w.r.t. the metric associated with the norm induced by the inner product.

Lemma 4
: Let $\mathcal{H}$ be a Hilbert and $Y\subset \mathcal{H}$  is a linear subspace, then $Y$ is a Hilbert space iff $Y$ is closed.

proof
: A subset of a complete metric space is complete iff it is closed.

$\Box$

Lemma 5
: Let $Y$ be a linear subspace of an inner product space $X$. Then 
$$ 
 x\in Y^\perp \Leftrightarrow || x-y|| \geq ||x||,\;\forall y\in Y.
$$

proof
: ($\Rightarrow$) $|| x - y||^2 = ||X||^2 + ||y||^2$ if $x\perp y$.

  $\Leftarrow$ $||x - \alpha y||^2 - ||x||^2$ is minimized at $\alpha = $.

$\Box$

Theorem 6 (Projection theorem)
: Let $A$ be a closed linear subspace of a $\mathcal{H}$. Then for any $x\in \mathcal{H}$, there exists a unique $x_0 \in A$ s.t. 
$$ 
 ||x-x_a|| = \inf_{y\in A} || x- y||,
$$
and $x - x_a \in A^\perp$.

proof
: Suppose  $\gamma = \inf_{y\in A} || x- y||$. We first prove the existence of $x_0$. For each $n$, there exists $x_n\in A$ s.t. 
$$ 
 ||x - x_n||^2 < \gamma^2+ 1/n.
$$
Applying the parallelogram rule to $x-x_n, x - x_m$, we can show that $\{x_n\}$ is Cauchy. So $x_n \to x_0 , x_0 \in A$. Then we obtain the equality by the continuity of inner product.

  Uniqueness. Suppose that $x'\in A$ makes the equality. Then $(x_0, x')/2 \in A$ by linearity, and $||x - (x_0, x')/2 \in A||\geq \gamma$. Applying the parallelogram rule to $x - x', x-x_0$, we obtain that $||x_0 - x'||^2 = 0$.
 
  Finally, $x-x_0\in A^\perp$ follows from Lemma 2.5.

 $\Box$


Let $\{e_n\}$ a orthonormal system in an infinite-dimensional Hilbert space $X$, then for any $x\in X$, 
$$ 
 x = \sum_{n=1}^\infty < x, e_n> e_n.
$$

proof
: By Bessel's inequality, we obtain that $ \sum_{n=1}^\infty |< x, e_n>|^2<\infty$. Also we can show that $y_k = \sum_{n=1}^k < x, e_n> e_n$ is Cauchy and converges to $x$.

$\Box$


Lemma 7 (**Bessel's inequality**)
: Let $X$ be an inner product space and let $\{e_n\}$ a orthonormal system in $X$. Then for any $x\in X$ the series $\sum_{n=1}^\infty |< x, e_n>|^2$ converges and 
$$ 
   \sum_{n=1}^\infty |< x, e_n>|^2 \leq ||x ||^2.
$$

proof
: Let $y_k = \sum_{n=1}^k < x, e_n> e_n$. Then 
$$ 
 ||x - y_k||^2 = ||x||^2 - ||y_k||^2.
$$
It shows that $||y_k||^2 \leq ||x||^2$ for all $k\in\N$. In addition $||y_k||^2$ is increasing and bounded, so it is convergent.

$\Box$

Definition (**Separability**)
: A Hilbert space $\mathcal{H}$ is called `seperable` if there is an at most countable orthonormal system $\{e_n\}$ s.t. 
$$ 
 \mathcal{H} = \overline{sp}(\{e_n\}) .
$$
