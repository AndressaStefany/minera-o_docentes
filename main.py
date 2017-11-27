import pandas as pd
from matplotlib import pyplot as plt
from sklearn.cluster import KMeans
import numpy as np

# pd.set_option('display.max_colwidth', -1)

var = pd.read_csv('avaliacaodocencia.csv', delimiter=';', error_bad_lines=False)

var= var.drop(['nome_docente', 'id_turma', 'ano', 'periodo', 'qtd_discentes'],1)
#var= var.rename(columns = {'postura_profissional_media':'ppm','postura_profissional_DP':'ppDP',
#                          'atuacao_profissional_media':'apm', 'atuacao_profissional_DP':'apDP',
#                          'autoavaliacao_aluno_media':'aam', 'autoavaliacao_aluno_DP':'aaDP'})

x= var.values[:,1:]

kmeans = KMeans(n_clusters=3, random_state=0).fit(x)
predict = kmeans.predict(x)

print(len(predict))
plot_colors = ['r','y','b']

clus= []
for i in range(3):
    c= x[predict==i]
    clus.append(c)

cont=0
a= x.shape[1]-1
b= x.shape[1]-1

#f, plots = plt.subplots(10)
for i in range(a):
    for j in range(i+1,b):
            print(i, j)
            fig1 = plt.figure(cont)
            for k in range(3):
                plt.plot(clus[k][:, i], clus[k][:, j], '.', c=plot_colors[k])
                plt.xlabel(var.columns[i+1])
                plt.ylabel(var.columns[j+1])
            cont+=1
plt.show()

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