+++
author = "Wang Chaohua"
title = "Mathematical Analysis | 3 Limit of Functions"
date = "2021-04-03T10:52:59+02:00"

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


## 1. Limit of Functions
Definition 1 (Limit at $\infty$)
: Given a function $f$ defined on $[a,\infty)$ and a constant $A$, if for any $\epsilon>0$ there exists $M$ s.t. for any $x\geq M$,
$$ 
 |f(x) - A|<\infty,
$$
we say that $f$ has limit $A$ as $x\to+\infty$, denoted by $\lim_{x\to +\infty}f(x) = A$.

If $\lim_{x\to +\infty}f(x)= \lim_{x\to -\infty}f(x) = A$, we deonte it by $\lim_{x\to \infty}f(x) = A$.

Definition 2 (Limit at $x_0$)
: Given a function $f$ that is well defined on $U^o(x_0,\delta')$ and a constant $A$, if for any $\epsilon>0$ there exists a $\delta$ s.t. 
$$ 
 |f(x)- A|<\infty,
$$
for any $x\in U^o(x_0,\delta)$, we say that $f$ has limit $A$ as $x\to x_0$, denoted by $\lim_{x\to x_0}f(x) = A$.

Definition 3 (One-sided limit)
: Given a function $f$ that is well defined on $U^o_+(x_0,\delta')$ and a constant $A$, if for any $\epsilon>0$ there exists a $\delta$ s.t. 
$$ 
 |f(x)- A|<\infty,
$$
for any $x\in U^o_+(x_0,\delta)$, we say that $f$ has right limit $A$ as $x\to x_0$ from right, denoted by $\lim_{x\to x_0^+}f(x) = A$. Similarly, the left limit can be defined.


Theorem 4
: $\lim_{x\to x_0}f(x) = A\Leftrightarrow \lim_{x\to x_0^+}f(x) = \lim_{x\to x_0^-}f(x) = A$.

Proposition 5 (Properties)
: 
1. uniqueness. If $\lim_{x\to x_0}f(x)$ exists, then the limit is unique.
2. local boundedness. If $\lim_{x\to x_0}f(x)$ exists, then $f$ is bouned on $U^o(x_0,\delta)$ for some $\delta$.
3. signed. If $\lim_{x\to x_0}f(x) = A>0$, then for any $0<r<A$, there exist a $U^o(x_0,\delta)$ on which $f(x)>r>0$.
4. ordered. If both $\lim_{x\to x_0}f(x)$ and $\lim_{x\to x_0}g(x)$ exist, and  $f(x)\leq g(x)$ on some $U^o(x_0,\delta)$, then $\lim_{x\to x_0}f(x)\leq \lim_{x\to x_0}g(x)$.
5. squeeze. If $\lim_{x\to x_0}f(x) =  \lim_{x\to x_0}g(x) = A$, and $f(x)\leq h(x)\leq g(x)$ on some $U^o(x_0,\delta)$, then  $\lim_{x\to x_0}h(x) = A$.


## 2. Existence of Limit

Theorem 6 (Heine-Cantor)
: Suppose $f$ is well defined on $U^o(x_0,\delta')$. The limit of $f(x)$ exists iff for any sequence $\{x_n\}\subset U^o(x_0,\delta')$ that is convergent to $x_0$, the sequence $\{f(x_n)\}$  converges to a fixed point. 

Proof: "$\Rightarrow$" is trivial. We only show the inverse. Suppse that  $f(x_n)\to A$ as $n\to\infty$ for all sequences described as the theorem. If $f(x)$ does not converge to $A$ as $x\to x_0$, then there exists $\epsilon_0$ s.t $\forall \delta>0$, there is some $x\in U^o(x_0,\delta)$ with $|f(x)- A|\geq \epsilon_0$. We take $\delta = \delta'/n$, $n = 1,2,\ldots$, and thus obtain a sequence $\{x_n\}$ s.t. 
$$ 
|f(x_n)- A|\geq \epsilon_0
$$
and $x_n\in U^o(x_0,\delta'/n)$. Obviously, $\{x_n\}\subset U^o(x_0,\delta')$ and thus $x_n\to x_0$ as $n\to\infty$. Now we see a contradiction since $f(x_n)$ does not converge to $A$. 

$\Box$

This theorem is useful because it transfers the limit of a function into the limit of sequences.

Theorem 7 (One-sided limit)
: Suppose $f$ is well defined on $U^o_+(x_0,\delta')$. $\lim_{x\to x_0^+}h(x) = A$ iff for every decreasing sequence $\{x_n\}\subset U^o(x_0,\delta')$ s.t. $x_n\to x_0$, we have $f(x_n)\to A$.

Theorem 8
: If $f$ is a monotone and bounded function defined on $U^o_+(x_0,\delta')$, then the right limit of $f(x)$ at $x_0$ exists.

Proof: W.l.o.g. we assume that $f$ is increasing, then $\inf_{x\in U^o_+(x_0,\delta')} f(x)$ exists, denoted by $A$. It follows that there exists $x'\in U^o_+(x_0,\delta')$ with $f(x') < A + \epsilon$. Because $f$ is increasing, for any $x\in U^o_+(x_0,\delta):= (x_0,x')$, 
$$ 
 f(x)\leq f(x')<A +\epsilon
$$
On the other hand, $A-\epsilon<f(x)$, hence $\lim_{x\to x_0^+}f(x) = A$.

$\Box$

Theorem 9 (Cauchy criterion)
: Suppose $f$ is well defined on $U^o(x_0,\delta')$. $\lim_{x\to x_0}f(x) = A$ iff for any $\epsilon>0$, there exists a $U^o(x_0,\delta)$ s.t. for any $x_1,x_2\in U^o(x_0,\delta)$ we have 
$$ 
 |f(x_1) - f(x_2)|<\epsilon.
$$
Proof: "$\Rightarrow$" is trivial. We only show the inverse. For any sequence $\{ x_n\}\subset U^o(x_0,\delta)$ with $x_n\to x_0$, by assumption, we can find an integer $N$ s.t. for any $n,m\geq N$, 
$$ 
 |f(x_n) - f(x_m)|<\epsilon.
$$
By Cauchy criterion for sequences, $\lim_{n\to\infty}f(x_n)$ exists, denoted by $A$. Now for any $x\in U^o(x_0,\delta)$ and $n\geq N$, 
$$ 
 |f(x) - f(x_n)|<\epsilon.
$$
With $n\to\infty$, it gives $|f(x) - A|\leq \epsilon$, thus $\lim_{x\to x_0}f(x) = A$.

$\Box$

## 3. Two Important Limits

### 3.1 show that $\lim_{x\to 0} \frac{\sin x}{x} = 1$.

Proof: for $x\in (0,\pi/2)$, $0<\sin x <> x < \tan x$. It follows that 
$$
   \cos x < \frac{\sin x}{x} < 1. \tag{1}
$$
The display (1) still holds when $x\in(-\pi/2,0)$. Then we can draw the conclusion by squeeze theorem.

$\Box$

### 3.2 show that $\lim_{x\to\infty} (1 + 1/x)^x = e$.

Proof: It is equivalent to show 
$$
\begin{aligned}
\lim_{x\to+\infty} (1 + 1/x)^x = e \cr
\lim_{x\to-\infty} (1 + 1/x)^x = e
\end{aligned} \tag{2}
$$
Use the fact $\lim_n(1 + 1/n)^n = e$. Because 
$$ 
 \lim_{n\to\infty}(1+1/(1+n))^n =   \lim_{n\to\infty}(1+1/n)^{(1+n)} = e,
$$
for any $\epsilon>0$, and sufficiently large $n$, 
$$ 
 e - \epsilon<  (1+1/(1+n))^n  <(1+1/n)^{(1+n)} < e + \epsilon. 
$$
Then for sufficiently large $x$, and let $n = [x]$, 
$$ 
   (1+1/(1+n))^n <  (1+1/x)^x <(1+1/n)^{(1+n)} \tag{3}
$$
It follows that $\lim_{x\to+\infty} (1 + 1/x)^x = e$. Similarly, we can show the second limit by replacing $x$ by $-y$.

$\Box$


## 4. Infinitesimals
Similar with the infinitesimals defind for sequences, the infinitesimal of functions is given by 

Definition 10 (Infinitesimal)
: Given a function $f$ that is defined on $U^o(x_0,\delta)$. If $\lim_{x\to x_0} f(x) = 0$, we say that $f$ is an *infinitesimal* as $x\to x_0$.

Let $f$ and $g$ be two infinitesimals as $x\to x_0$. 
1. If $\lim_{x\to x_0} \frac{f(x)}{g(x)} = 0$, we say that $f$ is an infinitesimal of higher order than $g$, denoted by $f(x) = o(g(x))$ as $x\to x_0$.
2. If there exist finite numbers $K$ and $L$ s.t. for any $x\in U^o(x_0,\delta)$,
$$ 
 K\leq |\frac{f(x)}{g(x)}| \leq L,
$$
we say that $f$ is an infinitesimal of the same order as $g$, denoted by $f(x) = O(g(x))$ as $x\to x_0$. In particular, if $\lim_{x\to x_0} \frac{f(x)}{g(x)} = c\neq 0$, $f$ and $g$ must be infinitesimals of the same order.

3. If $\lim_{x\to x_0} \frac{f(x)}{g(x)} = 1$, $f$ and $g$ are said to be equivalent, denoted by $f(x) \sim g(x)$ as $x\to x_0$.



