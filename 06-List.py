l1=[1,2,3,4,5,6,7,8,True,"abc",2.2,23.4]
print(l1)

#using list constructor
l2=list((1,2,3,4))
print(l2)

#list comprehension
squares = [i**2 for i in range(1,100) if i%2==0]
print(squares)

#Nested comprehension
num=[[1,2],[3,4]]
l=[[x**2 for x in row] for row in num]
print(l)

matrix=[[1,2],[3,4]]
flat=[num for row in matrix for num in row]
print(flat)

#List using range function
num=range(1,20,2)
print(list(num))

#Accessing Elements using index
print(l1[2])
print(l2[3])

#Slicing
print(squares[::])
print(squares[:6])
print(squares[23:7:-1])

#List Alias
a=[1,2,3]
print(a)
#Assigning like this a values will also change
b=a
#b[0]=23
print(a,b)
#copy method
b=a.copy()
b[2]=24
print(a,b)

#List Methods
#1.Append
print("List Append")
l=["abc",2.2,2,3,'w']
l.append("hello")
l.append(21)
print(l)

#2.Extend
print("List Extend")
c=[22,33,44,55]
l.extend(c)
print(l)

#3.Insert
print("List Insert")
l.insert(1,"INserted at 1 index")
print(l)

#4.Remove
print("List Remove")
l.remove("hello")
print(l)

#5.Pop
print("List Pop")
l.pop()
l.pop(-1)
print(l)

#6.clear
print("List Clear")
d=l.copy()
d.clear()
print(d)

#7.index
print("List Index")
print(l.index('w'))

#8.count
print("List count")
print(l.count(2.2))

#9.sort
e=[1,2,3,4,5]
e.sort(reverse=True)
print(e)

#10.min and max
print("List min and max")
print(max(e))
print(min(e))

#11.Length
print("length of List")
print(len(l))

