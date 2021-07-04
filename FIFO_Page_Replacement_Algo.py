print("\n** FIFO Page Replacement Algorithm **\n")

# Gathering Inputs.......
f=int(input("Please enter the number of page frames which are used by System for storing process pages in main memory : "))
print("Now, enter the page reference string for processing : ")
ref_str=input()

# FIFO ALGO.......
page_lst=list(map(int, ref_str.split(",")))
n=len(page_lst)
Hit=0
Miss=0
frame_lst=[]    # Here 'None' is showing that current frame is empty.

print("\nProcessing Start.....")
pointer=0
for page in page_lst:
    if page in frame_lst :
        Hit+=1
        #CheckPoint-1: print(page)
        print("Frame Table Entries : ",frame_lst)
    else:
        Miss+=1
        if len(frame_lst) < f :     # Initial steps
            frame_lst.append(page) 
        else:
            frame_lst.remove(frame_lst[pointer])
            frame_lst.insert(pointer,page)
            pointer+=1
            if pointer == f :
                pointer=0
        print("Frame Table Entries : ",frame_lst)        
                
print("\nTotal number of hit = ",Hit)
print("Total number of miss = ",Miss)
HR=(Hit/n)*100
MR=(Miss/n)*100
print("\nHit Ratio = %.2f"%HR,"%")
print("Miss Ratio = %.2f"%MR,"%")                   