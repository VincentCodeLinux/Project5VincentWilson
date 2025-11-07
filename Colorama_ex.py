import colorama
from colorama import Fore, Back, Style
colorama.init()

print(Fore.RED + "This text is red")
print(Fore.GREEN + "This text is green")

print ("hello world")

print(Style.RESET_ALL)

print("back to normal")

print(Back.CYAN + "This text is highlighted cyan")
print("still will be highlighted")
print(Back.RED + Style.BRIGHT + "This text is highlighted red")

print(Style.RESET_ALL)
print(Style.BRIGHT + "This will be bold")
print(Style.RESET_ALL)