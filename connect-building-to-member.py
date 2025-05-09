#import libraries
import pandas as pd
import requests
import json

#download pupil list

pupils=pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vQvbt9pfVpg0QmfIwhkzWoypt9HW-d_GGD2OG3eGZLjLgOo84gRhlC4szK_XQOp-NaTUNAeLXoGlHBo/pub?gid=453486092&single=true&output=csv')
#print(pupils.columns)

#250411hotosm_project_18553_buildings_polygons_geojson — hotosm_project_18553_buildings_polygons_geojson
layer_selected=iface.layerTreeView().selectedLayers()[0]
contribution=pd.DataFrame(columns=['id','user','timestamp'])

for feature in layer_selected.getFeatures():
    id=feature['osm_id']
    print('https://api.openstreetmap.org/api/0.6/way/'+str(id)+'/history.json')
    history = requests.get('https://api.openstreetmap.org/api/0.6/way/'+str(id)+'/history.json').json()['elements']
    for j in range(len(history)):
        new_row = {"id":id,"user": history[j]['user'], "timestamp": history[j]['timestamp']}
        contribution = contribution._append(new_row, ignore_index=True)
    
    
#check building history
history = requests.get('https://api.openstreetmap.org/api/0.6/way/813262595/history.json').json()['elements']
print(history[0]['user'],history[0]['timestamp'])

#write to csv
contribution.to_csv('/tmp/contribution_number.csv')