+++
author = "Wang Chaohua"
title = "Mathematical Analysis | 2 Limit of Sequences"
date = "2021-04-02T10:52:59+02:00"

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


## 1. Limit of Sequences
Given a function $f:\mathbb{N}\_{+}\to \mathbb{R}$, we call $f( \mathbb{N}_{+})$ as a *sequence*, enumerated as $a_1,a_2,\ldots$, denoted by $\{a_n\}$.

Definition 1 (Convergence)
: We say a sequence $\\{a_n\\}$ is *convergent* to $a$ if for any $\epsilon>0$, there exits a constant $N$ s.t. for any $n\geq N$,
$$ 
 |a_n - a|<\epsilon.
$$
And the point $a$ is called the *limit* of the sequence $\{a_n\}$, denoted by $\lim_{n\to\infty}a_n = a$.

An equivalent definition of the convergence of a sequence is given by,

Definition 2 (Convergence 2)
: The sequence $\\{a_n\\}$ is convergent to $a$ if for any $\epsilon>0$, there are at most finite elements $a_n$ outside the neighbourhood $U(a,\epsilon)$.

A sequence $\{a_n\}$ is called `infinitesimal` if $\lim_{n\to\infty}a_n = 0$.

Proposition 3 (Properties)
: 
1. the limit of a sequence is unique.
2. $\{a_n\}$ is bounded if $\lim_{n\to\infty}a_n = a$.
3. if $\lim_{n\to\infty}a_n = a>0$, then for any $b\in(0,a)$ there exists a constant $N$ s.t. for every $n\geq N$ 
$$ 
 a_n >b.  
$$
4. Given two convergent sequences $\{a_n\}$ and $\{b_n\}$. If there exist $N$ s.t for any $n\geq N$, $a_n\leq b_n$, then $\lim_{n\to\infty}a_n\leq \lim_{n\to\infty}b_n$.
5. Given sequences $\{a_n\}$,$\{b_n\}$ and $\{c_n\}$, if $\lim_{n\to\infty}a_n = \lim_{n\to\infty}b_n =a$ and there exists $N$ s.t for any $n\geq N$
$a_n \leq c_n\leq b_n,$ then $\lim_{n\to\infty}ac_n = a$.



Theorem 4 (Convergence)
: A sequence $\{a_n\}$ is convergent iff every subsequence of $\{a_n\}$ is convergent.

## 2. Existence of the limit of sequence

Theorem 5 (**Monotone convergence theorem**)
: If $\{a_n\}$ is monotonic and bounded sequence of real numbers, then $\{a_n\}$ is convergent.

Theorem 6 (Dense)
: If $\{a_n\}$ is bounded, then $\{a_n\}$ possesses a convergent subsequence.

Theorem 7 (**Cauchy criterion**)
: A sequence $\{a_n\}$ of real numbers is convergent iff it is a Cauchy sequence, i.e. for any $\epsilon>0$ there exists $N$ s.t. for any $n,m\geq N$ 
$$ 
 |a_n - a_m|<\epsilon.
$$
