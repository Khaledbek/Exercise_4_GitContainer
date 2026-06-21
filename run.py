from single_element import find_single


if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 3, 1, 2]
    result = find_single(numbers)

    print(f"Input: {numbers}")
    print(f"Single element: {result}")