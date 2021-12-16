#!/usr/bin/env python
# coding: utf-8

# # Introduction To Proofs
# 
# In the last section we learned Python.  Next we will cover proofs, which will be a complete change of gears.  Then in the next section, introduction to counter examples, we will make a first attempt at combining programming and proofs.
# 
# ## What Is Mathematics?
# 
# Although it's likely if you are reading this book you've studied mathematics before, potentially for a large part of your life, have you ever considered what mathematics is?  Take a moment to think about what mathematics means to you.  If you can, write down a definition.
# 
# Now that you've thought about it for a few minutes, and come up with your own definition, let's consider some possible definitions that I thought about.
# 
# Is mathematics the study of counting?  Certainly, mathematics started off about counting, and we can think of lots of ways to build from the counting to lots of other things.  But if all we interested in was counting, then things like geometry might be hard to think about.  So, I think we have to reject that as the definition.  Although, counting is certainly a _part_ of mathematics.  It's so important it's got it's own name, combinatorics.
# 
# Is mathematics the study of numbers?  Mathematics definitely involves numbers.  But again we run into the problem with geometry still?  We can think of numbers as a natural extension of counting for a while, but at some point we reach numbers like $\sqrt{2}$ which doesn't have an intuitive counting equivalent.  But this is a natural thing to do in geometry.
# 
# Consider the following triangle:

# In[5]:


import matplotlib.pyplot as plt

plt.plot([0, 1], [0, 1])
plt.plot([0, 1], [0, 0])
plt.plot([1, 1], [0, 1])


# If we are interested in it's hypotenuse we need to consider it's two other sides, which both measure length 1.  Then we apply the pythagorian formula for length:
# 
# $$ C^{2} = A^{2} + B^{2} $$
# 
# or
# 
# $$ C = \sqrt{A^{2} + B^{2}} $$
# 
# In our case this yields:
# 
# A = 1
# B = 1
# 
# Therefore,
# 
# $$ C = \sqrt{1^{2} + 1^{2}}$$
# 
# then we simply carry out the squaring:
# 
# $$ C = \sqrt{1 + 1}$$
# 
# And carry out the addition:
# 
# $$ C = \sqrt{2}$$

# It is not easy to count $\sqrt{2}$ and yet, it is a thing that occurs _very_ naturally.  So numbers cannot entirely be based on counting.  And even then, it's still not entirely obvious how to capture shapes in the numbers.  Of course, if we embed shapes in the cartesian plane, then this becomes clear, like we did above.  But what if we want to consider geometry _outside_ of the plane?  What then?
# 
# I think this is at least a somewhat convincing argument that numbers are not a strong enough basis for the foundations of all of mathematics.  
# 
# So is geometry?  Well geometry certainly can handle lots of cases.  But what happens when you need things like imaginary or complex numbers?  Or if you are dealing with dimensions that are fractional?  Or if a shape is not the right abstraction?  For instance, consider a social network:
# 
# What shape best describes the connections between you and your friends?  While you might be able to capture this, wouldn't a discrete graph be better than a continuous one?  What about transformations between spaces?  How does geometry think about that?  It may not be easy to capture transformations of an N dimensional plane geometrically.  Especially if there are _affine_ transformations.  Or worse yet, if the transformation makes the space _smaller_, decreasing the number of dimensions of the space.
# 
# No, I think geometry too must fail to be the central core of the study mathematics.  If you are unfamiliar with any of the above, not to worry!  The point of this book is to teach you about each of these things, to some degree.  At the very least, to introduce you to each of the above topics.  In case you've never seen the above topics before:
# 
# The study of complex numbers is called complex analysis.  The study of spaces is called linear algebra, when we are dealing with translations between cartesian coordinates.  If we are dealing with discrete graphs, we are studying graph theory.  The study of spaces when we are not dealing with translations between cartesian coordinates is called topology.  There are many more fields of mathematics, like probability theory, category theory, homology, abstract algebra, real analysis, calculus, differential equations, and many more.  Each discipline is a _part_ of mathematics, but not all of it.  
# 
# So in order to define mathematics, we have to ask ourselves, what do all of these things have _in common_?  My own working definition is this:
# 
# Mathematics is the study of falsifiable statements, and primarily concerned with coming up with _new_ true and false statements using a combination of logic, previously proven mathematical statements, and experimental evidence.
# 
# So in order to learn mathematics, we need to know the _definitions_ of our subfield, we need to know logic, and we need to be able to check our logic for errors or counter examples.  If we can do all that, then we can do mathematics in _any_ subfield, no matter how sophisticated or simple.  Notice, that our definition requires that any statement we consider to prove mathematically be such that, it be either true or false, but not both.  This becomes very tricky in some parts of mathematics.
# 
# For instance, if we consider probability, statistics, or machine learning, it's _not_ necessarily the case that any of the things we say or try to provide evidence for will _stay_ true.  This is where mathematics and science diverge.  Science necessarily has to allow for exceptional cases.  The hypotheses science attempts to prove necessarily have falsifiability.  But that doesn't mean that those statements _always_ be true.  Just that they be predictable.  There are millions of reasons a given experiment could fail, and that may or may not mean that the hypothesis under consideration is true or false.  That is because there is a component of experimental design, associated with an experiment.  And experimental design is subject to failures outside of the thing under observation.  One of these factors is, humans.  We define the parameters of our experiments, and that doesn't always mean we define them correctly.  We also have to analyze the data _after_ or _during_ the experiment has been carried out.  And often when that happens, there can be errors.  This implies that science is certainly interested in truth, but does not require the same tools, nor can we necessarily draw the same conclusions from mathematics that we can from science.
# 
# This is not to say that both aren't _important_ and that they can't work together - they absolutely can and do.  It is my ascertion that both are requirements for the other.  Science helps grounds mathematics in usefulness, and mathematics allows us to extend the technical capabilities of all science.  Therefore, when done well, and learned seriously, the two skills naturally reinforce one another.  But too much of one and not the other can lead to cellings in how far you can go.  
# 
# To summarize and extend, here are some of the areas of mathematics:
# 
# * combinatorics
# * number theory
# * algebra
# * abstract algebra
# * linear algebra
# * real analysis
# * complex analysis
# * topology
# * algebraic topology
# * category theory
# * graph theory
# * geometry
# * algebraic geometry
# * probability theory
# * statistics
# * machine learning
# * numerical methods
# 
# Each of these areas is rich with it's own storied history.  And each of these branches is certainly worthy of study.  That said, we will only have time and space in this text to study some of them, and only at the introductory level.  If you are interested in any of these topics, I highly recommend looking for a relevant set of sources at your nearest library.  Libribrians are a powerful resource, that often goes under utilized.  It's their job to help you find interesting source material, that is useful.  Think of them like google search on steriods.  
# 
# ## An Introduction To Logic
# 
# Logic is the study of statements that are true or false.  Using this binary set of cases, logicians build from basic notions to complex ones.  As an example of a falsifiable statement, consider the following statement:
# 
# P: The integer 5 is odd.
# 
# This statement can either be true or false, there is no wiggle room.  Either 5 is odd or it's even.  Those are our only options.  Whether or not 5 is odd will be proved soon, but for now, don't worry about that.  Now consider the following _open_ statement:
# 
# P(x): The integer 5x is odd.
# 
# The reason this statement is open is because we don't at the writing of the statement know the value of x.  That means it could be either case, until x is given.  If we were dealing with a Python program like this, it would be one where all the functions return a boolean.  Another example of an open statement, in Python would be:

# In[8]:


def is_x_even(x):
    return x % 2 == 0


# Here we are asking if x is even.  If it is, then the function returns true.  If it's odd, the function returns false.  Let's take some examples:

# In[9]:


is_x_even(2)


# In[10]:


is_x_even(3)


# See!  Pretty neat right?  If we want to assess whether an open statement is always true or always false however, we cannot rely on _any_ programming language.  This is because programs are constrained by the computers running those programs, and the compute power associated with those computers.  That means, there is a limit to what a computer can figure out for us.  Next let's look at how a human would check an open statement:
# 
# Suppose P is an open statement, that means it can be either True or False:
# 
# |   P |
# |---
# | T  |
# | F  |
# 
# So we have two possible states for our statement.  What if we had two open statements?  Then we would have 4 possible states:
# 
# | P   |  Q |
# |---  |---
# |  T | T | 
# |  T | F | 
# |  F | T |  
# |  F | F |
# 
# What if we have three open statements?  Then we have 8 possible states:
# 
# |P    | Q   | R |
# |---  |---  |---
# | T   | T   | T |
# | T   | T   | F |
# | T   | F   | T |
# | T   | F   | F |
# | F   | T   | T |
# | F   | T   | F |
# | F   | F   | T |
# | F   | F   | F |
# 
# The above three diagrams are called truth tables and describe the possible states of open statements.  What's powerful about these, is they describe the entire state of a set of statements.  As we'll come to see, when we combine these with boolean operators, we'll be able to make some powerful insights.  
# 
# ## Boolean Operators
# 
# We've already seen these in the last section on Python, for the most part.  There will be a few new additions, but for the most part, this should be review.  First consider a single open statement, like
# 
# P: The integer 2x is even.
# 
# What is the negation of that statement?
# 
# ~P: The integer 2x is not even.  
# 
# OR
# 
# ~P: The integer 2x is odd.
# 
# Next, let's write down the truth table for P and ~P:
# 
# | P  | ~P |
# |--- |--- |
# | T  | F  |
# | F  | T  |
# 
# Notice, that while the truth table for two variables has four possible states, the truth table for a statement and it's negation only has two.  That is because ~P contains the same amount of information as P, except with the opposite values.  In otherwords, there is no extra state information in the negation.
# 
# Let's look at the Python operator equivalent:

# In[1]:


p = True
print(not p)


# In[2]:


q = False
print(not q)


# As you can see, we capture the same amount of information with the Python code, that we do with the diagram.  
# 
# Next let's look at the AND operator.  Unlike the not operator (~), the AND operator has a binary input, because it takes in two open statements.
# 
# Let's look at an example of a compound statement, using AND.
# 
# P: 2x is an even number.
# Q: 3x is an odd number.
# 
# P AND Q: 2x is an even number and 3x is an odd number.
# 
# Now let's look at it's diagram:
# 
# |P    | Q   | P AND Q |
# |---  |---  |---
# | T   | T   | T |
# | T   | F   | F |
# | F   | T   | F |
# | F   | F   | F |
# 
# As you can see, a statement containing an AND is only true if both the components are true.  The next compound statement we will look at is OR:
# 
# Example:
# 
# P: 45x + 7 is an even number.
# Q: 17x - 12 is an odd number.
# 
# P OR Q: 45x + 7 is an even number or 17x - 12 is an odd number.
# 
# Now let's look at it's diagram:
# 
# |P    | Q   | P OR Q |
# |---  |---  |---
# | T   | T   | T |
# | T   | F   | T |
# | F   | T   | T |
# | F   | F   | F |
# 
# As you can see, a statement containing an OR is true unless both of it's components are false.  Now let's ask a question - are AND and OR opposites?  That is, is one true whenever the other is false?  We can check by comparing their truth tables:
# 
# |P    | Q   | P OR Q | P AND Q|
# |---  |---  |---     |---
# | T   | T   | T      | T | 
# | T   | F   | T      | F |
# | F   | T   | T      | F |
# | F   | F   | F      | F |
# 
# It looks like they aren't opposites.  That's because if the pair (P, Q) have the same value, then P AND Q, and P OR Q agree.  If a truth table can tell us when two operators are opposites, that means they can tell us _when they are the same_.  That means, we can use a truth table, to also _prove_ that two operators do the same thing.  
# 
# Consider the following operator which many computer programmers may have seen before:
# 
# |P    | Q   | P XOR Q | 
# |---  |---  |---     |
# | T   | T   | T      |
# | T   | F   | F      |
# | F   | T   | F      |
# | F   | F   | T      |
# 
# This operator says - if both P and Q have the same truth value, XOR will be true and false otherwise.  Can we use the operators we've developed so far to decompose XOR into the operators, AND, OR and NOT?  
# 
# Proof:
# 
# P XOR Q is equivalent to (P AND Q) OR (~P AND ~Q).
# 
# We have already seen the truth table for XOR, but we will add it below for completeness:
# 
# |P    | Q   | P XOR Q | 
# |---  |---  |---     |
# | T   | T   | T      |
# | T   | F   | F      |
# | F   | T   | F      |
# | F   | F   | T      |
# 
# Next, let's do the truth table for the second statement:
# 
# |P    | Q   | ~P | ~Q  | P AND Q | ~P AND ~Q | (P AND Q) OR (~P AND ~Q)|
# |---  |---  |--- |---  | ---     |---        |---                      |
# | T   | T   | F  | F   |   T     | F         |      T                  |
# | T   | F   | F  | T   |   F     | F         |      F                  |
# | F   | T   | T  | F   |   F     | F         |      F                  |
# | F   | F   | T  | T   |   F     | T         |      T                  |
# 
# As you can see they have equivalent truth values everywhere.  QED.
# 
# At the end of a proof we usually write QED, which is an acryonm in latin.  The words mean, "for that which is to be shown".  We can also implement the second operator pretty easily in Python:  

# In[14]:


p = True
q = True

(p and q) or ((not q) and (not p))


# In[13]:


p = False
q = True

(p and q) or ((not q) and (not p))


# In[11]:


p = False
q = False

(p and q) or ((not q) and (not p))


# In[34]:


p = True
q = False

(p and q) or ((not q) and (not p))


# More importantly, we've just seen our first proof!  Proofs are the building block of all of mathematics.  In general it is the main mechanism to verify a new idea.  With a proof, you can be sure you are on stable ground.  In addition to that, it can also be an important mechanism for understanding why a statement is true or false.  So even if we get a negative result by trying to come up with a new idea, often times, in attempting to prove it, we still come away with some deeper understanding.
# 
# In general the way knowledge discovery works is:
# 
# Start with a set of primitives.  Use those primitives to prove new results.  Take the new results as part of your set of primitives.  Prove new results using this new enhanced set of primitives.  
# 
# With a complete system, you could continue this process forever, and learn _everything_ in the world.  While this procedure doesn't _always_ work, it works to an incredibly effective degree.  
# 
# Next let's talk about a very important type of mathematical statement:  If P then Q.  We've already seen this logic play out with the if/elif/else statement in Python, however it's importance and power is greater in mathematics.  This is because if/elif/else statements are only useful for checking specific cases.  We can extend this with a for loop, however it's just not as powerful.  For instance, suppose you wanted to check the following state:
# 
# If x is an integer then 2x is even.
# 
# For let's see how we might check this with Python:

# In[1]:


count = 0
for i in range(100):
    if (i*2) % 2 == 0:
        count += 1
print(count == 100)


# At this point we have verified the statement for the first 100 integers.  But we haven't verified it for _all_ integers.  This is, unfortunately impossible for a machine.  This is because computers have _finite_ memory.  They literally cannot check all the cases.  And this means, we can _never_ be sure with code that a statement of this form will be true from a computer.  
# 
# Now let's look at the truth table for if P then Q.  We'll then use that truth table to prove the above statement.
# 
# |P    | Q   | If P then Q | 
# |---  |---  |---          |
# | T   | T   | T           |
# | T   | F   | F           |
# | F   | T   | T           |
# | F   | F   | T           |
# 
# As you can see we need to check three things - 
# 
# 1. Whether P is true or false
# 2. Whether Q is true or false
# 3. The combination of P and Q.
# 
# If P is False, then no matter what, the statement "if P then Q" is _always_ true.  If P happens to be true, then we need to ensure Q is true as well, otherwise the statement is false.
# 
# First let us verify that P is true.  In this case P is:
# 
# x is an integer.
# 
# To make this statement true, we can simply _assume_ P is true.  That is, we can let x be some integer.  No more work is required.  This will have consequences for our statement Q, because now we must also assume the x in 2x is an integer.  If it's not then the statement will be false.  Additionally, if 2x is not even, then the statement will be false.
# 
# So we need to check:
# 
# 1. Is x an integer?
# 2. Is 2x an integer?
# 3. Is 2x an _even_ integer?
# 
# If all three of those are true, then "If P then Q" will be true, and we are _done_.
# 
# Proof:
# 
# let x be an integer.  (by assumption)
# 
# `2 * x` an integer.  (by 2 an integer, x an integer and integers closed under `*`)
# 
# So now we know statements (1) and (2) are both true.  Next all we need to do is verify 2x is even.  At this point, we need the definition of even:
# 
# definition: if y is an integer and `y = 2*r` for some integer r, then y is even.
# 
# From the above definition we can write `2 * x = t` and t is an integer (by (1) and (2)).
# 
# Therefore,
# 
# If x is an integer, then 2x is even.
# 
# QED.
# 
# In this proof, we tried to _as explicit as possible_.  In some cases, being this explicit will be unnecessary.  However, sometimes, being more explicit than necessary will be helpful in finding errors in proofs.  The question of how much detail to include is much more an art than a science unfortunately.  
# 
# In any event, we've now seen how to prove a statement from a set of primitives.  I want to impress how _powerful_ the above statement is:
# 
# "If x is an integer, then 2x is even"
# 
# is _impossible_ for a computer to prove.  In a few lines of logic, we have shown something a computer can never do.  That's the power of proofs.  By being able to show statements are _always_ true, or _always_ false, we humans are more powerful computational machines than computers.  Perhaps there will come a day when computers _truly_ understand language.  Until that day comes, the human will always reign supreme in terms of computational prowess.  
# 
# Before we leave this proof, there are a few terms and phrases we need to define, that you may not already know.
# 
# During the proof we used the phrase "integers closed under `*`", this means that if you take _any_ two integers and multiply them together, you're answer is _still_ an integer.  
# 
# The second thing you may not be used to is the style of this sort of proof.  Here we made a statement like:
# 
# "let x be an integer.  (by assumption)"
# 
# The thing being stated is the primitive and the thing in the () is the justification.  Sometimes you need a seperate line for the justification.  In which case a () is cumbersome.  But when the reasoning is straight forward to state, using () can add to the readability.
# 
# As an aside, another way to write if P then Q is P => Q, read P implies Q.  The arrow notation is fairly standard and we will mostly use it going forward whenever possible.  
# 
# Now, let's consider - can we write the truth table P => Q using the primitives we've defined so far?  The answer is yes!  Let's state this as a lemma, which is a helper proof, and then prove it!
# 
# Lemma: P => Q is equivalent to (~ P) OR Q.
# 
# Proof:
# 
# In order to prove this, we need only show that the two statements are logically equivalent, which we can do with the truth table:
# 
# |P    | Q   | ~P | P => Q   | (~P) OR Q |
# |---  |---  |--- |---       | ---     |
# | T   | T   | F  | T        |   T     | 
# | T   | F   | F  | F        |   F     | 
# | F   | T   | T  | T        |   T     | 
# | F   | F   | T  | T        |   T     | 
# 
# As you can see, the truth table for the two columns are equivalent!  
# 
# QED.
# 
# While this proof is very straight forward, it gives us another powerful building block for proving results.  Specifically, it may be easier to negate a result and then check if both statements are false.  If both _are not_ false, then the implication P => Q is true!
# 
# Next let's establish the general paradigm for equivalence, because we don't use truth tables directly in proofs.  They are more like a guide for how the proof ought to flow.  And a rubric for what needs to be shown in order to prove the statement.  For this we need something called _the biconditional_.  Notationally the biconditional is often stated as:
# 
# P is equivalent to Q
# 
# OR
# 
# P <==> Q.
# 
# From a logical stand point, this is the same as, (P => Q) AND (Q => P).  Here is it's truth table:
# 
# |P    | Q   | P => Q | Q => P  | (P => Q) AND (Q => P) |
# |---  |---  |---     |---      |---                    |
# | T   | T   | T      | T       |   T                   |
# | T   | F   | F      | T       |   F                   |
# | F   | T   | T      | F       |   F                   |
# | F   | F   | T      | T       |   T                   |
# 
# As you can see, the biconditional is true if both P AND Q are the same and false when they are different.  The careful reader will have noticed that the biconditional is equivalent to _another_ logical operator we've already seen - XOR.
# 
# Lemma:  P <==> Q is equivalent to P XOR Q.
# 
# Proof:
# 
# We need only write down the truth table to verify this:
# 
# |P    | Q   | P => Q | Q => P  | (P => Q) AND (Q => P) |  P XOR Q |
# |---  |---  |---     |---      |---                    |---       |
# | T   | T   | T      | T       |   T                   |     T    |
# | T   | F   | F      | T       |   F                   |     F    |
# | F   | T   | T      | F       |   F                   |     F    |
# | F   | F   | T      | T       |   T                   |     T    |
# 
# QED.
# 
# Another way to prove this without relying on truth tables is to recall that, P => Q is equivalent to (~P) OR Q.  Let's look at that proof, since it doesn't relying on truth tables:
# 
# Lemma: P <==> Q is equivalent to P XOR Q.
# 
# Proof:
# 
# We begin by making use of the fact that we know:
# 
# P XOR is equivalent to (P AND Q) OR (~ P AND ~ Q), from our work above.
# 
# So we need to show (P AND Q) OR (~ P AND ~ Q) <==> (P <==> Q).
# 
# Whenever we are doing an equivalence proof, we need to show the implication in both directions, that is P => Q and then Q => P.  Let's begin with P => Q:
# 
# P <==> Q is equvalent to (P => Q) AND (Q => P). (by truth table in previous proof)
# 
# P => Q is equivalent to (~ P) OR Q.  (by lemma above)
# 
# Q => P is equivalent to ( ~Q) OR P.  (by lemma above)
# 
# Therefore,
# 
# P <==> Q is equivalent to (~ P OR Q) AND (~ Q OR P).  
# 
# We can rearrange (~ P OR Q) AND (~ Q OR P) to get (P AND Q) OR (~ P AND ~ Q).  Unfortunately, there are some laws we haven't introduced yet, so we'll need to use a truth table to verify this statement:
# 
# We have truth table for (P AND Q) OR (~ P AND ~ Q) below:
# 
# |P    | Q   | ~P | ~Q  | P AND Q | ~P AND ~Q | (P AND Q) OR (~P AND ~Q)|
# |---  |---  |--- |---  | ---     |---        |---                      |
# | T   | T   | F  | F   |   T     | F         |      T                  |
# | T   | F   | F  | T   |   F     | F         |      F                  |
# | F   | T   | T  | F   |   F     | F         |      F                  |
# | F   | F   | T  | T   |   F     | T         |      T                  |
# 
# And we have the truth table for (~P OR Q) AND (~Q OR P)
# 
# |P    | Q   | ~P | ~Q  | ~P OR Q | ~Q OR P   | (~P OR Q) AND (~Q OR P)  |
# |---  |---  |--- |---  | ---     |---        |---                       |
# | T   | T   | F  | F   |   T     | T         |      T                   |
# | T   | F   | F  | T   |   F     | T         |      F                   |
# | F   | T   | T  | F   |   T     | F         |      F                   |
# | F   | F   | T  | T   |   T     | T         |      T                   |
# 
# As you can see, the truth tables are equivalent.  This means that (P <==> Q) => (P AND Q) OR (~ P AND ~ Q).
# 
# Next, to go backwards we begin with (P AND Q) OR (~ P AND ~ Q) and need to show we can follow a series of logical connectives to get back to P <==> Q.  
# 
# Beginning from (P AND Q) OR (~ P AND ~ Q):
# 
# (P AND Q) OR (~ P AND ~ Q) is equivalent to (~ P OR Q) AND (~ Q OR P) (by above truth table).
# 
# Next we can break up (~ P OR Q) AND (~ Q OR P):
# 
# (~ P) OR Q  is equivalent to P => Q.  (by lemma above)
# 
# (~ Q) OR P is equivalent to  Q => P.  (by lemma above)
# 
# Therefore,
# 
# (~ P OR Q) AND (~ Q OR P) is equivalent to (P => Q) AND (Q => P).
# 
# And (P => Q) AND (Q => P) is equvalent to  P <==> Q (by definition).
# 
# Therefore (P AND Q) OR (~P AND ~Q) => (P <==> Q).
# 
# So, to sum up we have:
# 
# (P AND Q) OR (~P AND ~Q) <==> (P <==> Q)!
# 
# So P XOR Q <==> (P <==> Q).
# 
# QED.
# 
# While we did have to rely on _one_ truth table still, we mostly could work off of primitives we already established to show that a _new_ statement was true.
# 
# Now that we have some mechanisms for equivalence, let's talk about tautology and contradiction.
# 
# In general, a tautology is a compound statement, where _every_ value of the truth table is true.  Let's look at some examples:
# 
# Lemma: P OR ~P is a tautology.  
# 
# Proof:
# 
# For this we will simply look at the truth table for P and ~P.
# 
# | P   | ~P  | P OR ~P     | 
# |---  |---  |---          |
# | T   | F   | T           |
# | F   | T   | T           |
# 
# QED.
# 
# This means, the statement P OR ~P _will always be true_.  This is means _any_ open statement or it's negation will always be true.  In general tautologies that are compound statements should always be watched out for.  Because if a compound statement happens to take on the form of a tautology, we may simply need to notice that our statement is such to prove it.  
# 
# Hopefully in general it's clear why P or ~P is a tautology - this comes down to the binary nature of truth.  In general, any statement can be either true or false, _but not both_.  So whenever the statement P is true, it's negation will be false, and vice versa.
# 
# Next let's look at another less obvious tautology.
# 
# Lemma:  ~Q OR (P => Q) is a tautology.
# 
# Again we will simply look at the truth table to verify this:
# 
# |P    | Q   | ~Q     |  P => Q | (~Q) OR (P => Q)      |
# |---  |---  |---     |---      |---                    |
# | T   | T   | F      | T       |   T                   |
# | T   | F   | T      | F       |   T                   |
# | F   | T   | F      | T       |   T                   |
# | F   | F   | T      | T       |   T                   |
# 
# QED.
# 
# This one is a little easier to make sense of if we consider the more primative form of P => Q.  Namely, (~P) OR Q:
# 
# (~ Q) OR (~ P OR Q) <==> ~ Q OR Q OR ~ P.
# 
# To see this, we only need to drop the parentheses.  Then we can simply do this:
# 
# (~Q OR Q) OR ~P.
# 
# At this point, the tautology should be obvious - we have Q OR ~Q as one of our terms!  And since that's joined to the ~P with an OR it _doesn't matter_ what the value of ~P is.  If one of the statements true, the whole thing is _always_ true and Q OR ~Q is always true.  
# 
# Let's see one more tautology involving our less primitive operators, this time we'll look at the biconditional:
# 
# Lemma: (Q OR P) OR (P <==> Q) 
# 
# As per usual, we'll look at the truth table:
# 
# |P    | Q   | Q OR P    | P <==> Q |(Q OR P) OR (P <==> Q)|
# |---  |---  |---        |---       |---                   |
# | T   | T   |   T       |     T    |        T             |  
# | T   | F   |   T       |     F    |        T             |
# | F   | T   |   T       |     F    |        T             |
# | F   | F   |   F       |     T    |        T             |
# 
# QED.
# 
# This statement says either P is true, Q is true or P is equivalent to Q.  Not a particularly powerful statement, but certainly worth knowing.  There are _many_ forms for a tautology to take.  And some of them are more obvious, while others are less so.  But if you can notice that a statement is in the form of a tautology, you can _automatically_ prove it with a truth table rather than having to prove any of the actual open statements.  Pretty powerful!  Of course, this is only useful, in so far as the statements _themselves_ are useful for us to know.  Some tautologies are very powerful, while others are essentially useless.  It all depends.
# 
# Next we'll look at contradiction:
# 
# A contradiction is the opposite of a tautology, and comes up _a lot_ in proofs.  In a contradiction, all the values are false, instead of all of them being true.  The simplest contradiction is P AND ~P.
# 
# Lemma: P AND ~P is a contradiction.
# 
# Proof:
# 
# For this we will simply use a truth table, as is typical:
# 
# | P   | ~P  | P AND ~P     | 
# |---  |---  |---           |
# | T   | F   | F            |
# | F   | T   | F            |
# 
# QED.
# 
# What this says is, P can be true or false, but _not_ both.  Since P and ~P always have the opposite truth value, you can never have both being true at the same time.  Therefore, we always get a contradiction.  We leave as an exercise to the reader to come up with more examples of contradictions.
# 
# Next let's look at the "algebra" of AND and OR:
# 
# Commutative Laws:
# 
# 1. P OR Q is equivalent to Q or P.
# 2. P AND Q is equivalent to Q AND P.
# 
# Associative Laws:
# 
# 1. P OR (Q OR R) is equivalent to (P OR Q) OR R
# 2. P AND (Q AND R) is equivalent to (P AND Q) AND R
# 
# Distributive Laws:
# 
# 1. P OR (Q AND R) is equivalent to (P OR Q) AND (P OR R)
# 2. P AND (Q OR R) is equivalent to (P AND Q) OR (P AND R)
# 
# DeMorgan's Laws:
# 
# 1. ~ (P OR Q) is equivalent to (~ P) AND (~ Q)
# 2. ~ (P AND Q) is equivalent to (~ P) OR (~ Q)
# 
# We will leave it as an exercise to prove the above statements.
# 
# This concludes the section on boolean operators.  Congradulations!  You just learned the basics of how to prove things.
# 
# ## Sets
# 
# Now that we've learned about boolean operators and how to prove things, we are ready to introduce our next primitive, sets.  A set is a collection of objects.  In mathematicats this _usually_ means numbers, but not always.  As we've seen from Python, we can put many things into collections.
# 
# Some examples of collections we've seen so far:
# 
# A list:

# In[3]:


listing = [1,2,3,4,5]


# A dictionary:

# In[4]:


dicter = {1:2, 3:4}


# Python even has a builtin set collection:

# In[5]:


set_of_numbers = set([1,2,3,4,5])


# One of the important differences between sets in Python and mathematical sets is, Python sets are _always_ finite.  We have no such restriction in mathematics.  And in fact, _most_ of the sets we'll study are infinite.  The 'smallest' infinite set we'll typically look at is the natural numbers, that is the set:
# 
# $$\mathbb{N} = [0,1,2,3,4...]$$
# 
# Notice that $\mathbb{N}$ starts with $0$.  Not all mathematicians believe this to be the case.  So, it's important to check.  Most computer scientists start the $\mathbb{N}$ with 0, which is why we adopt this convention.
# 
# But before we get into the typical stuff, let's start with some primitives.
# 
# Set theory is about _membership_.  By understand what elements are in a set and what elements are outside a set, then we can prove things about the set.  In Python the equivalence here is the `in` operator.  
# 
# The proofs we will look at, will start by selecting a single "representative" element from a given set, and show how that element is contained or not contained in another set.  By doing so, the relationship between two sets will be understood.
# 
# Now let's look at some primitive operations on sets.  Consider the following diagram:

# In[16]:


from matplotlib_venn import venn2_circles, venn2
import matplotlib.pyplot as plt

c = venn2(subsets = (10, 11, 5))
plt.show()


# Here the numbers are just used as identifiers, and hold no numeric meaning.  Using the above diagram as a reference we can define the following subsets:
# 
# The '5' here represents the intersection of the two sets, written has A $\cap$ B
# 
# The '10' here represents all the elements only in A, written A - B.  
# 
# The '11' here represents all the elements only in B, written B - A
# 
# And finally the union which is all the elements in A, B or in their intersection is written A $\cup$ B
# 
# Notice that A $\cup$ B is always the largest of these four subsets of the diagram.  We cannot say the same for the smallest.  It could be any of A $\cap$ B, A - B, or B - A.
# 
# The above venn diagram is the most typical case, however sometimes all the elements in A are also in B, or vice versa.
# 
# If B is a subset of A:

# In[19]:


c = venn2(subsets = (10, 0, 3))
plt.show()


# In this case A $\cap$ B = B.  If that's the case then we write B $\subseteq$ A, for B is a subset of A.
# 
# Now let's prove some basic facts about sets:
# 
# Lemma: Let A and B be sets.  A $\cap$ B $\subseteq$ A $\cup$ B.
# 
# Proof:
# 
# In this proof we have a few cases:
# 
# 1. A $\cap$ B = $\emptyset$.
# 
# The $\emptyset$ is a short hand for the empty set, and means the set with no elements.  
# 
# 2. A $\cap$ B $\ne$ $\emptyset$
# 
# In this case the intersection contains at least 1 element.
# 
# Let's do case 2 first, since it's more typical:
# 
# Assume that A $\cap$ B $\ne$ $\emptyset$.  Thus let us define x such that x $\in$ A $\cap$ B.  The $\in$ operator indicates that our element is a _member_ of some set.
# 
# Now we have:
# 
# x $\in$ A $\cap$ B (by assumption)
# 
# Therefore x $\in$ A and x $\in$ B.
# 
# From here there are a couple of cases:
# 
# 1. A $\subseteq$ B
# 2. B $\subseteq$ A
# 3. some of the elements of A and B overlap, but not all of them.
# 
# If we are in case 3 then, the following picture is a good depiction:

# In[1]:


from matplotlib_venn import venn2_circles, venn2
import matplotlib.pyplot as plt

c = venn2(subsets = (10, 11, 5))
plt.show()


# In this case, then we can see x $\in$ A $\cap$ B, here labeled '5'.  We can also see clearly from the picture that the 'or' operator subsumes the 'and' operator.  In particular if x $\in$ A $\cap$ B, then it is in A and B, which doesn't include the elements in the union of the form A - B or B - A.  Therefore, we can state:
# 
# if x $\in$ A $\cap$ B => x $\in$ A $\cup$ B, but x $\notin$ A - B and x $\notin$ B - A.
# 
# Let's now consider the case where B $\subseteq$ A:
# 
# As before, we assume x $\in$ A $\cap$ B, but now we also know B $\subseteq$ A, so we have:
# 
# x $\in$ A $\cap$ B => x $\in$ B.  Suppose for a moment that, x $\in$ A - B, then x $\in$ A, but then x $\notin$ B, which would violate our assumption that x $\in$ A $\cap$ B.  Note, that the above logic assumes that, by definition of B $\subseteq$ A, all the elements in B are also in A, but the reverse is not true.
# 
# Finally, we consider case 1, A $\subseteq$ B:
# 
# As before, we assume x $\in$ A $\cap$ B, but now we also know A $\subseteq$ B, so we have:
# 
# x $\in$ A $\cap$ B => x $\in$ A.  Suppose for a moment that, x $\in$ B - A, then x $\in$ B, but then x $\notin$ A, which would violate our assumption that x $\in$ A $\cap$ B.  
# 
# Lastly, let us consider the case where A $\cap$ B = $\emptyset$.
# 
# In this case, there are no elements x $\in$ A $\cap$ B, therefore the proof is vaccuously true by 
# 
# False => True is True and False => False is True.  So there are no cases, where the proof false.
# 
# In the above, since the element x was non-specific, we can apply all of the steps above to any element of the sets.  Therefore it is true for all the elements of the sets.
# 
# QED.
# 
# One of the things we observed in this proof is:
# 
# A $\cup$ B = (A $\cap$ B) $\cup$ (A - B) $\cup$ (B - A).  While we have verified this by the venn diagram picture above, sometimes it is useful to simply restate.  This will end up being a very useful fact for many proofs.  It allows us to directly show certain cases without having to consider a representative element.
# 
# Next let's look at the following result:
# 
# For every two sets A and B,
# 
# A - B = A $\cap$ $\bar{B}$
# 
# Here $\bar{B}$ means the set of all the elements not in B.
# 
# Proof:
# 
# First we show that A - B $\subseteq$ A $\cap$ $\bar{B}$.
# 
# Let x $\in$ A - B.
# 
# Then x $\in$ A and x $\notin$ B.  Since x $\notin$ B, it follows that x $\in$ $\bar{B}$.  
# 
# Therefore, x $\in$ A and x $\in$ $\bar{B}$, so x $\in$ A $\cap$ $\bar{B}$.  Hence,
# 
# A - B $\subseteq$ A $\cap$ $\bar{B}$.
# 
# Next we show that A $\cap$ $\bar{B}$ $\subseteq$ A - B.
# 
# Let x $\in$ A $\cap$ $\bar{B}$.
# 
# Then x $\in$ A and $\bar{B}$.  Since x $\in$ $\bar{B}$, it follows that x $\notin$ B.
# 
# Therefore, x $\in$ A and x $\notin$ B, so x $\in$ A - B.  Hence,
# 
# A $\cap$ $\bar{B}$ $\subseteq$ A - B.
# 
# QED
# 
# Notice that in this proof we used a similiar mechanism for equality that we used for equivalence when we were going over logic.  
# 
# Therefore there is an "equivalence" between P <==> Q and A = B.  Specifically, that:
# 
# P => Q <==> A $\subseteq$ B.
# 
# Notice that, while these two operations are "equivalent" they are _not_ equal.  That's because P and Q are open statements, and A and B are _sets_.  These are different mathematical 'objects' and therefore equality is too strong a statement. 
# 
# There is a equivalent notion in Python for things that are similar but not the same:

# In[2]:


1 == True


# In[3]:


0 == False


# And yet,

# In[4]:


1 is True


# In[5]:


0 is False


# So even though `1` is _not_ `True` in Python, it is equivalent!  And even though `0` is _not_ `False`, it is also equivalent!
# 
# For our next proof we will look at a statement related to something we've already used:
# 
# Lemma: Let A and B be sets.  Then A $\cup$ B = A if and only if B $\subseteq$ A.
# 
# Proof:
# 
# First we show if A $\cup$ B = A then B $\subseteq$ A.  For this we'll need a new technique: the contrapositive.
# 
# Definition: **Contrapositive**
# 
# If P => Q, then the contrapositive is ~Q => ~P.  It has the following truth table:
# 
# |P    | Q   | ~P     | ~Q      | P => Q  | ~Q => ~P |
# |---  |---  |---     |---      |---      |---       |
# | T   | T   | F      | F       |   T     |     T    |
# | T   | F   | F      | T       |   F     |     F    |
# | F   | T   | T      | F       |   T     |     T    |
# | F   | F   | T      | T       |   T     |     T    |
# 
# As you can see, the contrapositive has the same truth table as the implication, so the two statements are equivalent.
# 
# Continuing with the proof:
# 
# The contrapositive of A $\cup$ B = A then B $\subseteq$ A is:
# 
# B $\subsetneq$ A then A $\cup$ B $\neq$ A.
# 
# So now we need to show the contrapositive:
# 
# By B $\subsetneq$ A we have there exists some element x $\in$ B such that x $\notin$ A.
# 
# Since x $\in$ B, it follows that x $\in$ A $\cup$ B.  However, since x $\notin$ A, we have A $\cup$ B $\neq$ A.
# 
# Next we prove the other direction:
# 
# If B $\subseteq$ A then A $\cup$ B = A.  Here we use a direct proof:
# 
# We begin by assuming B $\subseteq$ A.  To verify that A $\cup$ B = A, we need to show that A $\subseteq$ A $\cup$ B and A $\cup$ B $\subseteq$ A:
# 
# First, A $\subseteq$ A $\cup$ B follows from x $\in$ A then x $\in$ A $\cup$ B, by definition.
# 
# Second, A $\cup$ B $\subseteq$ A.
# 
# Here we begin with y $\in$ A $\cup$ B.  Thus y $\in$ A or y $\in$ B. 
# 
# Cases:
# 
# 1. y $\in$ A 
# 
# In this case, we are already done, because if y $\in$ A then A $\cup$ B $\subseteq$ A.
# 
# 2. y $\in$ B
# 
# In this case, we make use of the fact that, by assumption B $\subseteq$ A, which implies y $\in$ A, and therefore A $\cup$ B $\subseteq$ A.
# 
# QED.
# 
# This proof was different than a lot of the proofs we had seen so far, there were many cases, and a lot of techniques required to show each of the steps.  The number of "moving parts" was relatively large.  Whenever you end up in a proof like this, sometimes decomposing your logic into cases can be helpful and greatly reduce the amount of individual effort needed to prove each case.  This technique is useful as well for thinking about problem solving in computer science, as we will see throughout this book.
# 
# As a finale to our section on set theory (for now) we will look at some fundamental properties:
# 
# Let A, B, and C be sets.  Then the following laws are true:
# 
# Commutative Laws:
# 
# 1. A $\cup$ B is equivalent to B $\cup$ A.
# 2. A $\cap$ B is equivalent to B $\cap$ A.
# 
# Associative Laws:
# 
# 1. A $\cup$ (B $\cup$ C) is equivalent to (A $\cup$ B) $\cup$ C
# 2. A $\cap$ (B $\cap$ C) is equivalent to (A $\cap$ B) $\cap$ C
# 
# Distributive Laws:
# 
# 1. A $\cup$ (B $\cap$ C) is equivalent to (A $\cup$ B) AND (A $\cap$ C)
# 2. A $\cap$ (B $\cup$ C) is equivalent to (A $\cap$ B) $\cup$ (A $\cap$ C)
# 
# DeMorgan's Laws:
# 
# 1. $\overline{P \cup Q}$ is equivalent to $\bar{P} \cap \bar{Q}$
# 2. $\overline{A \cap B}$ is equivalent to $\bar{A} \cup \bar{B}$
# 
# If these three sets of laws look familiar, _they should_.  These are the same laws for OR/AND/NOT when we were looking at logic.
# 
# In general there are is a lot of overlap between logic and set theory.  In no small part this stems from how similar the primitives between the two branches of mathematics are.  To recap, those operators are:
# 
# * logical equivalence and equality
# * AND and Intersection
# * OR and Union
# * Not and Complement (the $\bar{A}$ operator).
# 
# At the beginning of this section, I mentioned _membership_ being a central theme of the proofs in set theory, but it goes deeper than that, membership is the main focus of study within set theory.  Though it may not be obvious, this is similar to the main focus of study in logic -> the truth of a statement.
# 
# We've already seen the reason why, from the Python code above:
# 
# * It's because we can map True -> 1
# * And we can map False -> 0
# 
# So what does 1 mean?  Well, think about what a membership function would need?  It would need to take in an element and a set, and return 1 if the element is a member of the set, and 0 if it's not.  
# 
# Let's write down such a function in Python:

# In[6]:


def membership(element, collection):
    return int(element in collection)

membership(5, set([1,2,3]))


# In[7]:


membership(3, set([1,2,3]))


# So our membership function maps elements to the set `{0, 1}`.  Now to ask a very important question, is there anything _special_ about the set `{0, 1}`?  Or could the set `{False, True}` work just as well?  I've made the answer pretty obvious if you look at the code above, but just to really hit you over the head with the point:

# In[8]:


def membership2(element, collection):
    return element in collection

membership2(5, set([1,2,3]))


# The `membership2` function uses `{False, True}` instead of `{0, 1}`!  So what does this mean?  Well, it _means_ that at a _fundamental level_, membership in a set is like the truth of a statement.  Both in terms of the semantics and the _syntax_.  That is sets are concerned at the most primitive level between mapping stuff to a set with two things, and logic is concerned with mapping stuff to a set with two things.
# 
# This connection will be very important for considering the next stop on our tour through mathematics, the (mathematical) function, which we will build up to from relations.
# 
# ## Towards Functions
# 
# Before we get to (mathematical) functions, we need the language to get there.  If you are reading this book, you've probably seen functions for much of your life, but have you ever considered a definition of a function?  What are the central ideas that make a function a function?  
# 
# If you took mathematics through precalculus you've probably seen this picture before:

# In[34]:


import numpy as np
import matplotlib.pyplot as plt

elem = -1
step_size = 2/1000
x = []
for _ in range(1000):
    x.append(elem)
    elem += step_size
y = [elem**3 for elem in x]
fig, ax = plt.subplots()
ax.plot(x, y)
ax.set_aspect('equal')
ax.grid(True, which='both')

ax.axhline(y=0, color='k')
ax.axvline(x=0, color='k')


# The blue line is the value of the function $x^{3}$ as it varies from -1 to 1.  But what about the _stuff_ around the graph?  The _space_ the graph is in.  Well that's called the coordinate system.  Specifically the _cartesian coordinate system_.
# 
# It turns out cartesian coordinates are _not_ restricted to graphs like the above, but will work for _any_ two sets.
# 
# Let's look at a definition for the cartesian product, which we will use to define a cartesian coordinate system:
# 
# A x B = {(a, b): a $\in$ A and b $\in$ B}
# 
# So suppose we had two sets:
# 
# A = {1,2,3}
# B = {4,5}
# 
# Then the cartesian product would be:
# 
# A x B = {(1, 4), (2, 4), (3, 4), (1, 5), (2, 5), (3, 5)}
# 
# If the elements in this set look familiar, it's because we've seen them already in the last chapter, these are just tuples!  In a sense, this is just the most _natural_ way to think about a tuple, as the elements of a discrete coordinate system.  
# 
# In general, we can think of the cartesian product as how we define the _space of the graph_ that we used above.  The big difference being, in the typical graph we use the real numbers, $\mathbb{R}$ instead of the integers, $\mathbb{Z}$.  
# 
# In fact, when we look at a graph we usually say $\mathbb{R}^{2}$ _because_ a graph is usually $\mathbb{R} \text{ } x \text{ } \mathbb{R}$, but let's digress.
# 
# Let's look at some results dealing with the cartesian product of two sets:
# 
# Lemma: Let A, B, C, D be sets.  If A $\subseteq$ C and B $\subseteq$ D, then A x B $\subseteq$ C x D.
# 
# Proof:
# 
# Let (x, y) $\in$ A x B.  (by assumption A $\ne$ $\emptyset$, B $\ne$ $\emptyset$)
# 
# Therefore x $\in$ A and y $\in$ B.  (by definition of cartesian product)
# 
# Since A $\subseteq$ and B $\subseteq$ D, it follows that x $\in$ C and y $\in$ D. (by definition of subset)
# 
# Hence, (x, y) $\in$ C x D. 
# 
# QED.
# 
# In general, proofs involving cartesian products aren't different than proofs involving sets.  You simply need to carry out the steps for every set in the product.  
# 
# Now that we have the basic definitions and language to talk about a multidimensional space, we are ready to take the next step in our journey towards functions.  For this we will need the notion of a relation.  In general a relation is _more general_ than a function and has fewer constraints on the types of properties it must have.  Informally, a relation describes how the elements of two sets _relate_.  If this _sounds_ like a function, it does so for good reason, that's because functions are just a special kind of relation.
# 
# Definition: 
# 
# Let A and B be two sets.  By a relation R from A to B we mean a subset of A x B.  That is, R is a set of ordered pairs, where the first coordinate of the pair belongs to A and the second coordinate belongs to B.  If (a, b) $\in$ R, then we say that a is related to b by R.  In general if a is related to b, we can write a R b.
# 
# An example of a familiar relation may help to make this concrete.  Consider the sets A = $\mathbb{Z}$, B = $\mathbb{Z}$, and the relation is $<$.
# 
# With the relation $<$, any two integers such that a < b will be related, for example:

# In[35]:


4 < 5


# So according to the relation $<$ 4 and 5 are related!  For this example, it would be impossible to write down all the ordered pairs of integers for which the relation $<$ is true.  Let's consider a simpler example:

# In[36]:


A = [1,2,3,4,5]
B = [6,7,8,9,0]


# If we want all the pairs we can generate them as follows:

# In[37]:


pairs = []
for a in A:
    for b in B:
        pairs.append((a, b))
        
pairs


# As you can see, no ordered pair appears twice in our list, so we've captured the entire cartesian product.  Now, let's use the relation `<=`, we can write down the relation as a subset of the pairs:

# In[38]:


relation = []
for element in pairs:
    if element[0] <= element[1]:
        relation.append(element)
        
relation


# Does the relation hold for every element of the cartesian product?  We can answer that by counting the size of the relation, versus the size of the product:

# In[39]:


len(relation) < len(pairs)


# Looks like there are fewer pairs in the relation than there are in the product, thus not every element is related via this relation.  As you can see, relations have a huge amount of value.  We can define them via the rule that describes what to do mechanically, or we can define them via the _set_ they produce.  Suppose we return to the first example, is it possible to describe the $<$ relation on the set $\mathbb{Z}$ x $\mathbb{Z}$?
# 
# It turns out it is!  We can use a short hand notation for sets with infinitely many elements:
# 
# R = { (a, b), a < b : a $\in$ $\mathbb{Z}$ and b $\in$ $\mathbb{Z}$ }
# 
# If this notation looks familar its because it is!  This is _almost_ the same notation that we used with the list comprehension.  In general, computer science and mathematics borrow heavily from each other, and much of the syntax you find in programming languages comes directly from mathematics.  Especially Python.
# 
# Now that we have a few examples of relations, let's consider the various properties that relations can follow:
# 
# * reflexive:
# 
# A relation R defined on a set A is called reflexive if x R x for every x $\in$ A.
# 
# So for example, the relation $<$ is _not_ reflexive.  For instance, consider the set $\mathbb{Z}$, then we have: 

# In[40]:


5 < 5


# Because 5 is _not_ less than itself, or because 5<5 is False, the relation is not reflexive.  Notice, that finding _one_ counter example is enough to prove a property is _not_ true.  However, to prove a statement _is_ true requires we show it for all elements in the set, a much harder feat usually.
# 
# Let's look at the next property:
# 
# * symmetry:
# 
# A relation R defined on a set A is called symmetric if whenever x R y, then y R x for all x, y $\in$ A.  
# 
# Let's look at another example.  Here we will consider the relation $=$ and the set $\mathbb{Z}$.  In order to prove that if x = y, then y = x, we will need some formalism:
# 
# Lemma: The relation $=$ is symmetric on $\mathbb{Z}$.
# 
# Proof:
# 
# let x, y $\in$ $\mathbb{Z}$.
# 
# if x = y, then x is the same as y, so we can substitute x for y, 
# 
# therefore we have, x = x.
# 
# And since x = y, y is the same as x, so we can substitute y for x,
# 
# therefore we have y = x.
# 
# QED.
# 
# Next let's prove that $=$ is reflexive.
# 
# Lemma: The relation $=$ is reflexive on $\mathbb{Z}$.
# 
# Suppose to the contrary that there exists some x $\in$ $\mathbb{Z}$ such that x $\neq$ x.
# 
# But this is in it of itself a contradiction, because it is impossible for a number to not equal itself.
# 
# Therefore $=$ is reflexive on $\mathbb{Z}$.
# 
# Let's look at the last property:
# 
# * transitivity:
# 
# A relation R defined on a set A is called transitive if whenever x R y and y R z, then x R z, for all x, y, z $\in$ A.
# 
# Example:
# 
# For this, let's use $<$ and $\mathbb{Z}$.
# 
# Lemma: The relation $<$ is transitive on $\mathbb{Z}$.
# 
# Proof:
# 
# Let x, y, z $\in$ A.
# 
# if x < y and y < z, and by the fact that y = y we have:
# 
# x < y < z.
# 
# Therefore, x < z, by the fact that there exists a number y which always seperates x and z.  There is another reason why x < z, given that there exists a number y between them such that y > x and y < z, the integers are an _ordered_ set.  That means we can always indicate which element is larger of two elements in the set.  In otherwords, there is a notion of size.  
# 
# In general, there is a property called the well ordering property, which we will prove later in the chapter which will help clarify _why_ the above proof works.  For now, hopefully this intuition is enough to satisfy you, the reader.  Feel free to skip to the end and read the well ordering property now, if you feel unconvinced.
# 
# In general, for the set $\mathbb{Z}$ and for most of the typical relations it is simply _obvious_ which relations have which properties.  However, these properties are not _always_ obvious.
# 
# Now let's consider some relations on discrete sets.
# 
# Consider the set = {a, b, c} and the following relations:
# 
# $R_{1}$ = { (a,b), (b, a), (c, a) }
# 
# $R_{2}$ = { (a,b), (b,b), (b,c), (c,b), (c,c) }
# 
# $R_{3}$ = { (a,a), (a,c), (b,b), (c,a), (c,c) }
# 
# $R_{4}$ = { (a,a), (a,b), (b,b), (b,c), (a,c) }
# 
# $R_{5}$ = { (a,a), (a,b) }
# 
# $R_{6}$ = { (a,b), (a,c) }
# 
# Which relations are flexibe?
# 
# * $R_{1}$ is not because a is not related to a, b is not related to b, and c is not related to c.
# * $R_{2}$ is not because a is not related to a.
# * $R_{3}$ is because (a,a), (b,b), (c,c) are all members of the relation set.
# * $R_{4}$ is not because c is not related to c.
# * $R_{5}$ is not because c is not related to c and b is not related to b.
# * $R_{6}$ is not because c is not related to c, b is not related to b, and a is not related to a.
# 
# Which relations are symmetric?
# 
# * $R_{1}$ is not because c R a but a (not R) c.
# * $R_{2}$ is not because a R b but b (not R) a.
# * $R_{3}$ is symmetric notice that b not R c but that's okay because c not R b.  Symmetry is about _pairs_ of relations.
# * $R_{4}$ is not because a R b but b (not R) a, c R a, but a (not R) c, and b R c, but c (not R) b).
# * $R_{5}$ is not because a R b but b (not R) a.
# * $R_{6}$ is not because a R b but b (not R) a, a R c, but c (not R) a.
# 
# Which relations are transitive?
# 
# Transitivity is the _hardest_ to show for discrete sets.  This is because we can have the following valid transitive relationship:
# 
# (a,a)
# 
# That's all we need!  How is that possible?  Well the definition of transitivity states:
# 
# if whenever x R y and y R z, then x R z, for all x, y, z $\in$ A.
# 
# So just plug a into x, y, and z:
# 
# If a R a and a R a then a R a.
# 
# It's true.  But it's _unsatisfying_.  Even tricker we can have:
# 
# (b, a), (a, a)
# 
# Why does this work?!
# 
# Well just put b into x and a into y and z:
# 
# If b R a and a R a then b R a.
# 
# It's _certainly_ true.  But very unintuitive.  Did we _even_ learn anything new with this property?  In this case and the case above, not really.  These are the _trivial_ cases.  They are true, but in a sense, who cares?  All that has been shown is _what we already know_.  Mathematics is _full_ of trivial cases.  The word gets thrown around a lot, and leads to a ton of hurt feelings most of the time, but in this case _it's appropriate_.  It may not be obvious _why_ the above two examples even _need_ to be stated.  But, once you've seen them, it should be clear why they are called trivial.  
# 
# In general, the way we prove that a relation is transitive or not is if the resulting final pair is in the relation.
# 
# So for $R_{1}$ we have:
# 
# (a,b), (b, a), which means we have a R b and b R a, therefore a R a should be in the relation.  It's not so $R_{1}$ is not transitive.  The reader should verify which other pairs lead to failures in this relation.
# 
# For $R_{2}$ we have:
# 
# (a,b), (b,c), which means a R b and b R c, therefore a R c should be in the relation.  It's not so $R_{2}$ is not transitive.  The reader should verify which other pairs lead to failures in this relation.
# 
# For $R_{3}$ we will have to verify transitivity across all pairs because the relation is transitive:
# 
# * (a,a)
# * (b,b)
# * (c,c)
# 
# By the general analysis we did above.  Next we move onto the more complex ones:
# 
# * (a,c), (c,a):
# 
# If a R c and c R a then (a,a) (and it is in the relation).
# If c R a and a R c then (c,c) (and it is in the relation).
# If a R c and c R c then (a,c) (and it is in the relation).
# If c R a and a R a then (a,a) (and it is in the relation).
# 
# Thus $R_{3}$ is transitive.
# 
# For $R_{4}$ we have:
# 
# * (a,a)
# * (b,b)
# 
# By the general analysis we did above.  Next we move onto the more complex ones:
# 
# * (a,b)
# 
# If a R b and b R b then (a,b) (and it is in the relation).
# If a R b and b R c then (a,c) (and it is in the relation).
# 
# * (b,c)
# 
# If b R b and b R c then (b,c) (and it is in the relation).
# 
# * (a,c) 
# 
# If a R a and a R c then (a,c) (and it is in the relation).
# 
# So $R_{4}$ is transitive.
# 
# For $R_{5}$ we have:
# 
# * (a,a)
# 
# By the general analysis we did above.  Next we move onto the more complex one:
# 
# * (a,b)
# 
# If a R a and a R b then (a,b) (and it is in the relation).
# 
# So $R_{6}$ is transitive.
# 
# * (a,b)
# 
# Since nothing starts with b there is nothing to check.
# 
# * (a,c) 
# 
# Since nothing starts with c there is nothing to check.
# 
# So $R_{6}$ is transitive.  
# 
# Some of these proofs likely felt unsatisifying either because they were trivial or because there was nothing to really check.  But this is the nature of mathematics sometimes.  Mathematics is about being precise, and sometimes that means being mechanical.  You might think of it like doing the paperwork before you get to go on a fun adventure.  Some of mathematics is truly deep and will lead you to vistas or truth that you never thought possible.  But other parts are incredibly mundane.  There are branches of mathematics that attempt to hide the mundanity through abstraction or by creating proof systems which "automatically" include checks for the mundane.  The author personally likes the mundane.  Trivial examples are important.  Mechanicistically checking cases can help develop intuitiion.  Thus it is the author's personal opinion - don't run from trivial examples, embrace them.  Because all humans learn by examples first, then see the light of theorems.  Mathematics has always come from the discret and weird sub-cases to the general, or at least most of the time, and certainly in the beginning.  Don't run from that, it may be the most important thing you do to gain understanding of the deeper truth.
# 
# Before we leave this section.  There is one final point to be made in detail:
# 
# Relations _are_ sets.  
# 
# This fact may not feel surprising given how we've worked with sets in this section.  That said, when you think about the relations:
# 
# * `<`
# * `<=`
# * `>`
# * `==`
# * `>=`
# 
# Do you see a set?  If your answer is 'no', and for most people it probably isn't 'yes', then a natural question forms:
# 
# Relations are sets, but not on their own.  So what kind of sets are they?
# 
# They are sets that _come from_ other sets.  Or rather, are defined in _terms_ of other sets.  We specify the 'from' set and the 'to' set.  We can also think about these sets as the full possible range of values for the first and second parameter of the relation.
# 
# If we were treating these relations as Python functions we might do something like this:

# In[1]:


def less_than(a, b):
    return a < b

less_than(5, 9)


# The first parameter, a, has to come from _somewhere_.  And when we are dealing with the numbers, we should really specify _what_ numbers.  There are lots of different _kinds_ of numbers, as we'll see in detail soon.  So by specifying the sets ahead of time, we are actually doing something _very_ computer science-y; we are specifying the _types_ of numbers we can pass.  
# 
# We already saw a little bit of types in the last section with integers, floats and booleans, all _types of numbers_.  But now we take the first step towards making it explicit _why_ we should specify types.  There are some technical reasons, to be sure.  For instance, integers and floats are different in terms of storage cost on a machine.  But that's just a superficial reason.
# 
# The _real_ reason for specifying types on a relation or as we'll see on a function is because the relations and functions _behave differently_ depending on what type of number you give it.
# 
# That means, passing in the _wrong_ type, will lead to _wrong_ answers.  And this is a very important notion.  It's one that has led to many systemic failures of systems.  Knowing what to pass in and why it works is an imperative.
# 
# For instance, suppose that one of the parameters in your function _had_ to be an integer.  Let's look at an example where that matters from a purely computer science/programmer perspective.  Suppose we had the following algorithm for multiplication:

# In[2]:


def multiplication(a, b):
    product = 0
    for _ in range(b):
        product += a
    return product

multiplication(5, 6)


# Seems like this works well enough.  Well what happens if we pass in 3.4 for b?

# In[3]:


multiplication(5, 3.4)


# The code breaks!  Luckily the error was caught by the Python interpreter.  But we may not _always_ be so lucky.  In any event, we'll see a lot more from types.  Deciding what types work with certain relations and functions matter.  And they can lead to catastrophic failures in some cases.  Especially when they create silent errors.  
# 
# Returning to the original point, relations are sets that are specified from _other_ sets.  That means we can think of a relation as a kind of subset of two other sets.  Or the way in which the two other sets _relate_.  If you recall from the beginning of this section, there was a graph:

# In[4]:


import numpy as np
import matplotlib.pyplot as plt

elem = -1
step_size = 2/1000
x = []
for _ in range(1000):
    x.append(elem)
    elem += step_size
y = [elem**3 for elem in x]
fig, ax = plt.subplots()
ax.plot(x, y)
ax.set_aspect('equal')
ax.grid(True, which='both')

ax.axhline(y=0, color='k')
ax.axvline(x=0, color='k')


# We can think of the x-axis as our first set, the y-axis as our second set and the _blue line_ as the relationship between our two sets.  This graphical representation doesn't make sense by accident.  It is the visualization of the above idea.  This revelation allows us to ask an interesting question:
# 
# What does the relation look like, when the sets on the x and y axis change?  That idea is left to the reader to think about.  But know this, there is an answer.  And it can lead to more surprising and interesting notions than perhaps many would believe.
# 
# To close out this section we conclude with the following:
# 
# Suppose R is a relation such that, a R b and a $\in$ A, b $\in$ B.
# 
# For each element in A, characterized here by a, there are four possible cases:
# 
# 1. a is related to all the elements b $\in$ B.
# 2. a is related to some of the elements b $\in$ B.
# 3. a is related to one of the elements b $\in$ B.  That is there is a unique b $\in$ B such that a R b.
# 4. a is related to _non_ of the elements b $\in$ B.
# 
# In the extreme cases:
# 
# If a is related to none of the elements in B, then R is $\emptyset$.
# 
# If a is related to all of the elements in B, then R is A x B, in other words, R is the cartesian product that we saw at the beginning of this section.
# 
# Finally, we consider case 3.  If a is related to exactly one of the elements b $\in$ B, then R is a _function_.
# 
# ## Functions
# 
# Let's start with a formal definition.
# 
# Let A and B be nonempty sets.  By a function f from A to B, written $f: A \rightarrow B$, we mean a relation from A to B with the property that every element a $\in$ A is the first coordinate of exactly one ordered pair in $f$.  Since $f$ is a relation, the set A in this case is the domain of $f$.  The set B is called the codomain of $f$.
# 
# For a function $f: A \rightarrow B$, let (a,b) $\in$ $f$, if (a,c) also $\in$ $f$ then b=c.  An example here might help.
# 
# Example:
# 
# Let A = $\mathbb{R}$, B = $\mathbb{R}$, and let $f$= $x^{2}$.
# 
# Then what is $f(5)=$?  Well it's 25.  Are there any _other_ valid answers for $f(5)$?  In other words, can we plug in 5 to the parameter of our function and _ever_ expect a different answer?  Nope.  That's what it means for something to be a function!  
# 
# So, in the case of dealing with a function, we can say:
# 
# If $f$ is a function, $f(a)=b$, and $f(a)=c$ then b = c.  In fact, it _must_ by definition.
# 
# Stepping backward for a second, suppose we asked the same question of a relation, could we find a relation such that some element a maps to possibly more than one place?  Well, yes!  Let's define one right now:
# 
# $$R = \{ (a,a), (a,b) \}$$
# 
# That's a valid relation (in fact it was one of our previous examples.  And it takes a to not one but _two_ places.  Can we think of any typical relations such that this is works?  An obvious example is: `<=`.  Let's look at an example in Python:

# In[1]:


5 <= 5


# In[2]:


5 <= 6


# So 5 <= 5, but _also_ 5 <= 6.  That means that both, (5,5) and (5,6) are in the relation `<=`.  In fact, every relation we've seen other than `==` will have a similar behavior.  For instance with `<`:

# In[3]:


5 < 6


# In[4]:


5 < 7


# There is an important point that must be made, but in order to do that, we'll need to introduce a few definitions.
# 
# Definition:
# 
# Image - If $f: A \rightarrow B$, for a $\in$ A, b $\in$ B, if $f(a) = b$ then $b$ is the _image_ of $a$ under $f$.
# 
# Preimage - If $f: A \rightarrow B$, for a $\in$ A, b $\in$ B, if $f(a) = b$ then $a$ is the _preimage_ of $b$ under $f$.
# 
# Now, an important point to note from one of the functions we saw earlier:  
# 
# Although it is the case that everything in the domain necessarily has _exactly_ one image, the reverse is not _necessarily_ true.  Namely, everything in the codomain does not necessarily have to have _exactly_ one preimage.
# 
# Specifically, let's look at the example of $f(x) = x^{2}$.
# 
# Consider the graph of the function for a moment:

# In[5]:


import numpy as np
import matplotlib.pyplot as plt

elem = -1
step_size = 2/1000
x = []
for _ in range(1000):
    x.append(elem)
    elem += step_size
y = [elem**2 for elem in x]
fig, ax = plt.subplots()
ax.plot(x, y)
ax.set_aspect('equal')
ax.grid(True, which='both')

ax.axhline(y=0, color='k')
ax.axvline(x=0, color='k')


# What do you see when you look at the graph?  Well one thing that might stand out is that negative and positive versions of _any_ number go to the same place.
# 
# That is for, $f(x) = x^{2}$, 
# 
# $f(a) = f(-a)$, $\forall a$ $\in$ $\mathbb{R}$.
# 
# As an aside, the $\forall$ is read _for all_.
# 
# So, in particular that means $f(5) = f(-5)$ and so on.  And _any_ function like this, is a _valid_ function.  
# 
# Given that some functions have this looseness, we can specify properties such that our functions map elements to one and _only_ one place.
# 
# Definition:
# 
# Injective - A function $f: A \rightarrow B$ is called injective if every two distinct elements of A have distinct images in B.
# 
# Lemma:
# 
# Let $f: \mathbb{R} \rightarrow \mathbb{R}$ be defined by $f(x) = 3x - 5$.  Then $f$ is injective.
# 
# Proof:
# 
# Assume that $f(a) = f(b)$, where $a$,$b$ $\in$ $\mathbb{R}$.  Then,
# 
# $3a - 5 = 3b - 5$.  
# 
# 3a - 5 + 5 = 3b - 5 + 5
# 
# 3a = 3b
# 
# $\frac{1}{3}$ * 3a = $\frac{1}{3}$ * 3b
# 
# a = b.
# 
# So f is injective.
# 
# QED
# 
# Here we started off by assuming that our elements in our codomain were equal.  If they produced distinct elements in our domain, in otherwords if our preimage mapped to different places, then we wouldn't have an injective function.  That's _why_ we 'undid' the operations of the function $f(x) = 3x - 5$ to both sides.  We _applied_ the preimage to the function.  Otherwise known as the inverse of a function.
# 
# When dealing with proofs of injectivity we always go backwards, this is because, since we are dealing with a function, we already know that mapping from the domain to the image will guarantee uniqueness.  It's the going backwards, the inverse, that we aren't sure about.  So that's what we need to prove, in general.
# 
# Definition:
# 
# Surjective - A function $f: A \rightarrow B$ is called surjective if every element of B is the image of some element of A.  
# 
# In general, functions can _miss_ part of the codomain.  We saw this when we looked at the graph of $f(x) = x^{2}$.  In specific, any number less than 0 doesn't show up in the codomain.  So that function is _not_ surjective.  Now let's prove that a certain function is surjective.
# 
# Lemma:
# 
# Let $f: \mathbb{R} \rightarrow \mathbb{R}$ be defined by $f(x) = 3x - 5$.  Then $f$ is surjective.
# 
# Proof:
# 
# Let $r$ $\in$ $\mathbb{R}$.  We show that there exists $x$ $\in$ $\mathbb{R}$ such that $f(x) = r$.  We can 'construct' our x to equal r by first applying the _inverse_ of $f(y) = 3y - 5$, namely $g(y) = \frac{y + 5}{3}$ to x.  Note: we _do not_ claim that the inverse g is an actualy function, merely that it reverses the mechanical operations of the function f.  For right now, we only claim that g is a rule for reversing $f$.  Moving on, we have:
# 
# $$ x = g(r) = \frac{r + 5}{3} $$
# 
# $$ f(x) = f(\frac{r + 5}{3}) = 3(\frac{r + 5}{3}) - 5 $$
# 
# $$ r + 5 - 5 $$
# 
# $$ r $$
# 
# Since we could find an x that produces r and because x and r were _generic_ elements of $\mathbb{R}$ this means $\forall$ elements this is true.  Therefore _every_ element in our codomain has a corresponding element in the domain.
# 
# Definition:
# 
# Bijective - A function $f: A \rightarrow B$ is called bijective if every element of B is the image of some element of A and if every two distinct elements of A have distinct images in B.  In other words, if $f$ is injective and surjective, it is bijective.
# 
# A bijective function just means that's it's inverse is _also_ a function.  Let's look at a counterexample first:
# 
# Consider the function $f(x) = x^{2}$, is it's inverse also a function?
# 
# We can show it's not by considering it's preimage and looking at some specific examples.
# 
# Consider the following elements:
# 
# (5, 25), (-5, 25).
# 
# Clearly,  $(5, 25), (-5, 25) \in f$.  
# 
# So to get the _preimage_ of $f$ we simply need to reverse the order of our coordinates.
# 
# Thus we have $f^{-1}$ (said as f inverse) with elements:
# 
# $(25, 5), (25, -5) \in f^{-1}$.
# 
# But now we have 25 -> 5 AND 25 -> -5.  So $f^{-1}$ is _definitely not_ a function.  In fact, we could have said:
# 
# $$ (a, a^{2}), (-a, a^{2}) \in f $$
# 
# And then looked at the inverse, $f^{-1}$:
# 
# $(a^{2}, a), (a^{2}, -a) \in f^{-1}$.
# 
# So there are _infinitely_ many counterexamples of $f$ failing to be bijective.  

# Note: Much of this section was inspired by A Transition To Advanced Mathematics by Gary Chartrand, Albert D. Polimeni and Ping Zhang.  Many of the examples are directly lifted from that text.  The words are the authors' own, even if the mathematics is not always.  We believe good examples are hard to find, and need to be celebrated when they are.  A Transition To Advanced Mathematics is well worth your money and time.  Since much of the work is outrite lifted this text will always be free, and intends only to educate the reader.

# In[ ]:




