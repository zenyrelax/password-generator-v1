import random, string
from colorama import Fore, Style, init

print(Fore.RED  + "               ╔═╗╔═╗╔╗╔╦ ╦╦═╗╔═╗╦  ╔═╗═╗ ╦" + Style.RESET_ALL)
print(Fore.RED  + "               ╔═╝║╣ ║║║╚╦╝╠╦╝║╣ ║  ╠═╣╔╩╦╝" + Style.RESET_ALL)
print(Fore.RED  + "               ╚═╝╚═╝╝╚╝ ╩ ╩╚═╚═╝╩═╝╩ ╩╩ ╚═" + Style.RESET_ALL)
print(Fore.RED + "------------------------------------------------------------------------------------" + Style.RESET_ALL)


output_file = "password.txt"
print("")
amount = int(input(Fore.BLUE  + "How many Words Do You Wanna Create : " + Style.RESET_ALL))
print(Fore.RED  + "------------------------------------------------------------------------------------" + Style.RESET_ALL)
for i in range(1):
    generated = ("").join(random.choices(string.ascii_letters + string.digits, k = (amount)))
    print(Fore.GREEN +"Your Password Has Been Generated" + Style.RESET_ALL)
    with open(output_file, "a") as f:
        f.write(generated + "\n")
input()
