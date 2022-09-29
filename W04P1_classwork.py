# -*- coding: utf-8 -*-
"""
Created on Thu Sep 22 11:32:51 2022

@author: Priyansh Desai
"""

import numpy as np
i = np.arange(0,20)
array2d = np.arange(20).reshape(4,5)
print(array2d)
rng = np.random.default_rng(0)
print(rng.random()) 
rand_array = rng.random((5,4))
print(rand_array)
array2d[1] = rand_array[:,2]
array2d = array2d.astype(float)
array2d[:,0] += rand_array[3,:]
print(array2d)
print(array2d.dtype)
value_range = (np.min(array2d), np.max(array2d))
print(value_range)
std = np.std(array2d)
print(std)
mean_rows = array2d.mean(axis = 1)
print(mean_rows)
sum_cols = array2d.sum(axis = 0)
print(sum_cols)
matrix_product = np.matmul(array2d, rand_array)
print(matrix_product)
array2d_T = array2d.transpose()
print(array2d_T)
concated = np.concatenate((array2d_T,rand_array),axis = 1)
print(concated)
stacked = np.stack((array2d_T, rand_array), axis = 0)
print(stacked)
print(stacked.shape)
stacked2 = np.stack((array2d_T, rand_array), axis = 2)
print(stacked2)
print(stacked2.shape)
flipped = np.flip(rand_array,1)
print(flipped)
names = ['Tokyo','Jakarta','Delhi','Manila','Sao Paulo','Seoul','Mumbai','Shanghai','Mexico City','Guangzhou',
         'Cairo','Beijing','New York','Kolkata','Moscow','Bangkok','Dhaka','Buenos Aires']
lats = [35.6839,-6.2146,28.6667,14.6,-23.5504,37.56,19.0758,31.1667,19.4333,23.1288,30.0444,
        39.904,40.6943,22.5727,55.7558,13.75,23.7289,-34.5997]
longs = [139.7744,106.8451,77.2167,120.9833,-46.6339,126.99,72.8775,121.4667,-99.1333,
         113.259,31.2358,116.4075,-73.9249,88.3639,37.6178,100.5167,90.3944,-58.3819]
#arr = []
'''
for i in range(len(lats)):
    arr += [(names[i],lats[i],longs[i])]
city_loc = np.array(arr, dtype = [('name','U16'),('lat','f4'),('long','f4')])
print(city_loc)
'''  
st_ar = list(map(lambda x, y, z:(x,y,z), names, lats, longs))
city_loc = np.array(st_ar, dtype = [('name','U16'),('lat','f4'),('long','f4')])
print(city_loc)

southern = city_loc[city_loc['lat'] < 0]
print(southern)


southwest = city_loc[(city_loc['lat'] < 0) & (city_loc['long'] < 0)]
print(southwest)


