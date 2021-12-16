#!/usr/bin/env python
# coding: utf-8

# # Introduction To Python
# 

# In this notebook we will be introducing the Python language, it's main ideas and the basic primitives of computation that are mostly language agnostic.

# ## What Is A Computer Program Anyway?

# In general a computer program is a series of commands called code that get executed in order.  Every application on your computer is just a series of these programs.  So anything you can do on a computer, you can automate with programs.  For instance, say you want a song to play at 8am every morning from your computer, you can write a program for that.  Suppose you want automatically transfer money from your savings to a diversified portfolio of investments, you can write a program for that.  Suppose you'd like to automatically detect when you are out of toilet paper and order more?  That too can be automated, with a little help from sensors around the house.  Many things can be automated.  And the point of computer programming, is to automate them.  
# 
# In addition to automation, there turns out to be deeper "generalizations" of the notions within automation that allow us to reason about automation and find "faster" or more "efficient" ways to carry out automation.  While performance will not be the central focus of this course, it will come up from time to time.  So we will look at an example or two in this chapter.

# ## The Main Concerns In Writing A Program
# 
# There are pretty much two sets of related concerns in programming at the end of the day: 
# 
# * Performance
# * Memory
# 

# How "big" something is determines how fast it can be processed by a machine.  Consider a giant file, say every written work in the world.  Or all the text on the internet.  Say you wanted to search that set of data for the occurrence of the word banana.  And you wanted to count all the occurrences.  Even a trivial task like that, over the full set of all that text would be incredibly time consuming.  Now consider doing the same task over a single one page word document.  It wouldn't even take a second.
# 
# This gives us a sense that the "size" of our data _matters_.  In addition to this, how we carry out the task effects how long it will take.  This means the code we write and _how_ we do things matters.  With an intelligent well written idea for how to perform the task, you can often save yourself minutes, to hours, to days, or even weeks.
# 
# It all depends on what you are trying to do.
# 

# ## Getting Started With Python
# 
# Now that we've covered the ideas behind programming, in very broad strokes.  Let's get into some basic code, after all, programming is not a spectators sport.

# In[1]:


print("Hello World!")


# This single line, by itself is actually an entire "program".  As shocking and simple as it is.  The tradition of writing the "Hello World" in any new language is supposed to signify the start of a journey down the computational path.  But also, it is supposed to signify the simplest possible program to write.  In doing so, you can concentrate on making sure the program runs, before worrying about making the code more complex.  It may or may not be easy to get "Hello World" running on your machine.  It will all depend on your specific computer, and it's set up.
# 
# You should try openning a terminal, writing this in a text file and saying the file with a `.py` extension.  Perhaps call the program `Hello.py`.
# 
# Then you can execute the program from the terminal by typing:
# 
# `python Hello.py`
# 
# Note: You must be in the same directory as the `Hello.py` program in order to execute it.
# 
# you can check if you are in the right place by typing:
# 
# `ls`
# 
# If you see `Hello.py` listed amongst the files and folders that will print to the terminal, you are in the right place.
# 
# You can change to the directory with `Hello.py` by using the `cd` command and specifying the folder path to the directory with the file you want to execute.
# 
# I recommend downloading Python from here: https://www.python.org/downloads/
# 
# Even if it's already installed on your computer, that may not be good enough!  Make sure you have Python 3.6 or higher, otherwise your assignments won't work.  
# 
# Please Note: Installing Python _may_ not be easy.  Programming is _always_ hardest at the start.  Being able to set up stuff for yourself is where most people stumble because you know the _least_ and have to move fast.  So it's okay if it takes you time to install Python and get it working from the command line.  It took me a while the first time.  Be patient with yourself.  It's tough out there.
# 
# Please take a moment to try out these steps now.  You'll need to be able to execute Python programs in order to do the assignments, so it's best that you figure this out now.
# 
# ## Variables In Python
# 
# The python language allows us to store data in named variables.  These variables hold data, which can either be mutated or not mutated.  Let's take a look at the main examples:
# 
# * int - these are the generic integers
# * float - these are sort of like the "real" numbers from math, but they aren't as dense and they aren't infinite.  We call these the "computables" or the floating point numbers.
# * bool - this type of variable can only be `True` or `False`.
# * string - this type of variable contains "characters" that are strung together.  Strings are different than integers and floats in that they don't represent numbers.
# 
# Examples in code:

# In[2]:


# Integer

x = 0
print(x)

x = x + 7
print(x)

x * 4
print(x)

x /= 5
print(x)


# Here we have a simple program that creates a variable `x` and stores the value `0` in `x`.  This is done through the use of `=`.  Which in a program is not equality, but _assignment_.  Notice that if we want to mutate the stored value of `x` we need to first update the original value by another value and then store the result in the original variable.
# 
# This is captured with the line:
# 
# `x = x + 7`.
# 
# As a counter example, if we simply multiple `x * 4`, but do not update it's value with an assignment statement, the value of x is not updated.  This is because programs are pedantic.  They will only do what you tell them, nothing more and nothing less.  And they will do it _exactly_.  
# 
# Finally, having to write `x = x + whatever` is annoying, so programmers came up with the `operater=` short hand.
# 
# 

# We see that here with `/`, which stands for division.  Specifically, `/=`.  But this will work with _any_ of the mathematical operators we've seen so far.  So:
# 
# * `+=` works
# * `-=` works
# * `*=` works
# * `/=` works
# 
# Now then, we can carry out the same exercise with floating point numbers, we'll use `y` this time, instead of `x` just to keep things fresh:

# In[4]:


# Floats

y = 0.7
print(y)

y = y + 7.1
print(y)

y * 4.8
print(y)

y /= 5.7
print(y)


# As you can see, everything we can do with the integers we can do with the floats!  The only real difference is that floats have a decimal point.  This is how you can tell the difference between the two.  There is nothing new here (very much on purpose), so we'll move onto bools:

# In[5]:


# Booleans

x = True
y = False

print(x and y)
print(x or y)
print(not x)


# Since booleans can only take on one of two values, we just capture both of them above.  The `and`, `or`, and `not` operator may be new to you.  But they should be pretty straight forward.
# 
# As you saw above, plus some additions:
# 
# * True and False = False
# * True and True = True
# * False and False = False
# * True or False = True
# * True or True = True
# * False or False = False
# * not True = False
# * not False = True
# 
# Boolean variables may not seem useful, but they are of _huge_ importance for programming in Python.  In fact, they allow us to do things like this:

# In[6]:


x = True
if x == True:
    print("woah it worked")
else:
    print("something has gone wrong here")


# The above code executes something called flow of control or conditional logic.  That means code will execute, only when certain conditions are true.  This opens up a whole _world_ of possabilities for us.  Now we can theoretically write programs that:
# 
# * Turn on lights around the house at specific times
# * Listen to us speaking when we say specific words
# * Only execute when we've run out of toilet paper
# 
# In general this gives us _far_ greater control over the programs we write and how they execute.  Also it turns out we don't need to specify `if x == True`.  The following will work as well:

# In[7]:


x = True
if x:
    print("woah it worked")
else:
    print("something has gone wrong here")


# This is because `if` statements only check for a boolean value to be True in order to execute.  The really nice thing is, now we can also make _statements_ that evaluate to _True_ and things will still work:

# In[8]:


x = 7
if x + 5 == 12:
    print("cool, math still works")
else:
    print("oh no, folks we've broken math")


# As you can see, we started off with a variable, namely `x = 7` and then added `5` to it.  What should be new is the `==` which is Python's way of doing _equality_.  Which means the statement:
# 
# `x + 5 == 12` 
# 
# Asks the question, does `x + 5` equal `12`?
# 
# If it does, return `True`, else return `False`.
# 
# Finally, let's look at strings:

# In[9]:


# Strings

greeting = "Hello there"

greeting += " new friend,"
print(greeting)


# There are two new elements here:
# 
# 1. Mutli letter semantic variable names
# 2. Strings!
# 
# In Python, generally speaking, it's always better for your names to be semantic, so you can easily reason about your code.  The closer you can get your code to english, the better.  
# 
# We also saw strings, which we can "concatenate" together with the `+` symbol.  This implies something important:
# 
# _Operators act differently depending on the data you supply them_.
# 
# This is not _always_ true.  It very much depends.  But for the primitive operators you can take it as a given.  This will be _very_ helpful for debugging your code, which happen a lot, and forever.  Almost nothing will ever work the first time.

# ## Iteration, The True Power Of Programming

# Remember how we mentioned efficiency?  Well the reason why programs efficiency matters, is because we are going to do things _a bunch_ of times.  And when I say a bunch of times, I some times mean trillions of times.  
# 
# In order to do this, we use a technique called "iteration".  This allows us to carry out an activity _many_, _many_ times.  
# 
# Let's look at an example:

# In[10]:


index = 0

while index < 10:
    print(index)
    index += 1


# The above simple example accomplishes a fairly trival task, it enumerates all the numbers between 0 and 9.  This is the basis for interation.  Iteration is _always_ indexed by the natural numbers.  That's why we name the variable we are "iterating over" the index.  As the index increases, we get closer and closer to the terminal statement.
# 
# Here the terminal statement is inside a "while" loop.
# 
# A while statement works somewhat like an if statement.  In an if statement, we check a condition and if the condition is True, then we execute a set of steps.  In a while loop, we check if a condition is True, the same way as before.  The difference being, we keep executing the statement, _until_ the statement is False.  This means any while loop has the potential to go on forever, without stopping.  
# 
# The way we get around this generally is with something called a for loop, which will get to in a little while.
# 

# ## Lists

# Now that we've gotten through how to represent data and iteration, the next thing to do is learn to represent "collections" of variables.  For this will need something called a list:

# In[11]:


listing = [1,2,3,4,5]

print(listing)


# Lists are different than the other variables we've seen thus far, in that in addition to being able to print the _entire_ collection, we can also print specific elements:

# In[12]:


print(listing[0])
print(listing[4])


# Notice that lists are "zero-indexed", so if there are "N" elements in our list, then the last number is in the "N"-1st position.  That's why, when we access the fourth index, we are actually getting the 5th element.
# 
# Let's look at how to iterate over a list using a while loop:

# In[13]:


listing = [1,2,3,4,5]

index = 0
while index < len(listing):
    print(listing[index])
    index += 1


# There is actually a short hand for above, the for loop that we talked about earlier:

# In[14]:


listing = [2,3,4,5,6]

for element in listing:
    print(element)


# I started this list at 2 just to make it clear that we iterate _over the elements_ of the list, not an index.
# 
# And if we'd like to print the index _and_ the elements we can do so as follows:

# In[18]:


listing = [1,2,3,4,5]

for index, element in enumerate(listing):
    print("The element is",element,"at index",index)


# Notice that we concatenated the element, index variables with the string by using `,`'s.  This will only work inside of a print statement.  If python sees a string and an integer then this won't work in general, so we cannot do the following:

# In[19]:


"thing " + 5


# And if we try to do this outside of a print statement we end up with:

# In[21]:


"thing", 5, "whatever"


# So if we are outside a print statement and want the equivalent we need to use something called an "f-string":

# In[22]:


x = 5

f"thing {x} whatever"


# Here the f stands for "format".  The way it works is we put `{}` around a variable we have access to and then the string will replace whatever is in the `{}` with that variable.  We can go even farther in making our loops clean, assuming they are doing a small amount of work:

# In[3]:


print([elem for elem in range(2, 7)])


# This little bit of syntactic sugar is called a _list comprehension_.  In general, it's best if you want to apply a transformation to the elements of an already existing list.  We'll get to see how to do transformations soon!

# ## Dictionaries

# While lists are always indexed by the natural numbers, we can also create collections indexed by whatever we want.  These are called dictionaries in Python, but they go by other names in other languages.  So if you are talking to programmers who work in other languages, don't be fooled if they call it something else.
# 
# They work as follows:

# In[23]:


dictionary = {0:1, 1:2, 3:4, 4:5}

print(dictionary)


# Here the first value of each "pair" is the key, or index of the dictionary and the second value is just called the "value".  
# 
# Here is how we get to specific elements:

# In[24]:


dictionary[0]


# Notice that I decided to use the same index that we might find in a list.  With a dictionary we can also do this:

# In[28]:


dictionary["narf"] = 6

print(dictionary)
print()
print(dictionary["narf"])


# As you can see, the index for a dictionary can be any of our primitives _as well as other things_.  We'll get to those later.
# 
# Additionally we can see all the keys of a dictionary at once:

# In[29]:


dictionary.keys()


# or all of the values:

# In[31]:


dictionary.values()


# One of the other differences between lists and dictionaries is how we add elements to each:

# In[32]:


listing = []

dictionary = {}

listing.append(1)
dictionary[0] = 1

listing, dictionary


# For the list we had to use something called "dot notation" to call a "method".  Whereas with a dictionary we can just update directly as part of the "syntax" of a dictionary.  We can _technically_ do this with a list as well, although it's not used as often:

# In[33]:


listing += [2]

listing


# Here the list is updated via concatenation.  Next let's look at some neat things we can do with very special lists, called sets:
# 
# Suppose you had a bunch of numbers in a list like this:

# In[4]:


import random

listing = [random.randint(0, 15) for _ in range(10000)]


# Figuring out how to see if all the elements betweeb 0 and 15 are in your randomly generated sample is very easy with a set:

# In[5]:


set(listing)


# That's because a set will have _at most_ one copy of each element in your list.  This means it's great for getting the _unique_ elements in a list.

# Now that we've gone over all our primitive collections, types and iterations, let's look at a new idea, called a "function".
# 
# In addition to being able to iterate over collections or an index, we can make our code appear more streamlined with functions.  Let's look at an example of a function first:

# In[35]:


def greeting_generator(name):
    return f"Hello there, {name}"

print(greeting_generator("Eric"))
print(greeting_generator("Bob"))
print(greeting_generator("Sally"))
print(greeting_generator("Abby"))


# Having to make each function call explicitly is annoying to type so we can make this more readable with the following iteration:

# In[36]:


def greeting_generator(name):
    return f"Hello there, {name}"

names = ["Eric", "Bob", "Sally", "Abby"]

for name in names:
    print(greeting_generator(name))


# This becomes especially useful if our lists are created from other "up-stream" functions or pulled from a data source.  Also, now our little bit of code can handle a lot more names than we can comfortably type with any sort of speed.
# 
# We'll look at functions in more detail later, but one last thing to consider when using them is that you want it to be clear and explicit what the function expects as well as what it returns.  You can do that with type annotations.  These are little hints to Python about the types we are passing, here is an example:

# In[37]:


def greeting_generator(name: str) -> str:
    return f"Hello there, {name}"

greeting_generator("Sandy")


# As you can see, now we know what _types_ the function expects and returns.  

# 
# In general the syntax for the parameters of the function are - `variable: type of variable` and then the return is after the close paranetheis of the function followed by the type and ending with a colon like so:
# 
# `) -> type of return:`.

# Now that we've seen functions, we can return to our list comprehension example.  Suppose we wanted to know all the squares of the first 200 numbers.  We can do the following:

# In[7]:


def square(x):
    return x*x

squares = [square(elem) for elem in range(200)]
squares[50]


# Taking this a bit further, what if we wanted to capture all the numbers _and_ their squares in a list.  For this we need a new collection called a tuple.
# 
# Tuples in general are pretty simple collections:

# In[8]:


dir(tuple([1,2,3]))


# As you can see tuples don't have much you can do with them, just count and index!  But that's _perfect_ for small collections that shouldn't change!
# 
# Let's go ahead and use them for our above example:

# In[9]:


def square(x):
    return x*x

squares = [(elem, square(elem)) for elem in range(200)]
squares[50]


# Now we've got both the input and the output!  Pretty neat!

# ## Classes
# 

# Now that we've seen how functions work, let's create our "own" class which will allow us to group collections of functions and data together for organizational purposes.  Instead of just using a class for a trivial notion of organizational structure, we'll motivate classes through the paradigm of static and dynamic memory addresses.  These two concepts form the backbone of how computation is done "practically" within a computer, as well why having a type system is useful.  To do this, we'll implement two versions of a list:
# 
# 1. An array type - arrays are have static memory and come pre-assigned with a certain amount of memory.  Then addition is used to index into the elements of the array.  The other reason arrays are useful as a construct, is because they motivate types and the different sizes of said types.  
# 
# 2. A linked list - linked lists have dynamic memory and don't come with any preassigned length.  This means linked lists can have _any_ type of data in them, but we have the drawback of having to iterate through the linked list to get to _any_ element.
# 
# Of course, modern python implementations don't make use of either of these data structures directly.  The largest point of common ground is notionally - all three data structures, the array, the linked list and python lists all are indexed by the natural numbers.
# 
# Let's get started with the array class:

# In[11]:


class Array:
    def __init__(self, of_type="int", start_size=100):
        self.of_type = of_type
        self.element_size = "0" * self.type_size()
        self.internal_memory = ""
        self.array_size = start_size
        self.cur_index = 0
        self.expand_array_size(start_size)
      
    def expand_array_size(self, update_size):
        self.internal_memory += " "
        self.internal_memory += " ".join(
            [self.element_size for _ in range(update_size)]
        )
        self.array_size += update_size
        
    def type_size(self):
        if self.of_type == "int":
            return 4
        if self.of_type == "char":
            return 1
        if self.of_type == "float":
            return 8
        
    def _type_cast(self, element):
        if self.of_type == "int":
            return int(element)
        if self.of_type == "char":
            return str(element)
        if self.of_type == "float":
            return float(element)
        
    def _reassign_slice(self, start_index, end_index, data):
        return self.internal_memory[:start_index] + data + self.internal_memory[end_index:]
        
    def append(self, data, _update_size=100):
        if self.array_size == self.cur_index:
            self.expand_array_size(update_size)
        data_length = len(str(data))
        pad = self.type_size() - data_length
        if pad < 0:
            raise Exception(
                f"Data is too big for this type, maximum length is {self.type_size()}"
            )
        start_index = self.cur_index * self.type_size()
        end_index = start_index + self.type_size()
        self.internal_memory = self._reassign_slice(
            start_index,
            end_index,
            pad*"0" + str(data)
        )
        self.cur_index += 1
        self.array_size += 1
    
    def index(self, key):
        start_index = key * self.type_size()
        end_index = start_index + self.type_size()
        element = self.internal_memory[start_index: end_index]
        return self._type_cast(element)
    
array = Array()
[array.append(i) for i in range(200)]
array.index(150)


# As we can see from the above code, we start off with a static amount of memory and then "index" into the array by virtue of the fact that memory is "continguous", that is, occurring together in sequence.  This partially motivates why we index lists _in general_ by the natural numbers.  It's because the first lists were contiguous in memory.
# 
# Next we'll look at a list with dynamic memory allocation - the Linkedlist.

# In[12]:


class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
        
    def __str__(self):
        return repr(self.data)
    
class LinkedList:
    def __init__(self):
        self.head = None
        
    def append(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = Node(data)
    
    def __str__(self):
        elements = []
        if self.head is not None:
            cur = self.head
            while cur:
                elements.append(cur.data)
                cur = cur.next
        return repr(str(elements))
        
linked_list = LinkedList()

for element in [0,1,2,3,4,5]:
    linked_list.append(element)
    
linked_list.append("a")
print(linked_list)


# As you can see from the above code, we have to dynamically iterate through the elements to get to access each element.  And even to append, we have to iterate to the end of the list, because we explicitly don't want to assume _anything_ about memory addressing.  The advantage of this is we can do things like append strings to our linked list without any thought at all.  But on the downside, we cannot get "fast" indexing, like we do with the array type.

# ## Supplemental Material
# 
# Because there are _many_ python tutorials out there and I don't assume that mine is the best, here are some links that might be helpful:
# 
# * https://www.programiz.com/python-programming/tutorial - a secondary guide to getting started with python that I really liked.
# 
# If you are feeling frustrated, this might make you feel better:
# 
# * http://veekaybee.github.io/2018/03/12/installing-python-is-hard/ - Vicki lays out all the frustrations of installing Python - I never said it would be easy, just possible :)
# 
# If you were completely lost by this first lecture I highly recommend checking out these introduction to Python classes:
# 
# * https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-189-a-gentle-introduction-to-programming-using-python-january-iap-2011/ - this is the most basic python course.  If you were completely lost start here.
# 
# * https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-0001-introduction-to-computer-science-and-programming-in-python-fall-2016/ - a slightly harder introduction.  If most of this made sense but you'd like to dive deeper or were confused by some things go watch these lectures.
# 
# * https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-0002-introduction-to-computational-thinking-and-data-science-fall-2016/ - this course doesn't really cover data science as much as it actually really covers "algorithms", but they do some data science as the course goes further.  As you can see 6-0002 picks up where 6-0001 left off.  This course is _harder_ than you need to understand for much of this class.  But if you really want to push yourself, here is a challenge.  Just make sure to not burn out!
# 

# In[ ]:




