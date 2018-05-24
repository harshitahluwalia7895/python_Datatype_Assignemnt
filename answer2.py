Q2.Add the following list to above created list(list created in q1):
['google','apple','facebook','microsoft','tesla']

new_list=[]
choice='y'
while choice=='y':
	element=input("Enter a element in the List: ")
	new_list.append(element)
	choice=input("Do you want to enter more? y/n: ")
print(new_list)
second_list=['google','apple','facebook','microsoft','tesla']
new_list.extend(second_list)
print(new_list)
