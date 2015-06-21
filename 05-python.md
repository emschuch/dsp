# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

[![Think Python](img/think_python.png)](http://www.greenteapress.com/thinkpython/)

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

Complete the following exercises to check your ability with Python.

These exercises are implemented with doctests, which are runnable tests inside docstrings. Fill in the function definitions. Correct solutions will make it possible to run (for example) `python -m doctest strings.py` with no messages about failures.

 * [Strings](python/strings.py)
 * [Lists](python/lists.py)


---

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

> Both lists and tuples are ordered collections of elements, so each element may be accessed by its index. For a list `lst` the first element can be accessed `lst[0]`, and the same for a tuple, `tup[0]`. They differ in that tuples are immutable (once values are assigned to a tuple, the tuple's elements cannot be changed), while lists are mutable (the elements can be re-ordered, deleted, or more elements can be added).
>
> Tuples will work as dictionary keys because only immutable elements will work as dictionary keys.

---


---

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

> Both lists and sets are a collection of elements, however a list is ordered and a set is unordered. In addition, sets do not contain duplicates, while a list may contain duplicate elements.
>
> A list may be used to keep track of elements that should remain in order. Say you roll a standard die 10 times and want to store the results: `rolls = [1, 4, 5, 2, 5, 3, 3, 6, 1, 2]`. Perhaps this is part of a 2 player game and you want to compare rolls at each index for each player. Lists will work because they are ordered and allowed to have duplicates.
>
> Sets are good for removing duplicates. Say you have two list of students, one for the fall semester and one for spring. Combining the lists and turning it into a set will remove duplicates of any students who took both fall and spring classes.
>
> For both lists and sets an element can be found with `element in list` or `element in set`, and a `True` value will be returned if the element is present. However, lists have additional methods such as `list.index(element)` (which returns an index to tell exactly where in the list the first instance exists), and `list.count(element)` (which returns how many times an element occurs). Sets do not have such methods because they are unordered, so there is no index, and elements are only able to occur once.

---


---

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

> The `lambda` operator is used for writing short, anonymous, in-line functions. A lambda function is limited to a single expression. For example, this lambda function returns the absolute difference between two numbers, x and y: `lambda x, y: abs(x - y)`. Lambda expressions are used to make quick throw away functions when defining a named function would be tedious.
>
> Lambda can also be used for sorting tuples using a `key` argument. I did exactly that in the lists.py exercises with `return sorted(tuples, key=lambda tup: tup[-1])` This sorts a list of tuples by the last element of each tuple.

---


---

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

> List comprehensions are a way of constructing new lists, often from other lists, sequences or iterables. They are useful for filtering lists or performing a function on a sequence of elements. For example, `lst = [x*2 for x in range(10) if x % 2 != 0]` creates a list of numbers from 0 to 10, multiplies the odd numbers by two, and stores them in a list, `lst = [2, 6, 10, 14, 18]`.
>
> The built-in `map()` function takes two arguments, a function and a sequence, and performs the function on each element in the sequence. The built-in `filter()` funtion also takes a function and a sequence as arguments and returns a list from the sequence for which the function is true. To rewrite the list comprehension above with map and filter, `lst = map(lambda x: x*2, filter(lambda x: x % 2 != 0, range(10)))`. While this outputs the same result as above, it is a bit less readable to a human.
>
> Set comprehensions work like list comprehensions but use curly brackets instead of square brackets. `st = {x*2 for x in range(10) if x % 2 != 0}` creates an unordered set of elements with the same values as the elements in `lst`.
>
> Dictionary comprehensions create dictionaries from arbitrary key and value expressions. `dct = {x: x*100 for x in (1, 2, 3)}` will create a dictionary `dct = {1: 100, 2: 200, 3: 300}`.

---


Write a Markov text generator, [markov.py](python/markov.py). Your program should be called from the command line with two arguments: the name of a file containing text to read, and the number of words to generate. For example, if `chains.txt` contains the short story by Frigyes Karinthy, we could run:

```bash
./markov.py chains.txt 40
```

A possible output would be:

> show himself once more than the universe and what I often catch myself playing our well-connected game went on. Our friend was absolutely correct: nobody from the group needed this way. We never been as the Earth has the network of eternity.

There are design choices to make; feel free to experiment and shape the program as you see fit. Jeff Atwood's [Markov and You](http://blog.codinghorror.com/markov-and-you/) is a fun place to get started learning about what you're trying to make.
