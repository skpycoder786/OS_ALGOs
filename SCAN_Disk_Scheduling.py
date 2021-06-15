print("\n*** SCAN DISK SHEDULING ALGORITHM ***")

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

# Calculation of Total Head Moment      <CHANGE OCCURES>
THM=0
visit=[head]
L_lst=[LL]      # MSL = L_lst + R_lst
R_lst=[UL]
for i in CR:                
        if i < head :
            L_lst.append(i)
        else:
            R_lst.append(i)
R_lst.sort()
L_lst.sort()
L_lst.reverse()  
current=head
          
if direc==1 :
    for t in R_lst : 
        if len(CR)==0:
            break
        visit.append(t) 
        THM+=abs(current-t)
        if t in CR :
            CR.remove(t)
        current=t    
    for k in L_lst :
        if len(CR)==0:
            break
        visit.append(k) 
        THM+=abs(current-k)
        if k in CR :
            CR.remove(k)
        current=k        
        
else:
    for k in L_lst :
        if len(CR)==0:
            break
        visit.append(k) 
        THM+=abs(current-k)
        if k in CR :
            CR.remove(k)
        current=k    
    for t in R_lst : 
        if len(CR)==0:
            break
        visit.append(t) 
        THM+=abs(current-t)
        if t in CR :
            CR.remove(t)
        current=t  
        
print("\nRESULT: The total head moment incurred (Using SCAN Disk Sheduling) = ",THM)
    
# Ploting line diagram :
from matplotlib import pyplot as plt
X_lst=visit
Y_lst=[(i+1) for i in range(len(visit))]
plt.plot(X_lst,Y_lst,color='green',marker='o')
plt.xlabel('Cylinders(OR Tracks)')
plt.xlim(LL,UL)
plt.ylabel('Steps')
plt.title('SCAN Disk Scheduling')
plt.show()