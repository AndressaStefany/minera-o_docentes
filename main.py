import pandas as pd
from matplotlib import pyplot as plt
from sklearn.cluster import KMeans
from matplotlib import colors as mcolors
import numpy as np

# pd.set_option('display.max_colwidth', -1)

dca= pd.read_csv('docentes.csv', delimiter=';', error_bad_lines=False)
#print(dca[dca.lotacao.str.contains('ESCOLA DE CIÊNCIAS E TECNOLOGIA')])
dca= dca[dca.id_unidade_lotacao==56] # dca 56 cet 4885

var = pd.read_csv('avaliacaodocencia.csv', delimiter=';', error_bad_lines=False)
var= var[var.nome_docente.isin(dca.nome.values)]

nomes= var

var= var.drop(['nome_docente', 'id_turma', 'ano', 'periodo'],1) # 'qtd_discentes'
#var= var.rename(columns = {'postura_profissional_media':'ppm','postura_profissional_DP':'ppDP',
#                          'atuacao_profissional_media':'apm', 'atuacao_profissional_DP':'apDP',
#                          'autoavaliacao_aluno_media':'aam', 'autoavaliacao_aluno_DP':'aaDP'})

x= var.values[:,1:]
x = x - x.mean(axis=0)
x = x / x.std(axis=0)
nclus= 3
kmeans = KMeans(n_clusters=nclus, random_state=0).fit(x)
predict = kmeans.predict(x)

print(len(predict))
plot_colors = dict(mcolors.BASE_COLORS, **mcolors.CSS4_COLORS) #['r','y','b','g']
plot_colors = list(plot_colors.keys())

clus= []
dfs= []
for i in range(nclus):
    c= x[predict==i]
    clus.append(c)
    dfs.append(nomes[predict==i])

cont=0
a= x.shape[1]-1
b= x.shape[1]-1

#f, plots = plt.subplots(10)
for i in range(a):
    for j in range(i+1,b):
            fig1 = plt.figure(cont)
            for k in range(nclus):
                plt.plot(clus[k][:, i], clus[k][:, j], '.', c=plot_colors[k])
                plt.xlabel(var.columns[i+1])
                plt.ylabel(var.columns[j+1])
            cont+=1
#print(var.head(5))
tops= []
for i in range(nclus):
    n= dfs[i]
    #print("Cluster ", i)
    tops.append(n.nome_docente.value_counts())
    #print(tops[-1])
    #print(n[n['nome_docente']==top5.keys()[0]].head(5))
    #print(n.nome_docente.value_counts()[:5])
#plt.show()

for i in range(nclus):
    for j in range(nclus):
        if i != j:
            for c1 in range(len(tops[i])):
                for c2 in range(len(tops[j])):
                    if tops[i].keys()[c1] == tops[j].keys()[c2]:
                        if tops[i][c1] > tops[j][c2]:
                            tops[j][c2]= 0
'''
for t1 in tops:
    for k1, k1c in zip(t1.keys(),t1):
        for t2 in tops:
            if not np.array_equal(t1.values, t2.values):
                for k2, k2c in zip(t2.keys(), t2):
                    if k1 == k2 and k1c > k2c:
                        k2c= 0
                    elif k1 == k2 and k1c < k2c:
                        k1c= 0
'''
for i in range(nclus):
    print("Cluster ", i)
    tops[i]= pd.DataFrame(tops[i])
    tops[i]= tops[i].reset_index()
    tops[i]= tops[i][tops[i].nome_docente != 0]
    print(tops[i]['index'].values)


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