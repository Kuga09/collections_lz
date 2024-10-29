N=int(input())
list=[0,1]
i=0
i1=1
while i1 < N:
    i1=i1+i
    list.append(i1)
    i=i1-i
list1=[]
for p in range(0,len(list)):
        if list[p] % 2 == 0:
            a=list[p]*2
            list1.append(a)
        else:
            a=list[p]**2
            list1.append(a)  
max=0
for d in range(0,len(list1)):
     if list1[d]>max:
          max=list1[d]
m=sum(list1)/len(list1)
print('Длина списка = ', len(list1))
print('Максимальный элемент = ', max)
print('Минимальный элемент = 0 ')
print('Медианное значение = ', m)