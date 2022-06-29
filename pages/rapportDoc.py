import collections
from subprocess import list2cmdline
from numpy.core.defchararray import lower
import streamlit as st
import numpy as np
import pandas as pd
import os


list = os.listdir('elem')


st.subheader("Ici vous trouverez les comptes rendu et rapport de stage")

opt = st.selectbox(
    'Quelle fichier voulez vous choisir',
    list
)
st.download_button(label="télecharger le fichier", data=opt, file_name= opt, mime= 'docx')
