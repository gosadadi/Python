for i in range(50):  # print all integers 0 to 50
    print(i)
for i in range(5, 1000):  # print all multiples of 5 from 5-1000
    if (i % 5 == 0):
        print(i)
for i in range(1, 100):
    if (i % 5 == 0):
        print("Coding")
    if (i % 10 == 0):
        print("Coding Dojo")
count = 0
for i in range(1, 500000):  # all odd between 1 and 500000
    if (i % 2 == 1):
        count += i
print(count)  # count down by 4
sum_of_count_down = 0
for i in range(2018, 0, -4):
    if (i > 0):
        sum_of_count_down += i
print(sum_of_count_down)
lowNum = 2
highNum = 20
mult = 3
for i in range(lowNum, highNum):
    if (i % mult == 0):
        print(i)
