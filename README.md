# Sort and Find Median – CLI Application

This repository contains a small command-line program that implements the provided **`sortAndFindMedian(numbers)`** pseudocode. It demonstrates:

- Implementing a **custom sorting algorithm** (insertion sort).
- Translating pseudocode into working code.
- Calculating the **median** of an array of numbers.
- Providing a simple user interface for inputting test data.

---

## Objective

> Below is a pseudocode for a more complex algorithm. Your task is to convert it into a working program in any programming language of your choice. The program should perform the exact function described in the pseudocode.

Pseudocode:

```text
FUNCTION sortAndFindMedian(numbers)
    CALL sort(numbers)
    DEFINE n AS length of numbers
    IF n MOD 2 = 0
        RETURN (numbers[n/2 - 1] + numbers[n/2]) / 2
    ELSE
        RETURN numbers[n/2]
    ENDIF
ENDFUNCTION

FUNCTION sort(numbers)
    // Implement a sorting algorithm (e.g., bubble sort, selection sort, etc.)
    // Sort the 'numbers' array in ascending order
ENDFUNCTION
