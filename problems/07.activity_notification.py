def activityNotifications(expenditure, d):
    notifications = 0

    medians = sorted(expenditure[0:d])
    median_index = d//2
    is_even = d % 2 == 0

    def fix_medians(index):
        # print(medians)
        length = len(medians)

        new_index = -1
        left_boundry = 0
        right_boundry = length - 1
        while new_index == -1:
            pivot = left_boundry + (right_boundry - left_boundry) // 2
            if right_boundry - left_boundry <= 1:
                if expenditure[index] < medians[left_boundry]:
                    new_index = left_boundry
                else:
                    new_index = right_boundry if expenditure[index] < medians[right_boundry] else right_boundry + 1
            # print(f'left:{left_boundry}, pivot:{pivot}, right:{right_boundry}')
            # left
            if expenditure[index] < medians[pivot]:
                # print(f'<-left:{left_boundry}, pivot:{pivot}, right:{right_boundry}')
                if pivot == left_boundry:
                    new_index = left_boundry
                right_boundry = pivot
            # right
            elif expenditure[index] > medians[pivot]:
                # print(f'->left:{left_boundry}, pivot:{pivot}, right:{right_boundry}')
                if pivot == right_boundry:
                    new_index = right_boundry
                left_boundry = pivot
            else:
                new_index = pivot

        left = medians[0: new_index]
        right = medians[new_index:length]
        # print(left + [expenditure[index]] + right)

        return left + [expenditure[index]] + right

    for i in range(d, len(expenditure)):
        if is_even:
            median = (medians[median_index] + medians[median_index - 1])/2
        else:
            median = medians[median_index]
        if expenditure[i] >= 2 * median:
            notifications += 1
        if i != len(expenditure)-1:
            medians.pop(0)
            medians = fix_medians(i)

    return notifications


print(activityNotifications([2, 3, 4, 2, 3, 6, 8, 4, 5], 5))
print(activityNotifications([10, 20, 30, 40, 50], 3))
print(activityNotifications([1, 2, 3, 4, 4], 4))
# print(activityNotifications([1, 2, 3, 4, 4], 40001))
