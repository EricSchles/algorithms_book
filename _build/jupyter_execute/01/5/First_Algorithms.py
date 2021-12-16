#!/usr/bin/env python
# coding: utf-8

# # First Algorithms
# 
# We are ready to start!  It may have felt like a long journey getting to this point - all the mathematics, proofs, and programming we had to cover just to get to analyzing our first algorithm, but it will be worth it to have gone through that earlier material.  Some books don't cover all that stuff, but _expect you to know it_.  It is the author's view that doing that to the reader is unfair!  So hopefully all the work was worth it to be at this point.
# 
# Now that we've talked about all that stuff, let's talk formally about what an algorithm is.  As we saw in the last section the computables were used to approximate various mathematical types.  This theme of approximation within a computational system extends to an algorithm as well.  At a fundamental level, algorithms approximate relations and functions.  Algorithms do this through the programming primitives we discussed in the Introduction_to_Python section.  Specifically through the use of the programming primitives:
# 
# * control flow
# * iteration
# * variable assignment
# * closure
# 
# And the data primitives:
# 
# * integer
# * float
# * boolean
# * string
# 
# We are able to express relations and functions as algorithms.  Because algorithms express these mathematical constructs through a lower level set of primitives we can express the same rules and behaviors via many implementations that all do the same thing.  Thus algorithms necessarily vary in how well they are able to approximate the underlying mathematical concept and how fast they are able to compute new values given input data.  The questions of correctness and asymptotic behavior will be central to our study of algorithms.  As you may recall from the las section Types_and_Induction, we discussed the asymptotic behavior of the logarithm function, and specifically that it has finite growth.  This leveling off point will be highly desirable in constructing our algorithms.  Therefore, often our algorithms have a few goals:
# 
# 1. Approximate the underlying mathematics as well as possible
# 2. Approximate the running time, the amount of time the algorithm takes to run for input of size N, as close to a logarithmic function as possible
# 3. Ensure that the algorithm is as clear and easy to read as possible
# 
# As you may have guessed constructing an algorithm to have a logarithmic running time will not always be easy, and in some cases is impossible.  Sometimes the best we will be able to do is a polynomial running time - that is an algorithm that runs in the following form:
# 
# $$O(N^{x}) = c_{0}N^{x} + c_{1}N^{x-1} + c_{2}N^{x-2} + ... + c_{x-1}N + c_{N} $$
# 
# Such an algorithm is approximated by the largest term in it's running time for notational convenience and because the highest order power _tends_ to dominate the running time of any given algorithm.  
# 
# Let's begin our study of algorithms by looking at an example algorithm and the analysis of it's correctness and running time.

# In[1]:


def fizz_buzz(number):
    if number % 3 == 0 and number % 5 == 0:
        return "fizz buzz"
    elif number % 3 == 0:
        return "fizz"
    elif number % 5 == 0:
        return "buzz"
    else:
        return number
    
def test_fizz_buzz():
    assert fizz_buzz(15) == "fizz buzz"
    assert fizz_buzz(3) == "fizz"
    assert fizz_buzz(5) == "buzz"
    assert fizz_buzz(22) == 22
    
test_fizz_buzz()


# The above test gives us some confidence of the corretness of the algorithm `fizz_buzz`.  Now what about the running time?
# 
# Well we can use the following analysis.  We begin by annotating the code of the algorithm:
# 
# ```python
# def fizz_buzz(number):
#     if number % 3 == 0 and number % 5 == 0:   𝑐1
#         return "fizz buzz"                    𝑐2
#     elif number % 3 == 0:                     𝑐3
#         return "fizz"                         𝑐4
#     elif number % 5 == 0:                     𝑐5
#         return "buzz"                         𝑐6
#     else:                                     𝑐7
#         return number                         𝑐8
# ```
# 
# Now we can add up the running times of each of the above:
# 
# $$c =  c_{1} + c_{2} + c_{3} + c_{4} + c_{5} + c_{6} + c_{7} + c_{8} $$
# 
# Please note that 𝑐1 = $c_{1}$ and so forth.  The reason for the change in notation is due to limitations in markdown.
# 
# Here each of the $c_{i}$ stand for constants.  Every line of code will always have _at least_ a constant term because everything must do some _unit_ of work.  Notice, we have different subscripts on each of the constants.  That's because although each line of code may run consistently in the same time, we cannot be sure how fast that will be.  This could be, because of the specifics of the programming language, the specifics of the hardware the program is running on or _any other number of factors_.  Since the specifics of these constants is _often_ not important and will only vary the running time of a program in a very small way, we typically _mostly_ ignore them.  Settling on denoting each line with it's own constant amount of running time.  
# 
# When we add up all the above constants, we get yet another constant, which we refer to as $c$, the total constant running time.  From a notational standpoint we typically denote this as:
# 
# $$ O(1)$$
# 
# Where O is a function of the running time of the algorithm and the $1$ here means constant time.  The choice of $1$ as the notation for $1$ is standard practice, hence it's use.  Some conventions we must all just live with.
# 
# For our next algorithm we will look at one which works in linear time:

# In[6]:


import random

def integer_multiplication(a, b):
    product = 0
    for _ in range(abs(b)):
        product += a
    return product

def test_integer_multiplication():
    for _ in range(10000):
        a = random.randint(0, 5000)
        b = random.randint(0, 5000)
        assert integer_multiplication(a, b) == a * b
        
test_integer_multiplication()


# We now have some sense of correctness, since we checked against the multiplication Python implements, which for the sake of argument we are going to trust as correct implementation for integer multiplication.
# 
# Now let's analyze the algorithm:
# 
# ```python
# def integer_multiplication(a, b):   
#     product = 0                      𝑐1
#     for _ in range(abs(b)):          𝑐2 b
#         product += a                 𝑐3 b
#     return product                   𝑐4
# ```
# 
# Our running time will now be:
# 
# $$ c_{1} + c_{2}b + c_{3}b + c_{4}$$
# 
# Thus our algorithm takes $O(b)$ time to run.
# 
# Next we will look at an algorithm for sorting a list of elements in ascending order.  Sorting is a fundamental notion in the design of algorithms and will help inform many of the techniques we will study throughout the book.

# In[8]:


import random

def simple_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i] < arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr

def test_simple_sort():
    for _ in range(1000):
        arr = [random.randint(0, 500000000) for _ in range(1000)]
        sorted_arr = arr[:]
        sorted_arr.sort()
        assert simple_sort(arr) == sorted_arr

test_simple_sort()


# As you can see from the test, our sorting algorithm at least appears to be correct.  We could actually calculate the probability of a 1000 random arrays of 1000 elements each being sorted by chance. This would give us a measure of how confident we should be in the correctness of our algorithm.  This will be done in the final section of this chapter along with curve fitting.
# 
# In any event, let's analyze this algorithm:
# 
# ```python
# def simple_sort(arr): 
#     for i in range(len(arr)):                    𝑐1 n           
#         for j in range(len(arr)):                𝑐2 ∑𝑡𝑗
#             if arr[i] < arr[j]:                  𝑐3
#                 arr[i], arr[j] = arr[j], arr[i]  𝑐4
#     return arr                                   𝑐5
# ```
# 
# Note that here $t_{j}$ is a shorthand for another constant.
# 
# The full formula for the running time for the above algorithm is:
# 
# $$ c_{1}n + c_{2}\sum_{j=1}^{n}t_{j} + c_{3} + c_{4} + c_{5} $$
# 
# You might be tempted to simply assume this means the running time is $O(n)$.  However, let's consider
# 
# $$c_{2}\sum_{j=1}^{n}t_{j}$$
# 
# Recall that in general,
# 
# $$ \sum_{i=1}^{n}i = \frac{n(n+1)}{2}$$
# 
# Thus, 
# 
# $$c_{2}\sum_{j=1}^{n}t_{j} = c_{2}\frac{n(n+1)}{2} = c_{2}\frac{n^{2} + n}{2}$$
# 
# So our total running time will be:
# 
# $$ c_{1}n + \frac{c_{2}}{2}(n^{2} + n) + c_{3} + c_{4} + c_{5} $$
# 
# So our algorithm runs in $O(n^{2})$.
# 
# Taking a step back so far we've seen how to analyze an algorithm's running time:
# 
# 1. figure out how many steps each line will take
# 2. sum all steps
# 3. reduce any summation notations to the relevant closed form solution.
# 4. find the highest order term which will dominate the equation.
