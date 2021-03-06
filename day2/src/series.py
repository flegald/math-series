# -*- coding: utf-8 -*-


def sum_series(i, a=0, b=1):
    """returns the n-th value of the requested sequence fibonacci or lucas"""
    if i == 1:
        return a
    if i == 2:
        return b
    if i == 3:
        return a + b
    if i > 3:
        prevVals = [a, b]
        for idx in range(i - 2):
            total = prevVals[0] + prevVals[1]
            prevVals[0] = prevVals[1]
            prevVals[1] = total
        return total


# return the 'n' value of the fibonacci sequence
# 0, 1, 1, 2, 3, 5, 8, 13, 21 ....
def fibonacci(n):
    return sum_series(n, 0, 1)

# return the 'n' value of the lucas sequence
# 2, 1, 3, 4, 7, 11, 18, 29 ....
def lucas(n):
    return sum_series(n, 2, 1)

if __name__ == "__main__":
    print "This module defines functions that implement mathematical series."

    print "fibonacci(n): Returns the nth value in the fibonacci series"

    print "fibonacci(2) returns " + str(fibonacci(2))

    print"lucas(n): Returns the nth value in the lucas sum_series"

    print "lucas(2) returns " + str(lucas(2))

    print "sum_series(n, a, b): Returns the nth value of a custom series with a and b being starting points(0,1) are default"
 
    print "sum_series(2,1,4) returns " + str(sum_series(2,1,4))
