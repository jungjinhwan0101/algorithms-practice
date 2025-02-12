input_value = [3, 1, 4, 1, 5]


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


assert bubble_sort(input_value) == [1, 1, 3, 4, 5]
