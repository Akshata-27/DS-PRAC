
import sys
import os
import pandas as pd

Base='D:/Datascience/Datascience/vkhcggit/practical-data-science/VKHCG'
sInputFileName='Good-or-Bad.csv'
sOutputFileName='Good-or-Bad-02.csv'
Company='01-Vermeulen'

if sys.platform == 'linux': 
    Base=os.path.expanduser('~') + 'VKHCG'
else:
    Base='D:/Datascience/Datascience/vkhcggit/practical-data-science/VKHCG'


print('Working Base :',Base, ' using ', sys.platform)

sFileDir=Base + '/' + Company + '/02-Assess/01-EDS/02-Python'
if not os.path.exists(sFileDir):
    os.makedirs(sFileDir)

sFileName=Base + '/' + Company + '/00-RawData/' + sInputFileName
print('Loading :',sFileName)
RawData=pd.read_csv(sFileName,header=0)

 
print('## Raw Data Values')  
 
print(RawData)
  
print('## Data Profile') 

print('Rows :',RawData.shape[0])
print('Columns :',RawData.shape[1])

sFileName=sFileDir + '/' + sInputFileName
RawData.to_csv(sFileName, index = False)

TestData=RawData.dropna(axis=1, how='any')
 
print('## Test Data Values')  

print(TestData)
 
print('## Data Profile') 

print('Rows :',TestData.shape[0])
print('Columns :',TestData.shape[1])

sFileName=sFileDir + '/' + sOutputFileName
TestData.to_csv(sFileName, index = False)

print('### Done!! #####################')

################################################################
