import sys
import os
import time
print("")
print("")
print("        ____             __     ")
print("       / __ \____ ______/ /__   ")
print("      / / / / __ `/ ___/ //_/   ")
print("     / /_/ / /_/ / /  / ,<      ")
print("    /_____/\__,_/_/  __/|_| __  ")
print("            | |     / /__  / /_ ")
print("            | | _  / / _ \/  _ /")
print("            | |/ |/ /  __/ /_/ /")
print("            |__/|__/\___/_.___/ ")
print("")
print("")
print("             [01] Join server")
print("             [02] Host server")
print("             [03] Help")
print("")
dark=input("[*] enter your choice: ")
if dark == "1":
      print("")
      ip=input("[*] enter ip address: ")
      print("")
      print("    type something in the chat")
      print("")
      netcat = "nc -nv "+ ip+" 4444"
      os.system(netcat)
elif dark == "2":
      print("")
      print("    Hosting server")
      time.sleep(1)
      print("        done")
      print("    send your ip to friends")
      print("     so they can join you")
      print("")
      host = "nc -lp 4444"
      os.system(host)
elif dark == "3":
      print("")
      print("    Welcome to Darkweb a place where you")
      print("    chat with your friends privatly. You")
      print("    can host servers or join them")
      print("")
      print("             list of ports")
      print("          --------------------")
      print("")
      print("       21               ftp")
      print("       22               ssh")
      print("       80               http")
      print("       443              https")
      print("       4444             http\s proxy")
      print("       8888             MAMP")
      print("")
      time.sleep(3)
      sys.exit()
