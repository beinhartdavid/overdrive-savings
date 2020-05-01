lst1 = []
lst2 = []

l1 = [1,2,3,4]
l2 = [2,3,4,5]
l3 = [3,4,5,6]
l6 = [4,5,6,7]

lst1.append(l1)
lst1.append(l2)
lst1.append(l3)

lst2.append(l1)
lst2.append(l3)
lst2.append(l6)

print(l2 in lst2)
for i in range(3):
    print(i)


str = "Highlight | loc: 159 "
print(str.split("|")[1].split(":")[1].strip())


lstttt = [[1,2,3],[4,5,6], [7,8,9]]
lstttt[-1].append("H")
print(lstttt)