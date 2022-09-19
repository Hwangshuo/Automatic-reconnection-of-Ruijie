import os
import sys
import time

ip = '114.114.114.114'
while True:
 print('Link test')
 if os.system('ping -c 2  %s'%ip):
  #if Request timeou, return value 1
  #else return value 0
  print('Packet lost')
  os.system('sudo ./rjsupplicant.sh -a 1 -n enp5s0 -d 1 -u your_account -p your_passwd')
  print(' link----------------------------')
 else :
  print('Link success')
 time.sleep(3)
 os.system("clear")
