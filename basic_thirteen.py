# print all interger from 1 255
# for i in range(1,256):
#     print(i)
# print integers 0-255 with sum of integers so far
# sum=0
# for i in range(255):
#     sum+=i
#     print (f" num:{i},sum:{sum}")
# given array find and print its largest element
# myList=[2,4,5,6,7,8,9,10,11,12,13]
# def largest_element(list):
#     max=list[0]
#     for i in list:
#         if i >max:
#             max=i
#     print(max)


# largest_element(myList)

# create an array with all the odd numbers between 1 and 255(inclusive)
# odds = []
# for i in range(1, 256):
#     if (i % 2 != 0):
#         odds.append(i)
# print(odds)
# given an array and value of Y, count and print the number of array value greater than Y
# def greaterCount(list,Y):
#     count=0
#     for val in list:
#         if(val>Y):
#             print(val)
#             count+=1
#     print(count)
# myList=[2,4,5,6,7,8,9,10,20,40,100,11]
# greaterCount(myList,10)
# given a list of, print the max, min ,and average values for that list.
def maxMinAverage(list):
    max=list[0]
    min=list[0]
    sum=0
    for i in list:
        if i >max:
            max=i
        if i < min:
            min=i
    print(f"max:{max},min:{min}")
myList=[2,4,5,6,7,8,9,10,20,40,400,200]
maxMinAverage=maxMinAverage(myList)
