#01-10-2020
#16:59
#Autor: Pedro Sequeira

import sys
import os 
from fractions import gcd

table = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def main():
	print("Welcome to Affine Cipher Hub!")
	opt = input("Do you want to encrypt or decrypt(e/d)")
	if opt == 'e':
		encryption()
	elif opt == 'd':
		decryption()
	else:
		print("Learn how to read")
		sys.exit()


def encryption():

	while True:
		key1 = eval(input("Key1 = "))

		key2 = eval(input("key2 = "))

		if gcd(key1, key2) != 1:
			print("Learn modular arithemetic")
		else:
			break
		

	plaintext = input("Message = ")

	ciphertext = ""

	for i in plaintext:
		n = Tableindex(i)
		if n >= 0 and n < 26:
			p = ((key1 * n) + key2) % 26
			ciphertext += table[p]
		elif i == " " or isdigit(i):
			ciphertext += i
		else:
			print("Learn how to write")
			sys.exit()

	print(ciphertext)

def Tableindex(n):
	counter = 0
	for i in table:
		if n == i :
			return counter
		else:
			counter += 1
	return -1

def decryption():
	while True:
		key1 = eval(input("Key1 = "))

		key2 = eval(input("key2 = "))

		if gcd(key1, key2) != 1:
			print("Learn modular arithemetic")
		else:
			break
		

	ciphertext = input("Message = ")

	plaintext = ""

	for i in ciphertext:
		n = Tableindex(i)
		if n >= 0 and n < 26:
			if ((n - key2) % key1 ) == 0:
				p = (n - key2) // key1
				plaintext += table[p]
			else:
				while ((n - key2) % key1 ) != 0:
					n += 26				
				p = (n - key2) // key1
				plaintext += table[p]
		elif i == " " or isdigit(i):
			plaintext += i
		else:
			print("Learn how to write")
			sys.exit()

	print(plaintext)


try:
	main()
except KeyboardInterrupt:
	sys.exit()

