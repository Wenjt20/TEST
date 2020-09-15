#hanoi.py
count = 0
def display(src,dst):
    print("{}->{}".format(src,dst))
    
def hanoi(n,src,dst,mid):
    global count
    if n == 1:
        display(src,dst)
        count+=1
    else :
        hanoi(n-1,src,mid,dst)
        display(src,dst)
        count+=1
        hanoi(n-1,mid,dst,src)

hanoi(4,'A','C','B')
print(count)
    
