#!/usr/bin/env python
# coding: utf-8

# # A Primer On Calculus
# 
# As with everything we've done thus far in this book, we will intersperse theory, application, and programming.  An honest attempt will be made to motivate the calculus and it's various operators, borrowing heavily from a course on real variables.
# 
# Before we move into the primer there is a bit of mathematical notation and a few definitions we'll need.  These are minor bits and pieces that don't fit in anywhere into the content, but will be important for us to understand.
# 
# 
# ## Set Results
# 
# Just as we can take the sum of n many numbers via:
# 
# $$\sum_{i=0}^{n}i$$
# 
# We can take the union of n many sets via:
# 
# $$ A = \bigcup_{i=0}^{n} A_{i}$$
# 
# Likewise we can take the intersection of n many sets via:
# 
# $$ A = \bigcap_{i=0}^{n} A_{i}$$
# 
# Next, recall that:
# 
# $$ A \setminus B = \{x \in A : x \notin B \} $$
# 
# Then the following theorems are true:
# 
# $$ A \setminus (B \cup C) = (A \setminus B) \cap (A \setminus C) $$
# 
# $$ A \setminus (B \cap C) = (A \setminus B) \cup (A \setminus C) $$
# 
# Proof:
# 
# We begin by showing every element of 
# 
# $$A \setminus (B \cup C) \subseteq (A \setminus B) \cap (A \setminus C)$$
# 
# If $x \in A \setminus (B \cup C)$, then $x \in A$, $x \notin (B \cup C)$. 
# 
# $\iff$
# 
# $x \in A$, $x \notin B$, $x \notin C$. 
# 
# $\iff$
# 
# $x \in (A \setminus B)$ and $x \in (A \setminus C)$.
# 
# $\iff$
# 
# $$x \in (A \setminus B) \cap (A \setminus C)$$
# 
# 
# Because we used $\iff$ we can trace the proof back up and end up with the desired result.  The same logic essentially works for the other case with only very minor modification.  Thus without loss of generality, the above is true.
# 
# Next we'll look at the __symmetric difference__:
# 
# $$ D = (A \setminus B) \cup (B \setminus A) $$
# 
# Here the set D is all the elements that belong to either A or B but both.  This is equivalent to the XOR operator we saw earlier.
# 
# ## Function Results
# 
# Now that we've covered all the necessary minor extensions to our knowledge within set theory, it's time to extend our knowledge of functions.
# 
# We begin by looking at restrictions and extensions:
# 
# If $f$ is a function with domain $D(f)$ and $D_{1}$ is a subset of $D(f)$, it is often useful to define a new function $f_{1}$ with domain $D_{1}$ by $f_{1}(x) := f(x)$ $\forall x \ in D_{1}$.  This function $f_{1}$ is called the restriction of f to the set $D_{1}$.  
# 
# Thus we have:
# 
# $$ f _{1} := \{(a, b) \in f : a \in D_{1} \} $$
# 
# Sometimes we may write $f_{1} = f | D_{1}$ to mean the restriction.  There is a secondary notion called extension which sort of 'goes the other way'.  If $g$ is a function with domain $D(g)$ and $D(g) \subseteq D_{2}$, then any function $g_{2}$ with domain $D_{2}$ such that $g_{2}(x) = g(x)$ $\forall x \in D(x)$ is called an extension of $g$ to the set $D_{2}$.
# 
# Next let's look at a notion called __composition__:
# 
# Let $f$ be a function with a domain $D(f)$ in A and range $R(f)$ in B and let $g$ be a function with domain $D(g)$ in B and range $R(g)$ in C.  Then the __composition__ $g \circ f$ is the function from A to C, such that 
# 
# $$g \circ f:A \rightarrow C$$
# 
# Note: Our definitions of restriction and extensions apply naturally to function composition.  If you could compose two functions, assuming they had the same  $R(f)$ and $D(g)$ except $D(g) \subset R(f)$, we can then restrict $R(f)$ such that $R(f) = D(g)$, thus allowing for the composition.
# 
# Now let's look at a slight modification to our understanding of injective, surjective and bijective functions.
# 
# Facts:
# 
# * Given an injective function we can define an inverse $f^{-1}$ by restricting the $D(f)$ to $R(f)$ such that $D_{R} = \{ x \in D(f) : f(x) \in R(f) \}$.  This gives us a function $f^{-1}: R(f) \rightarrow D_{R}(f)$.
# 
# In what follows let $f : A \rightarrow B$, such that $A = D(f)$ and $B = R(f)$.  We do not assume $f$ is injective.
# 
# * If $E \subseteq A$, then the __direct image__ of E under $f$ is the subet $f(E)$ of B given by
#     
#     $$ f(E) := \{f(x) : x \in E \} $$
#     
#     
# * If H is a subset of B, then the __inverse image__ of H under $f$ is the subset $f^{-1}(H)$ of A given by
#     
#     $$ f^{-1}(H) := \{x : f(x) \in H \} $$
# 
# ## The Real Numbers
# 
# Until now we have only provided a naive view of the real numbers.  Now we will need precise axiomatic understanding of the reals in order to build towards the calculus.  We begin by noting that the reals are a "complete ordered field".  We will rigourously define what that means piece by piece during the next section.  
# 
# Informally,
# 
# * A field has to do with the algebraic properties of addition and multiplication within the set.
# * An ordered set is one in which you can say whether or not a given element is larger than any other element in the set.  So we have a relations <,>,<=,>=,== defined on the set, such that those operations are always defined for any pair of elements.
# * Finally completeness has to do with 'holes' in the set.  Since R has no 'holes' it is complete.  We've already seen an example hole in the rationals, trying to define $sqrt{2}$ as a rational.  The reals have no 'holes' in this sense.  That isn't to say it is the _largest_ possible complete set.  This is an informal definition and should provide only naive understanding.
# 
# ### Algebraic Properties of the Reals 
# 
# In this section we will define what a field is in the context of the reals.  The reals have the following algebraic properties based on the standard definition of addition and multiplication.
# 
# Addition properties:
# * (A1) a + b = b + a $\forall a,b \in \mathbb{R}$
# * (A2) (a + b) + c = a + (b + c) $\forall a,b,c \in \mathbb{R}$
# * (A3) There exists an element 0 in R such that 0 + a = a and a + 0 = a $\forall a \in \mathbb{R}$
# * (A4) For each $a \in \mathbb{R}$, $\exists \text{ }(-a) \in \mathbb{R}$ such that a + (-a) = 0 and (-a) + a = 0
# 
# Multiplication properties:
# * (M1) a * b = b * a $\forall a,b \in \mathbb{R}$
# * (M2) (a * b) * c = a * (b * c) $\forall a,b,c \in \mathbb{R}$
# * (M3) There exists an element 1 in R such that 1 * a = a and a * 1 = a $\forall a \in \mathbb{R}$
# * (M4) For each $a \neq 0 \in \mathbb{R}$, $\exists \text{ }\frac{1}{a} \in \mathbb{R}$ such that $a * \frac{1}{a} = 1$ and $\frac{1}{a} * a = 1$
# 
# Distributive property:
# 
# * (D) a * (b + c) = (a * b) + (a * c) and (b + c) * a = (b * a) + (c * a) $\forall a,b,c \in \mathbb{R}$
# 
# Notice that we _implicitly_ have subtraction and division as the inverses of addition and multiplication, respectively.  
# 
# We will now present the following proofs to show how to prove results in the reals, making use of the above assumptions.
# 
# Theorem:
# 
# (a) if $z, a \in \mathbb{R}$ such that z + a = a, then z = 0.
# (b) if $u, b \in \mathbb{R}$, $b \neq 0$ such that u * b = b, then u = 1.
# 
# The above theorem may seem like two distinct theorems, but it is not.  We verify the same property, but for two seperate operators.
# 
# Proof.
# 
# (a)
# 
# $0 = a + (-a)$ (by A4)
# 
# $(z + a) + (-a)$ (by assumption)
# 
# $z + (a + (-a))$ (by A2)
# 
# $z + 0$ (by A4)
# 
# $z$ (by A3)
# 
# Thus, $0 = z$.
# 
# Q.E.D.
# 
# (b)
# 
# $1 = b * \frac{1}{b}$ (by M4)
# 
# $(u * b) * \frac{1}{b}$ (by assumption)
# 
# $u * (b * \frac{1}{b})$ (by M2)
# 
# $u * 1$ (by M4)
# 
# $u$ (by M3)
# 
# Thus, $1 = u$.
# 
# Q.E.D.
# 
# As you can see, we can freely make use of the axioms and this gives us the power to easily prove a number of results with relative easy and with only minor justification.  That is what axiomatic proof systems, like the reals so enticing.  The elegance of such systems allows us to take as primitive a number of helpful results to prove a broader range of proofs.  In general, this is how mathematical progress is made, by identifying a set of results which can work to prove a large number of results, or make it trivial to prove a large number of results.  Such knowledge allows us to 'build out' our knowledge rapidly.  For instance, the programming primitives:
# 
# * flow of control
# * variable assignment
# * functions
# * classes
# * primitive types
# * boolean operators
# 
# Is all we really need to construct a programming language.  And from there we can construct a staggering number of programs.  By establishing certain mathematical results, we can too, prove a very large set of results with relative ease.  By intelligently proving certain results, we can extend to whole new fields of study.  The art of discovering which proofs are important and how they lead to a large set of comparatively trivial results is unfortunately, mostly an art.  There are some tools that mathematicians have come up with to try and make this more procedural and straight forward, but due to the incompleteness theorems, you'll never know when you'll run into a 'sharp edge' (an unprovable result that happens to be true).  
# 
# ### The Order Properties of the Reals
# 
# 

# In[ ]:




