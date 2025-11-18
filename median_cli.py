
"""
Median Finder CLI

Implements the sortAndFindMedian(numbers) pseudocode using a hand-written
insertion sort and a simple command-line interface for entering test data.
"""

from typing import List


def insertion_sort(numbers: List[float]) -> None:
    """
    In-place insertion sort (ascending).

    Time complexity: O(n^2) in the worst case.
    Space complexity: O(1) additional space.
    """
    for i in range(1, len(numbers)):
        key = numbers[i]
        j = i - 1

        # Move elements of numbers[0..i-1], that are greater than key,
        # one position ahead of their current position.
        while j >= 0 and numbers[j] > key:
            numbers[j + 1] = numbers[j]
            j -= 1

        numbers[j + 1] = key


def sort(numbers: List[float]) -> None:
    """
    Sort the list of numbers in ascending order using a sorting algorithm
    (in this case, insertion sort). This function modifies the list in-place.
    """
    insertion_sort(numbers)


def sort_and_find_median(numbers: List[float]) -> float:
    """
    Sort the numbers (ascending) and return their median, following the
    provided pseudocode:

        CALL sort(numbers)
        DEFINE n AS length of numbers
        IF n MOD 2 = 0
            RETURN (numbers[n/2 - 1] + numbers[n/2]) / 2
        ELSE
            RETURN numbers[n/2]
        ENDIF
    """
    if not numbers:
        raise ValueError("Cannot compute median of an empty list.")

    sort(numbers)
    n = len(numbers)
    mid = n // 2

    if n % 2 == 0:
        # even length: average of the two middle elements
        return (numbers[mid - 1] + numbers[mid]) / 2.0
    else:
        # odd length: middle element
        return numbers[mid]


def parse_numbers(line: str) -> List[float]:
    """
    Parse a whitespace-separated string of numbers into a list of floats.
    """
    tokens = line.strip().split()
    if not tokens:
        return []

    try:
        return [float(tok) for tok in tokens]
    except ValueError as e:
        raise ValueError(
            "Invalid input. Please enter numbers separated by spaces, "
            "e.g. '1 2 3.5 4'."
        ) from e


def run_interactive() -> None:
    """
    Simple user interface:
    - Prompts the user to enter numbers separated by spaces.
    - If the user presses Enter with no input, runs a few predefined test cases.
    """
    print("Median Finder CLI")
    print("-----------------")
    print("Enter a list of numbers separated by spaces to compute its median.")
    print("Example: 1 3 5 7 9")
    print("Press Enter without typing anything to run predefined test cases.\n")

    line = input("Numbers: ")

    if line.strip():
        # User-provided numbers
        try:
            numbers = parse_numbers(line)
        except ValueError as e:
            print(f"Error: {e}")
            return

        try:
            median = sort_and_find_median(numbers)
        except ValueError as e:
            print(f"Error: {e}")
            return

        print(f"Sorted numbers: {numbers}")
        print(f"Median: {median}")
    else:
        # Predefined test cases
        test_cases = [
            [1, 3, 5],
            [4, 2, 1, 3],
            [10, 10, 10, 10, 10],
            [7.5, 2.3, 4.1, 9.8],
        ]

        for idx, case in enumerate(test_cases, start=1):
            nums = list(case)  # copy so we can sort in-place
            median = sort_and_find_median(nums)
            print(f"Test case {idx}: original={case}, sorted={nums}, median={median}")


def main() -> None:
    run_interactive()


if __name__ == "__main__":
    main()
