def bubble_sort(arr: list[int]):
    n = len(arr)

    for i in range(n - 1):
        j = n - 1
        swapped = False

        while j > i:
            if arr[j] < arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
                swapped = True
            j -= 1

        if not swapped:
            break

    return arr


if __name__ == "__main__":
    data = [64, 34, 25, 12, 22, 11, 90]
    print("정렬 전:", data)
    sorted_data = bubble_sort(data)
    print("정렬 후:", sorted_data)
