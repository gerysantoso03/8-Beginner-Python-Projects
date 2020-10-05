import pyfiglet
from colorama import init

# Run the init()
init()

# Import Fore - font color, Back - background color, and Style for styling
from colorama import Fore, Back, Style 

print(Fore.CYAN, "Halo Gery Santoso :)")
print(Back.WHITE, "Selamat Bekerja !!")

word = pyfiglet.figlet_format('WannaBeStart', font ="alphabet")
print(word)