"""
Array Practice Problems

How to use this file:
1. Pick one problem at a time.
2. Implement the function where you see `pass`.
3. Run this file and compare your output to the expected output.

Tip: Start from Warm-Up, then Easy, then Medium.
"""


# -----------------------------
# Warm-Up
# -----------------------------
from pyparsing import nums


from pyparsing import nums


def sum_array(nums):
	"""
	Problem 1: Return the sum of all elements in nums.

	Example:
	sum_array([2, 4, 6]) -> 12
	"""
	sum=nums[0]
	for i in range(1,len(nums)):
		sum+=nums[i]
	return sum


def count_even(nums):
	"""
	Problem 2: Return how many even numbers are in nums.

	Example:
	count_even([1, 2, 3, 4, 5, 6]) -> 3
	"""
	even_nums=0
	for i in range(len(nums)):
		if nums[i]%2==0:
			even_nums+=1
	return even_nums
	


def max_value(nums):
	"""
	Problem 3: Return the largest value in nums.
	Assume nums has at least one element.

	Example:
	max_value([7, 1, 9, 3]) -> 9
	"""
	max=0
	for i in range(len(nums)):
		if nums[i]>=max:
			max=nums[i]
	return max 


# -----------------------------
# Easy
# -----------------------------
def reverse_array(nums):
	"""
	Problem 4: Return a new list that is nums reversed.
	Do not use nums.reverse() or slicing [::-1] on first attempt.

	Example:
	reverse_array([1, 2, 3]) -> [3, 2, 1]
	"""
	rev_nums=[]
	total_len=len(nums)-1
	
	for i in range(len(nums)):
		rev_nums.append(nums[total_len])
		total_len-=1
	return rev_nums
	
	


def contains_duplicate(nums):
	"""
	Problem 5: Return True if any value appears at least twice, else False.

	Example:
	contains_duplicate([4, 2, 7, 2]) -> True
	contains_duplicate([1, 2, 3, 4]) -> False
	"""
	#I could sort the array and then check if any elements are the same 
	new_array=sorted(nums)
	for i in range(len(new_array)-1):
		if new_array[i]==new_array[i+1]:
			return True
	return False


def move_zeros_to_end(nums):
	"""
	Problem 6: Return a new list where all zeros are moved to the end,
	while keeping the order of non-zero elements.

	Example:
	move_zeros_to_end([0, 1, 0, 3, 12]) -> [1, 3, 12, 0, 0]
	"""
	pass


def second_largest(nums):
	"""
	Problem 7: Return the second largest distinct number in nums.
	If it does not exist, return None.

	Example:
	second_largest([10, 20, 4, 20]) -> 10
	second_largest([5, 5, 5]) -> None
	"""
	pass


# -----------------------------
# Medium
# -----------------------------
def two_sum_indices(nums, target):
	"""
	Problem 8: Return indices [i, j] where nums[i] + nums[j] == target.
	Assume exactly one valid answer exists and i != j.

	Example:
	two_sum_indices([2, 7, 11, 15], 9) -> [0, 1]
	"""
	pass


def rotate_right(nums, k):
	"""
	Problem 9: Return nums rotated to the right by k steps.

	Example:
	rotate_right([1, 2, 3, 4, 5], 2) -> [4, 5, 1, 2, 3]
	"""
	pass


def prefix_sums(nums):
	"""
	Problem 10: Return an array where each index i contains
	the sum of nums[0] through nums[i].

	Example:
	prefix_sums([1, 2, 3, 4]) -> [1, 3, 6, 10]
	"""
	pass


def max_subarray_sum(nums):
	"""
	Problem 11: Return the maximum sum of any contiguous subarray.
	(Kadane's algorithm problem)

	Example:
	max_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]) -> 6
	"""
	pass


def product_except_self(nums):
	"""
	Problem 12: Return an array output where output[i] is the product of
	all numbers in nums except nums[i].
	Do not use division on first attempt.

	Example:
	product_except_self([1, 2, 3, 4]) -> [24, 12, 8, 6]
	"""
	pass


if __name__ == "__main__":
	print("=== Array Practice Problems: Sample Checks ===")

	# Warm-Up checks
	print("sum_array([2, 4, 6]) ->", sum_array([2, 4, 6]), "| expected: 12")
	print("count_even([1, 2, 3, 4, 5, 6]) ->", count_even([1, 2, 3, 4, 5, 6]), "| expected: 3")
	print("max_value([7, 1, 9, 3]) ->", max_value([7, 1, 9, 3]), "| expected: 9")

	# Easy checks
	print("reverse_array([1, 2, 3]) ->", reverse_array([1, 2, 3]), "| expected: [3, 2, 1]")
	print("contains_duplicate([4, 2, 7, 2]) ->", contains_duplicate([4, 2, 7, 2]), "| expected: True")
	print("move_zeros_to_end([0, 1, 0, 3, 12]) ->", move_zeros_to_end([0, 1, 0, 3, 12]), "| expected: [1, 3, 12, 0, 0]")
	print("second_largest([10, 20, 4, 20]) ->", second_largest([10, 20, 4, 20]), "| expected: 10")

	# Medium checks
	print("two_sum_indices([2, 7, 11, 15], 9) ->", two_sum_indices([2, 7, 11, 15], 9), "| expected: [0, 1]")
	print("rotate_right([1, 2, 3, 4, 5], 2) ->", rotate_right([1, 2, 3, 4, 5], 2), "| expected: [4, 5, 1, 2, 3]")
	print("prefix_sums([1, 2, 3, 4]) ->", prefix_sums([1, 2, 3, 4]), "| expected: [1, 3, 6, 10]")
	print("max_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]) ->", max_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]), "| expected: 6")
	print("product_except_self([1, 2, 3, 4]) ->", product_except_self([1, 2, 3, 4]), "| expected: [24, 12, 8, 6]")
