# This is task-2
old_list = [1, 2, 3, 4, 5]

def addTwo(old_list):
    """This function will add 2 to each element of old_list"""
    return list(map(lambda x : x + 2, old_list)) # logic to add 2 to each element


new_list = addTwo(old_list)
print("old_list which was initialized", end=" ")
print(old_list)
print("new_list after adding two to each element", end=" ")
print(new_list)