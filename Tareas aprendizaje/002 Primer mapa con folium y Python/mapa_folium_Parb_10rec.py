# -*- coding: utf-8 -*-
"""
Created on Sat Feb 2, 2017

@author: Miguel
"""

# Esto no tiene nada que hacer en el código, son solo marcadores de seguimiento
# que usa Jupyter, elimínalos.
#TODO: eliminar In[2]:

"""
 Otra manera de agregar comentarios en bloque es lo que hago aquí mediante
 tres marcas de comillas seguidas al abrir y cerrar el bloque.

 Está bonito esto que hiciste, pero para nuestros fines ahorita es
 mejor hacerlo en la pantalla cmd pues sólo se necesita hacerlo
 una vez y ya queda disponible "para "siempre"

 Si dejas un comando como este que usaste:
   get_ipython().system('python -m pip install --upgrade pip')
 o
  get_ipython().system('pip install folium')
 Estas heciendo que cada vez que se ejecute el escript se verifique la
 instalación de los paquetes indicados. No está mal, pero en este caso
 es innecesario.

 TODO: Recuerda que # marca "no ejecutar lo que sigue, por lo tanto
 es una nota para uso humano". Anota libremente el código
 precisamente para a otros congéneres a entender lo que está
 haciendo el escript. Los que marcaste abajo "In[x]" no sirven para
 nada en este caso, sería mejor eliminarlos. Deja líneas en blanco
 para separar secciones del código. Procura no extenderte más allá
 de la columna 70 del texto, pues en muchas máquinas eso significa
 que no puedes ver todo el código en conjunto.
"""
#TODO: eliminar In[3]:


#TODO: eliminar In[9]:

# Carga y prepara la biblioteca realmente sólo necesitas la de folium
# la otra es para desplegar el mapa directamente.
import folium

# Crea un objeto de tipo "mapa" y
# centra la ventana en las coordenadas indicadas.
P_arb_map = folium.Map(location=[19.482, -96.988], zoom_start=12,
	tiles='Stamen Terrain')

# Añade 10 marcadores señalando la ubicación geográfica de 10
# registros de la rana Plectrohyla arborescandens
folium.Marker([19.46106, -97.046611], popup='01',
	icon = folium.Icon(color ='green')).add_to(P_arb_map)
folium.Marker([19.46075, -97.047222], popup='02',
	icon = folium.Icon(color ='green')).add_to(P_arb_map)
folium.Marker([19.45931, -97.046611], popup='03',
	icon = folium.Icon(color ='green')).add_to(P_arb_map)
folium.Marker([19.45947, -97.046305], popup='04',
	icon = folium.Icon(color ='green')).add_to(P_arb_map)
folium.Marker([19.45964, -97.045556], popup='05',
	icon = folium.Icon(color ='green')).add_to(P_arb_map)
folium.Marker([19.45653, -97.046222], popup='06',
	icon = folium.Icon(color ='green')).add_to(P_arb_map)
folium.Marker([19.45708, -97.046139], popup='07',
	icon = folium.Icon(color ='green')).add_to(P_arb_map)
folium.Marker([19.45653, -97.046278], popup='08',
	icon = folium.Icon(color ='green')).add_to(P_arb_map)
folium.Marker([19.45650, -97.046083], popup='09',
	icon = folium.Icon(color ='green')).add_to(P_arb_map)
folium.Marker([19.45658, -97.046222], popup='10',
	icon = folium.Icon(color ='green')).add_to(P_arb_map)

# Despliega el objeto "mapa" que creaste.
# Esto no ocurre en Anaconda, pues hay que agregar el código
# necesario para desplegar el html, Jupyter si lo hace
# pues ya estás en el browser!!!
P_arb_map

# Guarda el objeto "mapa"
P_arb_map.save('arborescandens10rec.html')