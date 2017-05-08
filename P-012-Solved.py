"""The sequence of triangle numbers is generated by adding the natural numbers. So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

Let us list the factors of the first seven triangle numbers:

 1: 1
 3: 1,3
 6: 1,2,3,6
10: 1,2,5,10
15: 1,3,5,15
21: 1,3,7,21
28: 1,2,4,7,14,28
We can see that 28 is the first triangle number to have over five divisors.

What is the value of the first triangle number to have over five hundred divisors?"""

def triangle(num):
	tri_num = num*(num+1)/2
	return int(tri_num)

def div(num):
	list_divisible = []
	num_sq = int(num**0.5)+1 # Take the squre root 
	for j in range(1,num_sq): # iterate to the square root instead till the num
		if num % j == 0 and int(num/j)!=j: # check for divisor and repeated divisors 
			list_divisible.append(j)
			list_divisible.append(int(num/j))
		elif num % j == 0 and int(num/j)==j: # check for divisor and repeated divisors 
			list_divisible.append(j)
	return list_divisible
			
Flag = True
i = 1
while Flag:
	if len(div(triangle(i)))>= 500:
		print(triangle(i))
		Flag = False
		break
	else:
		i +=1