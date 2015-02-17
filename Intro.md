#Welcome to Python

Our first python program/ Why you should learn python:

`import antigravity`

As this awesome comic shows - python is easy to learn, easy to use, and makes programming a breeze.

Tonight I'll show you how to make programs that do a number of great things:

1) Save the world
2) Build a website
3) Write an android application
4) 'Make' a friend
5) Make a game
6) Recognize a friend

Now that I've made a number of claims, let's discuss the philosophy of python

`import this`

Analysis of this text:

Beautiful is better than ugly.
--You should always write code that looks good.  
--The antithesis of this would be a language like brainfuck or (some) perl code.

Explicit is better than implicit.
--Your code should explain itself.  Code that is explicit is well written, and it's intention is clear.  This is accomplished by good naming of variables, by good naming of functions, by good naming of classes.  When you are writing code, you are inventing your own language of computation.  Making sure that this language will make sense to others is the goal here.

Simple is better than complex.

Complex is better than complicated.
--The real statement here is - always make your programs as simple as possible, but never simplier.
--If you can do something easily, do it that way.  For instance, let's say someone asks you to write a function that does addition - you have a number of ways you could do this:
Using the standard rule for addition
Writing a machine learning algorithm that takes in a number of cases of addition and tries to come up with what it thinks is a reasonable addition operator
Writing your own adder function from scratch with binary operations.
Or some other nuts thing.
The simple answer is simply wrap the addition operator and then add in any extra functionality you need.  


Flat is better than nested.
--The natural analogy here is to file systems (for those of you coming from a non-programming background).  It's always better to have folders with one set of files in them rather than a million subfolders with one file each.  

Sparse is better than dense.
--For those of you coming from other languages the idea is - Don't hide anymore functionality than you have to AND above all, don't have functions that do lots and lots of things.


Readability counts.
--Make sure even lay people can read your code, even if they don't fully understand it.

Special cases aren't special enough to break the rules.
Although practicality beats purity.
--Don't be cute.  Do things in a pure when you can, but know when not to.

Errors should never pass silently.
Unless explicitly silenced.
--Handle your errors intelligently.  When your program failes, make sure you know why it fails.

In the face of ambiguity, refuse the temptation to guess.
--Actually do your homework, don't just say things.

There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.

Namespaces are one honking great idea -- let's do more of those!
--OOP is probably something you should do.

##Our first program

In python:
print "Hello World"

In Java:
public class Hello{
	public static void main(String[] args){
		System.out.println("Hello World");
	}
}

In C++:
#include <iostream>
using namespace std;

int main(void){
	cout << "Hello World" << endl;
	return 0;
}

So what do we notice about this code?
How main points of failure do you have in python?  How many in Java? How about in C++?
How much do you have to remember in python?  In Java?  In C++?
How much slower is each piece of code versus the other? (profiler.py)

As we can see - Java and C++ are faster than python (but by tenths of a second).  Of course as the number of lines of code increases this starts to matter.  If you are executing millions of lines of code - a tenth or even a hundredth of a second per line will make a difference.  But for small programs - python usually does just fine.  Where small typically means anything else than 10,000 lines - depending on the application (of course).

##Our first real application

Developers are usually very anti-social - so let's build a friend.

```
print "Hello there"
name = str(raw_input("What's your name?")) #get's input from the user
print "Hello,"+name
print "How are you today?"
```

Let's save it in a file called friend.py and run it as follows - python friend.py

##Understanding the above code:

raw_input - Whatever is between the quotes is printed to the user and then the program waits for the next keystrokes from the person interacting with the program until the enter key is pressed.  Then raw_input will save those keystrokes to the program. 

##Math versus CS - functions

As you might recall from elementary school:

f(x) -> y can be thought of as: y = f(x)

Where x is the input of the function f, and y is the output of f.  In this way we can say, f is a function that 'maps' x to y.  Thus it is fair to say that f(x) is equal to y, hence y = f(x).  

In computer science you can say the same thing, y = f(x); for a function f, input x, and output y.  However, it's not exactly the same (but don't worry about that yet!)

###Back to our example

Now that we understand that functions take in input and send back output we can understand the piece of code:

`name = str(raw_input("What's your name?"))`

Really what's happening is:

`"What's your name?"` is the input of the function `raw_input` and the output is then passed as input to the `str` function.  Finally, the result is saved in the variable 	`name`.  Notice that we don't need to name the output of raw_input.  So,

`name = str(raw_input("What's your name?"))`

is the same as,

`tmp = raw_input("What's your name?")`

`name = str(tmp)`

except explicitly assigned the returned result to a variable `tmp`.

##Functions - Write your own!

Now that you understand what a function is, let's show you how to make your own.  In python there are a number of keywords - you can think of these words and phrases like power words, everytime you learn one, you can do so much more!  Here we'll learn about the `def` keyword.

Here's the structure for defining your own function:

```
def [name of function]([any input variables, ]):
	.. starts block of code
	ends block of code..
	[optional return statement] [return value]

```

Making the structure concrete:

```
def f(x): 
	return x

#calling this function:

print f("Hello there")
```	

If you try running this code you'll see that "Hello there" is printed to the screen.  The function f doesn't do very much - it takes the input, "Hello there" and then it simply returns the value "Hello there" to the function print.  So not very exciting.

Let's make our function do something!  

```
def f(name):
	return "Hello,"+name
	
print f("Eric")
```

If you run this code, you'll see it takes in a name (mine in this case) and returns a standard greeting "Hello,Eric" (in this case).  

Now let's go nuts!

```
def g(name,greeting):
	return greeting + name
	
print g("Eric","Hello there,")
```

In this function we have two inputs, name and greeting.  Since we are passing in input inside of quotes (called strings), when you `+` them it combines them.  

Now let's write a function that does something before returning.

```
def my_age_in_n_years(current_age,current_year,years_in_the_future):
	future_age = current_age + years_in_the_future
	future_year = current_year + years_in_the_future
	return "In " + str(years_in_the_future) + " it will be the year " + str(future_year) + " and you will be " + str(future_age)
	
print my_age_in_n_years(29,2015,72)
```

You should try running this code!   

The final thing about functions that are interesting in python - is that you can pass them as inputs in your functions!

```

def f(g,x):
	return g(x)
	
def thing(y):
	return y + 4

print f(thing,7)

```

If you ran the above code, you should see that the result returned is 11.  So how did that work?  Well, we first define a function f, which takes two inputs - g and x.  The input g is expected to be a function.  We call the function g on the input x by putting parentheses around g.  This signals to python that the input g should be treated as a function.  What actually happens is python checks to see if g has a specific attribute, in this case `__call__`.  Don't worry if that last sentence didn't make sense.  I'm going to explain it later on in the post.  

##Flow Of Control

Now that we can make some simple mathematical functions let's get a little more complicated!  It's time to learn about logic!  

###Boolean Values 

A boolean is a statement that evaluates to true or false.  The boolean was named after George Boole - it's creator.  They have proven to be extremely valuable for mathematics, computer science and a number of other fields.

Boolean statements typically involve one or more of the boolean operators. In python these are `and`, `or`, `not`, `<`,`>`,`==`,`<=`,`>=`.  

Here are some examples of boolean statements in python:

```
print 5 == '5'
print "this" == "this"
print 4<7
print 4 == 7
print 4 < 7 and 7 < 4
print 4 < 7 or 7 < 4
print not "everything" == "anything"
```

If you run the above code you will get back the boolean values true or false for each statement.  As an exercise, try figuring out what each statement should return before running it.

###If Statements

The simplest piece of logic in python is the following:


In generic terms the if statement looks like this:

```
if [boolean statement]:
	code block starts ..
	
	.. code block ends

```

If the boolean statement evaluates to true, the code inside the tabbed area will execute.

Here's a concrete example:
```
x = 4
if x < 5:
	print x
```

The above code first gives a variable x a value 4 and then checks to see if x is less than 5.  If it is, then the value of x is printed.  Try changing the value of x to 6 and see what happens.  

###If, Else conditionals

So now we know how to check if something is true before executing, which is great!  But what if we only want some other thing to execute if the boolean statement evaluates to false?  Enter the else clause.  

In general:

```

if [boolean statement]:
	code block starts ...
	... code block ends
else:
	code block starts ...
	... code block ends

some other code happens here possibly...
```

A concrete example:

```
x = 5
y = 7
if x < y:
	print "x is less than y"
else:
	print "x is greater than or equal to y"

print "all done"
```

Because of the values we set for x and y, the code block in the if statement will execute.  Can you change the code so that the else statement is executed instead?

Stepping back a bit, logically we can think of an if statement as saying - if the statement is true then execute the following code.  The if, else statement says: if the the statement is true then execute the following code, otherwise execute this other code.

### A real example of when to use if statements

Remember this code:

```
def f(g,x):
	return g(x)
	
def thing(y):
	return y + 4

print f(thing,7)
```

Our function f wasn't all that great - mostly because we don't account for the case when someone else (possibly ourselves in the future) calls f without passing the first input as a function.  In this case the above code doesn't work and will crash any programs we write.  Clearly this is no code.  But not to worry!  With the help of the if statement and a little bit of python magic, we'll be able to cover just such a case:

```
import types
def f(g,x):
	if type(g) == types.FunctionType:
		return g(x)
	else:
		return "g needs to be a function!"
def thing(y):
	return y + 4
	
print f(thing,7)
print f(4,5)
```

Try running the above code, what happens?  It should print:

11
g needs to be a function!

Which means we have programmed our code to work even when the user of our code does something we didn't account for or that they weren't supposed to.  This allows us to write safer code, that will work more often, which makes everyone happy.

So a natural question for some of you might be, what was that `import types` thing?  Well python comes with a whole bunch of code that isn't loaded for every program you write.  By importing the code you tell python to go look for that library and import it if you find it.  By importing the code into your program, you are able to make use of the functions, objects and anything else that imported code comes with, in your code.  

The number of libraries available for import with python are the reason the Python language is so great!  By way of explanation check out this XKCD comic that explains the idea behind how many imports python has: [xkcd comic](http://xkcd.com/353/)

##Basic Data Structures

A data structure in Python is kind of like a variable, except it holds more values or it treats values in a particular way.  The two most used data structures in Python are:

1. lists - > [ ]
2. dictionaries -> { }

lists hold elements like this:

```
	x = [1,2,3]	
	# or
	y = [5123,551,213]
	print x
	print y
```
Where as dictionaries hold values like this:

```
	x = {"a":5,"b":7}
	#or 
	y = {"blarg":[12,353,3123],"stuff":[15,12,"weee"]}
	print x
	print y
```

To access the values in lists do the following:

```
	x = [1,2,3]
	print x[0]
	print x[1]
	print x[2]
	print x[2] + x[0]
```

The numbers passed into the brackets is called the index of the value.  The index of a list starts at 0, for many good reasons, and increases in number based on the position in the list.  List elements are seperated by commas.  Notice that the index of a list is incremented by one for the next element in the list.  If this is still unclear please run the above code, which will produce:

1 
2
3
4

1 comes from x[0] since 1 is the value of the element in position 0.  

To access the values in dictionaries do the following:

```
	x = {"a":5,"b":7}
	print x["a"]
	print x["b"]
	print x["a"] + x["b"]
```

Dictionaries are like lists, except indexes are more explicit.  So "a" is the first index in the dictionary, and "b" is the second index.  These indexes are known as keys and they can be any string or integer so they aren't technically ordered like the indexes in a list.  Notice that we access the elements in a similar way.  Observe the output of the above code:

5
7
12

5 comes from x["a"] since 5 is the value of the element referenced by key "a".

Two important points that didn't make it into the above explanation:  

 1. Lists can store any type of value - lists, strings, objects, integers, or floats, etc.
 2. Dictionaries can only store primitive types (integers or strings) as keys, but anything as values.

##For Loops


Looping is possibly the most importand and powerful thing a program can do.  Without understanding loops, programming wouldn't be nearly as powerful.  

Possibly the easiest way to see this is with the following:

```
for i in xrange(100000):
	print i
```

If you run the above code you'll see that all the numbers are printed out.  The xrange function is a special one that creates a list of all the numbers from 0 to input-1.  In this case all the numbers from 0 to 100000-1 values will be created.  

Generally speaking a for loop has the following syntax:

```
for [iterator] in [list of values]:
	code block start ..
	.. code block ends
```

And a for loop accesses each of the elements in the list, sequentially starting at index 0 and going all the way up to the index of the last element in the list.  Because lists start at zero (this is referred to as zero-indexing or being zero-indexed) there are n - 1 elements in the list, where n is the size of the list. 

### A concrete example

Now that we understand how one might use a for loop, let's actually use it to do something cool!

A big problem in mathematics is that of optimization.  By making use of a for loop we can do discrete optimization easily and quickly:

```
def find_max(input):
	max = input[0]
	for elem in input:
		if elem > max:
			max = elem
	return max
	
print find_max([1,2,3,4,5])
```

This code will work on any example where all the elements are integers or floats.  As an experiment, you could try using a list of words.  The code will still work, but doesn't make much sense.


##Object Oriented Programming

The final topic of the day is that of object oriented programming.  This style of programming is used throughout industry and is chalked full of useful features to make a programmers life easier.  Here we will merely introduce you to objects and their power.

```
class Node:
	def __init__(self,val,next=None):
		self.val = val
		self.next = next
	def __str__(self):
		return repr(self.val)
		
x = Node(5)
y = Node(6)
x.next = y
print x
pritn x.next
```
The one of the reasons why objects are useful is, you can build your own data structures very easily.  The above code creates a simple linked list.  A linked list is a list of nodes that are connected together by references.  We've been playing with a more advanced version of the linked list for a while now.  With use of the list data structure provided by Python!  But if you ever wanted to make your own, now you can.

Now understanding what the above code means.  There is a ton of new syntax here.  

`class` - the class keyword is used to state the name of the class.  The general syntax is:

`class [name of class]([optionally any base classes]):`
 
 
Let's look at an even simpler example:

```
class Greeter: 
	def hello(name):
		return "Hello, "+name

g = Greeter()
print g.hello("Eric")
```
Before continuing it is important to note that when a function is defined inside a class it is called a method.

The class Greeter only has the single method called hello which takes name as input and then returns Hello + [name passed in].  Notice that to create a Greeter object you need to type it in with `()` and set it equal to a variable.  This is known as instantiation.

`def __init__(self,[optional inputs go here])` - most classes have a `__init__` method which takes in any input to the class.  Recall from the above example:

```
x = Node(5)
y = Node(6)
```

We can create as many nodes as we like and give them whatever initial values we like.  This is part of the power of objects, they can store variables internally.  

`self` - the self input is given to every single method of the class.  The self keyword is used to reference any variables at runtime.  You can think of the self keyword as a placeholder for the variable used for the class.  Let's look at a simple example to understand this further:

```
class Hello:
	def __init__(self,name):
		self.name = name
	def greet(self):
		print "Hello",self.name

hi = Hello("Eric")
hi.greet()
```

In the above code the self is replaced by the name hi that we instatiated the class with.  However we could have used a whole host of other names.  One of the strengths of object oriented programming is that you can write code in a very general way, being specific only when you need to be.  Which may make your code harder to understand to someone not familar, but will mean you can write fewer lines of code overall.

Notice also that self.name is used in the greet method and correctly prints out the name Eric, when the above code is run.  This is because the object hi knows about the value of self.name from the `__init__` method that was used above.

As a final point in this section, let's talk about functions with underscores - `__[name of function]__`.  Functions or methods with this extra bit of syntax aren't ever meant to be called explicitly.  Instead they have special names and special uses.  

Although you shouldn't call them, you can.  To see what special methods a given object has you can run a `dir` function on it.

Here's an example:

```
import os
print dir(os)
```

As you'll see there are a ton of methods and objects in the os library and some of them have the double underscore.  As a final note, the `__call__` method that comes with some functions is what the python interpreter calls when you type `[function name]()`.

So here's an example of this:

```
def f(x):
	return x+2
	
print dir(f)
```

Does it have `__call__` as one of it's methods? ;)


