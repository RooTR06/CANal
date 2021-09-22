import numpy as np 
import pandas as pd

filename= 'CANdata.log'

#Handle the Raw Data
RawData=pd.read_csv(filename, header = None)
RawData.columns=['Time']
#Divide Data to 3 main Columns
RawData['Data'] = RawData['Time'].str.split(' ').str[2]
RawData['Connection'] = RawData['Time'].str.split(' ').str[1]
RawData['Time'] = RawData['Time'].str.split(' ').str[0]
#Seperate Can Data into ID&param
RawData['canID']=RawData['Data'].str.extract('^(.+?)#')
RawData['Parameters']=RawData['Data'].str.extract('#(.+)')
RawData['Time'] = RawData['Time'].str.strip('[^("]|[)"$]')

#print(df)
print(RawData)