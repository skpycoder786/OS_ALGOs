# FIRST COME FIRST SERVE ALGO.
import pandas as pd
id=[]
N=int(input("Enter no. of processes in FCFS Sheduling :"))
for i in range(N):
    id.append(i)
# Making Sheduling Table or Processes DataFrame 'df' with PIDs   
df=pd.DataFrame(index=id,columns=["AT","BT","CT","TAT","WT"])
df.index.name="PID"
#print(df)
print("Now enter Arrival time and Burst time (in format \"AT BT\") of processes :")
for i in range(N):
    at,bt = map(int,input().split())
    df["AT"][i]=at
    df["BT"][i]=bt  
#print(df)    

# Sorting by values
def sort_tup(tup):
    tup.sort(key = lambda x: x[1])
    return tup
    
# Making of Gantt Chart (FCFS)    ****GAME_CHANGES_HERE****
print("\nGantt Chart for processes in FCFS Sheduling ...\n")
id_at = [(k,v) for k,v in df["AT"].items()]
sort_tup(id_at) # sorting by AT values
t = id_at[0][1]
print(t,end="   ")

for k,v in id_at:
    if t < v :      # special case
        delay = v-t
        print("Delay(%d)"%(delay),end="   ")
        t+=delay
        print(t,end="   ")
    print("P[%d]"%(k),end="   ")
    t = t + df["BT"][k]
    print(t,end="   ")
    # Compilation time calculated too.
    df["CT"][k]=t    

# Calculation of Avg. TAT and Avg. WT
for i in range(N):
    df["TAT"][i] = df["CT"][i] - df["AT"][i]
    df["WT"][i] = df["TAT"][i] - df["BT"][i]

print("\n\nSCHEDULING TABLE ...\n\n",df)   
avg_TAT = sum(df["TAT"])/N
print("\nAverage Turn Around Time = ",avg_TAT)
avg_WT = sum(df["WT"])/N
print("\nAverage Waiting Time = ",avg_WT)   