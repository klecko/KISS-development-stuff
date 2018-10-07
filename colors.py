import os

def c(n):
    return "\033[" + str(n) + "m"

def a(n):
    print(c(n) + "El veloz murciélago hindú comía feliz cardillo y kiwi" + c(0))

def intro(n):
    #ASCII
    
##    ascii= """
##     ___  ___    ___   ________    ________      
##    |\  \|\  \  |\  \ |\   ____\  |\   ____\     
##    \ \  \/  /|_\ \  \\\ \  \___|_ \ \  \___|_    
##     \ \   ___  \\\ \  \\\ \_____  \ \ \_____  \   
##      \ \  \\\ \  \\\ \  \\\|____|\  \ \|____|\  \  
##       \ \__\\\ \__\\\ \__\ ____\_\  \  ____\_\  \ 
##        \|__| \|__| \|__||\_________\|\_________\ 
##                         \|_________|\|_________|
##    """

    width = os.get_terminal_size().columns - 2
    
    # ~ print(" ___  ___    ___   ________    ________       ".center(width))
    # ~ print("|\  \|\  \  |\  \ |\   ____\  |\   ____\     ".center(width))
    # ~ print("\ \  \/  /|_\ \  \\\ \  \___|_ \ \  \___|_    ".center(width))
    # ~ print(" \ \   ___  \\\ \  \\\ \_____  \ \ \_____  \   ".center(width))
    # ~ print("  \ \  \\\ \  \\\ \  \\\|____|\  \ \|____|\  \  ".center(width))
    # ~ print("   \ \__\\\ \__\\\ \__\ ____\_\  \  ____\_\  \ ".center(width))
    # ~ print("    \|__| \|__| \|__||\_________\|\_________\ ".center(width))
    # ~ print("                     \|_________|\|_________| ".center(width) + "\n")
    # ~ log.header("       Klecko Is Spoofing and Sniffing".center(width) + "\n")
    
    
    print(c(n), " ___  ___    ___   ________    ________       ".center(width), c(0))
    print(c(n), "|\  \|\  \  |\  \ |\   ____\  |\   ____\     ".center(width), c(0))
    print(c(n), "\ \  \/  /|_\ \  \\\ \  \___|_ \ \  \___|_    ".center(width), c(0))
    print(c(n), " \ \   ___  \\\ \  \\\ \_____  \ \ \_____  \   ".center(width), c(0))
    print(c(n), "  \ \  \\\ \  \\\ \  \\\|____|\  \ \|____|\  \  ".center(width), c(0))
    print(c(n), "   \ \__\\\ \__\\\ \__\ ____\_\  \  ____\_\  \ ".center(width), c(0))
    print(c(n), "    \|__| \|__| \|__||\_________\|\_________\ ".center(width), c(0))
    print(c(n), "                     \|_________|\|_________| ".center(width) + "\n", c(0))
    print("       Klecko Is Spoofing and Sniffing".center(width) + "\n")
    
    
for i in range(100):
    print(i, end="")
    a(i)

print("\n")
for i in range(30,37):
    print(i, end="")
    a(i)
    print(i+60, end="")
    a(i+60)


# ~ print("31",c(31) + "[ERROR]" + c(0) + " This is the error msg")
# ~ print("31b",c(31) + c(1) + "[ERROR]" + c(0) + " This is the error msg")
# ~ print("91",c(91) + "[ERROR]" + c(0) + " This is the error msg")
# ~ print("91b",c(91) + c(1) + "[ERROR]" + c(0) + " This is the error msg")

# ~ print(c(31) + c(1) + "[ERROR]" + c(0) + c(91) + c(1) + "[ERROR]" + c(0))
# ~ print(c(91) + c(1) + "[ERROR]" + c(0) + c(31) + c(1) + "[ERROR]" + c(0))

for i in range(30,37):
    print(i, c(41) + c(i) + "[ERROR]" + c(0) + " This is the error msg")
    
    print(i+60, c(41) + c(i+60) + "[ERROR]" + c(0) + " This is the error msg")
    print(str(i)+"b", c(41) + c(1) + c(i) + "[ERROR]" + c(0) + " This is the error msg")
    
print("\n\n\n")
print("36",c(41) + c(1) + c(36) + "[ERROR]" + c(0) + " This is the error msg")
print("1b",c(41) + c(1) + "[ERROR]" + c(0) + " This is the error msg")
print("93b",c(41) + c(1) + c(93) + "[ERROR]" + c(0) + " This is the error msg")

# ~ for i in range(30, 37):
    # ~ print(i)
    # ~ intro(i)
    # ~ intro(i+60)
    # ~ print("\n")
