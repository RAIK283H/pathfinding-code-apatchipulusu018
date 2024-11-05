import config_data
import global_game_data
import graph_data



def stepOne(n):
    allOrderedNums = list(range(1, n + 1))
    directions = [-1] * n
    return allOrderedNums, directions

# def findLargestMobileVariable(n,perm,directions ):
#     largest_mobile_index = -1
#     for i in range(n):
        
#         target_index = i + directions[i] #basically index right before i
        
#         if 0 <= target_index < n and perm[i] > perm[target_index]: 
#         #makes sure target index is smaller than index n and checks to see value of n is larger than value of target to make sure its actually mobile
#             if largest_mobile_index == -1 or perm[i] > perm[largest_mobile_index]: #final check to see if the mobile int is the largest one
#                 largest_mobile_index = i
#     return largest_mobile_index

def findLargestMobileVariable(n, perm, directions):
    largest_mobile_index = -1
    for i in range(n):
        target_index = i + directions[i]
        
        # Check if `i` is mobile
        if 0 <= target_index < n and perm[i] > perm[target_index]:
            # Update if no mobile found yet or if this one is larger
            if largest_mobile_index == -1 or perm[i] > perm[largest_mobile_index]:
                largest_mobile_index = i
            elif perm[i] == perm[largest_mobile_index] and i > largest_mobile_index:
                # In case of tie, choose the rightmost mobile index
                largest_mobile_index = i

    return largest_mobile_index

def StepThreeSwap(perm, directions, largest_mobile_index):
    target_index = largest_mobile_index + directions[largest_mobile_index] #finds direction of the largest mobile index

    temp = perm[largest_mobile_index]
    perm[largest_mobile_index] = perm[target_index]
    perm[target_index] = temp

    temp_direction = directions[largest_mobile_index]
    directions[largest_mobile_index] = directions[target_index]
    directions[target_index] = temp_direction
    #perm[largest_mobile_index], perm[target_index] = perm[target_index], perm[largest_mobile_index]
    #directions[largest_mobile_index], directions[target_index] = directions[target_index], directions[largest_mobile_index]

def StepFourSwitch(perm, directions, mobile_value):
    n = len(perm)
    #mobile_value = perm[largest_mobile_index]
    for i in range(n):
        if perm[i] > mobile_value:
            directions[i] *= -1  # Reverse the direction
    return directions

def allPermutations(n):
    allOrderedNums = list(range(1, n + 1))
    directions = [-1] * n
    all_permutations = []
    largest_mobile_index = -30
    count = 0;

    print(f"All Ordered Nums: {allOrderedNums}, directions: {directions}")

    while largest_mobile_index != -1 and count < 5:
        largest_mobile_index = findLargestMobileVariable(n, allOrderedNums, directions)
        mobile_value = allOrderedNums[largest_mobile_index]
        # Print the largest mobile index at each stage
        print(f"Largest mobile index at this stage: {largest_mobile_index}")
        
        # Check if the largest mobile index is valid
        if largest_mobile_index == -1:
            break
        
        # Add current permutation to the list
        all_permutations.append(allOrderedNums.copy())
        print(f"Current permutation: {allOrderedNums}, directions: {directions}")

        # Swap and update directions
        StepThreeSwap(allOrderedNums, directions, largest_mobile_index)
        print(f"After StepThreeSwap: {allOrderedNums}, directions: {directions}")
        
        
        directions = StepFourSwitch(allOrderedNums, directions, mobile_value)
        print(f"After StepFourSwitch: {allOrderedNums}, directions: {directions}")
        
        # Increment count to limit to 5 permutations
        count += 1

    return all_permutations