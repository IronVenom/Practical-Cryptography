#Baconian Cipher [Can be used only on alphabets, no numbers and characters are allowed.]

key_dict = {'A':'aaaaa', 'B':'aaaab', 'C':'aaaba', 'D':'aaabb', 'E':'aabaa','F':'aabab', 'G':'aabba', 'H':'aabbb', 'I':'abaaa', 'J':'abaab', 
			'K':'ababa', 'L':'ababb', 'M':'abbaa', 'N':'abbab', 'O':'abbba','P':'abbbb', 'Q':'baaaa', 'R':'baaab', 'S':'baaba', 'T':'baabb', 
        	'U':'babaa', 'V':'babab', 'W':'babba', 'X':'babbb', 'Y':'bbaaa', 'Z':'bbaab'}

decode_dict = {i:j for (j,i) in key_dict.items()} 

# Encoding Function

def encode(string):

	encoded_string = ''
	for i in string.upper():
		if ord(i)>=ord('A') and ord(i)<=ord('Z'):
			encoded_string+=key_dict[i]
		else:
			encoded_string+=i
	print('\nThe encoded string is:-\n\n{}'.format(encoded_string))

#Decoding Function

def decode(string):

	decoded_string = ''
	words = []
	split_string = string.split(' ')
	for i in split_string:
		l=[]
		for j in range(0,len(i)-4,5):
			l.append(i[j:j+5])
		l = ''.join([decode_dict[k] for k in l])
		words.append(l)
	decoded_string = ' '.join(words)
	print('\nThe decoded string is:-\n\n{}'.format(decoded_string))

# Driver Code

query = input('\nEnter encode for encoding and decode for decoding.\n\n')

if query == 'encode':
	string = input('\nEnter string.\n\n')
	encode(string)

elif query == 'decode':
	string = input('\nEnter string.\n\n')
	decode(string)

else:
	print('Please try again.')