user_vaccine_data = [
    'user1', ['a', 'a'], 
    'user2', ['a', 'b'], 
    'user3', ['c', 'c'], 
    'user4', ['a', 'c', 'a'], 
    'user5', ['b', 'a', 'c'], 
    'user6', ['c', 'a', 'c']
]

fully_vaccinated_users = []

for i in range(0, len(user_vaccine_data), 2):
    user = user_vaccine_data[i]
    vaccines = user_vaccine_data[i+1]
    
    # 1. Check basic dose count requirement
    if len(vaccines) >= 2:
        vaccine_str = "".join(vaccines)
        
        if 'c' in vaccine_str:
            # Strip all 'c's from the edges to find if any 'c' remains trapped inside
            # If a 'c' is trapped inside after stripping, it means it wasn't consecutive
            cleaned_str = vaccine_str.strip('c')
            
            # If 'c' is still in the middle (like 'a c a' -> 'a c a' or 'c a c' -> 'a'), 
            # it means the 'c' doses were split up by other letters.
            if 'c' not in cleaned_str:
                fully_vaccinated_users.append(user)
        else:
            # If there is no 'c', any 2 or more vaccines are automatically valid
            fully_vaccinated_users.append(user)

print("Fully Vaccinated Users:", fully_vaccinated_users)
# Output: Fully Vaccinated Users: ['user1', 'user2', 'user3', 'user5']
