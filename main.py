from colorama import Fore, Back, Style, init
import keyboard, time, os, sys


letter = "l"
line = str(letter)*65

def print_line():
    cls()
    parts = [
        f"{Fore.RED + 'Instructions:'}",
        f"{Style.RESET_ALL} maximize your window and use the controls below to add more characters.\nOnce the characters split off onto a new line, you have reached your maximum character limit. Use the counter below to help.\n\n",
        f"{Fore.RED + 'Controls:'}",
        f"{Style.RESET_ALL}\nleft arrow = remove character\nright arrow = add character\n'e' = close program\n\n\n{line}\n\n\n",
        f"{Fore.RED + 'Character count:'}",
        f"{Style.RESET_ALL} {len(line)}\n",
        f"{Fore.RED + 'Letter:'}",
        f"{Style.RESET_ALL} {letter}",
    ]
    for index in parts:
        sys.stdout.write(index)
    print(Style.RESET_ALL)

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

print_line()
while True:
    try:
        if keyboard.is_pressed("left"):
            line = list(line)
            line.remove(letter)
            line = "".join(line)
            print_line()
            time.sleep(.01)
        elif keyboard.is_pressed("right"):
            line = list(line)
            line.append(letter)
            line = "".join(line)
            print_line()
            time.sleep(.01)
        elif keyboard.is_pressed("e"):
            break
    except:
        pass
