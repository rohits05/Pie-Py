# Performing various operations in python
import math
# ----- Arithmetic operator
print(19 + 14, 19-14, 19*14, 19/14, 19 % 14)

# Lets know the differnece b/w / & //
# / -> gives floating no. as output whereas // -> gives an integer no.
print(264 / 45, 264 // 45)

# Exponent using **
print(19 ** 5)


# ----- Assignment operator
ylv = 24
ylv = ylv + 19  # or ylv += 19 -> augmented/enhanced assignment operator
# ylv -= 1
# ylv *= 3
# ylv /= 5
# ylv %= 7
print(ylv)


# ----- Precedence
# parenthesis
# expo'
# mul or div
# add or substract
lays = 10 + 25 * 9 ** 2
bingo = (5 + 9) % 14 ** 3
print(lays, '\n', bingo)


# ----- Math function
gems = 14.47
burger = -95
print(round(gems))  # rounding off the no.
print(abs(burger))  # returns +ve represent' of val

print(math.ceil(4.2), math.floor(4.6))
