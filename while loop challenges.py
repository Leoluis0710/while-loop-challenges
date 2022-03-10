#while loop challenges.
number = int(input('enter a number'))
number2 = int(input('enter another number'))
total = (number + number2)
print(total)
answer = input('do you want to add another number')
while answer == 'y':
 number3 = int(input('enter another number'))
 print(total + number3)
 answer = input('do you want to add another number')
