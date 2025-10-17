# Q - You receive an API response code from your test script.
# Write an if-else block to check whether the response is successful (status code 200) or not.

# I/P response = 404 , O/P ❌ Failed API Request
# I/P response = 200 , O/P ✅ Passed API Request

Input_Response =int(input("Enter the API response code from your test script : ").strip())
print("Response Code : ", Input_Response)
if Input_Response ==200:
    print("✅ Passed API Request")
elif Input_Response == 404:
     print("❌ Failed API Request")
else:
    print("Response Code is Not Valid ")
