print("""
**********

Welcome...

**********
""")

username = "goktugsina"
password = "12345"
enterance_count = 3

while True:
    sys_username = input("Username:")
    sys_password = input("Password:")
    if (sys_username == username and sys_password != password):
        print("Password Incorrect. Please Try Again.")
        enterance_count -= 1
    elif (sys_username != username and sys_password != password):
        print("Password and Username Incorrect. Please Try Again.")
        enterance_count -= 1
    elif (sys_username != username and sys_password == password):
        print("Username Incorrect. Please Try Again.")
        enterance_count -= 1
    else:
        print("Succesful.")
        break
    if enterance_count == 0:
        break