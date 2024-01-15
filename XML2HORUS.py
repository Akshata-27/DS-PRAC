import pandas as pd
import xml.etree.ElementTree as ET
#=============================================================
def df2xml(data):
    header = data.columns
    root = ET.Element('root')
    for row in range(data.shape[0]):
        entry = ET.SubElement(root,'entry')
        for index in range(data.shape[1]):
            schild=str(header[index])
            child = ET.SubElement(entry, schild)
            if str(data[schild][row]) != 'nan':
                child.text = str(data[schild][row])
            else:
                child.text = 'n/a'
            entry.append(child)
    result = ET.tostring(root)
    return result
#=============================================================
def xml2df(xml_data):
    root = ET.XML(xml_data) 
    all_records = []
    for i, child in enumerate(root):
        record = {}
        for subchild in child:
            record[subchild.tag] = subchild.text
        all_records.append(record)
    return pd.DataFrame(all_records)

#=============================================================
# Input Agreement ============================================
#=============================================================
sInputFileName='D:/Datascience/Datascience/vkhcggit/practical-data-science/VKHCG/05-DS/9999-Data/Country_Code.xml'

InputData = open(sInputFileName).read()

print('=====================================================')
print('Input Data Values ===================================')
print('=====================================================')
print(InputData)
print('=====================================================')
ProcessDataXML=InputData

# XML to Data Frame
ProcessData=xml2df(ProcessDataXML)

# Sort data by CurrencyNumber
ProcessData.sort_values('CountryName', axis=0, ascending=False, inplace=True)
print('=====================================================')
print('Process Data Values =================================')
print('=====================================================')
print(ProcessData)

OutputData=ProcessData

sOutputFileName='D:/Datascience/Datascience/vkhcggit/practical-data-science/VKHCG/05-DS/9999-Data/Country_Code.xml'
OutputData.to_csv(sOutputFileName, index = False)

print('=====================================================')
print('XML to HORUS - Done')
