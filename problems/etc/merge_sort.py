def merge_sort(arr: list, start: int = 0, end: int | None = None) -> list:
    if end is None:
        end = len(arr)

    if end - start <= 1:
        return arr[start:end]

    mid = (start + end) // 2

    return merge(merge_sort(arr, start, mid), merge_sort(arr, mid, end))


def merge(left_list: list, right_list: list) -> list:
    sorted_list = []
    left_length = len(left_list)
    right_length = len(right_list)
    left = right = 0

    while left < left_length and right < right_length:
        if left_list[left] <= right_list[right]:
            sorted_list.append(left_list[left])
            left += 1
        else:
            sorted_list.append(right_list[right])
            right += 1

    sorted_list.extend(left_list[left:])
    sorted_list.extend(right_list[right:])

    return sorted_list


if __name__ == "__main__":
    data = [64, 34, 25, 12, 22, 11, 90]
    print("정렬 전:", data)
    sorted_data = merge_sort(data)
    print("정렬 후:", sorted_data)
