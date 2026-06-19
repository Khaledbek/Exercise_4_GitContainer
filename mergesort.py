import matplotlib.pyplot as plt


# Refactoring:
# Original name: ASSIGNMENT
# Renamed to follow Python naming conventions (snake_case).
def copy_value(target_list, target_index, source_list, source_index):
    """Copy a value from the source list to the target list."""
    target_list[target_index] = source_list[source_index]


# Refactoring:
# Original name: mergeSort
# Renamed to merge_sort according to PEP 8.
def merge_sort(values):
    """
    Sort a list in-place using the Merge Sort algorithm.
    """

    # Refactoring:
    # Original condition:
    #
    # if (
    #     len(list_to_sort_by_merge) > 1
    #     and not len(list_to_sort_by_merge) < 1
    #     and len(list_to_sort_by_merge) != 0
    # ):
    #
    # Simplified to a clear base case.
    if len(values) <= 1:
        return

    # Refactoring:
    # Original variable: mid
    midpoint = len(values) // 2

    # Refactoring:
    # Original variables: left, right
    left_half = values[:midpoint]
    right_half = values[midpoint:]

    merge_sort(left_half)
    merge_sort(right_half)

    # Refactoring:
    # Original variables: l, r, i
    left_index = 0
    right_index = 0
    merged_index = 0

    # Merge the sorted halves.
    while left_index < len(left_half) and right_index < len(right_half):
        if left_half[left_index] <= right_half[right_index]:
            copy_value(
                values,
                merged_index,
                left_half,
                left_index,
            )
            left_index += 1
        else:
            copy_value(
                values,
                merged_index,
                right_half,
                right_index,
            )
            right_index += 1

        merged_index += 1

    # Copy remaining values from the left half.
    while left_index < len(left_half):
        values[merged_index] = left_half[left_index]
        left_index += 1
        merged_index += 1

    # Copy remaining values from the right half.
    while right_index < len(right_half):
        values[merged_index] = right_half[right_index]
        right_index += 1
        merged_index += 1


if __name__ == "__main__":
    # Refactoring:
    # Original variable: my_list
    numbers = [54, 26, 93, 17, 77, 31, 44, 55, 20]

    x_values = range(len(numbers))

    plt.plot(x_values, numbers, label="Unsorted List")
    plt.title("List Before Merge Sort")
    plt.xlabel("Index")
    plt.ylabel("Value")
    plt.legend()
    plt.grid(True)
    plt.show()

    merge_sort(numbers)

    plt.plot(x_values, numbers, label="Sorted List")
    plt.title("List After Merge Sort")
    plt.xlabel("Index")
    plt.ylabel("Value")
    plt.legend()
    plt.grid(True)
    plt.show()

