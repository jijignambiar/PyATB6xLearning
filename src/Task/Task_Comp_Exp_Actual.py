# Write code to check if a test case passed or failed.
    # expected_title = "Dashboard"
    # actual_title = "Dashboard "
 #✅ Test Passed – Title matches

expected_title = input("Enter the expected title :")
actual_title = "Dashboard "
if expected_title == actual_title:
    print("Test Passed ✅")
else :
    print("Test Failed ❌")