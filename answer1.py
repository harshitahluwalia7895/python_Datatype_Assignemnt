#Q.1- Create a list with user defined inputs. 

new_list=[]
choice='y'
while choice=='y':
	element=input("Enter a element in the List: ")
	new_list.append(element)
	choice=input("Do you want to enter more? y/n: ")
print(new_list)
