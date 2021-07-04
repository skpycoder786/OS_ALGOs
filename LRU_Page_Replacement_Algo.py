print("\n** LRU Page Replacement Algorithm **\n")

# Gathering Inputs.......
f=int(input("Please enter the number of page frames which are used by System for storing process pages in main memory : "))
print("Now, enter the page reference string for processing : ")
ref_str=input()

# LRU ALGO.......
page_lst=list(map(int, ref_str.split(",")))
n=len(page_lst)
Hit=0
Miss=0
frame_lst=[]    # Here 'None' is showing that current frame is empty.

print("\nProcessing Start.....")
for i in range(n):
    page=page_lst[i]
    if page in frame_lst :
        Hit+=1
        #CheckPoint-1: print(page_lst[i])
        print("Frame Table Entries : ",frame_lst)
    else:
        Miss+=1
        if len(frame_lst) < f :     # Initial steps
            frame_lst.append(page)
        else:
            status=[]
            temp=page_lst[:i]
            temp.reverse()
            for t in frame_lst:
                for p in temp:
                    if p==t:
                        status.append(temp.index(p))
                        break
                    else:
                        continue
            #CheckPoint-2: print("This is status : ",status)            
            LRU_page=temp[max(status)]
            LRU_index=frame_lst.index(LRU_page)
            frame_lst.remove(frame_lst[LRU_index])
            frame_lst.insert(LRU_index,page)
        print("Frame Table Entries : ",frame_lst)
                
print("\nTotal number of hit = ",Hit)
print("Total number of miss = ",Miss)
HR=(Hit/n)*100
MR=(Miss/n)*100
print("\nHit Ratio = %.2f"%HR,"%")
print("Miss Ratio = %.2f"%MR,"%")                   