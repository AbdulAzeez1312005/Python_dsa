def max_one(arr):
    count=0
    maxi=0
    for i in range(0,len(arr)):
        if arr[i]==1:
            count+=1
            if count>maxi:
                maxi=count
        else:
            count=0
        
    return maxi

if __name__ =="__main__":
    arr=list(map(int,input().split()))
    print(max_one(arr))
