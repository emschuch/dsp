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
> A list may be used to keep track of elements that should remain in order. Say you roll a standard die 10 times and want to store the results: `rolls = [1, 4, 5, 2, 5, 3, 3, 6, 1, 2]`. Perhaps this is part of a 2 player game and you want to compare each roll to another player who also rolls 10 times. Lists will work because they are ordered and allowed to have duplicates.
>
> Sets are good for removing duplicates. Say you have two list of students, one for the fall semester and one for spring. Combining the lists and turning it into a set will remove duplicates of any students who took both fall and spring classes.
>
> For both lists and sets an element can be found with `element in list` or `element in set`, and a `True` or `False` value will be returned. However, lists have additional methods such as `list.index(element)` (which returns an index to tell you exactly where in the list the first instance of an element exists), and `list.count(element)` (which returns how many times an element occurs). Sets do not have such methods because they are unordered, so there is no index, and elements are only able to occur once.

---


---

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

> The `lambda` operator is used for writing short, anonymous, in-line functions.

---


---

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

REPLACE THIS TEXT WITH YOUR RESPONSE

---


Write a Markov text generator, [markov.py](python/markov.py). Your program should be called from the command line with two arguments: the name of a file containing text to read, and the number of words to generate. For example, if `chains.txt` contains the short story by Frigyes Karinthy, we could run:

```bash
./markov.py chains.txt 40
```

A possible output would be:

> show himself once more than the universe and what I often catch myself playing our well-connected game went on. Our friend was absolutely correct: nobody from the group needed this way. We never been as the Earth has the network of eternity.

There are design choices to make; feel free to experiment and shape the program as you see fit. Jeff Atwood's [Markov and You](http://blog.codinghorror.com/markov-and-you/) is a fun place to get started learning about what you're trying to make.
