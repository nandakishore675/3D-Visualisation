import pandas as pd
import numpy as np
from array import *
import plotly.graph_objects as go


df=pd.read_csv('Data_without_Time.csv')


df1=df[(df['Depth']==0)]
df2=df[(df['Depth']==50)]
df3=df[(df['Depth']==100)]
df4=df[(df['Depth']==150)]
df5=df[(df['Depth']==200)]
df6=df[(df['Depth']==250)]
df7=df[(df['Depth']==300)]
df8=df[(df['Depth']==350)]
df9=df[(df['Depth']==400)]
df10=df[(df['Depth']==450)]
df11=df[(df['Depth']==500)]
df12=df[(df['Depth']==550)]
df13=df[(df['Depth']==600)]
df14=df[(df['Depth']==650)]
df15=df[(df['Depth']==700)]
df16=df[(df['Depth']==750)]
df17=df[(df['Depth']==800)]
df18=df[(df['Depth']==850)]
df19=df[(df['Depth']==900)]
df20=df[(df['Depth']==950)]
df21=df[(df['Depth']==1000)]
df22=df[(df['Depth']==1050)]
df23=df[(df['Depth']==1100)]
df24=df[(df['Depth']==1150)]
df25=df[(df['Depth']==1200)]
df26=df[(df['Depth']==1250)]
df27=df[(df['Depth']==1300)]
df28=df[(df['Depth']==1350)]
df29=df[(df['Depth']==1400)]
df30=df[(df['Depth']==1450)]
df31=df[(df['Depth']==1500)]



df1.to_csv('Data_at_Depth00.csv')
df2.to_csv('Data_at_Depth50.csv')
df3.to_csv('Data_at_Depth100.csv')
df4.to_csv('Data_at_Depth150.csv')
df5.to_csv('Data_at_Depth200.csv')
df6.to_csv('Data_at_Depth250.csv')
df7.to_csv('Data_at_Depth300.csv')
df8.to_csv('Data_at_Depth350.csv')
df9.to_csv('Data_at_Depth400.csv')
df10.to_csv('Data_at_Depth450.csv')
df11.to_csv('Data_at_Depth500.csv')
df12.to_csv('Data_at_Depth550.csv')
df13.to_csv('Data_at_Depth600.csv')
df14.to_csv('Data_at_Depth650.csv')
df15.to_csv('Data_at_Depth700.csv')
df16.to_csv('Data_at_Depth750.csv')
df17.to_csv('Data_at_Depth800.csv')
df18.to_csv('Data_at_Depth850.csv')
df19.to_csv('Data_at_Depth900.csv')
df20.to_csv('Data_at_Depth950.csv')
df21.to_csv('Data_at_Depth1000.csv')
df22.to_csv('Data_at_Depth1050.csv')
df23.to_csv('Data_at_Depth1100.csv')
df24.to_csv('Data_at_Depth1150.csv')
df25.to_csv('Data_at_Depth1200.csv')
df26.to_csv('Data_at_Depth1250.csv')
df27.to_csv('Data_at_Depth1300.csv')
df28.to_csv('Data_at_Depth1350.csv')
df29.to_csv('Data_at_Depth1400.csv')
df30.to_csv('Data_at_Depth1450.csv')
df31.to_csv('Data_at_Depth1500.csv')




df1=pd.read_csv('Data_at_Depth00.csv',usecols=["Latitude","Longitude","Temperature","Salinity","Density"])
df2=pd.read_csv('Data_at_Depth50.csv',usecols=["Latitude","Longitude","Temperature","Salinity","Density"])
df3=pd.read_csv('Data_at_Depth100.csv',usecols=["Latitude","Longitude","Temperature","Salinity","Density"])
df4=pd.read_csv('Data_at_Depth150.csv',usecols=["Latitude","Longitude","Temperature","Salinity","Density"])
df5=pd.read_csv('Data_at_Depth200.csv',usecols=["Latitude","Longitude","Temperature","Salinity","Density"])
df6=pd.read_csv('Data_at_Depth250.csv',usecols=["Latitude","Longitude","Temperature","Salinity","Density"])
df7=pd.read_csv('Data_at_Depth300.csv',usecols=["Latitude","Longitude","Temperature","Salinity","Density"])
df8=pd.read_csv('Data_at_Depth350.csv',usecols=["Latitude","Longitude","Temperature","Salinity","Density"])
df9=pd.read_csv('Data_at_Depth400.csv',usecols=["Latitude","Longitude","Temperature","Salinity","Density"])
df10=pd.read_csv('Data_at_Depth450.csv',usecols=["Latitude","Longitude","Temperature","Salinity","Density"])
df11=pd.read_csv('Data_at_Depth500.csv',usecols=["Latitude","Longitude","Temperature","Salinity","Density"])
df12=pd.read_csv('Data_at_Depth550.csv',usecols=["Latitude","Longitude","Temperature","Salinity","Density"])
df13=pd.read_csv('Data_at_Depth600.csv',usecols=["Latitude","Longitude","Temperature","Salinity","Density"])
df14=pd.read_csv('Data_at_Depth650.csv',usecols=["Latitude","Longitude","Temperature","Salinity","Density"])
df15=pd.read_csv('Data_at_Depth700.csv',usecols=["Latitude","Longitude","Temperature","Salinity","Density"])
df16=pd.read_csv('Data_at_Depth750.csv',usecols=["Latitude","Longitude","Temperature","Salinity","Density"])
df17=pd.read_csv('Data_at_Depth800.csv',usecols=["Latitude","Longitude","Temperature","Salinity","Density"])
df18=pd.read_csv('Data_at_Depth850.csv',usecols=["Latitude","Longitude","Temperature","Salinity","Density"])
df19=pd.read_csv('Data_at_Depth900.csv',usecols=["Latitude","Longitude","Temperature","Salinity","Density"])
df20=pd.read_csv('Data_at_Depth950.csv',usecols=["Latitude","Longitude","Temperature","Salinity","Density"])
df21=pd.read_csv('Data_at_Depth1000.csv',usecols=["Latitude","Longitude","Temperature","Salinity","Density"])
df22=pd.read_csv('Data_at_Depth1050.csv',usecols=["Latitude","Longitude","Temperature","Salinity","Density"])
df23=pd.read_csv('Data_at_Depth1100.csv',usecols=["Latitude","Longitude","Temperature","Salinity","Density"])
df24=pd.read_csv('Data_at_Depth1150.csv',usecols=["Latitude","Longitude","Temperature","Salinity","Density"])
df25=pd.read_csv('Data_at_Depth1200.csv',usecols=["Latitude","Longitude","Temperature","Salinity","Density"])
df26=pd.read_csv('Data_at_Depth1250.csv',usecols=["Latitude","Longitude","Temperature","Salinity","Density"])
df27=pd.read_csv('Data_at_Depth1300.csv',usecols=["Latitude","Longitude","Temperature","Salinity","Density"])
df28=pd.read_csv('Data_at_Depth1350.csv',usecols=["Latitude","Longitude","Temperature","Salinity","Density"])
df29=pd.read_csv('Data_at_Depth1400.csv',usecols=["Latitude","Longitude","Temperature","Salinity","Density"])
df30=pd.read_csv('Data_at_Depth1450.csv',usecols=["Latitude","Longitude","Temperature","Salinity","Density"])
df31=pd.read_csv('Data_at_Depth1500.csv',usecols=["Latitude","Longitude","Temperature","Salinity","Density"])






#df1.to_csv('Depth0_latlontempsalden_datawithmissingvalues.csv')
#df2.to_csv('Depth1000_latlontempsalden_datawithmissingvalues.csv')
#df3.to_csv('Depth500_latlontempsalden_datawithmissingvalues.csv')
#df4.to_csv('Depth250_latlontempsalden_datawithmissingvalues.csv')
#df5.to_csv('Depth350_latlontempsalden_datawithmissingvalues.csv')
#df6.to_csv('Depth750_latlontempsalden_datawithmissingvalues.csv')




df1.interpolate(method ='linear', limit_direction ='forward', inplace=True)

#df1.to_csv('Depth0_latlontempsalden_data.csv')

df2.interpolate(method ='linear', limit_direction ='forward', inplace=True)

#df2.to_csv('Depth1000_latlontempsalden_data.csv')

df3.interpolate(method ='linear', limit_direction ='forward', inplace=True)

#df3.to_csv('Depth500_latlontempsalden_data.csv')

df4.interpolate(method ='linear', limit_direction ='forward', inplace=True)

#df4.to_csv('Depth250_latlontempsalden_data.csv')

df5.interpolate(method ='linear', limit_direction ='forward', inplace=True)

#df5.to_csv('Depth350_latlontempsalden_data.csv')

df6.interpolate(method ='linear', limit_direction ='forward', inplace=True)

#df6.to_csv('Depth750_latlontempsalden_data.csv')
df7.interpolate(method ='linear', limit_direction ='forward', inplace=True)
df8.interpolate(method ='linear', limit_direction ='forward', inplace=True)
df9.interpolate(method ='linear', limit_direction ='forward', inplace=True)
df10.interpolate(method ='linear', limit_direction ='forward', inplace=True)
df11.interpolate(method ='linear', limit_direction ='forward', inplace=True)
df12.interpolate(method ='linear', limit_direction ='forward', inplace=True)
df13.interpolate(method ='linear', limit_direction ='forward', inplace=True)
df14.interpolate(method ='linear', limit_direction ='forward', inplace=True)
df15.interpolate(method ='linear', limit_direction ='forward', inplace=True)
df16.interpolate(method ='linear', limit_direction ='forward', inplace=True)
df17.interpolate(method ='linear', limit_direction ='forward', inplace=True)
df18.interpolate(method ='linear', limit_direction ='forward', inplace=True)
df19.interpolate(method ='linear', limit_direction ='forward', inplace=True)
df20.interpolate(method ='linear', limit_direction ='forward', inplace=True)
df21.interpolate(method ='linear', limit_direction ='forward', inplace=True)
df22.interpolate(method ='linear', limit_direction ='forward', inplace=True)
df23.interpolate(method ='linear', limit_direction ='forward', inplace=True)
df24.interpolate(method ='linear', limit_direction ='forward', inplace=True)
df25.interpolate(method ='linear', limit_direction ='forward', inplace=True)
df26.interpolate(method ='linear', limit_direction ='forward', inplace=True)
df27.interpolate(method ='linear', limit_direction ='forward', inplace=True)
df28.interpolate(method ='linear', limit_direction ='forward', inplace=True)
df29.interpolate(method ='linear', limit_direction ='forward', inplace=True)
df30.interpolate(method ='linear', limit_direction ='forward', inplace=True)
df31.interpolate(method ='linear', limit_direction ='forward', inplace=True)





	
arr1 = df1['Temperature'].to_numpy()
arr1.resize((10,10))
arr2 = df2['Temperature'].to_numpy()
arr2.resize((10,10))
arr3 = df3['Temperature'].to_numpy()
arr3.resize((10,10))
arr4 = df4['Temperature'].to_numpy()
arr4.resize((10,10))
arr5 = df5['Temperature'].to_numpy()
arr5.resize((10,10))
arr6 = df6['Temperature'].to_numpy()
arr6.resize((10,10))
arr7 = df7['Temperature'].to_numpy()
arr7.resize((10,10))
arr8 = df8['Temperature'].to_numpy()
arr8.resize((10,10))
arr9 = df9['Temperature'].to_numpy()
arr9.resize((10,10))
arr10 = df10['Temperature'].to_numpy()
arr10.resize((10,10))
arr11 = df11['Temperature'].to_numpy()
arr11.resize((10,10))
arr12 = df12['Temperature'].to_numpy()
arr12.resize((10,10))
arr13 = df13['Temperature'].to_numpy()
arr13.resize((10,10))
arr14 = df14['Temperature'].to_numpy()
arr14.resize((10,10))
arr15 = df15['Temperature'].to_numpy()
arr15.resize((10,10))
arr16 = df16['Temperature'].to_numpy()
arr16.resize((10,10))
arr17 = df17['Temperature'].to_numpy()
arr17.resize((10,10))
arr18 = df18['Temperature'].to_numpy()
arr18.resize((10,10))
arr19 = df19['Temperature'].to_numpy()
arr19.resize((10,10))
arr20 = df20['Temperature'].to_numpy()
arr20.resize((10,10))
arr21 = df21['Temperature'].to_numpy()
arr21.resize((10,10))
arr22 = df22['Temperature'].to_numpy()
arr22.resize((10,10))
arr23 = df23['Temperature'].to_numpy()
arr23.resize((10,10))
arr24 = df24['Temperature'].to_numpy()
arr24.resize((10,10))
arr25 = df25['Temperature'].to_numpy()
arr25.resize((10,10))
arr26 = df26['Temperature'].to_numpy()
arr26.resize((10,10))
arr27 = df27['Temperature'].to_numpy()
arr27.resize((10,10))
arr28 = df28['Temperature'].to_numpy()
arr28.resize((10,10))
arr29 = df29['Temperature'].to_numpy()
arr29.resize((10,10))
arr30 = df30['Temperature'].to_numpy()
arr30.resize((10,10))
arr31 = df31['Temperature'].to_numpy()
arr31.resize((10,10))


arrlat=df1['Latitude'].to_numpy()
arrlon=df1['Longitude'].to_numpy()
arrlat=np.unique(arrlat)
arrlon=np.unique(arrlon)


fig = go.Figure(data=[go.Surface(z=arr1, x=arrlat, y=arrlon),go.Surface(z=arr2, x=arrlat, y=arrlon),go.Surface(z=arr3, x=arrlat, y=arrlon),
go.Surface(z=arr4, x=arrlat, y=arrlon),go.Surface(z=arr5, x=arrlat, y=arrlon),go.Surface(z=arr6, x=arrlat, y=arrlon),
go.Surface(z=arr7, x=arrlat, y=arrlon),go.Surface(z=arr8, x=arrlat, y=arrlon),go.Surface(z=arr9, x=arrlat, y=arrlon),
go.Surface(z=arr10, x=arrlat, y=arrlon),
go.Surface(z=arr11, x=arrlat, y=arrlon),
go.Surface(z=arr12, x=arrlat, y=arrlon),
go.Surface(z=arr13, x=arrlat, y=arrlon),
go.Surface(z=arr14, x=arrlat, y=arrlon),
go.Surface(z=arr15, x=arrlat, y=arrlon),
go.Surface(z=arr16, x=arrlat, y=arrlon),
go.Surface(z=arr17, x=arrlat, y=arrlon),
go.Surface(z=arr18, x=arrlat, y=arrlon),
go.Surface(z=arr19, x=arrlat, y=arrlon),
go.Surface(z=arr20, x=arrlat, y=arrlon),
go.Surface(z=arr21, x=arrlat, y=arrlon),
go.Surface(z=arr22, x=arrlat, y=arrlon),
go.Surface(z=arr23, x=arrlat, y=arrlon),
go.Surface(z=arr24, x=arrlat, y=arrlon),
go.Surface(z=arr25, x=arrlat, y=arrlon),
go.Surface(z=arr26, x=arrlat, y=arrlon),
go.Surface(z=arr27, x=arrlat, y=arrlon),
go.Surface(z=arr28, x=arrlat, y=arrlon),
go.Surface(z=arr29, x=arrlat, y=arrlon),
go.Surface(z=arr30, x=arrlat, y=arrlon),
go.Surface(z=arr31, x=arrlat, y=arrlon),])
fig.update_layout(title='3D Visualization')
fig.update_layout(scene = dict(
                    xaxis_title='LATITUDE',
                    yaxis_title='LONGITUDE',
                    zaxis_title='TEMPERATURE'))
fig.show()












#arr2 = df3['Salinity'].to_numpy()

#print(arr2)

#arr2.resize((10,10))
#print(arr2)

#fig = go.Figure(data=[go.Surface(z=arr2, x=arrlat, y=arrlon)])
#fig.update_layout(title='3D Visualization')
#fig.update_layout(scene = dict(
#                   xaxis_title='LATITUDE',
#                  yaxis_title='LONGITUDE',
#                 zaxis_title='SALINITY'))
#fig.show()





#arr3 = df3['Density'].to_numpy()
#print(arr3)
#arr3.resize((10,10))
#print(arr3)

#fig = go.Figure(data=[go.Surface(z=arr3, x=arrlat, y=arrlon)])
#fig.update_layout(title='3D Visualization')
#fig.update_layout(scene = dict(
#                    xaxis_title='LATITUDE',
#                    yaxis_title='LONGITUDE',
#                    zaxis_title='DENSITY'))
#fig.show()