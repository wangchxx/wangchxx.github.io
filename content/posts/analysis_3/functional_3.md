---
author : "Wang Chaohua"
title : "Functional Analysis | 3 Linear Operators"
date : "2021-04-23T10:52:59+02:00"

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



## 1. Continuous Linear Transformations

Lemma 1 (**Continuity**) <span id = "c3_lem_continuity">
: Let $X$ and $Y$ be two normed linear spaces and let $T:X\to Y$ be a linear transformation. The following are equivalent:
  1. T is uniformly continuous,
  2. $T$ is continuous,
  3. $T$ is continuous at $0$,
  4. there exists a number $M$ s.t. $||T(x)||_Y\leq M$ whenever $x\in X$ with $||x||_X\leq 1$,
  5. there exists a number $M$ s.t. $||T(x)||_Y \leq M||x||_X$ for all $x\in X$.

proof
: $1 \Rightarrow 2\Rightarrow 3$ are trivial. We prove the left assertions only. 
  $3\Rightarrow 4$. As $T$ is continuous at $0$, there exist $\delta$ s.t. $||T(x)||_Y < 1$ whenveer $||x||_X <\delta$. Let $w\in X$ and $||w||_X \leq 1$. As
  $$ 
   || \delta w/2 ||_X \leq \delta/2<\delta,
  $$
  $||T(\delta w/2)||_Y<1$ and as $T$ is linear, it implies that $ ||T(w)||_Y< 2/\delta$. We draw the conclusion by taking $M = 2/\delta$.

  $4 \Rightarrow 5$. Since $T(0) = 0$, it is clear that $||T(0)||_Y \leq M ||0||_X$. For any $w\in X, w\neq 0$, we have $||T(\frac{w}{||w||_X}) ||_Y < M$. By linearity again we have 
  $$ 
   ||T(W)||_Y \leq M ||w||_X.
  $$

  $5\Rightarrow 1$. By linearity and assumption, $||T(x) - T(w)||_Y = || T(x-w)||_Y \leq M||x-w||_X$. For any $\epsilon$, we take $\delta = \epsilon/M$, then the result is clear.

$\Box$ 
  

Definition 2 (**Bounded linear transformation**)
: A linear transformation $T:X\to Y$ is bounded if there exists a number $M$ s.t. 
$$ 
 ||T(x)||_Y \leq M ||x||_X, \; \forall x\in X.
$$

In view of [Lemma 3.1](#c3_lem_continuity), we see that `continuous` and `bounded` are equivalent for linear transformations. Let $X,Y$ be normed spaces. The set of all continuous linear transformations from $X$ to $Y$, denoted by $B(X,Y)$, is called the set of <span style = "color:orange"> *bounded linear operators* or *linear operators*</span>.


Theorem 3 (**Continuity and finite-dimensional normed space**) <span id = "c3_thm_continuous_finite_dimensional_norm">
: Let $X$ be a finite-dimensional normed space, let $Y$ be any normed linear space, and let $T:X\to Y$ be a linear transformation. Then $T$ is continuous.
  
proof
: We define a norm $||\cdot||_1 $ by $||x||_1 = ||x|| + ||T(x)||_Y$. Because $X$ is finite-dimensional, $||\cdot||$ and $||\cdot||_1$ are equivalent, so that there exists $M$ s.t. $||x||_1 \leq M||x||$. Hence $||T(x)||_Y\leq M||x||$ for all $x\in X$.

$\Box$ 

This theorem says that if the domain of a linear transformation is finite-dimensional then the linear transformation is continuous. However, if the range is finite-dimensional, the conclusion is not true.

The `kernel` of a linear transformation $T\in L(X,Y)$ is defined by $Ker(T) = \{x\in X: T(x) = 0\}$. Note that if $T\in B(X,Y)$ then $Ker(T)$ is closed because $\{0\}$ is closed in $Y$.

Definition 4 (**Graph**)    
: Let $X,Y$ be normed spaces, and let $T\in L(X,Y)$. The `graph` of $T$ is the linear subspace $\mathcal{G}(T)$ of $X\times Y$ defined by 
$$ 
 \mathcal{G}(T) = \{(x,Tx):x\in X\}.
$$

We can show that $\mathcal{G}(T)$ is closed if $T\in B(X,Y)$. Let $(x_n,y_n)\in \mathcal{G}(T)$ s.t. $(x_n,y_n)\to (x,y)$ for some  $(x,y)\in X\times Y$. Then the conclusion is an immediate result of the continuity of $T$. Also, it is easily checked that $B(X,Y)$ is a liner subspace of $L(X,Y)$ and thus $B(X,Y)$ is a vector space.


## 2. The Norm of $B(X,Y)$
In this Section we want to study if $B(X,Y)$ is a normed space.

Lemma 4 (**Norm on B(X,Y)**) <span id = "c3_thm_norm_on_B">
: Let $X,Y$ be normed spaces. The function $||\cdot||: B(X,Y) \to \R$ defined by 
$$ 
 ||T|| = \sup_{x:||x||\leq 1} ||T x||_Y
$$
is a norm on $B(X,Y)$.

By Lemma 3.1, the norm can be rewritten as $||T|| = \inf\{M: || Tx||_Y \leq M ||x||_X \;\forall x\in X\}$.

proof
: Let $S,T\in B(X,Y)$ and $\lambda\in\mathbb{F}$.
  1. $||T||\geq 0$ is clear,
  2. $|| T || = 0 \Leftrightarrow || Tx||_Y=0$ for all $x\in X$ $\Leftrightarrow$ $T$ is the zero linear transformation,
  3. as $|| Tx||_Y \leq ||T|| ||x||_X$ by Lemma 3.1, we have $||\lambda T || \leq |\lambda| ||T||$. If $\lambda= 0$, the equality is achieved. If $|\lambda|>0$, 
  $$ 
   || T|| = ||\lambda^{-1} \lambda T|| \leq   ||T||,
  $$
  4. $|| (S+T)x||_T \leq ||Sx||_Y + ||Tx||_Y\leq (||S|| + ||T||)||x||_X$ . Therefore, $||S+T||\leq ||S|| + ||T||$.

  $\Box$

Example 5 ($T: C([0,1])\to \mathbb{F}$)
: Let $f\in C([0,1])$. The linear transformation $T f = f(0)$ is continuous, because $|T f|= |f(0)|\leq \sup_x |f(x)| = ||f||$. Also, it follows that $||T||\leq 1$ since  
$$ 
||T|| = \inf\{M: |T f| \leq M ||f|| \;\forall f\in C[0,1]\}.
$$
On the other hand,  the function $g$ on $[0,1]$ defined by $g(x) = 1$ is a member of $C[0,1]$, hence $||T||\geq 1$. Therefore $||T|| =1$.

Since the norm of an operator is defined in terms of supremum, the norm can sometimes be hard to find, even if $X$ is finite-dimensional. But sometimes it is possible to use the norm of one operator to find that of another.

Theorem 6
: Let $X$ be a normed linear space and let $W\subset X$ be a dense subspace. let $Y$ be a Banach space and let $S\in B(W,Y)$. 
  1. If $x\in X$ and $\{x_n\} , \{y_n\}$ are sequences in $W$ converging to the same limit $x$, then $\{S x_n\}$ and $\{S y_n\}$ both converge to the same limit in $Y$.
  2. There exists $T\in B(X,Y)$ s.t. $||T|| = ||S||$ and agrees with $S$ in $W$, i.e. $Tx = Sx$ for all $x\in W$.

proof
: 1. $x_n$ is Cauchy, then so is $\{S x_n\}$, and it is convergent because $Y$ is a Banach space. Same results apply to $y_n$. We obtain the assertion by 
$$ 
 || S x_n - S y_n|| = || S (x_n - y_n) ||\leq ||S|| ||x_n - y_n||\to 0.
$$
 
  2. Since $W$ is dense, for any $x\in X$, we can find a sequence in $W$ s.t. $x_n \to x$. Now we define $T$ by 
  $$ 
   T x  = \lim_{n\to\infty} S x_n.
  $$
  
  $||T||\leq ||S||$ since $||Tx|| = \lim_{n\to\infty} ||S x_n||$. Moreover if $w\in W$, then we can set the constant sequence $\{w_n\}$ in $W$ converging to $w$, and so $T w =  S_w$. Thus $||S w|| = || T w|| \leq ||T|| ||w||$. Hence $||S||\leq ||T||$.
  $\Box$

Lemma 7 (**Complete codomain**)<span id = "c3_lem_BanachY_BanachDual">
: If $X$ is a normed linear space and $Y$ is a Banach space, then $B(X,Y)$ is a Banach space.

proof
: We need to show that $B(X,Y)$ is complete. Let $T_n$ be a Cauchy sequence in $B(X,Y)$, then $\{T_n\}$ is bounded, i.e. $|| T_n||\leq M$. Since 
$$ 
 ||T_n x - T_m x|| = || (T_n -T_m)x||\leq  || T_n - T_m || || x||\to 0,
$$
$\{T_n x\}$ is also a Cauchy sequence in $Y$, so it converges to some $y\in Y$. 

  Next, we, we show that $y = Tx$ for some $T\in B(X,Y)$ . Let $T x = \lim_{n\to\infty} T_n x$. It can be checked that $T$ is linear and $||T x|| \leq M||x||$, so $T\in B(X,Y)$.

  Finally, we show that $T_n \to T$. $|| Tx - T_m x|| \to 0$.

$\Box$

This Lemma shows that only the completeness of $Y$ matters.

Definition 7 (**Functionals and dual space**)
: Let $X$ be any normed space, and let $Y = \mathbb{F}$. Then $T\in L(X,Y)$ is called a linear `functional`, and $B(X,Y)$ is called the `dual space` of $X$, denoted by $X'$.

Since $\mathbb{F}$ is complete, $X'$ is a Banach space by [Lemma 3.7](#c3_lem_BanachY_BanachDual).

Definition 8 (**Isometry**) <span id = "c3_def_isometry">
: Let $X,Y$ be normed linear spaces and let $T\in L(X,Y)$. If $||T x|| = ||x||$ for all $x\in X$, then $T$ is called an `isometry`. Moreover, if if the isometry $T$ is bijective, $X$ and $Y$ are called `isometrically isomorphic`, and $T$ is called an `isometric isomorphism`.

On every normed space there is at least one isometry. And it is clear that  $||T|| = 1$ if $T$ is an isometry.

Theorem 8 
: Let $\mathcal{H}$ be an infinite-dimensional, separable Hilbert space over $\mathbb{F}$ with an orthonormal basis $\{e_n\}$. Then  is  an isometry $T$ from $\mathcal{H}$ to $\ell^2$ s.t. $T e_n = \tilde{e}_n$, where $\tilde{e}_n$ is the standard orthonormal basis in $\ell^2$ .

proof
: For $x\in\mathcal{H}$, it can be represented as $x  = \sum_{n=1}^\infty < x, e_n> e_n$. Write $\alpha_n := < x, e_n>$, then $\{\alpha_n\}\in\ell^2$ by Bessel's inequality. So we can define a linear transformation $T$ by $T x = \{a_n\}$. Now 
$$ 
 ||T x||^2 = ||x||^2.
$$
So $T$ is an isometry. Also by definition $T e_n = \tilde{e}_n$.

$\Box$


## 3. Inverses of Operators
In this Section we introduce some methods of determining invertibility of an operator, one is based on the norm, the second one is open mapping theorem, and the third one is based on denseness.

Definition 9 (**Inverse operator**)
: Let $X,Y$ be normed linear spaces. An operator $T\in B(X,Y)$ is said to be `invertible` if there exists $S\in B(Y,X)$ s.t. $ST = I_X$ and $TS = I_X$, in which case $S$ is the `inverse` of $T$, denoted by $T^{-1}$.

Definition 10 (**Isomorphic**)
: Let $X,Y$ be normed linear spaces. If there exists $T\in B(X,Y)$ that is invertible, then $X,Y$ are `isomorphic`, and $T$ is an `isomorphism`.


Lemma 11 
: If the normed linear spaces $X,Y$ are isomorphic, then 
  1. $dim(X) <\infty \Leftrightarrow dim(Y)<\infty$, in which case $dim(X) = dim(Y)$.
  2. $X$ is separable iff $Y$ is separable.
  3. $X$ is complete iff $Y$ is complete.


Theorem 12 (**1st, norm**)
: Let $X$ be a Banach space. If $T\in B(X)$ is an operator with $||T||<1$, then $I- T$ is invertible and the inverse is given by 
$$ 
 (I-T)^{-1} = \sum_{n=0}^\infty T^n.
$$

proof
: Because $X$ is a Banach space, so is $B(X)$ by Lemma 3.7. Since $|| T||<1$, the series $\sum ||T||^n$ converges, and as $||T^n||\leq ||T||^n$ the series $\sum ||T^n||$ also converges. Therefore the series $\sum T^n$ converges. Let $S = \sum T^n$ and $S_k = \sum_{n=0}^k T^n$. We see that $S_k \to S$.

  Now $||(I-T)S_k - I|| = ||I - T^{k+1} - I|| \leq ||T||^{k+1}\to 0$. It follows that $(I-T)S = I$. Similarly, $S(I-T) = I$.

$\Box$

Corollary 13
: Let $X,Y$ be Banach spaces. The set $\mathcal{A}$ of invertible operators in $B(X,Y)$ is open.

proof
: Let $T\in \mathcal{A}$, and let $\eta = ||T^{-1}||^{-1}$. It suffices to show that if $||T -S||<\eta$ then $S\in \mathcal{A}$. 
$$ 
 || (T-S) T^{-1}|| \leq || T -S|| ||T^{-1}||< 1
$$
By Theorem 3.12, $I_Y - (T-S) T^{-1} = ST^{-1}$ is invertible. So $S = ST^{-1} T$ is invertible.

$\Box$


Theorem 14 (**2nd, Open mapping theorem**)
: Suppose that $X,Y$ are Banach spaces and $T\in B(X,Y)$ is surjective. Let 
$$ 
 L = \{Tx: x\in X , ||x||\leq 1\},
$$
with closure $\overline{L}$. Then 
  1. there exists $r>0$  s.t. $\{y\in Y: ||y||\leq r\}\subset \overline{L}$,
  2. $\{y\in Y: ||y||\leq r/2\} \subset L$,
  3. if, in addition, $T$ is bijective then $T$ is invertible.

proof
: Let $U(r), V(r)$ be open balls with center $0$ and radius  $r$ in the space $X,Y$, respectively.
  1. For any $y\in Y$, there exists $x\in X$ s.t. $T x = y$. Thus $y\in ||x|| L$ and so 
  $$ 
   Y = \cup_n n \overline{L}
  $$
  Therefore, by Baire category theorem, there is $N\in\N$ s.t. $N\overline{L}$ contains an open ball, and hence $\overline{L}$ also contains an open ball. Therefore, there exists $p\in \overline{L}$ and $t>0$ s.t. 
  $$ 
   p + V(t) \subset \overline{L}.
  $$
  Then for any $y\in V(t)$, we have $y\in \overline{L}$ because $y+p,y-p \in \overline{L}$. This suggests that $V(t)\subset \overline{L}$. We finish the proof by taking $r = t/2$.

  2. let $y\in \overline{V}(r/2)$. Since $\overline{V}(r)\subset \overline{L}$, there exits $w_1\in L$ s.t. 
  $$ 
   ||2y - w_1  ||< r/2
  $$
  Since $2^2 y - 2 w_1 \in \overline{V}(r)\subset \overline{L}$, there exits $w_2\in L$ s.t. 
  $$ 
   || w^2 y - 2w_1 - w_2 ||  < r/2.
  $$
  Continuing in this way, we obtain a sequence $\{w_n\}$ is $L$ s.t. 
  $$ 
   || w^2 y - w^{n-1}w_1 - \cdots - w_n|| < r/2.
  $$
  Therefore, $|| y - \sum_{j=1}^n 2^{-j} w_j||< 2^{-n-1} r\to 0$. Hence $y = \sum_{j=1}^\infty 2^{-j} w_j$. Also, there exists $x_n\in \overline{U}(1)$ s.t. $w_n = Tx_n$. As $\sum_{j=1}^n 2^{-j} x_j$ is Cauchy, it converges to $x\in \overline{U}(1)$. Also, 
  $$ 
   Tx = T \sum_{j=1}^\infty 2^{-j} x_j =   \sum_{j=1}^\infty 2^{-j}  Tx_j = y.
  $$
  Therefore $y\in L$. The proof is complete.

  3. There exists a unique $S\in L(Y,X)$ s.t. $S T = I_X, TS = I_Y$. We need to show that $S$ is bounded. Let $y\in Y$ and $||y||\leq 1$, and let $w = ry/2$. As $w \in \overline{V}(r/2)$, by part 2. we have that $y = T (2x/r)$ for some $x\in X, ||x||\leq 1$. So $||Sy||\leq 2/r$. Thus $S$ is bounded.

  $\Box$


Corollary 15 (**Closed graph theorem**)
: Let $X,Y$ be Banach spaces, and $T\in L(X,Y)$ s.t. the graph $\mathcal{G}(T)$ is closed, then $T\in B(X,Y)$.

proof
: As $X\times Y$ is Banach, $\mathcal{G}(T)$ is Banach since it is a closed subspace of $X\times Y$. let $R:\mathcal{G}(T)\to X$ be defined by 
$$ 
 R(x,Tx) = x.
$$
We can see that $R$ is bijective. Since 
$$ 
 ||R(x, Tx) || = ||x|| \leq ||(x,Tx)||.
$$
we see that $R$ is bounded and $||R||\leq 1$. By the opening mapping theorem (3), there exists $S\in B(X,\mathcal{G}(T))$ s.t. $S = T^{-1}$, in particular $Sx = (x, Tx)$. As 
$$ 
 ||Tx||\leq ||x|| + ||Tx|| = ||S x||  \leq ||S||||x||,
$$
it follows that $T$ is bounded.

$\Box$


Lemma 16
: Let $X$ be a Banach space, $Y$ be a normed space, and let $T\in B(X,Y)$. If there exits $\alpha>0$ s.t. $||T x||\geq \alpha ||x||$ for all $x\in X$, then $T(X)$ is closed.

proof
: Let $y_n$ be a sequence in $T(X)$ converging to $y\in Y$. There exists a sequence $x_n$ s.t. $T x_n = y_n$. Since $y_n$ converges, 
$$ 
 0\leftarrow ||y_n - y_m|| = || T(x_n - x_m)|| \geq  \alpha ||x_n - x_m||  .
$$
It follows that $x_n$ converges as well, write the limit $x\in X$. By the continuity of $T$, we have $Tx = y\in T(X)$.

$\Box$

Theorem 17 (**3rd, dense**)
: Let $X,Y$ be Banach spaces, and $T\in B(X,Y)$. The following are equivalent: 
  1. $T$ is invertible,
  2. $T(X)$ is dense in $Y$, and there exists $\alpha>0$ s.t. $||Tx||\geq \alpha ||x||$ for all $x\in X$.

proof
: $1\Rightarrow 2$ is easy because $||x|| = ||T^{-1}T x||\leq ||T^{-1}|| ||Tx||$. 
  $2\Rightarrow 1$. By Lemma 3.16 $T(X)$ is closed and dense, hence $T(X) = Y$ (onto). For $x\in Ker(T)$, $Tx = 0$, so 
  $$ 
   0 =||Tx||  \geq \alpha ||x|| \Rightarrow x = 0.
  $$
  It follows that $Ker(T) = \{0\}$ (one-to-one), so $T$ is bijective and thus invertible.

  $\Box$
