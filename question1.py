#Write a Python program that prints numbers from 1 to 10.
• If the number is 5, skip printing it using the continue statement.
• If the number is 8, stop the loop using the break statement.


#CODE

for i in range(1, 11):
    if i == 5:
        continue   # skip 5
    if i == 8:
        break      # stop loop at 8
    print(i)
