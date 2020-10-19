from availability import time
from appointment import appointment_fil
def greetings():
    print()
    print("Hi,/***welcome to Padmavathi Multispeciality hospital***/")
    print("This bot gives you a brief information about the doctors presence")
    print("Here is the list of our doctors:")
    print("***Cardiologist:Dr.Pavan ")
    print("   Neuroligist:Dr.Tarun")
    print("   General Pracitioner:Dr.Prasana")
    print("   Pediatrician:Dr.HariPriya")
    print("   Opthamologist:Dr.Keerthana")
    print("   Nepralogist:Dr.Kushal Kumar")
    print("   Oncologist:Dr.Patel")
    print("   Dentist:Dr.lakshmi***")
    print()
    to_do()
    return
def to_do():
    help=["1.appointment","2.time"]
    for i in help:
        print(i)
    print("NOTE:Type the number")
    print("Choice")
    choice=int(input())
    if(choice==1):
        appointment_fil(choice)
    elif(choice==2):
        time(choice)
    else:
        print("check your information")
    return
def bot():
    greetings()
    print()

bot()