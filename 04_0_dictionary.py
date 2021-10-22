myDict={"hari":"noun",
        "school":"learning home" ,
        "car":"a vehicle" ,
        "students":{"learn":"study"},
        "marks":{45,67,98},
        3:7
       }
#print(myDict["hari"])#access keyword value by thiers keyword
#print(myDict["school"])#access keyword value by thiers keyword
#print(myDict["car"])#access keyword value by theirs keyword
#print(myDict["students"]["learn"])# accessing nested dictionary
#print(myDict.keys())#prints key by keywords
#print(myDict.values())#prints values by values
#print(myDict.items())#print contents 
updateDic={"code":{89,49,99}}
myDict.update(updateDic)
updateDict={"Md":"frind","helpful":"man"}
myDict.update(updateDict)
print(myDict)
