def dupfind(arr):
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i]==arr[j]:
                print(arr[i])
if __name__=="__main__":
    arr=list(map(int,input().split()))
    dupfind(arr)
