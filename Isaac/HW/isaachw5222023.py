# Sort Homework






############ ALL THIS TEST CODE SHOULD BE AFTER YOUR HOMEWORK SORT CODE ####################

def test_sort_numbers():
    numbers = [9, 4, 2, 7, 5]
    expected_output = [2, 4, 5, 7, 9]
    sorted_numbers = sort_numbers(numbers)
    assert sorted_numbers == expected_output, f"Expected: {expected_output}, Got: {sorted_numbers}"
    print("Test passed!")

# Helper function to sort the numbers
def sort_numbers(numbers):
    return homework_sort(numbers)

# Run the test
# WHEN YOU ARE READY TO TEST UNCOMMENT THIS!
# test_sort_numbers()