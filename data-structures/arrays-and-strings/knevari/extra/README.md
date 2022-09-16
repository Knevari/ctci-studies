# Chapter 1 Data Structures Implementations

In the first chapter it is said that it's a good exercise to create our own implementations of **StringBuilder,
HashTable and ArrayList**, since I found it quite interesting to understand how all these data structures work underneath,
I'm gonna give it a try.

### ArrayList

I decided to begin with **ArrayList**, since it's the concept I'm most familiar with and I have implemented it before a few times in other programming languages.

It feels weird to create an ArrayList class using a programming language
that has a default ArrayList behavior for all it's lists and no manual memory management at all. But for the sake of experiment, I'm gonna do it anyway.

I expect my **ArrayList** behavior to be the following:

```
arr = ArrayList(int, 20)

arr.append(2) # adds to the end of the arraylist
arr.prepend(10) # adds to the beginning of the arraylist

arr.has(value) # returns True if value is present, False otherwise
arr.is_empty() # returns True if list is empty, False otherwise

# I also want it to be iterable
for val in arr:
  pass

```

#### Post-implementation

The **ArrayList** class took about 86 lines from which most of it was from internal helpers and some private functions used to make the public code more readable, the main and important features are all defined under line 57 which are **is_empty, has, append and prepend** function implementations.

#### The following outline was used for adding new values to the ArrayList

- We check whether the new value to be added has a valid type
- Increase the capacity only if there is no available space left on the internal **Array**
- Increment the current size
- Place our new element in it's given position

In general those are all steps required to ensure our **ArrayList** maintains consistent types and size

```
self._validateValueType(value)
self._increaseInternalCapacityIfNotEnoughSpace()
self._incrementSize()
# add element to the beginning/end of the list
```

Since all operations necessary require constant time, our insertion operations takes O(1) time with the exception where we need to reallocate the array. Since we'd be copying every element to a new address, in that case it takes about O(n) steps to perform the insertion.

#### Verifying emptiness

This was very straightforward to write, since we just needed to check whether the **ArrayList** size was still zero in order to verify if it was empty or not. O(1) time complexity

#### Searching through the ArrayList

A basic linear search was performed in all elements of the **ArrayList**, excluding all empty spaces beyond it's size, if the element searched for was found, then we return True, otherwise just return False. Since every element needs to be checked in the worst case scenario, we assume it's O(n) time complexity.

---

### HashTable

**Hash Table** is going to be my second choice, since it's the holy grail of all data structures and basically every single language implements it in some way, I imagine it should be done in the best way possible. The book exemplifies a **Hash Table** built from a single **Array** with multiple **Linked Lists** being used as buckets. I wanted to build something similar, but color it a bit more with some new ideas.

The main difference between CTCI **Hash Table** example and my construction is that mine is going to use a **Priority Queue** instead of a **Linked List** as a bucket, I want it to be able to reposition all collisions in a manner that puts elements with higher frequency of use in front of less important ones, so it minimizes the access time.

One of the biggest problems when building a dynamically sized hash table is the need to recompute all indexes on the event of the access time growing too big in order to maintain the amortized O(1) access time. Thinking about a way to reduce the number of times I need to reallocate the lookup array, I came up with two ideas. The first one keeps track of the general number of elements currently saved in the lookup array within all buckets, and reallocates if it grows past a certain threshold. The second one takes into account only the buckets which are most active and tries to decide based on that whether we should increase the size to move some items to other buckets.

I expect my **Hash Table** behavior to be the following

```
table = HashTable() # I want to abstract away details like size, resizing factor, collisions, etc...

table.set(key, value)
table.get(key) # returns value if present, throws an error otherwise

table.has(key) # returns True if value is present, False otherwise

table.delete(key) # deletes a given key from the table
```

#### Post-implementation

It was quite a challenge to develop this data structure using the approach described above. I faced many problems when it came to implementation, and I had to go deeper than what CTCI was telling me in order to complete this exercise.

From a more holistic view of my progress with this specific data structure, I could see that the main challenge was not to implement the **Hash Table** itself, since it's interface it's quite straightforward and easy to comprehend, but in fact, the management of buckets. Getting to understand how I could effectively use a **Priority Queue** to correctly balance all elements within my **Hash Table** took me quite a bit of time, since I had to think about which **Priority Queue** implementation was the best to use and how to keep track of each item priority.

One of the reasons why I had to research a bit further, was to understand how to reduce the number of collisions in the Hash Table. My original criterion for defining whether or not it was necessary to reallocate all other buckets within the array was based solely on the number of elements compared against a fixed value given by me as the programmer, which isn't really scalable at all. So instead, I'm now using a ratio between the number of elements and the number of buckets as the metric to decide whether the internal array is getting full and if so, we should replace it for something that can accomodate more elements without compromising the access time. In general, the **Hash Table** is going to wait until it is at least 60% full in order to reallocate all the elements to a new array containing more buckets and better spread elements.

#### The following outline was used for inserting new values into the HashTable

- We check if the key is present in the hash table
- If it is, we update the key given bucket with the new value
- If it is not, we insert the new value within the key given bucket and increment the hash table size
- We reallocate the internal array if the load factor exceeds 60%

Every single one of those steps have O(1) time complexity, except when the load factor is bigger than 60%, in this case we should expect the hash table to be reallocated thus taking O(nm) time complexity where **m** is the number of available spots within each bucket, **m** is guaranteed to be less than **n** since for n to be equal m there would need to be n elements inside a single bucket, which is impossible since the heap is reallocated when it is 60% full.

#### Finding an element by it's key

We simply calculate the key's hash and get it's bucket in O(1) time, then we look for the element within the bucket in amortized constant time. The same goes for veryfying whether a given key exists in the hash table.

#### Deleting an element by it's key

We repeat the same process of calculating the key's hash and finding it's bucket, then we remove it completely from the bucket, again O(1) time complexity
