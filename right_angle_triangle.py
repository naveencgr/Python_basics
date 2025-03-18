n = 10
mid = n / 2
k = 0
for i in range(0, n + 1):
    if( i > mid):
        k = k - 1
    else: 
        k = i    
    
    print("*" * k)

z = 0
print("started")
k = n
for j in range(0, n):
    starts = ""
    for i in range(0, n):
       # print(f"{i} {mid-z} {mid+z}")
        if j <= mid:
            if( i >= mid - z and i <= mid + z ):
                starts += " *"
            else:
                starts += "  "
        elif j > mid:
            diff = j - mid
            if (i <= n -k or i >= k):
                starts += "  "
            else:
                starts += " *"               
    if(j <= mid ):
        z = z + 1
    else:
        k = k - 1    
    
    print(starts)        


for i in range(0, 10):
    print(" " * i * (2) + " *" * 2)    