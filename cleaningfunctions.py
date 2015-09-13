import pandas as pd
import numpy as np

def splitCol(column, numLevels, df, inplace):
    def specificitySplit(record, numLevels=numLevels):
        record = str(record)
        splitList = record.split(":")
        for i in range(numLevels):
            if len(splitList) < i + 1:
                splitList.append("NA")
        return splitList
    if inplace == True:
        df[column] = map(lambda x: specificitySplit(x), df[column])
        return df
    else:
        return map(lambda x: specificitySplit(x), df[column])

def categoryCols(colChange, newCols, df):
    df = splitCol(colChange, len(newCols), df, inplace=True)
    for i in range(len(newCols)):
        df[newCols[i]] = map(lambda x: x[i].strip(), df[colChange])
    return df.drop(colChange, 1)

 
