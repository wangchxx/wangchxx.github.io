+++
author = "Wang Chaohua"
title = "Mathematical Analysis | 7 Completeness of the Real Numbers"
date = "2021-04-07T10:52:59+02:00"

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


## 1. Nested Intervals Theorem

Definition 1 (**Nested intervals**)
: A sequence of closed intervals $\{[a_n,b_n]\}$ is called a sequence of `nested closed intervals` if 
1. $[a_{n+1}, b_{n+1}]\subset [a_n, b_n]$,
2. $\lim_{n\to\infty}(b_n - a_n) = 0$.

Theorem 2 (**Nested intervals theorem**)
: Let $\{[a_n,b_n]\}$ be a sequence of nested closed intervals, there exist a unique real number $\xi$ s.t. $\xi\in [a_n,b_n]$ for every $n$.

proof
: Notice that $\{a_n\}$ is an increasing and bounded sequence, and thus it has limit $\xi$ s.t. $\xi\geq a_n$ for all $n$. Similarly, the sequence $\{b_n\}$ also has a limit. Combing (ii) of the definition, we have 
$$ 
 \lim_{n\to\infty}a_n =   \lim_{n\to\infty}b_n = \xi,
$$
and $a_n\leq \xi\leq b_n$ for all $n$. The left work is to show the uniqueness. Suppose that there exists another $\xi'$ s.t. $a_n\leq \xi'\leq b_n$, we have 
$$ 
 |\xi - \xi'|\leq b_n - a_n \to 0,
$$
which means that $\xi = \xi'$.

$\Box$

## 2. Finite Open Covers

Definition 3 (**Closure point**)
: Let $S$ be a set of real numbers, $\xi$ be a fixed point, if for any neighbourhood of $x_0$, $U(x_0,\delta)$, we have 
$$ 
 |U(x_0,\delta)\cap S|  = \infty,
$$
we say that $\xi$ is a `closure point` of $S$.

The definition is equivalent to 

3' for any neighbourhood of $x_0$, $U(x_0,\delta)$, we have $U^o(x_0,\delta)\cap S \neq \emptyset$.

3'' there exists a convergent series $\{x_n\}\subset S$ with distinct elements s.t. $\lim_{n\to\infty} x_n = \xi$.

proof
: 3 $\Rightarrow$ 3' is trivial. 3'' $\Rightarrow$ 3 is trivial. We only show 3' $\Rightarrow$ 3''. Let $\delta_1 = 1$, we can find $x_1\in U^o(\xi,\delta_1)\cap S$, then we let $\delta_2 = \min\{1/2, |\xi - x_1|\}$, we can find $\xi_2\in U^o(\xi,\delta_2)\cap S$ and $x_1\neq x_2$, $\ldots$, let $\delta_2 = \min\{1/n, |\xi - x_{n-1}|\}$, we can find $\xi_2\in U^o(\xi,\delta_2)\cap S$ and $x_n$ is different from $x_1,...,x_{n-1}$.

Continue this procedure, we obtain a sequence of distinct numbers $\{x_n\}$ with $|\xi - x_n|<\delta_n\leq 1/n\to 0$.

Theorem 4 (**Bolzano–Weierstrass theorem**)
: Every bonded sequence of real numbers has at least one closure point.

proof
: `method 1:` suppose $\{x_n\}$ is bounded in $[-M,M] = [a_1,b_1]$, we can separate it into two equally long intervals and at least one of them contains infinitely many elements of the sequence. Apply this procedure iteratively, we can obtain a sequence of nested closed intervals $\{[a_n,b_n]\}$ in which every interval contains infinitely many elements of the sequence. 

By the nested intervals theorem, there exists a unique $\xi\in [a_n,b_n]$, $n=1,2,...$, then $\xi$ is a closure point.

`method 2:` we can take a subsequence with distinct elements of the sequence. Because it is bounded, we can find a further subsequence convergent to $x_0$, then $x_0$ is a closure point.

$\Box$

Definition 5 (**Open covers**)
: Let $S$ be a set of real numbers, $H$ be a set of open intervals. If $S\subset H$, we say that $H$ is an `open cover` of $S$. Furthermore, if $|H|<\infty$, we say that $H$ is a `finite open cover` of $S$.

Theorem 6 (**Heine-Borel finite open cover**)
: Let $H$ be an open cover of a closed interval $[a,b]$, then there exists a finite subset $H_1\subset H$ that covers $S$.

proof
: By contradiction. If such subset does not exist, we can separate $[a,b]$ equally into two intervals s.t. at least one of them cannot covered by a finite subset of $H$, denote such interval by $[a_1,b_1]$. It obvious that $[a_1,b_1]\subset [a,b]$ and $b_1 - a_1 = 1/2(b-a)$.

Apply this procedure for infinitely times, we can obtain a sequence of closed intervals $\{[a_n,b_n]\}$ a.t. $b_n - a_n = 1/2^n(b-a)\to 0$ and every $[a_n,b_n]$ cannot be covered by a finite subset of $H$.

By the nested intervals theorem, there exists a unique $\xi\in [a_n,b_n]$ for $n=1,2,...$. Since $H$ is an open cover of $S$, there exists an open interval $(\alpha,\beta)\in H$ s.t. $\xi \in (\alpha,\beta)$. Then there exists a integer $N$ s.t. for any $n\geq N$, $[a_n,b_n]\subset (\alpha,\beta)$, which contradicts with the fact that every $[a_n,b_n]$ cannot be covered by any finite subset of $H$.

$\Box$

Note that this theorem can be only applied to closed intervals $[a,b]$.

## 3. Equivalence

So far we have studied six fundamental theorems about the completeness of the real numbers. 

1.  `Least-upper-bound property`. If $S$ has an upper bound, then $\sup S$ exists. If $S$ has an lower bound, then $\inf S$ exists.
2. `Monotone convergence theorem`. If $\{a_n\}$ is monotonic and bounded sequence of real numbers, then $\{a_n\}$ is convergent.
3. `Nested intervals theorem`.
4. `Heine-Borel finite open cover`.
5. `Bolzano–Weierstrass theorem`.
6. `Cauchy completeness`. Every Cauchy sequence of real numbers converges.

proof
: $1\Rightarrow 2\Rightarrow 3 \Rightarrow 4$ has been shown. For $4\Rightarrow 5$, we can show it by contradiction. If it has not closure points, we cannot find an open interval containing infinitely many points of $S$. For $5\Rightarrow 6$, a Cauchy sequence is bounded.

$6\Rightarrow 1$. Construct a Cauchy sequence of upper bounds of $S$.

$\Box$


