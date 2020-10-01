# 1-10-2020
# 16:06
# Autor: Tiago Carriço

import sys
import os

table = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','x','z']


def main():
	print("Welcome to Caesar Cipher Hub!")
	op = input("Do you want to encrypt or decrypt (e/d) ").lower()
	if op == 'e':
		encrypt()
	elif op == 'd':
		decrypt()

def encrypt():
	k = eval(input("Key = "))

	plaintext = input("Message: \n\t").lower()

	ciphertext = ""
	counter = 0

	for i in plaintext:
		n = TableIndex(i)
		if n >= 0 and n < 26:
			p = (n + k) % 26
			ciphertext+= table[p]
			counter+=1
		elif i == ' ':
			ciphertext+= i
			counter+=1
		elif i.isdigit():
			ciphertext+= i
			counter+=1
		else:
			print("Error: Learn To Write!")
			sys.exit()

	print(ciphertext)

def decrypt():
	k = eval(input("Key = "))

	ciphertext = input("Message: \n\t").lower()

	plaintext = ""
	counter = 0

	for i in ciphertext:
		n = TableIndex(i)
		if n >= 0 and n < 26:
			p = (n - k) % 26
			plaintext+= table[p]
			counter+=1
		elif i == ' ':
			plaintext+= i
			counter+=1
		elif i.isdigit():
			plaintext+= i
			counter+=1
		else:
			print("Error: Learn To Write!")
			sys.exit()

	print(plaintext)

def TableIndex(i):
	c = 0
	for l in table:
		if l == i:
			return c
		c+=1
	return -1





try:
	main()
except KeyboardInterrupt:
		sys.exit()