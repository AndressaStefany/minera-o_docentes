import pandas as pd
import cluster as cl
import numpy as np

# pd.set_option('display.max_colwidth', -1)

var = pd.read_csv('avaliacaodocencia.csv', delimiter=';', error_bad_lines=False)

print(var.head(5))

# uni= pd.Categorical(var['unidade'])
# var['unidade']= uni.codes
# var['valor']= var['valor'].apply(lambda str : str.split('$')[1].replace('.', '').replace(',','.')).astype(float)
# cat= pd.Categorical(var['natureza_despesa'])
# var['natureza_despesa']= cat.codes
#
# print(var.head(5))
#
# x= var.values[:,1:]
# y= var.values[:,0]
#
# print(len(uni.categories))
# from matplotlib import pyplot as plt
# from sklearn.cluster import KMeans
#
# kmeans = KMeans(n_clusters=4, random_state=0).fit(x)
# predict = kmeans.predict(x)
#
# plt.plot(x[:,0], x[:,1], '.')
# plt.xlabel('natureza_despesa')
# plt.ylabel('valor')
# plt.show()

#print(var.head(5))

#print(var.columns)