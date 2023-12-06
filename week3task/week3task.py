#numbers iterating from 0-99 
for i in range(100):
    print(f'{i:02d}', sep=", ", end=" ")
    print()




#the three and five number task
for i in range(1, 51):
    if i % 2 ==0:
        if i % 3 == 0:
            print('three')
        elif i % 5 == 0:
            print('five')
        elif i % 3 and i % 5 != 0:
            print(i)

#the palindrom checker
user = str(input('enter a word to check: '))
users = user[::-1]

if users == user:
    print(f'the word {user} is a palindrom')
else:
    print(f'the word {user} isnot a palindrom, because the word {users} is not {user}')