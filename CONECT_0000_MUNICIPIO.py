#!/c/Python25 python
#import sys, os, numpy #sys, os, PIL, numpy, Image, ImageEnhance
import grass.script as grass
from PIL import Image
import wx
import random
import re
import time
import math
#from rpy2 import robjects
from datetime import tzinfo, timedelta, datetime
import win32gui
from win32com.shell import shell, shellcon
import os
import unicodedata
import math
import matplotlib.image as mpimg
import matplotlib.pyplot as plt

x=grass.read_command('r.stats',input="Municipios_merge_2015_02_d19_rast")
grass.run_command("g.region",rast="Municipios_merge_2015_02_d19_rast",res=500)
y=x.split('\n')
del y[-1]
del y[-1]

os.chdir(r'F:\data\john_pc2\nomade\grass\txt_conect_func_0000')
y=y[25:478]
for i in y:
    j=i
    ##print j
    name='000000'+j
    name=name[-4:]
    txt=open('Municipio_Conect_func_0000'+name+'.txt','w')
    #print name
    expressao1="mapa_"+name+"=if(Municipios_merge_2015_02_d19_rast=="+j+",0,null())"
    #print expressao1
       


    grass.mapcalc(expressao1, overwrite = True, quiet = True)
    grass.run_command('r.mask',input="mapa_"+name,overwrite = True) 
    expressao2="MA=if(mapa_"+name+"==0,confunc0000m_SemZeros_albers_tif,null())"
    grass.mapcalc(expressao2, overwrite = True, quiet = True)
    #print expressao2     
    grass.run_command("g.region",rast="mapa_"+name)
    grass.run_command('r.series',input='MA,mapa_'+name , output="mapa_"+name+'_bin',method='sum',overwrite = True)
    expressao3="mapa_"+name+"_bin_int=int(mapa_"+name+"_bin)"
    grass.mapcalc(expressao3, overwrite = True, quiet = True)
    pct=grass.read_command('r.univar',map="mapa_"+name+"_bin_int")
    pctsplit=pct.split('\n')
    #print pctsplit[9]
    #print pctsplit
    mean=pctsplit[9]
    mean=mean.replace('mean: ','')
    
    txt.write('Mean' '\n')
    txt.write(mean+'\n')
    txt.close()
    grass.run_command('g.remove',rast="mapa_"+name+',MA,mapa_'+name+'_bin,mapa_'+name+'_bin_int',flags='f')
    grass.run_command('r.mask',flags='r')

