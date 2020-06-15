# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 16:34:02 2020

@author: jinqi
"""
import pandas
import folium

#传入volcano数据
data = pandas.read_csv("C:/Users/jinqi/Desktop/apllication/app2\original/Volcanoes.txt")
lat=list(data['LAT'])  #转化成list操作更快
lon=list(data['LON'])
elev = list(data["ELEV"])    #类型为float类型
name = list(data["NAME"])

#设置字体等html参数
html="""Volcano name:<br><a href="http://www.google.com/search?q=%%22%s%%22" rarget="_blank">%s</a><br>
Height: %s m
"""

map=folium.Map(location=[31.22,121.48],zoom_start=6, tiles = "Stamen Terrain")  #改版背景
#加入object
#add_child  加入object
fgv = folium.FeatureGroup(name="Volcanoes")  #特征层,在该层addchild

def color_producer(height):
    if height<1000:
        return "green"
    elif height<3000:
        return "orange"
    else:
        return "red"
    

for lt,ln,el,name in zip(lat,lon,elev,name):  #同时遍历两个列表——zip   i进入lat， j进入lon
    iframe=folium.IFrame(html=html % (name,name,el), width=177, height=77)
    fgv.add_child(folium.CircleMarker(location=[lt,ln],popup=folium.Popup(iframe),tooltip="Click to get more information",radius=6,fill=True,fill_opacity=0.7,color=color_producer(el)))
#如果火山不放在featuregroup层里，则添加几次就有几个层

fgp = folium.FeatureGroup(name="Population")                                            #需要传入str类型  popup=folium.Popup(str(el),parse_html=True)
#加入polygamy层
#得到一个GeoJson object
fgp.add_child(folium.GeoJson(data=open("C:/Users/jinqi/Desktop/apllication/app2/geojson/world.json","r",encoding="utf-8-sig").read(),style_function=lambda x:{"fillColor":"green" if x["properties"]["POP2005"]<10000000 else "orange" if x["properties"]["POP2005"]<20000000 else "red"},tooltip="Click to amplify the country"))  #.read()转换为string，
                                            

map.add_child(fgp)
map.add_child(fgv)  #将特征层add入map中
map.add_child(folium.LayerControl())      #加入layer管理,需要在layer已经加入的情况下（fg）
                                        
                                            
                                            

map.save("Map1.html")


# data = pandas.read_csv("C:/Users/jinqi/Desktop/apllication/app2\original/Volcanoes.txt")   

