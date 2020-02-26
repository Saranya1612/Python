from win10toast import ToastNotifier
import random
import time
def toast():
    Quotes=["Yooooooo!!!! Take a Water Break","Dont forget to drink water and get some sun, you are basically a houseplant with more complicated emotions","Hello Friend!!! You should drink more water","Hows your water drinking going!!!","Keep Calm and Drink Water","Its Okay to Drink more!!!!"]
    toaster=ToastNotifier()
    toaster.show_toast("Health Alert",random.choice(Quotes),duration=10)
while True:
    print("Lets Toast")
    toast()
    time.sleep(300)