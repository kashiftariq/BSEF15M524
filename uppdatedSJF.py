process = []
waiting = []
burst_time = []
total_process = 0
print("Welcome to SJF - Non preemptive Program")


print("---------------------------------------")

def Input():
    global total_process
    total_process = eval(input("enter number of process: "))
    for i in range(0,total_process):
      print("enter burst time of Process", i + 1,": ", end='')
      burstTime = eval(input())
      process.append(i+1)
      burst_time.append(burstTime)


def printInput():
    print("Process\t|Burst time")
    print("-----------------------------")
    for i in range(0,total_process):
      print(process[i],"\t",burst_time[i])


def selectionSort():
    for j in range(0,total_process):
       min = burst_time[j]
       location = j
    for i in range(j+1,total_process):
        if min > burst_time[i]:
            min = burst_time[i]
            location = i
    temp=process[j]
    process[j]=process[location]
    process[location]=temp
    temp=burst_time[j]
    burst_time[j]=burst_time[location]
    burst_time[location]=temp


def waitingTimeCalculation():
    global waiting
    i = 0
    waiting += [i]
    for i in range(1, total_process):
      v1 = waiting[i-1]
      v2 = burst_time[i-1]
      waiting.append(v1+v2)


def output():
    sum = 0
    for i in range(0,total_process):
      print("the waiting time of process", process[i] ,": ", waiting[i])
      sum +=waiting[i]
    print("the average waiting time of all processes is: ",sum/total_process)

Input()
printInput()
selectionSort()
waitingTimeCalculation()    
output()
