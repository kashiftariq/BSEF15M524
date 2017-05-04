p = []
w = []
b = []
print("Welcome to FCFS - Non preemptive Program")
print("---------------------------------------")
n = eval(input("enter number of process: "))
for i in range(0, n):
    print("enter burst time of Process", i + 1,": ", end='')
    bt = eval(input())
    p.append(i+1)
    b.append(bt)
    #p += [i + 1]
    #b += [bt]
print("Process\t|Burst time")
print("-----------------------------")
for i in range(0,n):
    print(p[i],"\t",b[i])
i = 0
w += [i]
for i in range(1, n):
    v1 = w[i-1]
    v2 = b[i-1]
    w.append(v1+v2)
sum = 0
for i in range(0,n):
    print("the waiting time of process ", i+1,": ", w[i])
    sum +=w[i]
print("the average waiting time of all processes is: ",sum/n)
