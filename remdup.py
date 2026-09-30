def remove_duplicates(arr):
    result = []

    for i in range(len(arr)):
        found = False

        for j in range(len(result)):
            if arr[i] == result[j]:
                found = True
                break

        if found == False:
            result.append(arr[i])

    return result


if __name__ == "__main__":
    arr = list(map(int, input().split()))

    result = remove_duplicates(arr)

    print(result)
