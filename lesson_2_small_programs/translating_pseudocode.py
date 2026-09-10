def find_greatest(numbers):
    iterator = 0
    saved_number = numbers[iterator]

    while iterator < len(numbers):
        current_number = numbers[iterator]
        if current_number > saved_number:
            saved_number = current_number

        iterator += 1

    return saved_number

# print(find_greatest([2, 8, 1, 0, 4, 6, 9, 3, 5, 7]))
