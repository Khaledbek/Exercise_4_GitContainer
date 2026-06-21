def find_single(numbers):
    """
    Return the element that appears exactly once.

    All other elements must appear exactly twice.
    """

    if not numbers:
        raise ValueError("Input array must not be empty")

    if len(numbers) % 2 == 0:
        raise ValueError("Input array must have odd length")

    result = 0

    for number in numbers:
        result ^= number

    return result