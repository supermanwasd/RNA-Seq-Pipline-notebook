import pandas as pd

df = pd.read_table("counts/gene_counts.txt",header = 1)
df = df[['Geneid'] + list(df.columns)[6::]]

columns_list = list(df.columns)[1::]
columns_list.sort()
df = df[["Geneid"]+columns_list]

col_name = []
for i in list(df.columns)[1::]:
    i = i.split("/")[1].split("_b73v4")[0]
    col_name.append(i)

df.columns = ["Geneid"]+col_name

df.to_csv("counts.csv",index=False)