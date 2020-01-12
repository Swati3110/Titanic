import pandas as pd
import numpy as np
titanic=pd.read_csv('titanic.csv')
df=pd.DataFrame(titanic.select_dtypes(exclude=['object']))
for column in df:
    print(column)
    
    def outlier(column):
    #find outliers on basis of IQR
                upper=np.nanpercentile(df[column],75)
                lower=np.nanpercentile(df[column],25)
                IQR=upper-lower
                #print(IQR)
                upperresult=upper+1.5*IQR
                lowerresult=lower-1.5*IQR
                #print(upperresult)
                #print(lowerresult)
                resultlist=[]
                for y in df[column].values:
                        if y>upperresult or y<lowerresult:
                            resultlist.append(y) 
                print(resultlist)
                return(resultlist)
               # def outlier(df[column]):
#outlier(column)
if __name__ == "__main__":
            
                print(outlier(column))         

    