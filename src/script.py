#!/usr/bin/env python

import hashlib
import zlib 

flag = 0

input_hash = input("Enter hashed password: ")

input_file = input("Enter file name: ")

try:
    dict_file = open(input_file,"r")
except:
    print("No file found :(")
    quit()

hash_type = input("Enter hash type: ")

if hash_type == "md":
  
  for word in dict_file:
    enc_wrd = word.encode('utf-8')
    digest =hashlib.md5(enc_wrd.strip()).hexdigest()
    if digest.strip() == pass_hash.strip():
        print("password found")
        print("Password is " + word)
        flag = 1
        break
 
if flag == 0:
    print("password not in list")
    
    
    
    elif hash_type == "sha-256":

      for word in dict_file:
    enc_wrd =word.encode('utf-8')
    digest =hashlib.sha256(enc_wrd.strip()).hexdigest()
    if digest.strip() == pass_hash.strip():
        print("password found")
        print("Password is " + word)
        flag = 1
        break
 
if flag == 0:
    print("password not in list")
    
   elif hash_type == "crc-32":
    
        for word in dict_file:
    enc_wrd =word.encode('utf-8')
    digest =zlib.crc32(enc_wrd.strip()).hexdigest()
    if digest.strip() == pass_hash.strip():
        print("password found")
        print("Password is " + word)
        flag = 1
        break
 
if flag == 0:
    print("password not in list")
    
    
else:
  print("Hash algorithm not found")
