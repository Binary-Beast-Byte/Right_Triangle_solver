# You are responsible for writing a program that will calculate the hypotenuse and area of a right
# triangle given its two bases

import math
print("Welcome to the Right Triangle solver app !")

#Getting leg1 and leg2 from a user as a input
leg1 = float(input("What is the leg1 of your triangle: "))
leg2 = float(input("what is the leg2 of your triangle: "))

#calculating the hypotenuse
hypotenuse = math.sqrt((leg1**2) + (leg2**2))

#calculating the area
area = leg1*leg2*0.5

#rounding hypotenuse and the area into 3 decimal places
hyp_round = round(hypotenuse,3)
area_round = round(area,3)

print("\n")
print("\tThe hypotenuse of your triangele is: ",hyp_round)
print("\tThe area of your  triangle is : ", area_round)


