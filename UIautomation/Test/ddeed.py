# -*-coding=UTF-8-*-

# data=[('animal','bear'),('animal','duck'),('plant','cactus'),('vehicle','speed boat')]
# groups={}
# # for key,value in data:
# #     if key in groups:
# #         groups[key].append(value)
# #     else:
# #         groups[key]=[]
# #         groups[key].append(value)
# #
# # print groupse
# for key,value in data:
#     groups.setdefault(key,[]).append(value)
# keys={'a','b','c'}
# value=[]
# d=dict.fromkeys(keys,value)
# print d
array = [1,2,3,6,5,4]
for i in range(len(array)-1):
    for j in range(len(array)-1):
        if array[j] > array[j + 1]:
            array[j], array[j + 1] = array[j + 1], array[j]
print array