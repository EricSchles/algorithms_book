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

# In[ ]:




