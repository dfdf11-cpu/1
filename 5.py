def compare_strings_reverse_lexicographical(str1, str2):
    str1_reversed = str1[::-1]
    str2_reversed = str2[::-1]
    if str1_reversed > str2_reversed:
        return -1
    elif str1_reversed == str2_reversed:
        return 0
    else:
        return 1
string1 = (input())
string2 = (input())
result = compare_strings_reverse_lexicographical(string1, string2)
if result == -1:
    print(f"'{string1}' больше чем '{string2}' в обратном лексикографическом порядке")
elif result == 0:
    print(f"'{string1}' и '{string2}' равны в обратном лексикографическом порядке")
else:
    print(f"'{string1}' меньше чем '{string2}' в обратном лексикографическом порядке")
