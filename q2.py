# Question 2
# Level 1
#
# Question:
# Write a program which can compute the factorial of a given numbers.
# The results should be printed in a comma-separated sequence on a single line.
# Suppose the following input is supplied to the program:
# 8
# Then, the output should be:
# 40320
from math import factorial

number_list = list(map(int, input().split()))


def fact_def():
    if number_list == 0:
        return 1

    for i in number_list:
        print(i * factorial(i - 1), end=",\n")


fact_def()
