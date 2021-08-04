---
author : "Wang Chaohua"
title : "Functional Analysis | 4 Duality and Hahn-Banach Theorem"
date : "2021-04-24T10:52:59+02:00"

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



   

## 1. Dual Spaces

In this section we describe the dual of several of the standard spaces.

Theorem 1 <span id = "c4_functional_norm">
: If $X$ is a finite-dimensional normed linear space with basis $\{v_1,...,v_n\}$, then $X'$ has a basis $\{f_1,...,f_n\}$ s.t. $f_j(v_k) = \delta_{jk}$. In particular, $dim (X') = dim (X)$.

proof
: Let $x\in X$, we can represent is as $x = \sum_{k=1}^n \alpha_k v_k$. Define $f_j:X\to\mathbb{F}$ by 

$$f_j(x) = \alpha_j.$$

It can be verified that $f_j$ is a linear transformation s.t. $f_j(v_k) = \delta_{jk}$. Moreover, $f_j$ is continuous since $X$ is finite-dimensional, and thus $f_j\in X'$.

  Next, we show that $\{f_1,...,f_n\}$ is a basis for $X'$. Suppose that $\beta_1,...,\beta_n$ are scalars s.t. $\sum_{j=1}^n \beta_j f_j = 0$. Then 
  $$ 
   0  =   \sum_{j=1}^n \beta_j f_j (v_k) = \sum_{j=1}^n \beta_j \delta_{jk} = \beta_k,
  $$
   and so $\{f_1,...,f_n\}$ is linearly independent. Now for any $f\in X'$, let $\gamma_j = f(v_j)$. Then 
   $$ 
    \sum_{j=1}^n \gamma_j f_j(v_k) = \gamma_k = f(v_k).
   $$
   It follows that $f = \sum_{j=1}^n \gamma_j f_j $ since $v_1,...,v_n$ is a basis for $X$.

   $\Box$

Theorem 2 (**Riesz-Frechet theorem**) <span id = "c4_riesz_frechet">
: Let $\mathcal{H}$ be a Hilbert space and let $f\in \mathcal{H}'$. Then there is a unique $y\in \mathcal{H}$ s.t. $f(x) = f_y(x) = < x,y>$ for all $x\in\mathcal{H}$. Moreover, $||f|| = ||y||$.

proof
: Existence. If $f= 0$, then $y=0$ is a suitable choice. Otherwise, $Ker f = \{x: f(x) = 0\}$ is a closed subspace of $\mathcal{H}$ so that $(Ker f)^\perp \neq \{0\}$. Therefore there exists $z\in (Ker f)^\perp$ s.t. $f(z) = 1$. In particular, $z\neq 0$ so we may define $y=\frac{z}{||z||^2}$. Now let $x\in \mathcal{H}$ be arbitrary. Since $f$ is linear, 
$$ 
 f(x - f(x)z) = 0,
$$
and hence $x - f(x)z \in Ker f$. However, $z\in (Ker f)^\perp$ so 
$$ 
 < x - f(x)z , z> = 0  .
$$

  It follows that $< x, z> = f(x) ||z||^2$. It suggests that $f(x) = < x, y>$. Now, if $||x||\leq 1$, by the Cauchy-Schwarz inequality, $||f||\leq ||y||$. On the other hand, if $x = y/||y||$ then $||x|| = 1$, so $||f||\geq |f(x)|= ||y||$. Therefore, $||f|| = ||y||$.

  Uniqueness. If $y,w$ are s.t. $f(x) = < x, y> = < x, w>$ for all $x\in\mathcal{H}$, then $< x , y-w>=0$ for all $x$. Hence, we have $y-w = 0$.

  $\Box$


This theorem gives a representation of all the elements of the dual space $\mathcal{H}'$ of a general Hilbert space $\mathcal{H}$.


Theorem 3 <span id = "c4_thm_dual_hilbert">
: Let $\mathcal{H}$ be a Hilbert space, and define $T: \mathcal{H}\to \mathcal{H}'$ by $T y = f_y , \; y\in\mathcal{H}$. Then $T$ is a bijection, and for all $\alpha,\beta \in\mathbb{F}, y,z\in\mathcal{H}$:
  1. $T(\alpha y + \beta z) = \bar{\alpha} Ty + \bar{\beta}Tz$,
  2. $|| Ty|| = ||y||$.

  In addition, the inner product $<\cdot,\cdot>\_{\mathcal{H}'}$ can be defined on $\mathcal{H}'$ by 
  $$
   \begin{equation}
   < Tz , Ty>\_{\mathcal{H}'} = < y,z>\_{\mathcal{H}}.
   \end{equation}
  $$
  With this inner product, $\mathcal{H}'$ is a Hilbert space.

proof
: The bijectivity of $T$ and property $2$ follows immediately from [Riesz-Frechet, Theorem 4.2](#c4_riesz_frechet). Next, for all $x\in\mathcal{H}$ we have 
$$ 
 f_{\alpha y  + \beta z} (x) = < x, \alpha y + \beta z>  = \bar{\alpha} f_y(x) + \bar{\beta} f_z(x).
$$

  Next, we show (1). Obviously, it is a norm, and $||f_y||^2 = ||y||^2 = < f_y, f_y>_{\mathcal{H}'}$. $\mathcal{H}'$ is complete because it is a Banach space.

$\Box$



## 2. The Hahn-Banach Theorem
Sometimes we have a linear functional $f_W:W\to \mathbb{F}$ defined on a subspace $W\subset X$, but we want to extend this functional to the whole of $X$.

Definition 4 (**Extension**)
: Let $X$ be a vector space, $W$ a linear subspace of $X$, and $f_W$ a linear functional on $W$. A linear functional $f_X$ on $X$ satisfying 
$$ 
 f_X(w) = f_W(w),\\;\forall w\in W,
$$
is called an `extension` of $f_W$.


Definition 5 (**Sublinear functional**)
: Let $X$ be a real vector space. A `sublinear functional` on $X$ is a function $p:X\to \R$ s.t. for all $\alpha\geq 0, x,y\in X$,
  1. $p(x+y)\leq p(x) + p(y)$,
  2. $p(\alpha x) = \alpha p(x)$ .

Definition 6 (**Seminorm**)
: Let $X$ be a real or complex vector space. A `seminorm` on $X$ is a function $p:X\to \R$ s.t. for all $\alpha\in \mathbb{F}, x,y\in X$,
  1. $p(x+y)\leq p(x) + p(y)$,
  2. $p(\alpha x) = |\alpha| p(x)$ .


Theorem 7 (**The Hahn-Banach theorem, real**) <span id = "c4_H-B_real">
: Let $X$ be a real vector space, $W\subset X$ a linear subspace of $X$, and $p$ a sublinear functional  defined on $X$. If a linear functional $f_W:W\to \R$ satisfies 


$$ 
 f_W(w)\leq   p(w), \\; w\in W,
$$
then $f_W$ has an extension $f_X$ on $X$ s.t. 
$$ 
 f_X(x)\leq p(x),\\; x\in X.
$$

proof
: Prove it in next section.

$\Box$


Let $u$ be the real part of a complex-linear functional $f$ on $X$, then $u$ is real-linear and 
$$
\begin{equation}
 f(x) = u(x) - i u(ix), \\; x\in X,
\end{equation}
$$


Theorem 8 (**The Hahn-Banach theorem**) <span id = "c4_H_B_general">
: Let $X$ be a real or complex vector space, $W\subset X$ a linear subspace of $X$, and $p$ a seminorm on $X$. If a linear functional $f_W:W\to \R$ satisfies 
$$ 
 |f_W(w)|\leq   p(w), \\; w\in W,
$$
then $f_W$ has an extension $f_X$ on $X$ s.t. 
$$ 
 |f_X(x)|\leq p(x),\\; x\in X. 
$$

proof
: Let $u_W$ be the real part of $f_W$. Then $u_W$ has an extension $u_X$ s.t. $|u_X (x)|\leq p(x)$ on $X_R$. The results now follows by (2).

$\Box$



Lemma 9 <span id = "c4_lem_extension_M1">
: 1. $W$ is a linear subspace of a real vector space $X$,
  2. $p$ is a sublinear functional on $X$.
  3. $f_W:W\to\R$ is linear and $f_W(w)\leq p(w)$ on $W$.

  Suppose $x_1\in X\setminus W$, and let 
  $$ 
   M_1 = \{\alpha x_1 + w: \alpha\in R,w\in W\}.
  $$
  
   Then there exists $f_1:M_1\to\R$ and $\xi_1\in\R$ satisfying 
   $$
    \begin{equation}
    f_1(\alpha x_1 + w) = \alpha\xi_1 + f_W(w) \leq p(\alpha x_1 + w).
    \end{equation} 
   $$
   Clearly, $f_1$ is linear  and is an extension of $f_W$ on $M_1$.

proof
: For any $x,y\in W$, we have 
$$
 f_W(x) + f_W(y) \leq p(x+y) \leq p(x-x_1) + p(x_1 + y) ,
$$
and so 
$$ 
 f_W(x) - p(x-x_1) \leq -f_W(y) + p(x_1+y).
$$
Let $\xi_1$ be the least upper bound of the left side, as $x$ ranges over $W$. Then 
$$
 \begin{equation}
 f_W (x) - \xi_1 \leq p(x-x_1),
 \end{equation}
$$
and 
$$
 \begin{equation}
 f_W (y) + \xi_1 \leq p(y+x_1).
 \end{equation}
$$
Define $f_1$ on $M_1$ by $f_1(\alpha x_1 + w) = \alpha \xi_1 + f_W(w)$.

$\Box$

Theorem 10 (H-B for normed spaces) <span id = "c4_H-B_norm">
: 1. $W$ is a linear subspace of a real or complex vector space $X$,
  2. $f_W\in W'$,
  
  Then there exists an extension $f_X\in X'$ of $f_W$ s.t. $||f_X|| = ||f_W||$.

proof
: Let $p(x) = ||f_W||||x||$ for $x\in X$. Then $p$ is a siminorm on $X$. W.l.o.g. we assume that $W$ is not closed. We assume that $X$ is separable. If $X$ is real, we can find a sequence of unit vectors $\\{x_n\\}, x_n\in X\setminus M_{n-1}$,, where $M_0 = W$. Then we have $X = \overline{M}_{\infty}$ by separability. By Lemma 4.9, for $f_n$ there exists an extension $f_{n+1}\in M'_{n+1}$ with $||f_{n+1} || = ||f_n|| = ||f_W||$.

  We now show that there is an extension of these functionals to $M_\infty$, and then to $X$. For any $x\in M_\infty$, there exists an integer $n_x$ s.t. $x\in M_{m}$ and $f_m(x) = f_{n_x}(x)$ for all $m\geq n_x$. Thus we may define $f_\infty(x) = f\_{n_x}(x)$. It is clear that $f_\infty$ is an extension of $f_W$ and satisfies $||f_\infty|| = ||f_W||$.

  Finally, since $X = \overline{M}\_{\infty}$, $f_\infty$ has an extension by continuity, $f_X\in X'$, satisfying $||f_X|| = ||f_\infty|| = ||f_W||$.

  Similarly, we can extend the results to complex cases. It yields a complex linear functional $f_X\in X'$ s.t. 
  $$
   |f_X(x)|\leq p(x) = ||f_W||||x||, \; x\in X.
  $$
  Therefore $||f_X|| = ||f_W||$.

  $\Box$


We present some immediate consequences of [Theorem 4.10](#c4_H-B_norm).

Theorem 11 <span id = "c4_H-B_norm_cor">
: 1. $W$ is a linear subspace of a real or complex vector space $X$,
  2. $f_W\in W'$,
  3. For $x\in X$, $\delta:=\inf_{w\in W } ||x - w|| >0$.

  Then there exits $f\in X'$ s.t. $||f|| = 1,f(x) =\delta$ and $f(w) = 0$ for all $x\in W$.

proof
: W.l.o.g. we assume that $W$ is closed (if not, we replace it by its closure, which does not change the value of $\delta$). Given $x\in X$, we can define $M_1$ as before, and define a linear functional $f_1$ on $M_1$ by 
$$
 f_1(\alpha x + w) = \alpha \delta.
$$
Clearly,  
$$
 |f_1 (\alpha x + w)|   = |\alpha| \delta \leq |\alpha| || x - \alpha^{-1} w|| = ||\alpha x - w||,
$$
which implies that $f_1 \in M_1'$ and $||f_1||\leq 1$.

  We now prove that $||f_1||\geq 1$. For any $\epsilon\in (0,1)$, by Riesz' ([Theorem 1.12](functional_1.md#c1_Riesz)), there exists $y_\epsilon = \alpha_\epsilon x + w_\epsilon \in M_1$ s.t. $||y_\epsilon|| = 1$ and $||y_\epsilon - w||>1-\epsilon$ for all $w\in W$. Hence, 
  $$
   1-\epsilon< ||y_\epsilon - w|| = |\alpha_\epsilon| ||x + \alpha_\epsilon^{-1}(w_\epsilon -w)|| \leq |\alpha_\epsilon| \delta ,
  $$
  which implies that 
  $$
   |f_1(y_\epsilon)| = |\alpha_\epsilon| \delta  > 1-\epsilon.
  $$
  Therefore, $||f_q||\geq 1$.

  So far we have proved that $||f_1||=1$, so by [Theorem 4.10](#c4_H-B_norm), $f_1$ has an extension $f\in X'$ with $||f||=1$. By the construction, it is clear that $f(x) = \delta, f(w) = 0, w\in W$.

  $\Box$

Corollary 12
: $x_1,...,x_n\in X$ are linearly independent, then there exists $f_1,...,f_n\in X'$ s.t. $f_j(x_k) = \delta_{jk}$ for $j,k\leq n$.

proof
: Define $M = \overline{sp}\{x_1,...,x_n\}$, which is a Hilbert space, By [Theorem 4.1](#c4_functional_norm) there exists $f_1,...,f_n \in M'$ s.t. $f_j(x_k) = \delta_{jk}$. Then by [Theorem 4.10](#c4_H-B_norm), we can extend $f_1,...,f_n$ to $X'$.

$\Box$


Theorem 13 (**Dual and separability**) <span id = "c4_thm_dual_separable">
: $X'$ is separable then so is $X$.

proof
: Let $B = \{f\in X': ||f||=1\}$. It follows immediately from the separability of $X'$ that we can choose a countable set of functionals $F= \{f_1,f_2,...\}\subset B$ which is dense in $B$. For each $n$, we choose $w_n\in X$ s.t. $||w_n|| =1$ and $f_n(w_n)\geq 1/2$, and let $W = \overline{sp}\{w_1,w_2,...\}$. Clearly, $W\subset X$. Now we suppose that $W\neq X$. Then by [Theorem 4.11](#c4_H-B_norm_cor) there exits $f\in B$ s.t. $f(w) = 0$ for all $w\in W$. However, this yields that 
$$
 1/2 \leq |f_n(w_n)| = |f_n(w_n) - f(w_n)| \leq ||f- f_n|| ,\;n\geq 1,
$$
which contradicts the density of $F$ in $B$, and so proves that $W =X$. It follows that $\{w_1,w_2,...\}$ is a countable dense set in $X$, and so $X$ is separable.

$\Box$


## 3. Proof of H-B Theorem.

In this section we will prove [Theorem 4.7](#c4_H-B_real).

Definition 14 (**Ordered set**) <span id = "c4_def_order">
: Suppose that $M$ is a non-empty set and $\prec$ is an ordering on $M$. Then $\prec$ is an `partial order` on $M$ if 
  1. $x\prec x$ for all $x\in M$,
  2. $x\prec y, y\prec x \Rightarrow x= y$,
  3. $x\prec y, y\prec z\Rightarrow x\prec z$,
 
and then $M$ is a `partially ordered set`. If, in addition, $\prec$ is defined for all pairs of elements (for any $x,y\in M$, either $x\prec y$ or $y\prec x$), then $\prec$ is a `total order` and $M$ is a `totally ordered set`.

The usual order $\leq$ on $\R$ is a total order.

Lemma 15 (**Zorn's**) <span id ="c4_lem_zorn's">
: Let $M$ be a non-empty, partially ordered set s.t. every totally ordered subset of $M$ has an upper bound. Then there exists a maximal element in $M$.



Proof of [Theorem 4.7](#c4_H-B_real)
: Let $E$ denote the set of linear functionals $f$ on $X$ satisfying the conditions:
  1. $f$ is defined on a linear subspace $D_f$ s.t. $W\subset D_f\subset X$,
  2. $f(w) = f_W(w)$, $w\in W$,
  3. $f(x)\leq p(x)$, $x\in D_f$.

  In other words, $E$ is the set of all extensions  $f$ of $f_W$ to general subspaces $D_f\subset X$. We apply [Zorn's](#c4_lem_zorn) to the set $E$ ans show that the resulting maximal element of $E$ is the desired functional.

  First, we verity that $E$ satisfies the hypotheses of Zorn's. $E$ is non-empty since $f_W\in E$. Define a relation $\prec$ on $E$ as follows: for any $f,g\in E$,
  $$
   f\prec g \Leftrightarrow D_f \subset D_g, f(x) = g(x) ,\; \forall x\in D_f. 
  $$
  In other words, $f\prec g$ iff $g$ is an extension of $f$. Now suppose that $G\subset E$ is totally ordered. i.e. for any $f,g\in G$, one of these functionals is an extension of the order. We will construct an upper bound for $G$ in $E$. 

  Define $Z_G = \cup_{f\in G} D_f$. It can be verified that $Z_G$ is a linear subspace of $X$. We now define a linear functional $f_G$ on $Z_G$ as follows:
    1. choose $z\in Z_G$, then there exists $\xi\in E$ s.t. $z\in D_\xi$,
    2. define $f_G(z) = \xi(z)$

  By the total ordering of $G$, we can see that $f_G$ is linear. And since $\xi\in E$, we have $f_G(z) = \xi(z)\leq p(z)$, and if $z\in W$ then $f_G(z) = f_W(z)$. Hence $f_G\in E$ and $f\prec f_G$ for all $f\in G$. Thus $f_G$ is an upper bound for $G$.

  So far we have verifies that all conditions of Zorn's are satisfied, then we can conclude that there exists a maximal element $f_{\max}$ in $E$. If $D_{f_{max}}\neq X$, by [Lemma 4.9](#c4_lem_extension_M1) $f_{max}$ has an extension, which also lies in $E$. However, this contradicts the maximality of $f_{max}$ in $E$, so $D_{f_{max}} = X$, and hence $f_X = f_{max}$ is the desired extension.

  $\Box$


## 4. The Second Dual
Throughout this section $X$ will be a $\color{orange}{\text{normed linear space}}$. Given $X$ a normed linear space, by [Lemma 3.7](functional_3.md#c3_lem_BanachY_BanachDual) we see that $X'$ is a Banach space, so $X'$ itself also has a dual space $(X')'$, denoted by $X''$, which is called the `second dual` of $X$.

Lemma 16 <span id = "c4_lem_functional_in_second_dual">
: For any $x\in X$, defined $F_x:X'\to \mathbb{F}$ by 
$$ 
 F_x(f) = f(x),\; f\in X'.
$$
Then $F_x\in X''$ and $||F_x|| = ||x||$.

proof
: Clearly, $F_x$ is linear. Moreover, 
$$ 
 ||F_x(f)|| = ||f(x)||\leq ||f|| ||x|| ,
$$
and so $F_x\in X''$ with $||F_x||\leq ||x||$. Finally by [Theorem 4.11](#c4_H-B_norm_cor), 
$$ 
 ||x|| = \sup_{||f|| = 1} |f(x)| = \sup_{||f|| = 1}|F_x(f)| \leq ||F_x||,
$$
which completes the proof.

$\Box$


Then we can define a linear transformation $J_X:X\to X''$ by 
$$ 
 J_X x = F_x.
$$

According to [Lemma 4.16](#c4_lem_functional_in_second_dual), $J_X$ is an isometry. Moreover, if $J_X(X) = X''$, we say that $X$ is <span style = "color  :orange"> *replexive* </span>. In other words, $X$ is reflexive iff, for any $g\in X''$, there exists $x_g\in X$ s.t. $g = J_X x_g$, i.e. $g(f) = J_Xx_g(f) = f(x_g)$, for any $f\in X'$. <span style = "color  :orange">It follows that if $X$ is reflexive, then $J_X$ is an isometric isomorphism of $X$ onto $X''$ </span> <span id = "c4_reflexive_invertible">.

From the definition of reflexive, we see that the only normed linear spaces that can be reflexive are Banach spaces. However, not all Banach spaces are reflexive.

Theorem 17 (**Reflexive and Banach**)<span id = "c4_thm_reflexive_Banach">
: A Banach space $X$ is reflexive iff $X'$ is reflexive.

proof
: Suppose that $X$ is reflexive. Let $\rho\in X'''$. Then $\rho \circ J_X\in X'$. Let $f=\rho\circ J_X$ and let $g\in X''$. Since $X$ is reflexive, there exists $x\in X$ s.t. $g = J_X x$, and so 
$$
 (J_{X'}f)(g) = g(f) = f(x) = \rho\circ J_X (x) = \rho(g).
$$
Hence $\rho = J_{X'}f$, so $X'$ is reflexive.

  Conversely, suppose that $X'$ is reflexive but there exists $w\in X''\setminus J_X(X)$. Since $J_X(X)$ is closed, by [Theorem 4.11](#c4_H-B_norm_cor) there exists $\kappa\in X'''$ s.t. $\kappa(w) \neq 0$ while $\kappa(J_X x) = 0$ for all $x\in X$. Since $X'$ is reflexive there exists $g\in X'$ s.t. $\kappa = J_{X'}(g)$. Thus 
  $$ 
   g(x) = (J_Xx)(g) = \kappa(J_X x) = 0,; x\in X,
  $$
  and so $g = 0$. Since $w(g) = \kappa(w)\neq 0$, which is a contradiction, hence $X$ is reflexive.

  $\Box$



Theorem 18
: Let $X,Y$ be two normed linear spaces and $T\in B(X,Y)$. Then there exists a unique operator $T'\in B(Y',X')$ s.t. 
$$ 
 T'f(x) = f(Tx),\; x\in X, f\in Y'. 
$$

proof
: For any $f\in Y'$, define $T'f = f\circ T$. Since $T,f$ are bounded, $T'f \in X'$, so that $T'$ is a function from $Y'$ to $X'$ s.t. $T'f(x) = f(Tx)$ for all $x\in X,f\in Y'$. Furthermore, if $S\in B(Y',X')$ satisfies $Sf(x) = f( Tx)$, then $Sf - T'f$ for all $y\in Y'$. Therefore $T'$ is unique.

  It remains to show that $T'\in B(Y', X')$. It clear that $T'$ is linear. And since $T'$ is a composition of two bounded operator, $T'$ is also bounded. The proof is complete.

$\Box$

The operator $T'\in B(Y', X')$ constructed in this theorem is called the `dual` of $T$.

Example 18 (**Reflexive and Hilbert**)<span id = "c4_eg_reflexive_hilbert">
: Any Hilbert space $\mathcal{H}$ is reflexive.

proof
: By [Theorem 4.3](#c4_thm_dual_hilbert), $\mathcal{H}'$ is a Hilbert space, so the mapping $T_{\mathcal{H}'}:\mathcal{H}'\to \mathcal{H}''$ is well defined, and is a bijection. In particular, for any $f\in \mathcal{H}'$ and $g\in \mathcal{H}''$, they have the form $f = T_{\mathcal{H}}x$ and $g = T_{\mathcal{H}'}(T_{\mathcal{H}}y )$ for unique $x,y\in \mathcal{H}$ (see [Riesz-Frechet](#c4_riesz_frechet)). Now we have 
$$
 J_{\mathcal{H}}y(f) = f(y) = < y,x>_{\mathcal{H}} = < T_{\mathcal{H}}x, T_{\mathcal{H}}y >_{\mathcal{H}'} =  < f, T_{\mathcal{H}}y>_{\mathcal{H}'},
$$
which is equal to $T_{\mathcal{H}'}(T_{\mathcal{H}}y)(f) = g(f)$, so $J_{\mathcal{H}}y  = g$. Thus, $J_{\mathcal{H}}$ is onto, and hence $\mathcal{H}$ is reflexive.

$\Box$


## 5. Weak and Weak-* Convergence

We have seen that closed bounded sets are compact in finite dimensional spaces. Unfortunately, this is not true in infinite dimensional spaces. However, if this section we will show that a partial analogue of this result can be obtained in infinite dimensions if the adopt a weaker condition of the convergence.

Throughout this section, $X$ will be a $\color{orange}{\text{Banach space}}$.

Lemma 19
: 1. $S = \{s_\alpha: \alpha\in A\}\subset X$, s.t. $\overline{sp}S = X$.
  2. $\{f_n\}\subset X'$ with $||f_n||\leq C$ for some $C$ s.t. $f_n(s_\alpha)$ converges for all $\alpha\in A$.

  Then there exists $f\in X'$ s.t. $f_n (x)\to f(x)$ for all $x\in X$.

proof
: By the completeness of $X$ and $X'$.

$\Box$

The following results provides a motivation for the new idea of convergence.

Lemma 20 <span id = "c4_lem_motivation_weak">
: 1. $X$ is separable.
  2. $\{s_k\}$ is a dense sequence in $X$ with $s_k\neq 0$ for all $k$.

  Then the function function $d_w:X'\times X'\to \R$ defined by 
$$ 
 d_w(f,g) = \sum_{k} \frac{1}{2^k} \frac{|f(s_k) - g(s_k)|}{||s_k||},\;  f,g\in X',
$$
is a metric on $X'$.

  If $\{f_n\}\subset X'$ and $f\in X'$, the following are equivalent:
  (a). there exists $C>0$ s.t. $||f_n||\leq C$ for all $n$ and $d_w(f_n,f)\to 0$.
  (b). $f_n(x)\to f(x)$ for all $x\in X$.

proof
: The metric is easy to verity. If condition (a) holds, then it is clear that $f_n(s_k)\to f(s_k)$. And by the density of $\{s_k\}$, we have $f_n(x)\to f(x)$ for all $x\in X$.

  Next, if (b) holds, the boundedness assertion is trivial as $||f||\leq C$. Also, $d_w(f_n,f)\to 0$ is easy. W.l.o.g. we assume that $f = 0$, then 
  $$ 
   d_w(f_n,f) \leq   \sum_{k} \frac{1}{2^k} ||f_n||\leq \sum_{k} \frac{1}{2^k} C<\infty.
  $$
  It follows that there exists $K$ s.t. $\sum_{k\geq K} \frac{1}{2^k} ||f_n||<\epsilon.$ Together with $f_n \to 0$, there exists $N$ s.t. $||f_n||<\epsilon/K$ whenever $n\geq N$. It follows that $d_w(f_n,0)\to 0$.

  $\Box$

Definition 21 (**Weak and weak-* convergence) <span id = "c4_def_weak">
: For any Banach space $X$, let $\{x_n\},\{f_n\}$ be sequences in $X,X'$, respectively.
  1. $\{x_n\}$ is `weakly` convergent to $x\in X$ if $f(x_n)\to f(x)$ for all $f\in X'$, denoted by $x_n\rightharpoonup x$.
  2. $\{f_n\}$ is `weak-*` convergent to $f\in X'$ if $f_n(x)\to f(x)$ for all $x\in X$, denoted by $f_n\overset{*}{\rightharpoonup}f$.

Notice that the separability is not involved in this definition. We also remark at this point that the idea of weak convergence makes sence in $X'$, by using functionals in $X''$. If X $X$ is reflexive then weak and weak-*convergence in $X'$ coincide.

We have seen that an arbitrary Hilbert space $\mathcal{H}$ is reflexive ([eg reflexive Hilbert](c4_eg_reflexive_hilbert)), and also $\mathcal{H}$ can be identified with its dual $\mathcal{H}'$, by Riesz-Frechet, so weak and weak-*convergence coincide.

Theorem 22 (**Compactness**) <span id = "c4_lem_weak_compact">
: If $x$ is separable and $B = \{f\in X': ||f||\leq 1\}$, then any sequence in $B$ has a subsequence which is weak-* convergent to an element of $B$ (B is compact w.r.t. $d_w$).

proof
: First, we show that any bounded sequence $\{f_n\}\subset X'$ has a weak-* convergent subsequence if $X$ is separable. 

  Let $\{s_k\}$ be a dense sequence in $X$. Since the sequence $\{f_n(s_1)\}$ is bounded, it has a convergent subsequence $\{f_{n,1}(s_1)\}$. Similarly, the the sequence $\{f_{n,1}(s_2)\}$ has a convergent subsequence $\{f_{n,2}(s_2)\}$, and so on. Finally, the diagonal subsequence $\{f_{n,n}\}$ in $X'$ is bounded and $\{f_{n,n}(s_k)\}$ converges for every $k$, so it is weak-* convergent.

  Next, for any sequence $\{f_n\}\subset B$, it has a subsequence weak-*converging to $f'\in X'$. Now, 
  $$ 
   |f(x)| = \lim_{n\to\infty}|f_{n,1}(x) |\leq ||x||, \; x\in X .
  $$
  so that $f\in B$. Also, [Lemma 4.20 (a)](#c4_lem_motivation_weak) shows that $d_w(f_n,f)\to 0$.

  $\Box$


Theorem 23(**Reflexive and weak-\*convergence**) <span id = "c4_thm_weak_reflexive">
: If $X$ is reflexive and $\{x_n\}$ is bounded sequence in $X$, then $\{x_n\}$ has weakly convergent subsequence.

proof
: Let $Y= \overline{sp}\{x_1,x_2,...\}$. Then $Y$ is separable and reflexive (<span style = "color: orange">closed subspace of reflexive is reflexive</span>). Thus $Y''$ is separable ($J_Y(Y)= Y''$ is invertible), and hence $Y'$ is separable ([Theorem 4.13](#c4_thm_dual_separable)). Now, $\{J_Y x_n\}$ is bounded sequence in $Y''$, so we may suppose that $\{J_Y x_n\}$ is weak-* convergent in $Y''$ (taking subsequence if necessary) to a limit of the form $J_Y y$ for some $y\in Y$ (by reflexive). Now for any $f\in X'$, the restriction $f_Y\in Y'$, and so by the weak-* convergence in $Y''$, 
  $$ 
   \lim_{n\to\infty} f(x_n) = \lim_{n\to\infty} J_Yx_n(f_Y) = J_Yy(f_Y) = f(y),\; f\in X',
  $$
  which shows that $x_n\to y$.

  $\Box$

  
