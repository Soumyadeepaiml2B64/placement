def remove_empty_strings(lst):
    return [s for s in lst if s != ""]

sample_list = ["apple", "", "banana", "", "cherry", ""]
result = remove_empty_strings(sample_list)
print(result)  