# 1-misol
list1 = [1, 3, 5]
list2 = [2, 4, 6]

def merge_lists(lst1, lst2):
    return lst1 + lst2

def sort_merged(lst):
    return sorted(lst)

def get_evens(lst):
    return [x for x in lst if x % 2 == 0]

def sum_evens(lst):
    return sum([x for x in lst if x % 2 == 0])

merged = merge_lists(list1, list2)
sorted_merged = sort_merged(merged)
evens = get_evens(merged)
sum_even_numbers = sum_evens(merged)

print(merged)
print(sorted_merged)
print(evens)
print(sum_even_numbers)

# 2-misol
values = [12, 5, 8, 19, 3, 15]

def find_min_max(lst):
    return min(lst), max(lst)

def diff_min_max(lst):
    return max(lst) - min(lst)

def index_max(lst):
    return lst.index(max(lst))

def remove_min(lst):
    lst2 = lst.copy()
    lst2.remove(min(lst2))
    return lst2

min_max = find_min_max(values)
difference = diff_min_max(values)
idx_max = index_max(values)
removed = remove_min(values)

print(min_max)
print(difference)
print(idx_max)
print(removed)

# 3-misol
words = ['apple', 'banana', 'cherry', 'date']

def reverse_list(lst):
    return lst[::-1]

def swap_ends(lst):
    lst2 = lst.copy()
    lst2[0], lst2[-1] = lst2[-1], lst2[0]
    return lst2

def sort_alpha(lst):
    return sorted(lst)

def length_list(lst):
    return len(lst)

rev = reverse_list(words)
swapped = swap_ends(words)
sorted_words = sort_alpha(words)
length = length_list(words)

print(rev)
print(swapped)
print(sorted_words)
print(length)
