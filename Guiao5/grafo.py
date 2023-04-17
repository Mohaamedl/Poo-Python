# site onde se obteve as distancias ==> https://pt.distance.to

import networkx as nw
import matplotlib.pyplot as plt
G = nw.Graph()
cities  = [('Lisboa','Porto',274.22),('Lisboa','Aveiro', 218.37 ),('Lisboa','Coimbra',176.86),
           ('Lisboa','Faro',188.74),('Lisboa','Braga',320.87),('Lisboa','Viana do castelo',331.96),
           ('Aveiro','Viana do castelo',117.69),('Aveiro','Porto',56.27),('Porto','Coimbra',106.23),
           ('Lisboa','Lagos',184.65),('Lisboa','Beja',143.88),('Lisboa','Evora', 107.54),
           ('Faro','Evora',154.09),('Faro','Beja',74.67),('Faro','Lagos', 46.66),('Braga','Coimbra',148.87),
           ('Braga','Aveiro',102.50),('Aveiro','Coimbra', 52.39)
           ] # 10 cidades 
G.add_weighted_edges_from(cities)
print(nw.dijkstra_path_length(G,'Porto','Faro'),' - distancia entre faro e porto')
print(nw.dijkstra_path_length(G,'Porto','Lagos'),' - distancia entre porto e lagos')
print(nw.dijkstra_path_length(G,'Viana do castelo','Beja'),' - distancia entre Viana do castelo e beja')
print(nw.dijkstra_path_length(G,'Lisboa','Lagos'),' - distancia entre Lisboa e Lagos')
print(nw.dijkstra_path_length(G,'Braga','Faro'),' - distancia entre Braga e Faro')
print(nw.dijkstra_path_length(G,'Coimbra','Evora'),' - distancia entre Coimbra e evora')
# 6 testes 
elarge = [(u, v) for (u, v, d) in G.edges(data=True) if d["weight"] > 100]
esmall = [(u, v) for (u, v, d) in G.edges(data=True) if d["weight"] <= 100]
pos = nw.spring_layout(G, seed=7) 

nw.draw_networkx_edges(G, pos, edgelist=elarge, width=2)
nw.draw_networkx_edges(
    G, pos, edgelist=esmall, width=2, alpha=0.5, edge_color="b", style="dashed"
)

# node labels
nw.draw_networkx_labels(G, pos, font_size=15, font_color='g', font_family="sans-serif")
# edge weight labels
edge_labels = nw.get_edge_attributes(G, "weight")
nw.draw_networkx_edge_labels(G, pos, edge_labels)

ax = plt.gca()
ax.margins(0.08)
plt.axis("off")
plt.tight_layout()
plt.show()
