numbers=(1,2,3,4,5,6,7,8,9)
len_number= len(numbers)
even_number=0
odd_number=0
for i in range(len_number):
    if i%2==0:
        even_number=even_number+1
    else:
        odd_number=odd_number+1

print("Number of even numbers:",even_number)
print("Number of odd numbers:",odd_number)
