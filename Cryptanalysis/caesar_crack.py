# Cracking Right Shifted Caesar Ciphers

from math import log10
from prettytable import PrettyTable

# Loading the quadgrams and creating a frequency dictionary.

file = open('english_quadgrams.txt','r')

quads = file.readlines()
quads = [i.split(' ') for i in quads]
quads = {i[0]:int(i[1].split('\n')[0]) for i in quads}

string = input('\nEnter right shifted Caesar cipher encoded string for cracking.\n')

keys = [i for i in range(1,26)]

# Finding alll sets of all possible quadgrams of the string for all the possible keys and finding the fitness for the respective keys.

qs_global = []

sum_global = []

for key in keys:

	decoded_string = ''

	for i in string:

		if ord(i)>=ord('A') and ord(i)<=ord('Z'):
			if ord(i)-key<ord('A'):
				decoded_string+=chr(ord('Z')-key+ord(i)-ord('A')+1)
			else:
				decoded_string+=chr(ord(i)-key)
		elif ord(i)>=ord('a') and ord(i)<=ord('z'):
			if ord(i)-key<ord('a'):
				decoded_string+=chr(ord('z')-key+ord(i)-ord('a')+1)
			else:
				decoded_string+=chr(ord(i)-key)
		else:
			decoded_string+=i

	quadgrams = decoded_string.split(' ')

	sum = 0

	for i in quadgrams:

		if len(i)>=4:
			
			qs_local = [i[j:j+4] for j in range(0,len(i)) if j+4<=len(i)]
			qs_local = [i for i in qs_local if len(i)>=4]
			qs_global.append(qs_local)
			for i in qs_local:
				try:
					sum+=log10(float(quads[i.upper()]/len(quads)))
				except KeyError:
					sum+=0

	sum_global.append([key,sum])

sum_global.sort(key=lambda x:x[1],reverse = True)
top_key = sum_global[0][0]

# Printing out the fitnesses of the variations according to keys :

print('\nThe Fitness Table for the given string is as follows:\n')

fitness_table = PrettyTable(['Key','Fitness'])

for i in sum_global:
	fitness_table.add_row(i)

print(fitness_table)

# Printing out the decoded cipher :

print('\nThe Required key for decoding is {}.\n'.format(top_key))

decoded_string = ''

for i in string:

	if ord(i)>=ord('A') and ord(i)<=ord('Z'):
		if ord(i)-top_key<ord('A'):
			decoded_string+=chr(ord('Z')-top_key+ord(i)-ord('A')+1)
		else:
			decoded_string+=chr(ord(i)-top_key)
	elif ord(i)>=ord('a') and ord(i)<=ord('z'):
		if ord(i)-top_key<ord('a'):
			decoded_string+=chr(ord('z')-top_key+ord(i)-ord('a')+1)
		else:
			decoded_string+=chr(ord(i)-top_key)
	else:
		decoded_string+=i

print('The decoded string is:- \n\n{}\n'.format(decoded_string))
