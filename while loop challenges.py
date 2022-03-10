#while loop challenges.

count = 0
name = input('who do you want to invite to the party')
print(name,'has now been invited')
count = (count + 1)
print(count)
answer = input('do you want to invite someone else Y or N')

while answer == 'y':
    name = input('who do you want to invite to the party')
    print(name,'has now been invited')
    count = (count + 1)
    print(count)
    answer = input('do you want to invite someone else Y or N')
    
