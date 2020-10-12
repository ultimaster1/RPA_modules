import pandas as pd
import datetime

file = 'C:/Users/kir/Desktop/actions/log.txt'
def lcount(fname):
    df = pd.DataFrame()
    main_line = ''
    with open(fname) as infile:
        for line in infile:
            if 'Exe_file ' in line:
                df[line] = ""
                main_line = line
            else:
                df = df.append({main_line:line},ignore_index=True)
    return df
df = lcount(file)
df_splited = df

for i in df_splited.columns:
    df_splited[i] = df_splited[i].str.split('.').str[1]

for i in df_splited.columns:
    print(df_splited[i].value_counts())


print(len(df_splited.columns))
res = list(zip(df_splited.columns, df_splited.columns[1:] + df_splited.columns[:1]))
for i in res:
    print(datetime.datetime.strptime(i[0].split('.')[0],'%Y-%m-%d %H:%M:%S') - datetime.datetime.strptime(i[1].split('.')[0],'%Y-%m-%d %H:%M:%S'))
    print(datetime.datetime.strptime(i[0].split('.')[0],'%Y-%m-%d %H:%M:%S'))
    print(datetime.datetime.strptime(i[1].split('.')[0],'%Y-%m-%d %H:%M:%S'))
