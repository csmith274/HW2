import sys
import hashlib   
import time     

password = ''
passwordHash = ''
#argument saved here
hash = argv

#print 'Hash to compare? (SHA-1)'
#hash = raw_input('>')

answer = ''


#password file goes here
f = open("C:/Users/Cameron/code/passlist2.txt", "r")
lines = f.readlines()
  
for x in lines: 
	passwordHash = hashlib.sha1(x).hexdigest()
	if hash == passwordHash
		Print (lines[x])

   

	
f.close()





password1 = 'letmein'
passwordHash1 = hashlib.sha1(password1).hexdigest() 
print(password1)
print(passwordHash1)

password1 = 'vjhtrhsvdctcegth'
passwordHash1 = hashlib.sha1(password1).hexdigest() 
print(password1)
print(passwordHash1)

password1 = 'slayer'
passwordHash1 = hashlib.sha1(password1).hexdigest() 
print(password1)
print(passwordHash1)


