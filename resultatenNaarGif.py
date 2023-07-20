#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  4 19:31:39 2023

@author: rwhut
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.animation as animation
import cv2
import pandas as pd
import ffmpeg
tempAllTowels = pd.read_pickle("rawMeeting1") 

tempAllTowelsFiltered = tempAllTowels.rolling(30*10).median().rolling(30*60).mean()

#tempAllTowelsFiltered.plot(y=['A nat', 'A droog'], 
#                   xlabel = 'tijd in minuten', 
#                   ylabel = 'Temperatuur in graden celsius').legend(['A nat','A droog'],loc = 'lower right')

tempAllTowelsFiltered['A'] = tempAllTowelsFiltered['A droog'] - tempAllTowelsFiltered['A nat'];
tempAllTowelsFiltered['B'] = tempAllTowelsFiltered['B droog'] - tempAllTowelsFiltered['B nat'];
tempAllTowelsFiltered['C'] = tempAllTowelsFiltered['C droog'] - tempAllTowelsFiltered['C nat'];
tempAllTowelsFiltered['D'] = tempAllTowelsFiltered['D droog'] - tempAllTowelsFiltered['D nat'];
tempAllTowelsFiltered['E'] = tempAllTowelsFiltered['E droog'] - tempAllTowelsFiltered['E nat'];
tempAllTowelsFiltered['F'] = tempAllTowelsFiltered['F droog'] - tempAllTowelsFiltered['F nat'];


fig = plt.figure(figsize = [16,10],dpi = 72)
ax = fig.add_subplot()

handdoekenMeta = {'A':'Decathlon (blauw)',
               'B':'Hema (blauw)',
               'C':'Care Plus Travel (blauw)',
               'D':'ANWB (groen)',
               'E':'Xenos (groen)',
               'F':'Normale katoenen handdoek'}
               

def plotPartially(i):
    ax.clear()
    tempAllTowelsFiltered[tempAllTowelsFiltered.index < (float(i)/8)].plot(ax=ax, y=list(handdoekenMeta.keys())).legend(list(handdoekenMeta.values()),loc = 'lower left',prop={'size': 24})
#    tempAllTowelsFiltered[tempAllTowelsFiltered.index < (float(i))].plot(ax=ax, y=['A','B','C','D','E','F']).legend(['A','B','C','D','E','F'],loc = 'lower left')
    plt.xlabel('tijd sinds start meting in minuten',size = 24)
    plt.ylabel('temperatuur verschil in graden Celcius', size = 24)
    plt.title('temperatuur verschil tussen natte en droge handdoek van verschillende merken \n gedurende een meting van een 80 minuten', size = 24)
    plt.ylim(-1,9)
    plt.xlim(2,78)
    ax.tick_params(axis='both', which='major', labelsize=24)
    rect = patches.Rectangle([2 , 2], 78, 7, linewidth=1, edgecolor='none', facecolor='#DAF0FF')
    ax.add_patch(rect)
    plt.text(70,3,"nat",size = 24)
    plt.text(70,1,"droog", size = 24)

    
animator = animation.FuncAnimation(fig, plotPartially, interval = 33, frames = 900)
animator.save('meeting1Movie.gif')

