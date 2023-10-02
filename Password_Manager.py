master_pass = input("What is your master password?")

def view():
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
             data = line.rstrip()
             user, passw = data.split("|")
             print("User: ", user, "| Password:", passw)

def add():
    username = input("Account Username: ")
    master_pass = input("Password: ")
    try:
        with open('passwords.txt', 'a') as f:
            f.write(username + "|" + master_pass + "\n")
        print("Succesfully added to system")
    except Exception as e:
        print("An error has occured")
while True:
    mode = input("Would you like to add a new password, view existing ones, or quit (view, add, quit)")
    if mode == "quit":
        print("Stay safe!")
        break
    elif mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invavid mode")