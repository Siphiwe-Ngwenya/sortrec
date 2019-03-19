def quick_sort(items, index=-1):

    len_i = len(items)

    if len_i <= 1:
        #runing a test to c if the array is not empty
        return items

    pivot = items[index]# finding a number in the array to compare all the numbers
    #in the array too starting from the index -1 and assigning that item to pivot
    small = [] #innitialising an empty array
    large = [] #innitialising an empty array
    dup = [] #innitialising an empty array
    for i in items:
        if i < pivot:#comparing if the item is less than the pivot
            small.append(i) #if condition is true we are allocating item into array small
        elif i > pivot:#comparingif the item is greater than the pivot
            large.append(i)#if the condition is true we allocate the intem into array large
        elif i == pivot:#comparing if item is equal to pivot
            dup.append(i)#if the condition is allocate item into dup array

    small = quick_sort(small)#sorting array small
    large = quick_sort(large)#sorting array large

    return small + dup + large#adding the three arrays together


def bubble_sort(items):

    out = items.copy() #innitialising out which is a copy of item array
    for i in range(len(out)):#iterating through the array from the front
        for j in range(len(out)-1-i):#iterating through the array from the back
            if out[j] > out[j+1]:
                out[j], out[j+1] = out[j+1], out[j]

    return out

def merge_sort(x):
    for a in range(len(x)):#iterating through the array to get its size
        for b in range(len(x)-1-a):#iterating through array in reverse
            if x[b]>x[b+1]:
                x[b],x[b+1]=x[b+1],x[b]
    return x
