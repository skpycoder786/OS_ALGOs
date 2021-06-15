# Banker's Algorithm
import numpy as np 

# Gathering Data :
#--------------------------------------------------------
P=int(input("Enter the number of processes in system :"))
R=int(input("Enter the types of Resources available for system :"))

# Allocated Matrix   
print("Enter the allocated resources for each process (\"Allocated Matrix\") :")
LOL1=[]
for i in range(P):
    LOL1.append(list(map(int, input().split())))
allocated=np.array(LOL1)
   
# MAX Matrix   
print("Enter the maximum count of each resource used for each process (\"MAX Matrix\") :")
LOL2=[]
for i in range(P):
    LOL2.append(list(map(int, input().split())))
MAX=np.array(LOL2)

# Need Resources : (MAX-allocated)
Need=(MAX-allocated)

# Available Resources : (total-allocated  OR  given in question)
print("Are total Available resources given in this problem ? (press only \"YES/NO\")")
inp=input()
if inp=="YES":
    print("Then please enter each Resource's total instances in system :")
    total_res=list(map(int, input().split()))
    In_work=[] 
    for i in range(R):
        Alloc_sum=[sum(x) for x in zip(*allocated)]
        In_work.append( total_res[i] - Alloc_sum[i] )
else:  
    print("Then please enter each Resource's rest available instances in system :")
    In_work=list(map(int, input().split()))

# EXTRA: Comparing lists for lst1>=lst2 :
def lst_comp(lst1,lst2):
    lst=[]
    for i in range(len(lst1)):
        if lst1[i] >= lst2[i] :
            lst.append(True)
        else:
            lst.append(False)
    if all(lst)==True :
        return True
    else:
        return False
        
        
# PART-1) Safety Algorithm :
#***************************
def Safety_Algo(work,Need): 
    # Process exeution status list : Finish
    Finish=[]   # True=1 and False=0
    for i in range(P):
        Finish.append(0)
    sequence=[]
    while all(Finish)!=1 :
        c_var=work
        for i in range(P):
            if Finish[i]==0 and lst_comp(work,list(Need[i])) :
                Finish[i]=1
                work=list(map(sum, zip(work,list(allocated[i]))))
                sequence.append(i)
            else:
                continue
        if work==c_var :
            break

    if all(Finish)==1 :
        print("the System is in safe State and the safe sequence will be: ")
        for i in sequence:
            print("P[%d]"%i,end="       ")
    else:
        print("the System is not in safe State.")

print("Initially Available Resources :\n",In_work)  
print("Need Matrix :\n",Need)        
print("Do you want to check that, is the system in a safe state ? (press only \"YES/NO\")")
inp=input()
if inp=="YES":
    Safety_Algo(In_work,Need)
else:
    pass
   
# PART-2) Resource Request Algorithm :
#*************************************
print("\n\nAny Additional Resources Request ? (press only \"YES/NO\")")
inp=input()
if inp=="YES":
    while inp=="YES" :
        n=int(input("From how many Processes, request are coming ?\n"))
        for i in range(n):
            print("please enter the Process ID from which no-%d request is came :"%(i+1))
            p=int(input())
            req_lst=[]
            for j in range(R):
                print("How much instances need of Resource-%d in this request ?"%(j+1))
                req_lst.append(int(input()))
            if lst_comp(list(Need[p]),req_lst) :
                if lst_comp(In_work,req_lst) :
                    In_work=[b-a for (a,b) in zip(req_lst,In_work)]
                    allocated[p]+=np.array(req_lst)
                    Need[p]-=np.array(req_lst)
                    print("Now Available Resources :\n",In_work)
                    print("Need Matrix:\n",Need)
                else:
                    print("Required Resources are not available at this moment, please try again later.")
            else:
                print("Request Rejected, since the process has exceeded its maximum claim.")
                
            print("Do you want to check that, is the system in a safe state ? (press only \"YES/NO\")")
            inp1=input()
            if inp1=="YES":
                Safety_Algo(In_work,Need)
            else:
                pass
        print("\n\nAnother Request ? (press only \"YES/NO\")")
        inp=input()
else:
    pass