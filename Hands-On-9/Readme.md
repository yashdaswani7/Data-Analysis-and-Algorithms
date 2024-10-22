### Name: Yash Daswani  
### Student ID: `1002257766`

# Hash Table Implementation

## Description

This is a Python implementation of a **Hash Table** that uses:
- **Multiplication and Division Methods** for the hash function.
- **Chaining with Doubly Linked Lists** for collision resolution.
- **Dynamic resizing** (growth and shrink) based on load factors.
- A generic design that allows any hash function to be easily plugged in.

The implementation is entirely done using **C-style arrays** (no Python lists or libraries like `collections`). The hash table dynamically grows when the load factor exceeds 75% and shrinks when it falls below 25%.

## Features

1. **Hash Function**: Combines multiplication and division methods using the constant `A = 0.618033` (related to the golden ratio).
2. **Collision Resolution**: Implemented via chaining using **doubly linked lists**.
3. **Dynamic Resizing**: 
   - When the table becomes full (load factor > 75%), it **doubles** in size.
   - When the table becomes sparsely populated (load factor < 25%), it **halves** in size.
4. **Basic Operations**:
   - **Insert**: Insert a key-value pair into the hash table.
   - **Get**: Retrieve the value associated with a key.
   - **Remove**: Remove a key-value pair.
   - **Print Table**: Print the entire hash table showing the contents of each bucket.