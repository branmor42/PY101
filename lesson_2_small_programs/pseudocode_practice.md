"[...] try a few practice rounds using pseudocode to guide your problem-solving logic. For example, write out pseudocode (both casual and formal) that does the following:"
----------------------------------------------------
"a function that returns the sum of two numbers"

casual pseudocode:
- Given two numbers.
    - Add the two numbers.
    - Return the sum.

formal pseudocode:
START

GET first integer from user
SET number1 = integer from user
GET second integer from user
SET number2 = integer from user
sum = number1 + number2
PRINT sum

END

"a function that takes a list of strings, and returns a string that is all those strings concatenated together"

casual pseudocode:
- Given a list of strings.
    - Initialize a placeholder variable to an empty string.
    - Iterate through the list one by one.
        - for each iteration, concatenate the current string element to the placeholder variable.
    - After iterating through the list, return the variable (that is now a string of concatenated strings).

formal pseudocode:
START

# Given a list of strings called "list_of_strings"

SET iterator = 0
SET c_string = ""

WHILE iterator < length of list_of_strings
    c_string = (c_string + value within list_of_strings at space "iterator")
    iterator = iterator + 1

PRINT c_string

END

"a function that takes a list of integers, and returns a new list with every other element from the original list, starting with the first element. For instance:

every_other([1,4,7,2,5]) # => [1,7,5]"

casual pseudocode:
- Given a list of integers.
    - Initialize a placeholder variable to an empty list.
    - Iterate through the list by even-indexed elements.
        - for each iteration, add the current value to the empty list.
    - After iterating through the list, return the newly created list.

formal pseudocode:
START

# Given a list of integers called "list1"

SET list2 = []
SET iterator = 0

WHILE iterator < length of list1
    list2 = (list2 + value within list1 at space "iterator")
    iterator = iterator + 2

PRINT list2

END

"a function that determines the index of the 3rd occurrence of a given character in a string. For instance, if the given character is 'x' and the string is 'axbxcdxex', the function should return 6 (the index of the 3rd 'x'). If the given character does not occur at least 3 times, return None."

casual pseudocode:
- Given a string.
    - Given a character in the string.
        - Save the character to a variable.
        - Initialize an "index" variable to 0.
        - Initialize a counter variable to 0.
        - Iterate through the string one by one.
            - if the current element is equal to the saved character
                - increase counter variable by one
                    - if the counter variable is equal to 3
                        - return the value of the current iteration (representing the index of the third occurrence of the saved character)

        - If the counter variable is less than 3
            - Return None

formal pseudocode:
START

# Given a string called "string1" and a character within that string called "char1"

SET counter = 0
SET iterator = 0

WHILE iterator < length of string1
    IF currentChar == char1
        counter = counter + 1
        IF counter == 3
            PRINT iterator
            END
    iterator = iterator + 1

IF counter < 3
    PRINT None

END

"a function that takes two lists of numbers and returns the result of merging the lists. The elements of the first list should become the elements at the even indexes of the returned list, while the elements of the second list should become the elements at the odd indexes. For instance:

merge([1, 2, 3], [4, 5, 6]) # => [1, 4, 2, 5, 3, 6]

You may assume that both list arguments have the same number of elements."

casual pseudocode:
- Given two lists of numbers.
    - Save the first list to a variable.
    - Save the second list to a variable.
    - Initialize a "new list" variable to an empty list.
    - Initialize a "counter1" variable to zero to track the indexing through the first list.
    Initialize a "counter2" variable to zero to track the indexing through the second list.
    - Initialize a variable to a range of numbers starting from 0 and ending at the integer equal to the total length of both of the given lists together minus 1.
    - Iterate through the range one by one.
        # each range number represents an index for the "new list" -- even numbers for each element of the first list and odd range numbers for each element of the second list}
        - if the current number is even
            - append the value at index "counter1" of the first list to the "new list"
            - increase counter1 by one
        - if the current number is odd
            - append the value at index "counter2" of the second list to the "new list"
            - increase counter2 by one
    - After iterating through the range, return the new list.

formal pseudocode:
START

# Given two lists--"list1" for the first list and "list2" for the second list

SET new_list = []
SET my_range = (0, length of both lists together minus 1)
SET iterator = 0
SET counter1 = 0
SET counter2 = 0

WHILE iterator < length of range
    IF iterator % 2 == 0
        append list1[counter1] to new_list
        # assign value at each index of each list to a number that represents the index of the new list.
        counter1 = counter1 + 1
    ELSE
        append list2[counter2] to new_list
        counter2 = counter2 + 1
    iterator = iterator + 1

PRINT new_list

END