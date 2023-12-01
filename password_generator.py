import string
import random
char=list(string.ascii_letters + string.digits + '!@#$%^&*')
random.shuffle(char)
random.shuffle(char)

def generate_password():
    password_length=int(input("Enter The Length Of your Password: "))
    data=random.sample(char,password_length)
    password ="".join(data)
    print(password)

print("cooking a solid password like dravid's defence....")
generate_password()
quit()

