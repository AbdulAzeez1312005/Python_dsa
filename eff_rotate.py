def reverse(nums, start, end):
    while start < end:
        nums[start], nums[end] = nums[end], nums[start]

        start += 1
        end -= 1


def rotate(nums, k):
    n = len(nums)

    k = k % n

    # Reverse entire array
    reverse(nums, 0, n - 1)

    # Reverse first k elements
    reverse(nums, 0, k - 1)

    # Reverse remaining elements
    reverse(nums, k, n - 1)


if __name__ == "__main__":
    nums = list(map(int, input().split()))
    k = int(input())

    rotate(nums, k)

    print(nums)
