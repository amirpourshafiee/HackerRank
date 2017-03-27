import math
def find_power_sum(list, i, nth_power, number):
    if i < 0:
        return 0
    if math.pow(list[i], nth_power) == number:
        return 1 + find_power_sum(list, i-1, nth_power, number)
    elif math.pow(list[i],nth_power) < number:
        return find_power_sum(list, i-1, nth_power, number-math.pow(list[i], nth_power)) + find_power_sum(list, i-1, nth_power, number)
    else:
        return find_power_sum(list, i-1, nth_power, number)


number = int(input().strip())
nth_power = int(input().strip())
index = 2;
foo = True;
while foo:
    if math.log(number, index) <= nth_power:
        foo = False
    else:
        index += 1
list = []
for i in range(1, index+1):
    list.append(i)
count = 0
i = len(list) - 1

while i > 0:
    if math.pow(list[i], nth_power) == number:
        count += 1
    elif math.pow(list[i], nth_power) < number:
        count += find_power_sum(list, i-1, nth_power, number - math.pow(list[i], nth_power))
    list.pop(i)
    i -= 1
print (count)
