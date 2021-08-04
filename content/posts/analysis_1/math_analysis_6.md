+++
author = "Wang Chaohua"
title = "Mathematical Analysis | 6 Mean Value Theorem"
date = "2021-04-06T10:52:59+02:00"

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


## 1. Rolle's Theorem

Theorem 1 (Rolle's theorem)
: If a function $f$ satisfies 
1. $f$ is continuous on a closed interval $[a,b]$,
2. $f$ is differentiable on $(a,b)$,
3. $f(a) = f(b)$,

then there exists a number $\xi\in(a,b)$ s.t. $f'(\xi)= 0$.

proof
: Because $f$ is continuous on $[a,b]$, $f$ has maximum and minimum, denoted by $M$ and $m$ respectively. If $m= M$, then $f$ is constant, hence the assertion is true. In the case $m<M$, the assumption $f(a) = f(b)$ implies that at least one of the maximum and minimum is achieved at $\xi\in(a,b)$. Then the Fermat's theorem completes the proof.

$\Box$

Theorem 2 (Lagrange's theorem)
: If a function $f$ satisfies
1. $f$ is continuous on a closed interval $[a,b]$,
2. $f$ is differentiable on $(a,b)$,

then there exists a number $\xi\in(a,b)$ s.t. 
$$ 
 f'(\xi) = \frac{f(b)- f(a)}{b -a}.
$$
We can see that the Rolle's theorem is a special case of Lagrange's theorem with $f(a) = f(b)$.

proof
: Define a function $F(x) = f(x) - f(a) -\frac{f(b)- f(a)}{b -a} (x- a)$. Obviously, $F(a) = F(b) = 0$, then by Rolle's we see the existence of $\xi\in(a,b)$ s.t. $F'(\xi) = 0 \Rightarrow f'(\xi) =\frac{f(b)- f(a)}{b -a}$.

$\Box$

Theorem 3 (Increasing)
: Given a function $f$ that is differentiable on an interval $I$, $f$ is increasing iif $f'(x)\geq 0\; \forall x\in I$.

proof   
: By Lagrange's theorem.

$\Box$

## 2. Cauchy's Theorem
Theorem 4 (Cauchy's theorem)
: If functions $f$ and $g$ satisfy
1. continuous on $[a,b]$,
2. differentiable on $(a,b)$,
3. at least one of $f'(x)$ and $g'(x)$ is not zero
4. $g(a)\neq g(b)$,

then there exists $\xi\in(a,b)$ a.t. 
$$ 
 \frac{f'(\xi)}{g'(\xi)} = \frac{f(b) -f(a)}{g(b) - g(a)}.
$$
We can see that Lagrange's theorem is a special case of Cauchy's with $g(x) = x$.

proof
: Define  $F(x) = f(x) - f(a)- \frac{f(b) - f(a)}{g(b) - g(a)}(g(x) - g(a))$. ThE proof is complete by Rolle's theorem.

$\Box$

Theorem 5 (L'Hospital $0/0$)
: For functions  $f$ and $g$, if 
1. $\lim_{x\to x_0} f(x) = \lim_{x\to x_0} g(x) = 0$,
2. are both differentiable on $U^o(x_0,\delta)$ and $g'(x_0)\neq 0$,
3. $\lim_{x\to x_0} \frac{f'(x)}{g'(x)} = A$, possibly $A = \pm\infty$,

then $\lim_{x\to x_0} \frac{f(x)}{g(x)} = \lim_{x\to x_0} \frac{f's(x)}{g'(x)} = A$.

proof
: Let $f(x_0) = g(x_0) = 0$, then on any interval $[x_0, x]$, by Cauchy's, we have $\xi\in(x_0,x)$
$$ 
   \frac{f'(\xi)}{g'(\xi)} = \frac{f(x)}{g(x)}.
$$
Let $x\to x_0$, we obtain the result.

$\Box$

Theorem 6 (L'Hospital $0/\infty$)
: For functions  $f$ and $g$, if 
1. differentiable on $(x_0,x_0+\delta)$, and $g'(x)\neq 0$,
2. $\lim_{x_0^+}g(x) = \infty$,
3. $\lim_{x\to x_0^+} \frac{f'(x)}{g'(x)} = A$, possibly $A = \pm\infty$,

then $\lim_{x\to x_0}^+ \frac{f(x)}{g(x)}  = A$.

## 3. Taylor's Formula

It has been seen that if $f$ is differentiable at $x_0$, then $f(x) = f(x_0) + f'(x_0)(x - x_0)  + o(x- x_0)$. Now for a function that is $n$ times differentiable at $x_0$, we can define a `Taylor polynomial` by 
$$ 
 T_n(x) = f(x_0) + \frac{f'(x_0)}{1!}  (x - x_0)+\cdots + \frac{f^{(n)}(x_0)}{n!}  (x - x_0)^n.
$$

Theorem 7
: If  function $f$ is $n$ times differentiable at $x_0$, then $f(x) = T_n(x) + o((x-x_0)^n)$.

proof
: Let $R_n(x) = f(x) - T_n(x)$, and $Q_n(x) = (x-x_0)^n$. If suffices to show that $\lim_{x\to x_0} \frac{R_n(x)}{Q_n(x)} = 0$. Obviously, $R_n(x_0) = R'_n(x_0) = \cdots = R_n^{(n)}(x_0) = 0$ and $Q_n(x_0) = Q'_n(x_0) = \cdots = Q_n^{(n-1)}(x_0) = 0, Q_n^{(n)} = n!$. The result is obtained by applying L'Hospital $n-1$ times.

$\Box$

Theorem 8
: If $f$ is $n$ times continuously differentiable on $[a,b]$ and differentiable on $(a,b)$, then for any $x,x_0\in [a,b]$, there exists $\xi\in(a,b)$ s.t. 
$$ 
 f(x) = T_n(x) +   \frac{f^{(n+1)}(\xi)}{(n+1)!}  (x - x_0)^{n+1}.
$$

## 4. Extremum

We have studied the sufficient and necessary conditions for $f$ taking local extremum at $x_0$. Now we study the sufficient conditions.

Theorem 9 (1st sufficient)
: Given a function $f$ that is continuous at $x_0$, and differentiable on $U^o(x_0,\delta)$,
1. if $f'(x)\leq 0$ for all $x\in (x_0-\delta,x_0)$ and $f'(x)\geq 0$ for all $x\in (x_0,x_0+\delta)$, then $f$ achieves its local minimum at $x_0$.
2. ..., then $f$ achieves its local maximum at $x_0$.

Theorem 10 (2nd sufficient)
:  Given a function $f$ that is twice differentiable at $x_0$, differentiable on $U(x_0,\delta)$, and $f'(x_0)=0, f''(x_0)\neq 0$,
1. if $f''(x_0)<0$, then $f$ achieves its local maximum at $x_0$,
2. if $f''(x_0)>0$, then $f$ achieves its local minimum at $x_0$.

Theorem 11 (3rd sufficient)
: Given a function $f$ that is $n$ times differentiable at $x_0$, $n-1$ times differentiable on $U(x_0,\delta)$,  and $f^{(k)}(x_0)=0,k = 1,...,n-1, f^{(n)}(x_0)\neq 0$,
1. if $n$ is even, $f$ achieves it local extremum at $x_0$. Moreover, if $f^{(n)}<0$, it achieves its local maximum, and $f^{(n)}>0$, it achieves its local minimum.
2. if $n$ is odd, $f$ does not take its local extremum at $x_0$.


## 5. Convexity and Concavity

Definition 12 (Convexity)
: For a function $f$ defined on interval $I$, if for any $x_1,x_2\in I$ and $\lambda\in (0,1)$,
$$ 
 f(\lambda x_1 + (1-\lambda)x_2) \leq \lambda f(x_1) + (1-\lambda)f(x_2),
$$
we say $f$ is a `convex function` on $I$.

It is easy to check that $f$ is convex $\Leftrightarrow$ $f'$ is increasing $\Leftrightarrow$ $f(x_2)-f(x_1)\geq f'(x_1)(x_2- x_1)$. Moreover, if $f$ is twice differentiable on $I$, it is also equivalent to $f''(x)\geq 0$.