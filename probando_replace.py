romance = """Verde que te quiero verde.
Verde viento. Verdes ramas.
El barco sobre la mar
y el caballo en la montaña.
Con la sombra en la cintura
ella sueña en su baranda,
verde carne, pelo verde,
con ojos de fría plata.
Verde que te quiero verde.
Bajo la luna gitana,
las cosas le están mirando
y ella no puede mirarlas."""

azul = romance.lower().replace('verde', 'azul') # => paso todo a minuscula primero, y despues remplazo todas las verdes por azul
print(azul)

#Ouput =
"""azul que te quiero azul.   
azul viento. azuls ramas.  
el barco sobre la mar      
y el caballo en la montaña.
con la sombra en la cintura
ella sueña en su baranda,  
azul carne, pelo azul,     
con ojos de fría plata.    
azul que te quiero azul.   
bajo la luna gitana,       
las cosas le están mirando 
y ella no puede mirarlas.  """