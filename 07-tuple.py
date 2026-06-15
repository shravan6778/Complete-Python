t1=(1,2,3,4,5,6,7,8,True,"abc",2.2,23.4)
print(t1)

#using tuple constructor
t2=tuple((1,2,3,4))
print(t2)

#tuple comprehension
squares = tuple(i**2 for i in range(1,100) if i%2==0)
print(squares)

#tuple using range function
num=range(1,20,2)
print(tuple(num))

#Accessing Elements using index
print(t1[2])
print(t2[3])

#Slicing
print(squares[::])
print(squares[:6])
print(squares[23:7:-1])


#Tuple Methods
t=(1,2,3,4,5,6,7,8,True,"abc",2.2,23.4)
#7.index
print("List Index")
print(t.index('abc'))

#8.count
print("List count")
print(t.count(2.2))

#9.sort
e=(1,2,3,4,5)
# e.sort() tuples are immutable (unchangeable)
print(e)

#10.min and max
print("List min and max")
print(max(e))
print(min(e))

#11.Length
print("length of List")
print(len(t))

