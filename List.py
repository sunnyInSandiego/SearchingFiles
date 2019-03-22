"""
Author: Glenn Marcus
Date: March 2, 2019
Purpose: Create a list using random generator where the list[index]
greater than or equal to the predecessor and less than twice list[index],
print list, sum, median, average
"""

import random

lst = [2]
len_lst = random.randint(5, 8)
for index in range(len_lst - 1):
	lst.append(random.randint(lst[index], 2 * lst[index] - 1))
print("List: " + " ".join(str(x) for x in lst) + " - " + "Sum: " + str(sum(lst)) + " " + "- " + "Median: " +
		str((lst[(len(lst) - 1)//2] + lst[(len(lst) + 1)//2])/2 if len(lst) % 2 == 0 else lst[(len(lst) - 1)//2]) + " - "
	  + "Avg: " + str((sum(lst)) / len(lst)))


