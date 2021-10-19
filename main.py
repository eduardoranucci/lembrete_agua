from time import sleep
from win10toast import ToastNotifier

toaster = ToastNotifier()


while True:
    
    toaster.show_toast(
    "Água",
    "Bebe água aí nmrl",
    threaded = True,
    icon_path = r".\water_frask.ico",
    duration = 4
    )

    sleep(300)
