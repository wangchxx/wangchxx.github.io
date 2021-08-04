+++
author = "Wang Chaohua"
title = "Mathematical Analysis | 1 Real Numbers and Functions"
date = "2021-04-01T10:52:59+02:00"

tags = [
    "math",
]
categories = [
    "analysis"
]
series = ["math analysis"]
aliases = ["migrate-from-jekyl"]
math=true

+++




## 1. Real Numbers

Definition 1 (Bounds)
: $S\in\mathbb{R}$. We say that $S$ is *bounded above* if there exits $M$ s.t. for every $x\in S$ $x\leq M$, and $M$ is called the *upper bond* of $S$. Similarly, we say that $S$ is *bounded from below* if $x\geq M$, and $M$ is called the *lower bound* of $S$.

We say that $S$ is bounded if its upper bounds and lower bounds exist.

Definition 2 (Supremum and infimum)
: Let $\eta$ be an upper bound of $S$. If for any $\alpha<\eta$ there exists $x_0\in S$ s.t. $x_0>\alpha$, then $\eta$ is called the *supremum* of $S$, denoted by $\eta = \sup S$. Similarly, $\eta$ is the *infimum* of $S$, denoted by $\eta = \inf S$, if for any $\alpha>\eta$, there exits $x_0\in S$ s.t. $x_0<\alpha$.

Theorem 3 (Existence)
: If $S$ has an upper bound, then $\sup S$ exists. If $S$ has an lower bound, then $\inf S$ exists.

Corollary 4
: Given nonempty sets $A,B$. If $\forall x\in A,\forall y\in B$ $x\leq y$, then $\sup A$ and $\inf B$ exist. Moreover, $\sup A\leq \inf B$.

proof:
The existence of $\sup A$ and $\inf B$ is immediate by Theorem 3. We show the inequality only. Because $y$ is an upper bound of $A$ for any $y\in B$, $\sup A\leq y$. It suggests that $\sup A$ is a lower bound of $B$, hence $\sup A\leq \inf B$. 



## 2. Functions
Definition 5 (Functions)
: A mapping $f: D\to M$ is a *function* if for every $x\in D$, there exists a unique $y\in M$ s.t. $f(x) = y$. $D$ is called the *domain* of $f$, $M$ is called the *codomain* of $f$, and $f(D):=\{f(x): x\in D\}$ is the *range* of $f$.

Definition 6 (Inverse functions)
: Given a function $f: D\to M$, if for any $y\in f(D)$ there is a unique $x\in D$ s.t. $f(x) = y$, then we can define a function 
$$ 
 f^{-1}: f(D)\to D,
$$
which is called the *inverse function* of $f$.


It is obvious that $f^{-1}$ exists $\Leftrightarrow$ $f$ is bijective.

Definition 7 (Elementary functions)
: 
1. constants, $f(x) = c$.
2. power of $x$, $f(x) = x^a$.
3. exponential, $f(x) = a^x$.
4. logarithm, $f(x) = \log_a x$.
5. trigonometric, $f(x) = \sin x$.
6. inverse trigonometric, $f(x) = \arcsin x$.


Definition 8 (Bounded functions)
: A function $f: D\to M$ is *bounded* if there exists a constant $M$ s.t. $f(x)\leq M$ for every $x\in D$.


Definition 9 (Monotonicity)
: $f$ is an *increasing function* if $f(x_1)\leq f(x_2)$ for every $x_1< x_2$, and is *strictly increasing* if $f(x_1)<f(x_2)$.


Theorem 10 
: If $f:D\to M$ is a strictly increasing function, then $f^{-1}$ exists. Moreover, $f^{-1}$ is also strictly increasing on $f(D)$.


