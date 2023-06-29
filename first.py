def find_leaders(arr):
    leaders = []
    current_leader = arr[-1]  # Assume the last element as the leader
    leaders.append(current_leader)

    # Iterate the array from right to left
    for i in range(len(arr)-2, -1, -1):
        if arr[i] > current_leader:
            current_leader = arr[i]
            leaders.append(current_leader)

    return leaders[::-1]  # Reverse the leaders list to get the correct order

# Test the function
array_length = int(input("Enter the number of elements in the array: "))
array = []
for _ in range(array_length):
    element = int(input("Enter an element: "))
    array.append(element)

result = find_leaders(array)
print("The leaders in the array are:", result)
