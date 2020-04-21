import pandas as pd
from collections import OrderedDict
import json

#The below function converts the input dataframe to specific json output
def dataParser(inputData):
    data=OrderedDict()
    for index, row in inputData.iterrows():
        data["person_id"]=str(row["Person Id"])
        data["datetime"]=row["Floor Access DateTime"]
        data["floor_level"]=row["Floor Level"]
        data["building"]=row["Building"]
        with open(jsonFilePath, 'a') as fp:
            json.dump(data, fp)

#path of the source file and json file
sourceFilePath="/Users/chandan/Downloads/data.csv"
jsonFilePath="/Users/chandan/Downloads/schema.json"

#read data.csv in a dataframe
personData=pd.read_csv(sourceFilePath)

#target function call
dataParser(personData)

