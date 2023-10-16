print("Enter The No. Of Frames: ",end="")
capacity = int(input())
f,fault,top,pf = [],0,0,'No'
print("Enter The Reference Page: ",end="")
s = list(map(int,input().strip().split()))
print("\nString|Frame →\t",end='')
for i in range(capacity):
    print(i,end=' ')
print("Fault\n   ↓\n")
for i in s:
    if i not in f:
        if len(f)<capacity:
            f.append(i)
        else:
            f[top] = i
            top = (top+1)%capacity
        fault += 1
        pf = 'Yes'
    else: