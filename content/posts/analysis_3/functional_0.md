---
author : "Wang Chaohua"
title : "Functional Analysis | 0 Preliminaries"
date : "2021-04-20T10:52:59+02:00"

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

# Functional Analysis | 0 Preliminaries


---
Notation:

- $\R$: the set of real numbers,
- $\mathbb{C}$: the set of complex numbers,
- $\N$: the set of positive integers.
- $\mathbb{F} = \{\R,\mathbb{C}\}$,
- $\Re_z$: the real part of complex number $z$,
- $\Im_z$: the imaginary part of complex number $z$,
- $sp(A)$: span of set $A$.
- $dim V$: dimension of vector space $V$.
---

## 1. Linear Algebra

Definition 1 (**Vector space**)
: A `vector space` over $\mathbb{F}$ is a non-empty set $V$ together with two function $x+y:V\times V\to V, \alpha x: \mathbb{F}\times V\to V$ satisfying for all $x,y,z\in V$ and all $\alpha,\beta\in\mathbb{F}$, 

    1. $x+y = y+x$,
    2. there exists a unique $0\in V$ s.t. $x+0 = x$,
    3. there exists a unique $-x\in V$ s.t. $x + (-x) = 0$,
    4. $1x = x$,
    5. $\alpha(x+y) = \alpha x + \alpha y, (\alpha+\beta)x = \alpha x + \beta x$.



Definition 2 (**Linear subspace**)
: Let $V$ be a vector space. A non-empty set $U\subset V$ is a `linear subspace` of $V$ if $U$ is itself a vector space, which is equivalent to the condition
$$ 
   \alpha x + \beta y \in U, \;\forall \alpha,\beta\in \mathbb{F}, x,y\in U.
$$

Definition 3 
: Let $S$ be a set and let $V$ be a vector space over $\mathbb{F}$. We denote the set of functions $f:S\to V$ by $F(S,V)$. With the definition of scalar multiplication and vector addition, $F(S,V)$ is a vector space over $\mathbb{F}$.

Definition 4 (Linear transformation)
: Let $V,W$ be vector spaces over $\mathbb{F}$. A function $T: V\to W$ is called a `linear transformation` if, for all $\alpha,\beta\in \mathbb{F}$ and $x,y\in V$
$$ 
 T(\alpha x + \beta y) = \alpha T(x) + \beta T(y).
$$
The set of all linear transformations $T:V\to W$ is denoted by $L(V,W)$. With the definition of scalar multiplication and vector addition, $L(V,W)$ is a vector space.

## 2. Metric Spaces

Definition 5 (Metric space)
: A `metric` on a set $M$ is a function $d:M\times M\to \R$ with the following properties,
  1. $d(x,y)\geq 0$,
  2. $d(x,y)= 0 \Leftrightarrow x=y$,
  3. $d(x,y) = d(y,x)$,
  4. $d(x,z)\leq d(x,y) + d(y,z)$.
  
  If $d$  is a metric on $M$, then the pair $(M,d)$ is called a `metric space`.

Given a metric space $(M,d)$ and a subset $U\subset M$, the restriction of $d$ to the subset $N$, denoted by $d_N$, is called the  the metric `induced` on $N$ by $d$.


Definition 6 (**Continuity**)
: Let $(M,d_M), (N,d_N)$ be two metric spaces and let $f:M\to N$ be a function.
    1. $f$  is continuous at $x\in M$, if for any $\epsilon>0$, there exists $\delta>0$ s.t. $y\in M, d(x,y)<\delta$ implies 
    $$ 
     d_N(f(x),f(y))<\epsilon.
    $$
    2. $f$ is continuous on $M$ if it is continuous at each $x\in M$.
    3. $f$ is uniformly continuous on $M$, if for any $\epsilon>0$, there exists $\delta>0$ s.t. $d(x,y)<\epsilon$ implies 
    $$ 
     d_N(f(x),f(y))<\epsilon.
    $$
    
    

Definition 6 (Completeness)
: A metric space $(M,d)$ is `complete` if every Cauchy sequence in $(M,d)$ is convergent. A subset $A\subset M$ is complete if every Cauchy sequence lying in $A$ converges to an element of $A$.

Theorem 7 (**Baire's category theorem**)
: If $(M,d)$ is a complete metric space and $M=\cup_{j\in\N}A_j$, where $A_j\subset M$, $j=1,2,...$, is closed, then at least one of the sets $A_j$ contains an open ball.

Definition 8 (**Compactness**)
: Let $(M,d)$ be a metric space. A set $A\subset M$ is `compact` if every sequence $\{x_n\}$ in $A$ contains a subsequence that converges to an element of $A$. The set $A$ is `relatively compact` if the closure $\bar{A}$ is compact. If he set $M$ itself is compact, then we say that $(M,d)$ is a compact metric space.

Compactness can also be defined in terms of `open coverings`, which is more appropriate in more general topological spaces. But in metric spaces both definitions are equivalent.

Theorem 8
: Suppose  that $(M,d)$ is a metric space and $A\subset M$. Then 
    1. if $A$ is complete, then $A$ is closed,
    2. if $M$ is complete,then $A$ is complete $\Leftrightarrow$ $A$ is closed,
    3. if $A$ is compact, then $A$ is closed and bounded,
    4. (Bolzano-Weierstrass theorem) every closed, bounded subset of $\mathbb{F}$ is compact.

A subset $A\subset M$ is bounded if $d(x,y)< M$ for all $x,y\in A$.

Theorem 9
: Let $(M,d)$ be a compact metric space, and let $f:M\to\mathbb{F}$ be a continuous function. Then 
    1. there exists $M>0$ s.t. $f(x)\leq M$ for all $x\in M$ ($f$ is bounded),
    2. in particular, if $\mathbb{F}=\R$  then $\sup_x f(x),\inf_x f(x)$ exist and are finite,
    3. furthermore, there exist $x_s,x_i\in M$ s.t. $f(x_s)=\sup_x f(x),f(x_i)=\inf_x f(x)$.


Definition 9
: Let $(M,d)$ be a compact metric space. The set of continuous functions $f:M\to \mathbb{F}$ will be denoted by $C(M)$. We define a metric on $C(M)$ by 
$$ 
 d(f,g) = \sup_{x\in M} |f(x) - g(x)|.
$$

The metric space $C(M)$ is complete.


Definition 10 (separable)
: A metric space $(M,d)$ is `separable` if it contains a countable, dense subset.


Theorem 11
: Suppose that $(M,d)$ is a metric space and $A\subset M$. 
    1. If $A$ is compact then it is separable.
    2. If $A$ is separable and $B\subset A$ then $B$ is separable.


