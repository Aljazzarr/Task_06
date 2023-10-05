seperator = "=-" * 50
print("Question No.1")
lst = [30, 75, 9, 97, 50, -4, 70, 59]
# A
print(f"The Largest Number Is :{max(lst)}")
# B
smallestNumber = min(lst)
lst.remove(smallestNumber)
print(f"the lst without the smallest number is : {lst}")
# C
lst.sort()
print(f"the ranked list in ascending order is {lst}")
# D
print(lst[:4])
# ====================================================
print(seperator)
print("Question No.02")
main_lst = [["python", 3], [5, 7.8], ["python", 11], ["python",1]]
print((main_lst[0].count("python")) + (main_lst[1].count("python")) +
      main_lst[2].count("python") + (main_lst[0].count("python")))
# or by loop on the nested lists
python_repeat_times = 0
for nested_Lst in main_lst:
    if "python" in nested_Lst:
        python_repeat_times += 1

print(python_repeat_times)

# ====================================================
print(seperator)
print("Question No.03")
my_lst = ["I", "LOvE", "GAZa", "sKy", "GEEks"]
print(" ".join(my_lst).title())  # I Love Gaza Sky Geeks
# ====================================================
print(seperator)
print("Question No.04")
my_lst = [12, 3.8, "GSG", ["sKy", "zak"]]
my_list_clone = my_lst[:] # by slicing and indexing
print(my_list_clone)
# ====================================================
print(seperator)
print("Question No.05")
my_lst = ["GSG", "zakaria", 19, 9.8, "Omar"]
my_lst[2],my_lst[4]= my_lst[4],my_lst[2]

print(my_lst)
# ====================================================
print(seperator)
print("Question No.06")
nums = [33, 5.9, 6, -43, 9, 7, 39, 0, -40]
print(sum(nums))
# ====================================================
print(seperator)
print("Question No.07")
tuple1 = (4, 'python', 'GSG', [8, 3, 1])
tuple_of_9 = 9,
tuple1 = tuple1 + tuple_of_9
print(tuple1)
# ====================================================
print(seperator)
print("Question No.08")
tuple2 = ('Java', 'C++', 7.8)
newTuple = tuple1 + tuple2
print(newTuple)
# ====================================================
print(seperator)
print("Thank You")