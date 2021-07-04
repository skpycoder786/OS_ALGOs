print("\n** Worst Fit Algorithm using Fix Partition **\n")

# Gathering Inputs.......
# Memory Partitions's List
mp=int(input("Please enter the total number of memory partitions : "))
print("Now enter the partions's size(Asuming all are in same unit like 'KB') : ")
MP_lst=[]
for i in range(mp):
    MP_lst.append(int(input()))   
# Processes's List
p=int(input("Please enter the total number of Processes which have to be allocated to memory partitions : "))
print("Now enter the Processes's size(Asuming all are in same unit like 'KB') : ")
P_lst=[]
for j in range(p):
    P_lst.append(int(input()))

# WorstFit ALGO.......
IF=0    # Internal Fragmentation
EF=0    # External Fragmentation
print("\nPreferred filling order of Memory Partitions for Worst Fit Algo...")
MP_lst.sort()
MP_lst.reverse()
print(MP_lst)
P_status=[0 for i in range(p)]
MP_status=[0 for i in range(mp)]
for i in range(p):
    pro=P_lst[i]
    for j in range(mp):
        mem=MP_lst[j]
        if MP_status[j] == 0 :
            if pro <= mem :
                P_status[i],MP_status[j]=1,1
                IF+=(mem-pro)
                #CheckPoint-1: print(IF)
                #CheckPoint-2: print(MP_status)
                break
            else:
                continue
        else:
            continue
    if P_status[i]==0 :
        EF+=pro
       
if all(P_status)==1 :
    print("\nAll processes allocated successfully.\n")
else:            
    print("\nExternal fragmentation's problem occurs, can't allocate all processes.\n")

print("Total Internal Fragmentation = ",IF)
print("Total External Fragmentation = ",EF)    