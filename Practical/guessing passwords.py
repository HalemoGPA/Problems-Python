import pyautogui
import random
chars="1234567890"
chars1="5879460132"
chars2="3405126978"
chars1_list=list(chars1)
chars_list=list(chars)
chars2_list=list(chars2)
password=pyautogui.password("enter a password: ")
guess_password=""
guess_password1=""
guess_password2=""
guess_password3=''
guess_password4=''
guess_password5=''
guess_password6=''
print("wait for 5 minute until it find your password")
while (guess_password !=password) :
    guess_password=random.choices(chars_list, k=len(password))
    guess_password1=random.choices(chars_list,k=len(password))
    guess_password2=random.choices(chars_list,k=len(password))
    guess_password3=random.choices(chars1_list,k=len(password))
    guess_password4=random.choices(chars1_list,k=len(password))
    guess_password5=random.choices(chars2_list, k=len(password))
    guess_password6=random.choices(chars2_list,k=len(password))
    if (guess_password==list(password)) :
        print("your password is :"+"".join(guess_password))
        break
    elif guess_password1==list(password):
        print("your password is1 :"+"".join(guess_password1))
        break
    elif guess_password2==list(password):
        print("your password is2 :"+''.join(guess_password2))
        break
    elif guess_password3==list(password):
        print("your password is3 :"+''.join(guess_password3))
        break
    elif guess_password4==list(password):
        print("your password is4 : "+''.join(guess_password4))
        break
    elif guess_password5==list(password):
        print('your password is5 : '+''.join(guess_password5))
        break
    elif guess_password6==list(password):
        print("your password is6 : ",'.join(guess_password6)')
        break
