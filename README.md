# SimpleKMP
Simple KMP Algorithm Implementation

# What Is KMP?
KMP is an algorithm for finding a pattern in a string. Its time complexity is O(n + m) that n is length of pattern and m is length of string.

# How To Use SimpleKMP Class?
Simply create an object of class SimpleKMP like below:
obj = SimpleKMP([string], [pattern])
Then you can use get_temporary_array function and find like below:
get_temporary_array = obj.get_temporary_array()
found_index = obj.find()
