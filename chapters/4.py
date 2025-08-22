def rec_sum(arr: list[int]) -> int:
    if len(arr) == 0:
        return 0
    return arr[0] + rec_sum(arr[1:])


def rec_len(arr: list[int]) -> int:
    if len(arr) == 0:
        return 0
    return 1 + rec_len(arr[1:])


def rec_max(arr: list[int]) -> int:
    if len(arr) == 1:
        return arr[0]
    return arr[0] if arr[0] > (m := rec_max(arr[1:])) else m


def rec_binary_search(arr: list, item):
    if len(arr) == 0:
        return None

    low = 0
    high = len(arr) - 1
    mid = low + high // 2
    guess = arr[mid]

    if guess == item:
        return mid

    if guess > item:
        return rec_binary_search(arr[:mid], item)
    else:
        result = rec_binary_search(arr[mid + 1:], item)
        return mid + result + 1 if result else None


def quick_sort(arr: list) -> list:
    if len(arr) < 2:
        return arr

    pivot = arr[0]
    less = [i for i in arr[1:] if i < pivot]
    greater = [i for i in arr[1:] if i >= pivot]

    return quick_sort(less) + [pivot] + quick_sort(greater)
