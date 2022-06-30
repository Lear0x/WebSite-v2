
#STEP 1 ---- WEB INTERACTIVE DATA ----


from cmath import log
from io import StringIO
from operator import index
from posixpath import basename
from sqlite3 import DateFromTicks
import string


import numpy as np
import pandas as pd
from pyparsing import col, srange
import streamlit as st
import plotly.graph_objs as go
import plotly.figure_factory as ff
import plotly.express as px
from pathlib import Path
import struct
from numpy import loadtxt, zeros, zeros_like



from openpyxl import Workbook
from openpyxl.chart import PieChart, Reference, Series

#-----------function----------- 

#tri le tableau des paramètres
def tabParama(tab : str ):
    col2 = []
    dt_basename = tab[0:5]
    col2.append(dt_basename)
    dt_title = tab[6:11]
    col2.append(dt_title)
    dt_sample = tab[12:23]
    col2.append(dt_sample)
    dt_counting = tab[24:29]
    col2.append(dt_counting)
    dt_monitor =  tab[30:37]
    col2.append(dt_monitor)			
    dt_date = tab[38: 47]
    col2.append(dt_date)	 					
    dt_time = tab[48 : 55]	 
    col2.append(dt_time)					
    dt_max = tab[56:60]
    col2.append(dt_max)					
    dt_selectorSpeed = tab[61:65]
    col2.append(dt_selectorSpeed)			
    dt_lambda = tab[66:67]
    col2.append(dt_lambda)						
    dt_dist_sample_detector = tab[68:72]
    col2.append(dt_dist_sample_detector)	
    dt_X0 = tab[73:76]	
    col2.append(dt_X0)						
    dt_Y0 = tab[77:80]
    col2.append(dt_Y0)						
    dt_base_angle = tab[81:85]
    col2.append(dt_base_angle)				
    dt_distance_window_detector = tab[86:90]
    col2.append(dt_distance_window_detector)	
    dt_beam_catcher = tab[91:95]
    col2.append(dt_beam_catcher)				
    dt_sample_changer = tab[96:100]
    col2.append(dt_sample_changer)			
    dt_sum = tab[101:108]
    col2.append(dt_sum)		
    dt_comment = tab[109:255]	
    col2.append(dt_comment)
    return col2
#--------------------------- 

if __name__ == '__main__':
    #---------------------------------SIDE BAR----------------------------------

    #---------------------------------------------------------------------------


    #---------------------------------Body--------------------------------------

    #TITLE
    st.title("LOOK DATA")

    st.subheader(".32")
    st.write("download file .32 for use application")
    with open("data32.zip", "rb") as fp:
        btn = st.download_button(
        label="Download ZIP",
        data=fp,
        file_name="data32.zip",
        mime="application/zip"
    )

    data_file = st.file_uploader("Upload Images", type=["32"])

    if data_file is not None:
        # To See details
        file_details = {"filename": data_file.name, "filetype": data_file.type,
                                                    "filesize": data_file.size}
        st.write(file_details)

        data_buffer = data_file.getvalue()


        #Découpage fichier en 3 parties
        str_header = data_buffer[0:255]
        intensity_tab = data_buffer[256:65792]
        str_footer = data_buffer[65794:]

        #décodage 1ere partie en (utf_8)
        stringio = StringIO(str_header.decode("utf-8"))

        # To read file as string:
        string_data = stringio.read()

        #----------- tableau des paramètres -----------


        #colonne tableau paramètre
        col2 = tabParama(string_data)
        col1 = ['basename','title','sample', 'counting','monitor','date','time','max','selectorSpeed','lambda','dist_sample_detector','X0','Y0','base_angle','distance_window_detector','beam_catcher','sample_changer','sum','comment']

        #décodage dernier partie
        output = str_footer.decode().replace("\r", "").split("\n")
        print(output)
        
        #suppression des espace vide de la dernière partie
        output_final1 = [x for x in output if x!='']
        print(output_final1)

        #suppression des commentaires de la dernière partie
        output_final2 = [ x for x in output_final1 if not ('-' in x)]
        print(output_final2)

        #ajout de la dernière partie au tableau de paramètre
        for line in output_final2:
            tab_final = line.split(" = ")
            col1.append(tab_final[0])
            col2.append(tab_final[1])

        d = {'nom':  col1, 'valeur': col2}
        df = pd.DataFrame(data=d)
        
        left_column, right_column = st.columns(2)
        
        #affichage du tableau
        with left_column:
            st.write("tableau des paramètres")
            st.write(df)

        #----------- tableau des intensitées -----------
        with right_column:
            st.write("tableau des intensitées")
            info = [intensity_tab[i:i+4] for i in range(0, len(intensity_tab), 4)]
            print(info)
            colIntensity =[]
            for line in info:
                int_val = int.from_bytes(line, "little")
                print(int_val)
                colIntensity.append(int_val)
            d2 = {'intensité' : colIntensity}
            df2 = pd.DataFrame(data=d2)
            st.write(df2)


        #----------- Affichage des intensitées en 2D -----------
        st.write("Intensité en 2D")
        a = np.array(colIntensity).reshape(128,128)
        fig = px.imshow(a, color_continuous_scale='bluered')
        Type = st.radio("Choissisez votre affichage",('normal','Logarithm'))
        color = np.random.randint(0,1000, [100])
        if Type == 'normal':
            fig = px.imshow(a, color_continuous_scale='bluered')
            st.plotly_chart(fig)
        else:
            fig = px.imshow(a,  color_continuous_scale= [
            [0, "rgb(20, 10, 71)"], [0.0001, "rgb(20, 11, 189)"], [0.001, "rgb(14, 3, 255)"], [0.01, "rgb(144, 3, 255)"], [0.1, "rgb(221, 3, 5)"], [1.0, "rgb(255, 1, 1)"]])
            st.plotly_chart(fig)

        #----------- Affichage des intensitées en 3D -----------
        st.write("Intensité en 3D")
        z = df2.values
        z = z.reshape(128, 128)#tableau 2 dimension
        x, y = np.linspace(0, 127, 128, dtype=int), np.linspace(0, 127, 128, dtype=int)
        fig3 = go.Figure(data=[go.Surface(z=z, x=x, y=y)])
        fig3.update_layout(title='Intensity', autosize=False,
             width=500, height=500,
             margin=dict(l=65, r=50, b=65, t=90))
        st.plotly_chart(fig3)

        #----------- Affichage des intensitées sous forme de courbe -----------
        st.write("Courbe des intensitées")
        s = np.sum(z, axis=0)
        print(s)

        df = pd.DataFrame(data=s, columns=['a'])
        print(df)
        fig = px.line(df, x = df.index, y= 'a')
        st.write(fig)

    #---------------------------------------------------------------------------
