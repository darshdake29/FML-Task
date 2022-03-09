# <<<<<<< HEAD
# this is task-3
a, b = 2, 3
def swapNum(a, b):
    """This function is for swapping the numbers"""
    a, b = b, a  # Swapping logic
    return a, b


ans = swapNum(a, b)
print(ans)

# =======
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
# >>>>>>> 960ba1d6860221f846c501bdaf94c558332897c4
