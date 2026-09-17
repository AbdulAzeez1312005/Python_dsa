def second_largest(arr):
    largest = arr[0]
    second = arr[0]

    for i in range(1, len(arr)):
        if arr[i] > largest:
            second = largest
            largest = arr[i]

        elif arr[i] > second and arr[i] != largest:
            second = arr[i]

    return second


if __name__ == "__main__":
    arr = list(map(int, input().split()))

    print(second_largest(arr))
