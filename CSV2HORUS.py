
import pandas as pd

sInputFileName='D:/Datascience/Datascience/vkhcggit/practical-data-science/VKHCG/05-DS/9999-Data/Country_Code.csv'
InputData=pd.read_csv(sInputFileName,encoding="latin-1")
print('Input Data Values ===================================')
print(InputData)
print('=====================================================')
ProcessData=InputData

# Rename Country and ISO-M49
ProcessData.rename(columns={'CountryName': 'Country'}, inplace=True)
ProcessData.rename(columns={'CountryNumber': 'ISO-M49'}, inplace=True)

# Sort data by CurrencyNumber
ProcessData.sort_values('Country', axis=0, ascending=False, inplace=True)

print('Process Data Values =================================')
print(ProcessData)
print('=====================================================')


# Output Agreement ===========================================
OutputData=ProcessData

sOutputFileName='D:/Datascience/Datascience/vkhcggit/practical-data-science/VKHCG/05-DS/9999-Data/Country_Code.csv'
OutputData.to_csv(sOutputFileName, index = False)

print('CSV to HORUS - Done')
print('CSV to HORUS - Done')
