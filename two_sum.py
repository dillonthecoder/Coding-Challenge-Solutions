"""

Two Sum:

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.


Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].


Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]


Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]

Constraints:

20 <= nums.length <= 104
-109 <= nums[i] <= 19
-109 <= target <= 109
Only one valid answer exists.

"""

# Solution 1: Brute Force

class Solution(object):

    def twoSum(self, nums, target):

        # This gives us the length of the list "nums"
        length_of_nums = len(nums)

        # This loop iterates over each index of the list "nums"
        for current_index in range(length_of_nums):
            
            # We start from current_index + 1 to ensure we look at every index after the current one.
            # This helps in comparing the number at current_index with every subsequent number in the list "nums".
            for next_index in range(current_index + 1, length_of_nums):

                # Check if the sum of the number at current_index and the number at other_index equals "target"
                if nums[current_index] + nums[next_index] == target:

                    # Return the indices of the two numbers that add up to "target"
                    return [current_index, next_index]


# Solution 2: Brute Forced, Slightly Optimized

class Solution:

    def two_sum(self, nums, target):

        # Here, we improve our code by eliminating the need to create the length_of_nums variable
        # Instead of creating a variable, we simply call for the length of the list "nums" directly in the for looop
        for current_index in range(len(nums)):
            
            # Again, we call for len(nums) directly in the loop rather than creating the variable length_of_nums
            for next_index in range(current_index + 1, len(nums)):

                if nums[current_index] + nums[next_index] == target:

                    return [current_index, next_index]
                

# Solution 3: Optimized for Speed (but not memory)

class Solution:

    def two_sum(self, nums, target):

        # Create an empty dictionary named "seen". This will store numbers we've encountered as keys, 
        # and their indices in the "nums" list as corresponding values.
        seen = {}

        # Start looping through each number "num" in the list "nums". 
        # The "enumerate()" function also gives us each number's index in the list, stored in "index".
        for index, num in enumerate(nums):
            
            # For the current number "num", calculate its complement with respect to the target.
            # In other words, determine what other number you'd need to add to "num" to get the "target".
            complement = target - num
            
            # Check if this "complement" number is already in our "seen" dictionary. 
            # If it is, it means we've found two numbers that add up to "target".
            if complement in seen:
                
                # Return a list containing two indices:
                # 1) The index of the "complement" number (which we get from the "seen" dictionary)
                # 2) The index of the current number "num"
                return [seen[complement], index]
            
            # If the complement wasn't found in the "seen" dictionary, 
            # add the current number "num" to the dictionary with its index as the value.
            # This way, if we encounter a number later in the list that pairs with "num" to reach the target, 
            # we'll know where "num" was in the list.
            seen[num] = index


"""
Notes on 'Enumerate':

he enumerate() function is one of Python's built-in functions and is particularly useful 
when you want to iterate over a list (or other iterable) and want to have access to both the index and 
the value of each item in the list.

Here's the basic structure of how enumerate() works -

for index, value in enumerate(iterable):
    # do something with index and value


A Simple Example -

fruits = ['apple', 'banana', 'cherry']

for idx, fruit in enumerate(fruits):
    print(idx, fruit)

Output = 

0 apple
1 banana
2 cherry

As you can see, enumerate() gives you both the index (idx) and the value (fruit) for each item in the list.
"""

"""
Explination of Optimized Version:

Both versions solve the same problem, but they do so using different strategies and with different efficiencies.


1. Brute Force Version -

This version uses a nested loop, which means it 
First, it takes each number in the list (using the outer loop).
Second, for each of those numbers, it checks it against every other number that follows it in the list (using
the inner loop).

This approach is straightforward and easy to understand. It systematically checks each pair of numbers in
the list to see if they add up to the target.

Efficency - This method has the time complexity of O(n^2), where n is the number of items in the list.
This is because, in the worst case, for every number in the list, you are potentially looking at almost
every other number.


2. Optimzed "enumerate()" Version -

This version uses a single loop and a dictionary.

First, it loops throught the numbers in the list just once
Next, for each number, it calculates what the "complement" would be. (The complement is the number that
you would need to add to the current number to get the target.)
Finally, it checks if this complement is in the dictionary (if we've seen this number before while looping).
If the complement is in the dictionary, it means the current number and the complement add up to the target.
If not, it adds the current number and its index to the dictionary.

The dictionary, in this case, serves as a kind of 'memory' for the function. It remembers numbers
it has seen before and where it saw them.

Efficiency - This method has a time complexity of O(n), where n is the number of items in the list.
Even though dictionary operations (like checking for a key or adding a key) can have variable times in some
scenarios, they average out to constant time, O(1), for this use case. So the overall time complexity is
linear.


Comparing the two - 

The first version is easier for many beginners to understand because it directly represents the problem's
requirements.

However, the optimized 'enumerate()' version is more efficient, especially for large lists, because it avoids
the need for a nested loop.

While the 'enumerate()' version is faster, it does use more memory because of the dictionary. So the brute
force version uses minimal memory.

In practice, which version you should use would depend on the specific requirments and constraints of the 
situation. If the input list can be very long, the efficient version might be preferable. If memory use is 
a concern, and the list won't be too long, the brute force verion might be okay.
"""