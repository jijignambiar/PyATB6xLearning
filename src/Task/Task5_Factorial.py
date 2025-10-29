# Given a Number a number you need to calculate the factorial of that number

# n = 5
# Fact = 5×4×3*2*1 = 120
# Fact = 0 → 1,

#n=5
num = int(input("Enter a number :"))
fact =1
if num < 0:
    print("Fact is not defined!")
elif num == 0:
    print("The Factorial of",num,"is : ",fact)
else:
    while num > 0:
        fact = fact * num
        num =num-1
    print("The Factorial of",num,"is : ",fact)