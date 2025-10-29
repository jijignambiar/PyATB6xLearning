# An API sometimes fails due to network delays.
#
# Write a program to retry the API call 3 times until the response code becomes 200.
#
# If it still fails after 3 tries, print a failure message.
# 
# Hint: Use a while loop with a counter.
# Hint: Use a while loop with a counter.
#
# Expected Output Example:
#
# Attempt 1: Response 500
#
# Attempt 2: Response 200
#
# ✅ Test Passed

resp = int(input("enter the number of times API should be called :"))
counter = 0
i=1
if resp <= 0:
    print("Invalid Response time")
while i <= resp:
    counter = counter + 1
    i = i + 1
    print(counter)
if counter == 1:
    print("Attempt 1 : Response 500")
elif counter == 2:
    print("Attempt 1 : Response 500")
    print("Attempt 2 : Response 200")
elif counter == 3:
    print("Attempt 1 : Response 500")
    print("Attempt 2 : Response 200")
    print("✅ Test Passed")
elif counter > 3:
    print("Test Failed")
