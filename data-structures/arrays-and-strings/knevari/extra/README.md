# Chapter 1 Data Structures Implementations

In this first chapter it is said that a good exercise is to create our own implementations of StringBuilder,
HashTable and ArrayList, since I found it quite interesting to understand how all these data structures work underneath,
I'm gonna give it a try.

### ArrayList

I decided to begin with ArrayList, since it's the concept I'm most familiar with and I have implemented it before a few times in other programming languages.

It feels weird to create an ArrayList class using a programming language
that has a default ArrayList behavior for all it's lists and no manual memory management at all. But for the sake of experiment, I'm gonna do it anyway.

I expect my ArrayList behavior to be the following:

```
arr = ArrayList(20)

arr.append(2) # adds to the end of the arraylist
arr.prepend(10) # adds to the beginning of the arraylist

arr.has(value) # returns true if value is present, false otherwise
arr.is_empty() # returns true if list is empty, false otherwise

# I also want it to be iterable
for val in arr:
  pass

```

The ArrayList class took about 86 lines from which most of it was from internal helpers and some private functions used to make the public code more readable, the main and important features are all defined under line 57 which are **is_empty, has, append and prepend** function implementations.

#### The following outline was used for adding new values to the ArrayList

- We check whether the new value to be added has a valid type
- Increase the capacity only if there is no available space left on the internal array
- Increment the current size
- Place our new element in it's given position

In general those are all steps required to ensure our ArrayList maintains consistent types and size

```
self._validateValueType(value)
self._increaseInternalCapacityIfNotEnoughSpace()
self._incrementSize()
# add element to the beginning/end of the list
```

Since all operations necessary require constant time, our insertion operations takes O(1) time with the exception where we need to reallocate the array. Since we'd be copying every element to a new address, in that case it takes about O(n) steps to perform the insertion.

#### Verifying emptiness

This was very straightforward to write, since we just needed to check whether the ArrayList size was still zero in order to verify if it was empty or not. O(1) time complexity

#### Searching through the ArrayList

A basic linear search was performed in all elements of the ArrayList, excluding all empty spaces beyond it's size, if the element searched for was found, then we return True, otherwise just return False. Since every element needs to be checked in the worst case scenario, we assume it's O(n) time complexity.
