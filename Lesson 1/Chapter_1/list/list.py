import os

directory = os.listdir("/Users/defogui/Documents/")
print(directory)
directory.append("my_book")
print(directory)
directory.insert(1, "expert_dataEngineer")
print(directory)
directory.pop(2)
print(directory)
print(directory[1])
print(directory[6])


# for loop with list
names = ["Bob", "Jenn", "Genna", "Shayon"]

for name in names:

    if len(name) > 4:
        print(name)


# List comprehension

name_list = [name for name in names if len(name) > 5]
print(name_list)
