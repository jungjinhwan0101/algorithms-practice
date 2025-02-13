def selection_sort(arr: list[int]):
    n = len(arr)

    for i in range(n - 1):
        min_index = i
        # print(f"[{i=}]")
        for j in range(i, n):
            # print(f"{j=}")
            if arr[j] < arr[min_index]:
                min_index = j
        # print()
        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr


if __name__ == "__main__":
    data = [64, 34, 25, 12, 22, 11, 90]
    print("정렬 전:", data)
    sorted_data = selection_sort(data)
    print("정렬 후:", sorted_data)
