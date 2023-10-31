import random
import string

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

if __name__ == "__main__":
    password_length = 12  # You can change the length as per your preference
    generated_password = generate_password(password_length)
    print("Random_Generated_Strong_Password:", generated_password) 
    print("(No one can broke the password!)")
    print(  "."   )
    print(   "."  )
    print(   "."  )
    
    print("_________THANKS_________\nYou can contact with us:\nCall:+8801332340710\nEmail:manis.programmer@gmail.com")
   

