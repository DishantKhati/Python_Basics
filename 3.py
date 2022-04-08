print("Dishant khati")
l=input("Enter the list: ")
ul=l.split()
i=0
t=[]
for i in ul:
    if i not in t :
     t.append(i)
ul=t
print("List without duplicates",ul)               