# Atbash Cipher Encoding and Decoding

# Dictionaries for encoding and decoding

list_1 = [chr(i) for i in range(ord('A'),ord('Z')+1)]
list_2 = [chr(i) for i in range(ord('a'),ord('z')+1)]
listr_1 = list_1[::-1]
listr_2 = list_2[::-1]
encode_dict_upper = {x:y for x,y in zip(list_1,listr_1)}
encode_dict_lower = {x:y for x,y in zip(list_2,listr_2)}


#Encoding and Decoding.

def atbashcypher(string):
	encoded_string=''
	for i in string:
		if ord(i)>=ord('a') and ord(i)<=ord('z'):
			encoded_string+=encode_dict_lower[i]
		elif ord(i)>=ord('A') and ord(i)<=ord('Z'):
			encoded_string+=encode_dict_upper[i]
		else:
			encoded_string+=i
	print("\nThe encoded string is:- \n\n{}\n".format(encoded_string))


#Driver code

query = input('\nEnter encode for encoding and decode for decoding.\n\n')

if query == 'encode':
	string = input('\nEnter string.\n\n')
	atbashcypher(string)

elif query == 'decode':
	string = input('\nEnter string.\n\n')
	atbashcypher(string)

else:
	print('Please try again.')


