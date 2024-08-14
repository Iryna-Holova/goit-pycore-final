from colorama import Fore, Back, Style, init

# Initialize Colorama
init(autoreset=True)

# Palitra for ********************* TEXT *********************
def green(text):
    return Fore.GREEN + text + Style.RESET_ALL

def blue(text):
    return Fore.BLUE + text + Style.RESET_ALL

# Palitra for ********************* BackGround *********************
def success(text):
    return Fore.WHITE + Back.GREEN + text + Style.RESET_ALL

def warning(text):
    return Fore.WHITE + Back.YELLOW + text + Style.RESET_ALL

def danger(text):
    return Fore.WHITE + Back.RED + text + Style.RESET_ALL

