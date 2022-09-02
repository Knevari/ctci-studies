# Arrays and Strings - Notes

This first chapter was quite a nice introduction to easy/medium algorithms. Most of this chapter's problems
were very easy to solve, but I still feel like I was able to learn a lot by being able to refresh some of these old concepts
in my mind. It feels like most problems in this chapter were focused on showing us the idea of using multiple pointers
to move things around arrays, strings and matrices. It has also shown that hash tables are often very useful
for keeping count of things and positions we can reference later in little to no overhead because of constant time access.

# About in-place algorithms

According to the book Clean Code, functions should have one and only one reason to exist, they should perform one single task
and be very good at it. Even though I'm not following every single guideline of the book in this repo, I find it more intuitive
to have functions that modify the input to return the given input anyway, even if passed by reference. It serves the purpose of a function
monoid that operates on a single value, returning it's value reinforces it's meaning for the reader, the meaning of a function that operates on that value
and returns it's modification.

## Analyzing Average Time Complexity

### Arrays

- Access: O(1)
- Search: O(N)
- Insertion: O(N)
- Deletion: O(N)

### Hash Tables

- Access: O(1)
- Search: O(1)
- Insertion: O(1)
- Deletion: O(1)
