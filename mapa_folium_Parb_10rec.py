
# coding: utf-8

# In[2]:

get_ipython().system('python -m pip install --upgrade pip')


# In[3]:

get_ipython().system('pip install folium')


# In[9]:

# Carga y prepara la biblioteca
import folium 

# Crea un objeto de tipo "mapa" para la ventana centrada en las coordenadas indicadas.
P_arb_map = folium.Map(location=[19.482, -96.988], zoom_start=12, tiles='Stamen Terrain')
#Añade 10 marcadores señalando la ubicación geográfica de 10 registros de la rana Plectrohyla arborescandens
folium.Marker([19.46106, -97.046611], popup='01', icon = folium.Icon(color ='green')).add_to(P_arb_map)
folium.Marker([19.46075, -97.047222], popup='02', icon = folium.Icon(color ='green')).add_to(P_arb_map)
folium.Marker([19.45931, -97.046611], popup='03', icon = folium.Icon(color ='green')).add_to(P_arb_map)
folium.Marker([19.45947, -97.046305], popup='04', icon = folium.Icon(color ='green')).add_to(P_arb_map)
folium.Marker([19.45964, -97.045556], popup='05', icon = folium.Icon(color ='green')).add_to(P_arb_map)
folium.Marker([19.45653, -97.046222], popup='06', icon = folium.Icon(color ='green')).add_to(P_arb_map)
folium.Marker([19.45708, -97.046139], popup='07', icon = folium.Icon(color ='green')).add_to(P_arb_map)
folium.Marker([19.45653, -97.046278], popup='08', icon = folium.Icon(color ='green')).add_to(P_arb_map)
folium.Marker([19.45650, -97.046083], popup='09', icon = folium.Icon(color ='green')).add_to(P_arb_map)
folium.Marker([19.45658, -97.046222], popup='10', icon = folium.Icon(color ='green')).add_to(P_arb_map)


# Despliega el objeto "mapa" que creaste.
P_arb_map

#Guarda el objeto "mapa"
P_arb_map.save('arborescandens10rec.html')

