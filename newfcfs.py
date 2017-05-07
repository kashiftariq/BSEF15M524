



p = []
w = []
b = []
a = []
aa = []
print("Welcome to FCFS - Non preemptive Program")
print("---------------------------------------")
n = eval(input("enter number of process: "))


for i in range (0,n):
	at=eval(input("Enter arrival time of the process: "))
	if(i==0):
		min=at	
	elif(min>at):
		min=at	
	a.append(at)

for i in range(0, n):
    print("enter burst time of Process", i + 1,": ", end='')
    bt = eval(input())
    p.append(i+1)
    b.append(bt)
    
print("Process\t|Burst time\t|Arrival time")
print("-----------------------------")
for i in range(0,n):
    print(p[i],"\t",b[i],"\t","\t",a[i])
i = 0
w += [i]
res=0
total=min
if(total>0):
	print ("0 ---", total , "idle time of cpu")


for i in range(1,n):
            
            b_time = b[i-1]
             
            total = total + int(b_time)
            
            v3=a[i]
            w.append(total-v3)
            min = total

sum = 0
for i in range(0,n):
    print("the waiting time of process ", i+1,": ", w[i])
    sum +=w[i]
print("the average waiting time of all processes is: ",sum/n)
