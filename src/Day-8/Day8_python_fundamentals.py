import numpy as np
a = np.array([[1, 2, 3],
              [4, 5, 6]])
b = np.array([10, 20, 30])
result = a + b
print(result)

#Numpy array creation
import numpy as np
a = np.array([])
b = np.array([1, 2, 3])
c = np.array([[4,5,6],[7,8,9]])
d = np.array([[4,2,5],[8,3,2],[2,0,6]])
print(a,"\n",b,"\n",c,"\n",d)
              
#Vectorized vs loop example
import numpy as np
arr=np.random.rand(10)
#Vectorized
squared=arr**2
print("Squared elements are:\n",squared)

#reshaping arrays
import numpy as np
arr=np.random.rand(12)
reshaped=arr.reshape(3,4)
print("Reshaped array:\n",reshaped)
a=np.array([1,2])
b=np.array([3,4])
vstacked=np.vstack((a,b))
print("Vertically stacked array:\n",vstacked)
hstacked=np.hstack((a,b))   
print("Horizontally stacked array:\n",hstacked)

#Statistical function in numpy
import numpy as np
data = np.array([[10, 20, 30],
                 [40, 50, 60]])
print(np.mean(data))
print(np.mean(data, axis=0))
print(np.mean(data,axis=1))

#Linear algebra
import numpy as np
A=np.array([[1,2],[3,4]])
B=np.array([[5,6],[7,8]])
print(np.dot(A,B))

#linespace
import numpy as np
arr=np.linspace(0,3,6)
print(arr)

arr=np.random.rand(2,2)
print(arr)

arr=np.random.uniform(20,30,size=(2,2))
print(arr)

arr=np.random.randint(1,10,size=(3,3))
print(arr)
print(arr.shape)    

arr=np.array([1.2,2.8,-3.7])
print(np.floor(arr))

arr=np.array([1.2,2.8,-3.7])
print(np.ceil(arr))
print("truncated values:\n",np.trunc(arr))
print("rounded values:\n",np.round(arr))

#Task-1
import numpy as np
scores = np.random.randint(50, 101, size=(5, 3))
subject_mean = scores.mean(axis=0)
centered_scores = scores - subject_mean
print("Original Scores:\n", scores)
print("Subject-wise Mean:\n", subject_mean)
print("Centered Scores:\n", centered_scores)

#Task-2
import numpy as np
data=np.arange(24)
reshaped=data.reshape(4,3,2)
transposed=reshaped.transpose(1,0,2)
print("Final shape:\n",transposed.shape)
print("Final array:\n",transposed)


