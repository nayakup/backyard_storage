#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sys
from array import  *


# In[2]:


#Create an Array and Traverse it

price_list = array('i', [12,13,15,23,45,70,34,50])
print(f"Size of array {sys.getsizeof(price_list)}")
print(f"Size of list {sys.getsizeof([12,13,15,23,45,70,34,50])}")


for i in price_list:
    print(i)


# In[3]:


#Access Individual elements of array O(1)
price_list[0]


# In[4]:


#Append value to array O(1)
price_list.append(100)
price_list


# In[5]:


#Insert value to array O(N)
price_list.insert(0,-1)
price_list.insert(5,-2)
price_list


# In[6]:


#Extend Python array O(N), N is the length of the iterable to be appended to the existing list 
price_list.extend([101,102,103,104,105])
price_list


# In[7]:


#Add items to the array using another array (Same as Extend)
temp_list = [106,107,108]
price_list.fromlist(temp_list)
price_list


# In[8]:


#Remove an array element (First Occurence) : O(N)
price_list.remove(107)
price_list


# In[9]:


#Remove last element O(1)
price_list.pop()
price_list


# In[ ]:





# In[10]:


#Reverse
price_list.reverse()
price_list


# In[11]:


price_list.reverse()
price_list


# In[12]:


#COunt occurence
price_list.count(-2)


# In[13]:


#Transpose a Matrix
x = [[1,2,3],
     [4,5,6],
     [7,8,9]]

print([[x[j][i] for j in range(len(x))] for i in range(len(x[0]))])


# In[14]:


#Matrix Traversal
print([[f"{i},{j}" for j in range(3)] for i in range(3)])


# In[15]:


#All Combinations
countries=['India', 'France', 'Germany', 'United Kingdom']
capitols=['New Delhi', 'Paris', 'Berlin', 'London']

print([(country, capitol) for country in countries for capitol in capitols])


# In[16]:


#ZIP achived in list comprehension
countries=['India', 'France', 'Germany', 'United Kingdom']
capitols=['New Delhi', 'Paris', 'Berlin', 'London']

print([(countries[i], capitols[j]) for i in range(len(countries)) for j in range(len(capitols)) if i==j])


# In[17]:


#2D Array Creation
import numpy as np
twoDArray = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
twoDArray


# In[18]:


#Add Column , O(MN)
newtwoDArray1 = np.insert(twoDArray, 0, [[-1,-1,-1,-1]], axis=1)
newtwoDArray1


# In[19]:


#Add Row, O(MN)
newtwoDArray2 = np.insert(twoDArray, 0, [[-1,-1,-1,-1]], axis=0)
newtwoDArray2


# In[20]:


#Add Row at the end use append (O(MN)
newtwoDArray3 = np.append(twoDArray, [[-1,-1,-1,-1]], axis=0)
newtwoDArray3


# In[21]:


#Add Column at the end use append  (Need to check)
newtwoDArray4= np.append(twoDArray, [[-1,-1,-1,-1]], axis=1)
newtwoDArray4


# In[ ]:


# Accessing element
def accessElement2D(array, row, column):
    assert row < len(array), "Row argument should be less then the number of Rows in the input array"
    assert column < len(array[0]), "Column argument should be less then the number of Columns in the input array"
    return array[row][column]


# In[ ]:


print(twoDArray)
accessElement2D(twoDArray,3,3)


# In[ ]:





# #### One Dimensional Array Complexities

# ![1D Array Complexities](https://raw.githubusercontent.com/upnayak/learning/main/data_structures/resource/1D%20Array.png)
# 

# #### Two Dimensional Array Complexities

# ![1D Array Complexities](https://raw.githubusercontent.com/upnayak/learning/main/data_structures/resource/2D%20Array.png)
# 

# In[ ]:





# In[ ]:


#Question 1 - Missing Number [1 100]
my_list = [1,2,3,4,5,6,7,9,10]
def missing(list,n):
    sum1 = (n*(n+1))/2
    sum2 = sum(list)
    return (sum1-sum2)


# In[ ]:


missing(my_list,10)


# In[ ]:


my_list = [1,4,2,3,7,5]

def find_pairs(list, n):
    try:
        list = sorted(list)
        start = 0
        end = 1
        results = []
        while(start<len(list)):
            sum = list[start]+list[end]
            print(f"Start = {start}, End = {end}, sum = {sum}")
            if(sum==n):
                results.append((list[start], list[end]))
                end += 1
            elif(sum<n):
                end += 1
            else:
                start += 1
                if(end<len(list)-1):
                    end = start + 1
            
        return results
    except Exception as e:
        print(e)
        print(f"Start = {start}, End = {end}")
            


# In[ ]:


print(find_pairs(my_list, 5))


# In[ ]:


def linear_search(list, n):
    for i in range(len(myArray)):
        if(list[i] == n):
            print(i)


# In[ ]:


myArray = [1,4,2,6,3,6,9,2,5]

linear_search(myArray, 6)


# In[ ]:


def max_product(list):
    max_product = -1
    for i in range(len(list)):
        for j in range(len(list)):
            product = list[i]*list[j]
#             print(f"{product}>{max_product} = {product>max_product}")
            if((i!=j) & (product>max_product)):
                max_product = product
#                 print(f"{max_product}")
                
    return max_product


# In[ ]:


mylist = [1,5,2,6,3,7,1,0]
print(max_product(mylist))


# In[ ]:


def isUnique(list):
    mylist = []
    for i in list:
        if i in mylist:
            print(i)
            return False
        else:
            mylist.append(i)
    return True


# In[ ]:


isUnique([1,4,2,5])


# In[ ]:


isUnique([1,7,4,2,7,5])


# In[ ]:


#Permutations
def is_anagram(str1, str2):
    list1 = list(str1)
    for i in str2:
        if i in list1:
            list1.remove(i)
        else:
            return False
    return True
            


# In[ ]:


print(is_anagram('keep','peek'))
print(is_anagram('mail','liam'))
print(is_anagram('feet','feat'))
print(is_anagram('harte','heart'))
print(is_anagram('got','goot'))


# In[ ]:


matrix = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
matrix


# In[ ]:


matrix1 = np.array([[1,2,3],[4,5,6],[7,8,9]])
matrix1


# In[ ]:


def transpose(matrix):
    return np.array([[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))])


# In[ ]:


print(transpose(matrix))
print(transpose(matrix1))


# In[ ]:


def rotate_90degrees(matrix):
    n = len(matrix)
    for layer in range(n//2):
        first = layer
        last = n-layer-1
        for i in range(first, last):


# In[ ]:




