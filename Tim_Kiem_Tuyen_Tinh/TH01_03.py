def linearsearch(arr,key):
    for i in range(len(arr)):
        if arr[i]==key:
            return i
    return -1
arr=['Bao','An','Dat','Duc','Hung','Phi','Vinh','Dung']
key='Phi'
res=linearsearch(arr,key)
print("vi tri tim thay thu i la: "+str(res))