


def first_method():
    second_method()
    print("Hello, I am the First Method")

def second_method():
    third_method()
    print("Hello, I am the Second Method")
    
def third_method():
    fourth_method()
    print("Hello, I am the Third Method")
    
def fourth_method():
    print("Hello, I am the Fourth Method")


# In[2]:


first_method()


# In[3]:


#Program to calculate the factorial of a number
def factorial(n):
    if(n==0):
        return 1
    return n * factorial(n-1)


# In[9]:


factorial(1000)


# In[5]:


#Fibonacci
def fib(n):
    if(n==0):
        return 0
    if(n==1):
        return 1
    return fib(n-2) + fib(n-1)
    


# In[6]:


[fib(n) for n in range(15)]


# In[12]:


#Sum of digits of a number
def sum_of_digit(n):
    rem = n%10
    if(n//10==0):
        return rem
    return rem +  sum_of_digit(n//10)


# In[16]:


sum_of_digit(1234)


# In[17]:


#Power
def power(n, e):
    if (e==0):
        return 1
    return n * power(n, e-1)


# In[22]:


power(10,5)


# In[23]:


#GCD
def gcd(a,b):
    if a<b:
        a,b=b,a
    if(a%b)==0:
        return b
    return gcd(b,a%b)


# In[26]:


gcd(8,12)


# In[9]:


def binary(n):
    if(n/2==0):
        return str(n%2)
    return str(n%2)+binary(n//2)


# In[10]:


binary(10)


# In[4]:


#Total number of pathns in n, m grid
def paths_in_a_grid(n,m):
    if(n==1 or m==1):
        return 1
    return paths_in_a_grid(n,m-1)+paths_in_a_grid(n-1,m)


# In[3]:


paths_in_a_grid(3,4)


# In[25]:


def arrange_n_triangle(n):
    if(n==0):
        return 0
    if(n==1):
        return 1
    if(n==2):
        return 3
    return arrange_n_triangle(n-1)*(n+1)


# In[11]:


arrange_n_triangle(4)


# In[ ]:




