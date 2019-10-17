import json
import glob
import re
import xmltodict
import os

def doConvertion(path):
    files = os.listdir(path)
    for file in files:
        if file.endswith('.xml'):
            openFile = open(path+file, "r");
            nameFile = file.split('.')[0];
            contenu = openFile.read();
            monJson = xmltodict.parse(contenu)
            fichierSrc = open(path+nameFile+".json", "a");
            fichierSrc.write(json.dumps(monJson));
            fichierSrc.close();
            openFile.close();


chemin = os.getcwd()+"/train/";
if not os.path.isdir(chemin):
    print('Rajouter le dossier train dans le dossier courant :) ! ');
else :
    doConvertion(chemin);
