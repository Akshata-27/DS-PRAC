import sys
import os
import pandas as pd
import sqlite3 as sq

sDatabaseName='D:/Datascience/Datascience/vkhcggit/practical-data-science/VKHCG\\99-DW\\datawarehouse.db'
conn1 = sq.connect(sDatabaseName)
sSQL="SELECT PersonID,\
       Weight\
  FROM [Dim-BMI];\
 "
PersonFrame0=pd.read_sql_query(sSQL, conn1)
print(PersonFrame0)
print('Full Data Set (Rows):', PersonFrame0.shape[0])
print('Full Data Set (Columns):', PersonFrame0.shape[1])

