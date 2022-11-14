import pandas as pd
import os

df_0 = pd.read_table("assembly/"+os.listdir("assembly/")[0]+"/genes.fpkm_tracking")
df_0 = df_0[["gene_short_name","FPKM"]]
df_0.columns = ["gene_id",os.listdir("assembly/")[0]+"_FPKM"]

for i in os.listdir("assembly/")[1:]:
    df = pd.read_table("assembly/"+i+"/genes.fpkm_tracking")
    df = df[["gene_short_name","FPKM"]]
    df.columns = ["gene_id",i+"_FPKM"]
    df_0 = df_0.merge(df,on="gene_id")
    df_0 = df_0.drop_duplicates('gene_id',keep='first')


columns_list = list(df_0.columns)[1::]
columns_list.sort()
df_0 = df_0[["gene_id"]+columns_list]
df_0.to_csv("FPKM_list.csv",index= False) 
