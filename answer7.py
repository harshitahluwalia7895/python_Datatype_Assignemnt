#Answer_7

new=[]
print("Enter elements in the list-->: ")
c='y'
while c=='y':
	element=input('Enter element: ')
	new.append(int(element))
	c=input("Do you want to enter more elements? y/n: ")
even=0
odd=0
for i in new:
	if i%2==0:
		even=even+1
	else:
		odd=odd+1
print('odd numbers are:',odd,' and even numbers are:',even)
