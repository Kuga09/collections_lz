import matplotlib.pyplot as plt
x=list(range(-100,101))
y=[]
for i in x:
  y.append(i**3) 
plt.title('Кубическая парабола',color='#173544', fontstyle="italic", fontweight="bold") 
plt.xlabel('Ось X',color='#173554', fontweight="bold")
plt.ylabel('Ось Y',color='#173554', fontweight="bold")
plt.plot(x,y)
plt.show()