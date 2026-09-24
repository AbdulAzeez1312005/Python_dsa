def rotate(nums, k):
    for i in range(k):
        last = nums[-1]

        for j in range(len(nums) - 1, 0, -1):
            nums[j] = nums[j - 1]

        nums[0] = last


if __name__ == "__main__":
    nums = list(map(int, input().split()))
    k = int(input())

    rotate(nums, k)

    print(nums)
