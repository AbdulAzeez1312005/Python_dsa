def findlar(arr):
    largest=arr[0]
    for i in range(1,len(arr)):
        if arr[i] > largest:
            largest=arr[i]
    return largest
if __name__=="__main__":
    arr=list(map(int,input().split()))
    print(findlar(arr))

