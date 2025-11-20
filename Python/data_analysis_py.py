# # import numpy as np

# # arr1=np.array([1,2,3,4,5])
# # print(arr1)
# # arr2=np.array([1,2,3,4,5])
# # arr3=np.array([1,2,3,4,5])
# # arr2.reshape((1,5))
# # #arr3.reshape((4,5))
# # print(arr1)
# # print(arr2)
# # print(arr3)
# # arr4=np.array([1,2,3,4,5])
# # arr4=np.array([10,20,30,40])
# # print(arr4)

# # ## To calc mean and standard deviation of data

# # data=np.array([1,2,3,4,5,6])

# # mean=np.mean(data)
# # print(mean)

# # dev=np.std(data)
# # print(dev)

# # normalised_data=(data-mean)/dev
# # print(normalised_data)

# # print(data>3)
# # print(data[data>3])
# # print(data[(data>3) & (data<6)])

# # import pandas as pd
# # data2=pd.read_csv('sample_sales_data.csv')
# # pd.DataFrame(data2)
# # print(data2)
# # print(data2.head(5))
# # print(data2['Total'])
# # print(data2.loc[6])
# # print(data2.at[6,'Total'])
# # print(data2.at[6,'Total']) 


# import pandas as pd
# data=pd.read_csv('sample_sales_data.csv')
# print(data.head(5)) # first 5 rows
# print(data.tail(5)) # last 5 rows
# print(data.describe()) 
# print(data.dtypes)

# # handlinfg missing values
# print(data.isnull().any()) # returns column names and its missing values
# print(data.isnull().sum()) # returns number of missing values from cols
# data.fillna(0) # missing vlaues is filled by 0 

# # To fill a column with a mean of that specific value 
# data['data_filled']=data['transactions'].fillna(data['transactions'].mean())

# # Renaming Cols
# data=data.rename(column={'transaction','meow'})
# # Changes data tpye of column
# data['new_meow']=data['meow'].fillna(data['meow'].mean()).astype(bool)

# # updating values
# data['new_values']=data['meow'].apply(lambda x:x**2)

# # Group By and aggregation
# data.groupby(['meow,values'])['meow'].agg(['mean','sum','avg'])

# import pandas as pd
# from io import StringIO
# # # Merging and joining dataframes

# # df1=pd.DataFrame({'keys':['A','B','C'],'Value1':[10,20,30]})
# # df2=pd.DataFrame({'keys':['A','E','B'],'Value2':[20,15,12]})

# # # Keys cols
# # data=pd.merge(df1,df2,on='keys',how="inner")
# # print(data)


# Data = '''
# {
#   "employee_name": "James",
#   "email": "james@gmail.com",
#   "job_profile": [
#     {
#       "title1": "Team Lead",
#       "experience": 5
#     },
#     {
#       "title2": "Sr. Developer",
#       "experience": 3
#     }
#   ]
# }
# '''
# # newD=pd.read_json(StringIO(Data))
# # print(newD)
# # newD.to_json() 
# url='https://www.w3schools.com/html/html_tables.asp'
# data=pd.read_html(url)
# print(data[0])
# data[0].to_csv('w3.csv',index='records')

# MATPLOTLIB
import matplotlib.pyplot as py

x=[1,2,3,4,5]
y=[1,4,9,16,25]

print(py.plot(x,y))