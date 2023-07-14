# 0.0在数组下标i位置处插入元素e：注意下标可以为负数
def inseart(arr,i,e):
    """
        arr=[1,2,3,4,5,None]
        insert(arr,0,6)=>arr=[6,1,2,3,4,5]
        insert(arr,-1,6)=>arr=[1,2,3,4,5,6]
    """
    l=len(arr)
    # 判断边界条件（下标）
    if i==-1 or i==l-1:
        arr[-1]=e
    elif i==0 or i==-1*l:
        for j in range(l-1,0,-1):
            arr[j]=arr[j-1]
        arr[0]=e
    else:
        if i>0:
            for j in range(l-1,i-1,-1):
                arr[j]=arr[j-1]
            arr[i]=e
        else:
            for j in range(l-1,i+l-1,-1):
                arr[j]=arr[j-1]
            arr[i]=e
    # print(arr)
        
# 0.1找到数组中的中心索引
def find_mid_idx(arr):
    l=len(arr)
    # 边界条件
    if l<=2:
        return -1
    sum_left=arr[0]
    sum_right=sum(arr[2:])
    for i in range(1,l-1):
        if sum_left>sum_right:
            return -1
        elif sum_left==sum_right:
            return i
        else:
            sum_left+=arr[i]
            sum_right-=arr[i+1]
    return -1
    
        
        
        


# 1.使用python实现冒泡排序
# 实现思路：使用flag标志进行判断当前两个数字是否有序，有序就后移一个位置，否则就交换两个数字的位置
import copy
def bubble_sort(arr,mode):
    #两种方式，向前（把最小值往前移动）、向后（把最大值往后移动）
    arr=copy.deepcopy(arr)
   
    n=len(arr)
    lastExchangeIndex=0
    sortBorder=n-1
    for i in range(n):
        flag=True
        for j in range(sortBorder):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                flag=False
                lastExchangeIndex=j
        sortBorder=lastExchangeIndex
        if flag:
            break
    return arr

def selection_sort(arr):
    # 简单选择排序，每次选择两个交换位置
    arr=copy.deepcopy(arr)
    n=len(arr)
    for i in range(n-1):
        mark=i
        for j in range(i+1,n):
            if arr[j]<arr[mark]:
                mark=j
        if mark!=i:
            arr[i],arr[mark]=arr[mark],arr[i]
    return arr

# 2.对圆进行n等分
# 实现思路：找规律，注意边界情况，例如划分为1等分的时候
def split_circle(n):
    if n==1:
        return 0
    if n%2==0:
        return n//2
    return n

        
if __name__=="__main__":
    test_=[1,2,4,5,3]
    # print(test_,bubble_sort(test_))
    print(test_,selection_sort(test_))
    

