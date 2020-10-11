for i in range(0,6):
   print(i);

sum=0  
for n in range(1,11):  
    sum+=n  
print("Total = ",sum)


for i in range(1,6):  
    for j in range (1,i+1):  
        print(i),
    print();



for i in range (1,6):  
    for j in range (5,i-1,-1):  
        print("*"),  

    print();

num=100;
for i in range(1,10):
    for j in range(1,num):
        if(j%i==0):
          print(j);
            
