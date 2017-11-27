import numpy as np

class Cluster:
    def __init__(self, vector, label):
        self.elements= np.array([vector], dtype=float)
        self.label= [label]

    def __str__(self):
        str= "Cluster( "
        for l in self.label:
            str+=l
            if l != self.label[-1]:
                str+=","
        str+=" )"
        return str

    def add(self, other):
        self.elements= np.vstack((self.elements, other.elements))
        self.label= self.label+other.label

    def centroid(self):
        return np.mean(self.elements.T,axis=1)

    def distance(self, other):
        k= (self.elements.shape[0]*other.elements.shape[0])/\
           (self.elements.shape[0]+other.elements.shape[0])
        return np.sum((self.centroid()-other.centroid())**2)*k


def computeClusters(clusters, media):
    R = []
    PST2= []
    while len(clusters) > 1:
        min_dis = 999999
        a = Cluster([], "")
        b = Cluster([], "")

        for ci in clusters:
            for cl in clusters:
                if ci != cl and ci.distance(cl) < min_dis:
                    min_dis = ci.distance(cl)
                    a = ci
                    b = cl

        print(a, " com ", b)
        a.add(b)
        clusters.remove(b)

        str= ''
        for ci in clusters:
            str+=ci.__str__()+", "

        SSB = 0
        SST = 0
        for ci in clusters:
            SSB += ci.elements.shape[0] * np.sum((ci.centroid() - media) ** 2)
        for ci in clusters:
            for x in ci.elements:
                SST += np.sum((x - ci.centroid()) ** 2)
        R.append(SSB / SST)
        # print(SSB, SST, R[-1])

        '''
        # rever esse indice
        pstMax= 0

        for ci in clusters:
            for cl in clusters:
                Bil= ci.distance(cl)
                s1= 0
                s2= 0
                for x in ci.elements:
                    s1= np.sum((x - ci.centroid()) ** 2)
                for x in cl.elements:
                    s2= np.sum((x - cl.centroid()) ** 2)
                if (s1+s2) == 0:
                    continue
                pst= Bil/(s1+s2)*(ci.elements.shape[0]+cl.elements.shape[0]-2)
                if pst > pstMax:
                    pstMax= pst

        PST2.append(pstMax)
        '''

    return R