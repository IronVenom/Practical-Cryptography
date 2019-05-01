alphabets = 'abcdefghijklmnopqrstuvwxyz'

#Encoding Function

def encode(string,key):
 
	dict_encode = {i:j for i,j in zip(alphabets,key) }
	encoded_string = []
	for i in string:

		if ord(i) >= ord('a') and ord(i) <=ord ('z'):
			encoded_string.append(dict_encode[i])
		else:
			encoded_string.append(i)
	print('\nThe encoded string is:- \n\n{}\n'.format(''.join(encoded_string)))

# Decoding Function

def decode(string,key):

	dict_decode = {j:i for i,j in zip(alphabets,key) }
	decoded_string = []
	for i in string:

		if ord(i) >= ord('a') and ord(i) <=ord ('z'):
			decoded_string.append(dict_decode[i])
		else:
			decoded_string.append(i)
	print('\nThe decoded string is:- \n\n{}\n'.format(''.join(decoded_string)))


#Driver Code

query = input('\nEnter encode for encoding and decode for decoding.\n\n')

if query == 'encode':
	string = input('\nEnter string.\n\n')
	key = input('\nEnter key.\n\n')
	encode(string,key)

elif query == 'decode':
	string = input('\nEnter string.\n\n')
	key = input('\nEnter key.\n\n')
	decode(string,key)

else:
	print('Please try again.')