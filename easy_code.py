# 使用python实现冒泡排序
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


        
if __name__=="__main__":
    test_=[1,2,4,5,3]
    print(test_,bubble_sort(test_))
    
    

