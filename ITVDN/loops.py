'''
counter = 5
while counter > 0:
    print("Iteration, counter = ", counter)
    counter -=1
print("_____")
print(counter)

for number in range(5):
    print(number)

for num in range(6):
    if num ==3:
        break
    print(num)

for num in range(101):
    if num % 2 == 0:
        print(num)

counter = 0
end_val = 101

while counter< end_val:
    if counter %2 == 0:
        print(counter)
    counter += 1

word = 'hello'
for n in word:
    if n == "l":
        print("s")
    else:
        print(n)

back_counter = 99
end_value = 0

while back_counter > end_value:
    if  back_counter % 5 == 0:
        print(back_counter)
    back_counter -=1
'''
back_counter = 99
end_value = 0
while back_counter > end_value:
    if back_counter % 5 != 0:
        back_counter -= 1
        continue
    print(back_counter)
    back_counter -=1

