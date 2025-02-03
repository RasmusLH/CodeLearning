# Email slicer program

email = input("Enter your email: ").strip()

def slicer(email):
    username = email[0:email.index("@")]
    domain = email[email.index("@")+1:]
    print(f"Your username is {username} and your domain is {domain}")

slicer(email)