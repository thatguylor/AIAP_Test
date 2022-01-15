import pandas as pd 

def logging(df,pathtosummary):
    file = open(pathtosummary,"w")
    file.truncate(0)
    file.close()
    print("Summary file has been created at:", pathtosummary)

    for column in df:
        file = open(pathtosummary,"a")
        file.write(str(df[column].value_counts()))
        file.write('\n')
        file.write('='*20)
        file.write('\n')
        file.close() 
    print("Logging has been completed. View the summary in the path above.")