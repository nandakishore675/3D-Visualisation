import pandas as pd
import numpy as np
import plotly.graph_objects as go


df=pd.read_csv('Data_without_Time.csv')

print(df.head())
print(df.tail())



df1=df[(df['Depth']==0)]

print(df1.head())
print(df1.tail(100))


df1.to_csv('Data_at_Depth00.csv')


#df2=pd.read_csv('Data_without_Time.csv',usecols=["Latitude","Longitude","Temperature"])


df3=pd.read_csv('Data_at_Depth00.csv',usecols=["Latitude","Longitude","Temperature","Salinity","Density"])

print(df3.head())


df3.to_csv('Depth0_latlontempsalden_datawithmissingvalues.csv')



df3.interpolate(method ='linear', limit_direction ='forward', inplace=True)

df3.to_csv('Depth0_latlontempsalden_data.csv')






m=df3['Latitude'].nunique()
n=df3['Latitude'].nunique()
print(df3['Latitude'].nunique())
print(df3['Longitude'].nunique())
print(m)
print(n)


arr = df3['Temperature'].to_numpy()
print(arr)
arr.resize((10,10))
print(arr)


arrlat=df3['Latitude'].to_numpy()
arrlon=df3['Longitude'].to_numpy()
arrlat=np.unique(arrlat)
arrlon=np.unique(arrlon)
print(arrlat)
print(arrlon)

fig = go.Figure(data=[go.Surface(z=arr, x=arrlat, y=arrlon)])
fig.update_layout(title='3D Visualization')
fig.update_layout(scene = dict(
                    xaxis_title='LATITUDE',
                    yaxis_title='LONGITUDE',
                    zaxis_title='TEMPERATURE'))
fig.show()












arr2 = df3['Salinity'].to_numpy()
print(arr2)
arr2.resize((10,10))
print(arr2)

fig = go.Figure(data=[go.Surface(z=arr2, x=arrlat, y=arrlon)])
fig.update_layout(title='3D Visualization')
fig.update_layout(scene = dict(
                    xaxis_title='LATITUDE',
                    yaxis_title='LONGITUDE',
                    zaxis_title='SALINITY'))
fig.show()





arr3 = df3['Density'].to_numpy()
print(arr3)
arr3.resize((10,10))
print(arr3)

fig = go.Figure(data=[go.Surface(z=arr3, x=arrlat, y=arrlon)])
fig.update_layout(title='3D Visualization')
fig.update_layout(scene = dict(
                    xaxis_title='LATITUDE',
                    yaxis_title='LONGITUDE',
                    zaxis_title='DENSITY'))
fig.show()