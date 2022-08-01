
lst = []
n = input("Enter the standard wise fees: ")

for i in range(0, 12):
    ele = int(input())

    lst.append(ele)

N = int(input("Enter the number of students: "))
sum = 0
for i in range(0, N):
    index = int(input())
    sum = sum + lst[index]

print(sum / 12)


