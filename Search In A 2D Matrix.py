def BinarySearch(arr,low,high,target):
    while low <= high:
        mid = (high+low)//2
        if arr[mid] == target:
            return True
        elif arr[mid] > target:
            high = mid-1
        else:
            low = mid+1
    return False

def searchMatrix(matrix,target):
    n = len(matrix)
    m = len(matrix[0])
    row = n-1
    midcol = (m-1)//2
    rowlower = 0
    rowupper = row
    while row+1 > 2:
        mid = (rowlower+rowupper)//2
        if matrix[mid][midcol] == target:
            return True
        elif matrix[mid][midcol] > target:
            rowupper -= 1
        else:
            rowlower += 1
        row -= 1
    part1 = matrix[rowlower]
    part2 = matrix[rowupper]
    valid1 = BinarySearch(part1,0,len(part1)-1,target)
    valid2 = BinarySearch(part2,0,len(part2)-1,target)
    if valid1 or valid2:
        return True
    else:
        return False

    
        
    
    