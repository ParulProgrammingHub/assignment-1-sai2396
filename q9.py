list=[]
total=0
print ("Enter marks for ")
for i in range(0,5):
    print('Subject', i)
    val=int(input())
    list.insert(i,val)

for i in range(0,5):
    total+=list[i]

per = (total * 100) / 500
print ("Percentage:", per)
if (per < 35):
    print("Fail")
else:
    print("Pass")
