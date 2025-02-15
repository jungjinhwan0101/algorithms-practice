import random
import time


def insertion_sort(arr: list) -> list:
    n = len(arr)

    for i in range(1, n):
        position = i
        current_value = arr[i]

        while position > 0 and arr[position - 1] > current_value:
            arr[position] = arr[position - 1]
            position -= 1

        arr[position] = current_value

    return arr


def merge_sort(arr: list, start: int = 0, end: int | None = None) -> list:
    if end is None:
        end = len(arr)

    if end - start <= 1:
        return arr[start:end]

    mid = (start + end) // 2

    return merge(merge_sort(arr, start, mid), merge_sort(arr, mid, end))


def hybrid_sort(arr: list, start: int = 0, end: int | None = None) -> list:
    if end is None:
        end = len(arr)

    if (end - start) <= 10:
        return insertion_sort(arr[start:end])

    mid = (start + end) // 2

    return merge(hybrid_sort(arr, start, mid), hybrid_sort(arr, mid, end))


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


def measure_sorting_performance(array_size=10000, num_trials=5):
    results = {"Merge Sort": [], "Hybrid Sort": []}

    for _ in range(num_trials):
        # 랜덤 리스트 생성 (1~100 사이의 숫자)
        test_data = [random.randint(1, 100) for _ in range(array_size)]

        # 병합 정렬 성능 측정
        test_copy = test_data[:]  # 원본 보호
        start_time = time.time()
        merge_sort(test_copy)
        merge_sort_time = time.time() - start_time
        results["Merge Sort"].append(merge_sort_time)

        # 하이브리드(병합+삽입) 정렬 성능 측정
        test_copy = test_data[:]  # 원본 보호
        start_time = time.time()
        hybrid_sort(test_copy)
        builtin_sort_time = time.time() - start_time
        results["Hybrid Sort"].append(builtin_sort_time)

    # 평균 실행 시간 계산
    avg_merge_sort_time = sum(results["Merge Sort"]) / num_trials
    avg_hybrid_sort_time = sum(results["Hybrid Sort"]) / num_trials

    # 결과 출력
    print(f"평균 실행 시간 ({num_trials}회 반복, 배열 크기 {array_size})")
    print(f"Merge Sort: {avg_merge_sort_time:.6f} 초")
    print(f"Hybrid Sort: {avg_hybrid_sort_time:.6f} 초")


# 성능 테스트 실행
if __name__ == "__main__":
    measure_sorting_performance(array_size=100_000, num_trials=5)
