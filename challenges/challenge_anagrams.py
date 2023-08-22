def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    middle = len(arr) // 2
    left = arr[:middle]
    right = arr[middle:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)


def merge(left, right):
    result = []
    left_index, right_index = 0, 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1

    result.extend(left[left_index:])
    result.extend(right[right_index:])
    return result


def is_anagram(first_string, second_string):
    def sorted_string(s):
        return "".join(merge_sort(list(s.lower())))

    if not first_string and not second_string:
        return "", "", False

    first_sorted = sorted_string(first_string)
    second_sorted = sorted_string(second_string)

    def char_count(s):
        count = {}
        for char in s:
            count[char] = count.get(char, 0) + 1
        return count

    first_count = char_count(first_sorted)
    second_count = char_count(second_sorted)

    return first_sorted, second_sorted, first_count == second_count


