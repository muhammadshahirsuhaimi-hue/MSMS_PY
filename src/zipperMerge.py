def zipper_merge_loop(str1, str2):
    result = []
    i, j = 0, 0
    
    # Alternate adding until one string runs out
    while i < len(str1) and j < len(str2):
        result.append(str1[i])
        result.append(str2[j])
        i += 1
        j += 1
        
    # Append whatever is left over from either string
    result.append(str1[i:])
    result.append(str2[j:])
    
    return "".join(result)
