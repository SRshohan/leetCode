def fruitsbasket(fruits):
    # Since I only can have 2 types of fruit that I can choose from
    # I can create a hashMap which would be typesOfTrees = { each_trees : [ how many on the list ]
    # Then check in the dictionary sequentially

    start = 0 # Initialize the start of the window and maximum length of fruit collection
    max_length = 0
    fruitsTree_count = {} #We use a hash map 'basket' to each types of fruit


    for index, value in enumerate(fruits): # Iterate through each fruits
        # If the type fruit already in the dictionary, this statement will increment
        if value in fruitsTree_count:
            fruitsTree_count[value] += 1
        else:
            fruitsTree_count[value] = 1 # If the key is not in the fruitscount dictionary, it will add a value

        while len(fruitsTree_count) > 2: # IF the dictionary has more than 2 keys
            fruit_to_start = fruits[start] # Identify the fruit and decrease it first window that it finds
            fruitsTree_count[fruit_to_start] -= 1


            if fruitsTree_count[fruit_to_start] == 0:
                del fruitsTree_count[fruit_to_start]

            start += 1

        max_length = max(max_length, index - start + 1)

    return max_length









fruits = [1,2,3,2,2]

print(fruitsbasket(fruits))
