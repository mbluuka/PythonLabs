#LZWcoding
string =input('Please enter the string to be compressed:')
dictionary = {chr(i): i for i in range(1, 123)}#Import ASC code into dictionary 1

last = 256#New encoding starts at 256th bit
p = ""#Define the previous character, start empty
result1 = []#Define an empty array as encoding output

for c in string:  #c is the next character, if c executes a loop in the string, c points to the next character after executing once
    pc = p + c    #Combine the two characters before and after to form a new character with pc
    if pc in dictionary:  #If pc is in the dictionary, take pc as the previous character
        p = pc
    else:
        result1.append(dictionary[p])  #If pc is not in the dictionary, output the previous character encoding
        dictionary[pc] = last    #Encode and store pc in the dictionary
        last += 1
        p = c   #P points to the next character

if p != '':   #Process the last character
   result1.append(dictionary[p])
x2 = len(result1)   #Calculate code length
print('The compressed code is:',result1)  #Output encoding

#Decoding
dictionary2 = {i: chr(i) for i in range(1, 123)}  #Reverse import ASC code into dictionary 2
last2 = 256

result2 = []
p = result1.pop(0)     #Give code 1 to p and delete it from the output array
result2.append(dictionary2[p])   #Store the decoded characters of code 1 into the decoding array

for c in result1:  #Because code 1 is deleted, c starts from the second code
    if c in dictionary2:
        entry = dictionary2[c]
    result2.append(entry)   #Store the decoded characters in the decoded array
    dictionary2[last2] = dictionary2[p] + entry[0]   #Combine the characters translated from the previous two codes into a new character and store them in the dictionary 2
    last2 += 1
    p = c

print('The decoding result is:')
print(''.join(result2)) #Output the decoding result as a string

x1 = len(string)  #Calculate the length of the input string
x3 = (x2*9)/(x1*8)  #Calculate compression ratio
print('String length:',x1)
print('Length after encoding:',x2)
print('LZW compression ratio:',x3)