print("first come first serve")

def findWaitingTime(processes, n, bt, wt):
    wt[0] = 0
    for i in range(1, n):
        wt[i] = bt[i - 1] + wt[i - 1]


def findTurnaroundTime(processes, n, bt, wt, tat):
    for i in range(n):
        tat[i] = bt[i] + wt[i]


def findAvgTime(processes, n, bt):
    wt = [0] * n
    tat = [0] * n
    total_wt = 0
    total_tat = 0

   
    findWaitingTime(processes, n, bt, wt)
    findTurnaroundTime(processes, n, bt, wt, tat)

   
    print("Process\tBurst Time\tWaiting Time\tTurnaround Time")
    for i in range(n):
        total_wt += wt[i]
        total_tat += tat[i]
        print(str(processes[i]) + "\t\t" + str(bt[i]) + "\t\t" +
              str(wt[i]) + "\t\t" + str(tat[i]))

    
    print("\nAverage Waiting Time = {:.2f}".format(total_wt / n))
    print("Average Turnaround Time = {:.2f}".format(total_tat / n))


if __name__ == "__main__":
    processes = [1, 2, 3]
    n = len(processes)
    burst_time = [24, 3, 3]

    findAvgTime(processes, n, burst_time)

