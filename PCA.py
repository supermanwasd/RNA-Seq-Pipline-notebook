import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

data = pd.read_csv("RNASeq_fpkm_v4-01.04.2019.csv")
data.index = data['Unnamed: 0']
del data['Unnamed: 0']

from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler()
df_scaled = pd.DataFrame(scaler.fit_transform(data), columns=data.columns)

pca = PCA(n_components=2)
X = pca.fit_transform(df_scaled.T)

b = np.random.rand(len(X),3)

plt.figure(figsize=(35, 15))
c = 0

for i in X:
    d = c // 4
    plt.scatter(i[0],i[1],c=b[d],marker='o',s=100) 
    c += 1
plt.legend(df_scaled.columns,loc = 'upper right',fontsize = 'small',frameon=False)
plt.xlabel('PCA1 '+str(pca.explained_variance_ratio_[0]),size=20) 
plt.ylabel('PCA2 '+str(pca.explained_variance_ratio_[1]),size=20) 
plt.show()