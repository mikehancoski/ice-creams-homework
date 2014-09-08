instructions =  """
Write a program that will input a number, add 5 to the number, multiple it

by 3.1 and then divide the the result by 10. The program should printout the 

number that was input and the result. Put words explaining what you are 

printing out.
"""
number = float(input("Enter a number..."))

numbercalc = (number + 5) * 3.1 / 10

print("The nubmer entered was:",number )
print("The number plus 5, times 3.1 and divied bye 10 is:" , numbercalc)
