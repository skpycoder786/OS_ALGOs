print("\n*** FCFS DISK SHEDULING ALGORITHM ***")

# Required inputs
n=int(input("\nPlease enter the total number of cylinders required for servicing request : "))
print("\nNow enter the each Cylinder's no. which will be used for servicing request : ")
CR=list()   
for i in range(n):
    CR.append(int(input()))
head=int(input("\nPlease enter the current position of R/W Head : "))
direc=int(input("\nAlso enter the Moving direction of R/W Head (Enter '1' if it is moving towards larger cylinder numbers AND '0' if it is moving towards smaller cylinder numbers) : "))
print("\nPlease enter a valid range(\"Lower_limit Upper_limit\") in which R/W Head can be move : ",end="")
LL,UL=map(int,input().split())    

# Moving Space Lst
MSL=[head]
MSL.extend(CR) 

# Calculation of Total Head Moment
THM=0 
for i in range(n):
    THM+=abs(MSL[i+1]-MSL[i])
print("\nRESULT: The total head moment incurred (Using FCFS Disk Sheduling) = ",THM)
     
# Ploting line diagram :
from matplotlib import pyplot as plt
X_lst=MSL
Y_lst=[(i+1) for i in range(len(MSL))]
plt.plot(X_lst,Y_lst,color='blue',marker='o')
plt.xlabel('Cylinders(OR Tracks)')
plt.xlim(LL,UL)
plt.ylabel('Steps')
plt.title('FCFS Disk Scheduling')
plt.show()