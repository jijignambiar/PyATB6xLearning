# Check if the user can log in based on correct username and password.
#
# I/p
#
# username = "admin"
# password = "1234"
# O/p
# ✅ Login Successful

username  = input("Enter the username :")
password = input("Enter the password :")

username_act = "admin"
password_act = "1234"

if username == username_act and password == password_act:
    print("Login Successful ✅")
else:
    print("❌ Invalid Credentials")