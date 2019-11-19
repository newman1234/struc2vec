# -*- coding: utf-8 -*-
import inspect
import networkx as nx
import matplotlib.pyplot as plt
import os.path

dir_f = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
print(dir_f)

fh=open(dir_f + "/../graph/karate-mirrored.edgelist", 'rb')
G=nx.read_edgelist(fh)
nx.draw_spring(G, with_labels=True, font_weight='bold')
plt.show()

fh=open(dir_f + "/../emb/karate-mirrored.emb", 'rb')
x = list()
y = list()
n = list()
for i, l in enumerate(fh.readlines()):
    if i == 0:
        continue

    l = l.decode('utf8').split()
    x.append(float(l[1]))
    y.append(float(l[2]))
    n.append(str(l[0]))
plt.figure(figsize=(12, 8))
plt.scatter(x, y)
for i, txt in enumerate(n):
    plt.annotate(txt, (x[i], y[i]))
plt.show()
fh.close()