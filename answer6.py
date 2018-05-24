#answer 6

	#implementation_of_Stack_using_List

	stack = ["Harshit", "Kartik", "Shubham"]
	print('Before Insertion')
	print(stack)
	print('After Insertion')
	stack.append("Rajat")
	stack.append("Ashu")
	print(stack)
	print('Upper element Deleted',stack.pop())
	print(stack)
	print('Upper elemnt Deleted',stack.pop())
	print(stack)

#implementation_of_Queue_using_Lists
	from collections import deque
	print('Insertion is done from front end and Deletion is done by rear end')
	queue = deque(["Harshit", "Shubham", "Aisha", "Himanshi"])
	print('Before Insertion')
	print(queue)
	print('After Insertion')
	queue.append("Vinayak")
	print(queue)
	print('After Insertion')
	queue.append("Kartik")
	print(queue)
	print("poped element is "+queue.popleft())                 
	print("poped Element is "+queue.popleft())                 
	print(queue)
