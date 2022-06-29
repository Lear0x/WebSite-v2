import collections
import streamlit as st
import numpy as np
import pandas as pd



st.subheader("Qui suis-je ?")
with open('utils/accueil.txt', encoding='utf8') as f:
    for line in f:
        st.write(line.strip())
