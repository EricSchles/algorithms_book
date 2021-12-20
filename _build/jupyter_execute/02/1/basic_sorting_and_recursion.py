#!/usr/bin/env python
# coding: utf-8

# # Basic Sorting
# 
# In this section we will look at three basic sorting algorithms that will aid in practicing the analysis of algorithms.  The first algorithm we will look at is simple sort from chapter 1:

# In[10]:


import random

def simple_sort(arr: list) -> list:
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i] < arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr

def test_simple_sort():
    for _ in range(100):
        arr = [random.randint(0, 500000000) for _ in range(100)]
        sorted_arr = arr[:]
        sorted_arr.sort()
        assert simple_sort(arr) == sorted_arr
        
test_simple_sort()


# Though admittedly very straight forward, simple_sort gives us a window into how sorting works.  The fundamental operations that all sorting algorithms must perform is:
# 
# * comparison, seen with the line:
# 
# ```python
# if arr[i] < arr[j]
# ```
# 
# * swaps, seen with the line:
# 
# ```python
# arr[i], arr[j] = arr[j], arr[i]
# ```
# 
# That's _all_ sorting algorithms are.  Everything else we'll see in the remainder of this chapter on sorting is really more about how to make these simple ideas as efficient as possible.  And since sorting is such a simple notion, we can build up the complexity making the sorting interesting through the lens of efficiency.  That said, every sorting algorithm just boils down to these two lines.  
# 
# Since we already carried out the running time analysis for the above algorithm at the end of chapter 1, we'll now move onto our next sorting algorithm.  Now we'll look at insertion sort, which works on the same principal as simple sort, but in reverse.  Let's look at an implementation:

# In[11]:


def insertion_sort(arr: list) -> list:
    for j in range(1, len(arr)):
        pivot = arr[j]
        i = j - 1
        while (i >= 0) and (arr[i] > pivot):
            arr[i + 1] = arr[i]
            i -= 1
        arr[i + 1] = pivot
    return arr

def test_insertion_sort():
    for _ in range(100):
        arr = [random.randint(0, 500000000) for _ in range(100)]
        sorted_arr = arr[:]
        sorted_arr.sort()
        assert insertion_sort(arr) == sorted_arr
        
test_insertion_sort()


# First let's identify the comparison and swap lines in the algorithm.
# 
# * comparison happens here:
# 
# ```python
# while (i >= 0) and (arr[i] > pivot)
# ```
# 
# In this code a while loop is used instead of an if statement, but while and if have similar behavior since they both check a condition.  Thus the difference is _artificial_.
# 
# * swap happens here:
# 
# ```python
# arr[i + 1] = arr[i]
# ```
# 
# And swap also happens here:
# 
# ```python
# arr[i + 1] = pivot
# ```
# 
# Additionally, you can see the swap happens in two places - the first swap happens based on the comparison condition:
# `(i >= 0) and (arr[i] > pivot)`.  While the final swap places the pivot back into the array at the index before all the elements that were just swapped.
# 
# There is one sort of new idea here that we didn't see in the last algorithm, the notion of a pivot.  Implicitly simple sort had a pivot, if you took the outer loop as the pivot, but this wasn't made explicit.  By explicitly selecting a pivot element as the reference to build our sorting routinue around, we only need to worry about one element.  In a sense, all the other elements in the array 'pivot' around this element and are reorganized with respect to the pivot element.  Once all the other elements have been reorganized, the pivot element can be placed in sorted order _before_ the other elements that were just sorted with respect to the current pivot.
# 
# Next let's analyze the running time of insertion sort:
# 
# ```python
# def insertion_sort(arr: list) -> list:
#     for j in range(1, len(arr)):              𝑐1 n
#         pivot = arr[j]                        𝑐2 n - 1
#         i = j - 1                             𝑐3 n - 1
#         while (i >= 0) and (arr[i] > pivot):  𝑐4 ∑𝑡𝑗
#             arr[i + 1] = arr[i]               𝑐5 ∑𝑡𝑗−1
#             i -= 1                            𝑐6 ∑𝑡𝑗−1
#         arr[i + 1] = pivot                    𝑐7 n - 1
#     return arr
# ```
# 
# In total this turns out to be:
# 
# $$ c_{1}n + c_{2}(n-1) + c_{3}(n - 1) + c_{4}\sum_{j=2}{n}t_{j} + c_{5}\sum_{j=2}{n}(t_{j} - 1) + c_{6}\sum_{j=2}{n}(t_{j} - 1) + c_{7}(n-1) $$
# 
# We can use the result we proved in the last chapter to update this to be:
# 
# $$ c_{1}n + c_{2}(n-1) + c_{3}(n - 1) + c_{4}(\frac{n^{2} + n}{2} - 1) + c_{5}\frac{n^{2}-n}{2} + c_{6}\frac{n^{2}-n}{2} + c_{7}(n-1) $$

# $$ c_{1}n + c_{2}n - c_{2} + c_{3}n - c_{3} + c_{4}\frac{n^{2} + n - 2}{2} + c_{5}\frac{n^{2}-n}{2} + c_{6}\frac{n^{2}-n}{2} + c_{7}n-c_{7} $$
# 
# $$ n(c_{1} + c_{2} + c_{7} + c_{3}) + c_{4}\frac{n^{2} + n - 2}{2} + c_{5}\frac{n^{2}-n}{2} + c_{6}\frac{n^{2}-n}{2} -(c_{2} + c_{3} + c_{7}) $$
# 
# From here it should be clear that $n^{2}$ terms dominate the sum and thus the running time will be $O(n^{2})$.  The next algorithm we will look at will be similar to the last two we observered, it's name is selection sort.  First let's look at an implementation:

# In[12]:


def selection_sort(arr: list) -> list:
    index = 0
    while index < len(arr):
        pivot = arr[index]
        j = index
        smallest = arr[j]
        smallest_index = j
        while j < len(arr):
            if arr[j] < smallest:
                smallest = arr[j]
                smallest_index = j
            j += 1
        arr[index] = smallest
        arr[smallest_index] = pivot
        index += 1
    return arr

def test_selection_sort():
    for _ in range(100):
        arr = [random.randint(0, 500000000) for _ in range(100)]
        sorted_arr = arr[:]
        sorted_arr.sort()
        assert selection_sort(arr) == sorted_arr

test_selection_sort()


# First let's identify the comparisons:
# 
# ```python
# if arr[j] < smallest
# ```
# 
# As you can see, selection works off the idea of finding the smallest possible value within a range of indices.  
# 
# Now let's look at the swap:
# 
# ```python
# arr[index] = smallest
# arr[smallest_index] = pivot
# ```
# 
# Here the swap occurs, where the smallest value is swapped with the current index and then the pivot is swapped with the smallest index.  You may be tempted to think:
# 
# ```python
# smallest = arr[j]
# smallest_index = j
# ```
# 
# Is also a swap, but because we aren't exchanging any values within the array, it is not.  That is we are only mutating a place holder value, preparing it for swapping.  
# 
# While insertion sort is a somewhat specific pattern, the pattern of finding a value based on a condition, is one we'll see over and over again.  As an aside we can pull out the pattern found in selection sort to make two new algorithms:

# In[7]:


def get_biggest(arr: list) -> int:
    biggest = 0
    for value in arr:
        if value > biggest:
            biggest = value
    return biggest

get_biggest([71,4,12,32,19273,5])


# In[8]:


def get_smallest(arr: list) -> int:
    smallest = 99999999999
    for value in arr:
        if value < smallest:
            smallest = value
    return smallest

get_smallest([71,4,12,32,19273,5])


# Returning to the original problem, let's calculate the running time for selection sort:
# 
# ```python
# def selection_sort(arr: list) -> list:
#     index = 0                                     𝑐1
#     while index < len(arr):                       𝑐2 n - 1
#         pivot = arr[index]                        𝑐3 n - 1
#         j = index                                 𝑐4 n -1
#         smallest = arr[j]                         𝑐5 n - 1
#         smallest_index = j                        𝑐6 n - 1
#         while j < len(arr):                       𝑐7 ∑𝑡𝑗-index
#             if arr[j] < smallest:                 𝑐8 ∑𝑡𝑗-index
#                 smallest = arr[j]                 𝑐9 ∑𝑡𝑗-index
#                 smallest_index = j                𝑐10 ∑𝑡𝑗-index
#             j += 1                                𝑐11 ∑𝑡𝑗-index
#         arr[index] = smallest                     𝑐12 n - 1
#         arr[smallest_index] = pivot               𝑐13 n - 1
#         index += 1                                𝑐14 n - 1
#     return arr
# ```
# 
# Summing up as per usual we find:
# 
# $$c_{1} + (n - 1)(c_{2} + c_{3} + c_{4} + c_{5} + c_{6} + c_{12} + c_{13} + c_{14}) + \frac{n(n+1)}{2}(c_{7} + c_{8} + c_{9} + c_{10} + c_{11})$$
# 
# Thus the worst case running time is $O(n^{2})$.
# 
# Something to note in the above analysis - it's not clear if $c_{9}$ and $c_{10}$ will not always have ∑𝑡𝑗-index running time.  However, they will in the _worst case_, that is, if the element is completely unsorted.  
# 
# Now that we've covered the basics on sorting algorithms it's time to introduce a new programming technique which we will make use of to implement a new class of sorting algorithms.
# 
# ## Recursion
# 
# The idea behind recursion appears confusing at first to almost everyone.  It is a powerful tool, but that doesn't make it any easier to grasp.  That said, we will try to break it down into steps and motivate the idea to make it as clear as possible.
# 
# Definition:
# 
# Recursion is a programming technique that uses repeated calls to the same function, rather than a loop to iterate over the contents of a data structure.  
# 
# The term recursion is related to self reference.  In writing it means to each step you will take will feed into the next.  Any thing that is recursive is defined in part by it's previous part.  At this point an example may help:

# In[15]:


def get_largest(arr: list, index: int, largest: int) -> int:
    if arr[index] > largest:
        largest = arr[index]
    if index == 0:
        return largest
    return get_largest(arr, index-1, largest)

arr = [5,4,3,2,1]
index = len(arr) - 1
largest = 0
get_largest(arr, index, largest)


# The above example shows how recursion traverses an array.  Now let's go over the structure of a recursive algorithm.  In some sense, recursion is similar to induction, except in the opposite direction.  In induction, your base case is your starting point, then you assume your kth case and prove your k+1st case.  In recursion, your base case is your end state.  Additionally, you write down your kth case and then use a function call to get to your k-1st case.  In otherwords, you start at the end of your array and go down to the first element _always_.
# 
# In the above code the base case is defined here:
# 
# ```python
# if index == 0:
#     return largest
# ```
# 
# What this says, is if we are in the beginning of the array, there are no more elements to check and we should return.  The return from the base case, in this case will exit the function.  However, _that is not always the case_.
# 
# Next let's look at what happens in the kth step:
# 
# ```python
# if arr[index] > largest:
#     largest = arr[index]
# ```
# 
# This is the actual _work_ of the recursive algorithm.  Here we are checking the array at the index to see if that element is larger than our current value of largest.  If it is, we update our value for largest.  
# 
# Finally we have our code for getting to the k-1st case:
# 
# ```python
# return get_largest(arr, index-1, largest)
# ```
# 
# This is the single hardest step to grasp, if any of this is easy, because it's the most foreign.  Here you will pass the array, unchanged, and _decrement_ the index.  By decrementing the index your next call will check the array all over again, but at the _next smallest index_.  Finally, the current value of largest is passed to the array.  From the 'kth step' part, we see that this value _may have changed_ during the function call.  So we keep track of it's current state and pass it into the next call of the function.
# 
# After we've reached the base case, some more stuff happens.  For most 'simple' recursive algorithms there is no more work to do and we can functionally think of the function returning and leaving the scope of the function.  But for complex recursive algorithms, like the ones we'll use to sort arrays, we need to actually be aware of this next step.  
# What happens after recursion is, _every other function call returns_.  So when you get to the base case, which we will call the kth function call, you then return _up to_ the k-1st function call, which then returns up to the k-2nd function call, and so on, until you get to the _very first function call that was made_.  And that function call exits the function closure.  
# 
# You might be thinking - that sounds like a lot of extra work, why would you ever want to do that?  Well it turns out for some specific problems the ability to recurse is _very useful_.  
# 
# Since recursion is such a confusing topic for those new to it, the author recommends taking some code that uses a single for loop and creating a recursive version of the code.  Since recursion is just a kind of iteration, any code that you can write with a for or while loop can be converted to a recursive version.  It's worth it to practice, as hard as recursion is, it's a valuable tool in the design of efficient algorithms.  
# 
# _That said_, outside of an algorithms course there is _very little_ use of recursion.  The reason being, if we have a recursive algorithm, we can _always_ convert it to one with a for or while loop.  We will see how to do this when we cover dynamic programming.  Finally, it's worth it to state, learning recursion does have value, it teaches you in an intimate way how the machine works.  And the underlying semantics of function calls in a deep way.  Plus the notions that one can express recursively have merit.  Enough digressions though, let's see some more examples.
# 
# Next let's look at an algorithm we've already seen, in an iterative form:

# In[18]:


import random

def factorial_recursive(n):
    if n == 0:
        return 1
    return n*factorial_recursive(n-1)

def factorial(n):
    listing = [1]
    for i in range(1, n+1):
        listing.append(i * listing[i-1])
    return listing[n]

def test_factorial_recursive():
    n = random.randint(0, 15)
    assert factorial(n) == factorial_recursive(n)
    
test_factorial_recursive()


# This function, `factorial_recursive` does the same thing as the factorial we implemented in chapter one.  In fact, the recursive version is typically what students see first.  Notice the points of comparison:
# 
# The return statement found in factorial recursive:
# 
# ```python
# return n*factorial_recursive(n-1)
# ```
# 
# Is virtually the same as the append line:
# 
# ```python
# listing.append(i * listing[i-1])
# ```
# 
# The difference is, the list in `factorial` stores the previous results and we _dynamically_ resize the array to account for the added input.
# 
# Also note the bases cases are identical:
# 
# ```python
# if n == 0:
#     return 1
# ```
# 
# is equivalent to:
# 
# ```python
# listing = [1]
# ```
# 
# Let's see one more example where we are just working with the code.  After this, we'll go back and analyzing the above algorithms to get the running times:

# In[38]:


def fibonacci(n):
    if n == 0 or n == 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

[fibonacci(i) for i in range(12)]


# Here we see an algorithm where our function calls matter, because we are making _multiple_.  This means `fibonacci` happens in stages.  
# 
# Stage 1:
# 
# Make all the recursive function calls, until you get to the base case.
# 
# Stage 2:
# 
# propage up the 'tree' of function calls, adding each intermediate result and then returning up to the next function call.
# 
# In otherwords, since the function is recursive to figure out what fibonacci(3) is, we need to know what fibonacci(2) and fibonacci(1) are.  And to know what fibonacci(2) is we also need two other copies of fibonacci(1).  Each call to the function is not aware of any other function calls with the same input value, so we need to evaluate down to the base case for _each_ call, before we can carry out the sum and return 'up' to the next function call.
# 
# If you need a visual representation to understand the above, I recommend the [following video](https://www.youtube.com/watch?v=dxyYP3BSdcQ&ab_channel=mycodeschool) which walks through a function call to fibonacci(5).

# In[ ]:




