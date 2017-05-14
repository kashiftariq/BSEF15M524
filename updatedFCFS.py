

minimum = 0
total=0
total_process=0
process = []
waiting_time = []
burst_time = []
arival_time = []

print("Welcome to FCFS - Non preemptive Program")
print("---------------------------------------")

def Input():
    
    global total_process
    global minimum
    total_process = eval(input("enter number of process: "))

    for i in range (0,total_process):
     arrivalTime=eval(input("Enter arrival time of the process: "))
     
    if(i==0):
            minimum = arrivalTime	
    elif(minimum> arrivalTime):
            minimum= arrivalTime	
    arival_time.append(arrivalTime)

    for i in range(0, total_process):
     print("enter burst time of Process", i + 1,": ", end='')
     burstTime = eval(input())
     process.append(i+1)
     burst_time.append(burstTime)
Input()
def printData():
    print("Process\t|Burst time\t|Arrival time")
    print("-----------------------------")
    for i in range(0,total_process):
     print(process[i],"\t",burst_time[i],"\t","\t")
printData()    

def waitingCalculation():
    global waiting_time
    global total
    i = 0
    waiting_time += [i]
    res=0
    total=minimum
    if(total>0):
     print ("0 ---", total , "idle time of cpu")


    for i in range(1,total_process):
            
            b_time = burst_time[i-1]
             
            total = total + int(b_time)
            
            v3=arival_time[i]
            waiting_time.append(total-v3)
            minimum = total
waitingCalculation()
sum = 0

def printOutput():
    for i in range(0,total_process):
     print("the waiting time of process ", i+1,": ", waiting_time[i])
     sum +=waiting_time[i] 
     print("the average waiting time of all processes is: ",sum/total_process)
printOutput()
