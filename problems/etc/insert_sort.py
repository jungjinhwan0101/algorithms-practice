def insertion_sort(arr: list[int]):
    n = len(arr)
    for i in range(1, n - 1):
        position = i
        current_value = arr[i]

        while position > 0 and arr[position - 1] > current_value:
            arr[position] = arr[position - 1]
            position -= 1

        arr[position] = current_value

    return arr


if __name__ == "__main__":
    data = [64, 34, 25, 12, 22, 11, 90]
    print("정렬 전:", data)
    sorted_data = insertion_sort(data)
    print("정렬 후:", sorted_data)
