nums = [4,1,9,22,15,7]
# 1. 최솟값 찾기
    # (1) 함수 이용
    # print(min(nums))

    # (2) for문
    # min_num = nums[0]
    # for idx,num in enumerate(nums) :
    #     if num <= min_num:
    #         min_num = num
    #         min_idx = idx


# 선택정렬, 삽입정렬, 버블정렬, 퀵정렬, 병합정렬 -> 기초적인 정렬 알고리즘으로 알아두기
    # 선택 정렬, 삽입정렬, 버블정렬은 효율성이 낮다.
    # 퀵 정렬 : 피봇이라는 기준을 세워놓고, 해당 기준에서 범위를 나누어 값을 비교 -> 효율성 높음


# 선택정렬 : 리스트 내 가장 최솟값을 맨 앞으로 위치 -> 최솟값을 제외한 범위에서 가장 작은 값을 두번째에 위치 -> ... 

# n_nums = len(nums)
# for idx in range(n_nums):
#     min_idx = idx
#     for i in range(idx+1, n_nums):
#         if nums[min_idx] >= nums[i]:
#             min_idx = i
#     temp = nums[min_idx]
#     nums[min_idx] = nums[idx]
#     nums[idx] = temp
# print(nums)        

# 버블 정렬 : 인접한 두 수간의 대소를 비교하여 정렬

# n_nums = len(nums)
# for rep_cnt in range(n_nums):
#     for idx in range(n_nums-(rep_cnt+1)):
#         if nums[idx] >= nums[idx+1]:
#             temp = nums[idx+1]
#             nums[idx+1] = nums[idx]
#             nums[idx] = temp
# print(nums)

# 삽입정렬 : 리스트 내 이전 N-1개의 수와 N번째 수를 비교하여, N번째 수를 이전 N-1개의 수 중에서 정해진 위치에 삽입하여 정렬(N=1,2,...)

n_nums = len(nums)
# for idx in range(1,n_nums):
#     for i in range(idx):
#         if nums[idx] <= nums[idx-(i+1)]:
#             temp = nums[idx-(i+1)]
#             nums[idx-(i+1)] = nums[idx]
#             nums[idx] = temp

for i in range(1, n_nums):
    for j in range(i, 0, -1): 
        if nums[j] < nums[j-1]:
            nums[j], nums[j-1] = nums[j-1], nums[j]
        else:
            break
print(nums)

        # nums[idx-(i+1)] = nums[idx]
        # nums[idx] = temp





# 병합정렬 : 리스트를 2개 수로 나누어 