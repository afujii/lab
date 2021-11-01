from rdflib import Graph,Literal

g = Graph()


g.parse('./ogura_ttl.txt',format='ttl')
for s ,p ,o in g:
   print((Literal(s),p,Literal(o)))
