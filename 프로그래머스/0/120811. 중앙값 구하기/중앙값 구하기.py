def solution(array):
    array.sort() #오름차순
    mid_index = len(array) // 2 
    return array[mid_index]