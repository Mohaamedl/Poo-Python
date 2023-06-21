# site onde se obteve as distancias ==> https://pt.distance.to

import networkx as nw
import matplotlib.pyplot as plt
G = nw.Graph()
cities  = [('Lisboa','Porto',274.22),('Lisboa','Aveiro', 218.37 ),('Lisboa','Coimbra',176.86),
            ('Lisboa','Faro',188.74),('Lisboa','Braga',320.87),('Lisboa','Viana do castelo',331.96),
            ('Aveiro','Viana do castelo',117.69),('Aveiro','Porto',56.27),('Porto','Coimbra',106.23),
            ('Lisboa','Lagos',184.65),('Lisboa','Beja',143.88),('Lisboa','Evora', 107.54),
            ('Faro','Evora',154.09),('Faro','Beja',74.67),('Faro','Lagos', 46.66),('Braga','Coimbra',148.87),
            ('Braga','Aveiro',102.50),('Aveiro','Coimbra', 52.39),
            ('Coimbra', 'Leiria', 73),('Aveiro', 'Agueda', 35),('Porto', 'Agueda', 79),('Agueda', 'Coimbra', 45),
            ('Viseu', 'Agueda', 78),('Aveiro', 'Porto', 78),('Aveiro', 'Coimbra', 65),('Figueira', 'Aveiro', 77),
            ('Braga', 'Porto', 57),('Viseu', 'Guarda', 75),('Viseu', 'Coimbra', 91),('Figueira', 'Coimbra', 52),
            ('Guarda', 'Castelo Branco', 96),('Leiria', 'Castelo Branco', 169),('Figueira', 'Leiria', 62),
            ('Santarem', 'Lisboa', 82),('Santarem', 'Castelo Branco', 160),('Castelo Branco', 'Viseu', 174),
            ('Santarem', 'Evora', 122),('Lisboa', 'Evora', 132),('Evora', 'Beja', 105), # era 80 depois 105?('Lisboa', 'Beja', 178),
            ('Faro', 'Beja', 147), ('Leiria', 'Santarem', 78),
           ]
G.add_weighted_edges_from(cities)
print(nw.dijkstra_path_length(G,'Porto','Faro'),' - distancia entre faro e porto')
print(nw.dijkstra_path_length(G,'Porto','Lagos'),' - distancia entre porto e lagos')
print(nw.dijkstra_path_length(G,'Viana do castelo','Beja'),' - distancia entre Viana do castelo e beja')
print(nw.dijkstra_path_length(G,'Lisboa','Lagos'),' - distancia entre Lisboa e Lagos')
print(nw.dijkstra_path_length(G,'Braga','Faro'),' - distancia entre Braga e Faro')
print(nw.dijkstra_path_length(G,'Coimbra','Evora'),' - distancia entre Coimbra e evora')
# 6 testes 





# node labels


ax = plt.gca()
ax.margins(0.08)
plt.axis("off")
plt.tight_layout()
plt.show()
