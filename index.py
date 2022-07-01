import collections
import streamlit as st
import numpy as np
import pandas as pd
from utils import carroussel


st.subheader("Qui suis-je ?")
with open('utils/accueil.txt', encoding='utf8') as f:
    for line in f:
        st.write(line.strip())


if __name__ == "__main__":
    carroussel.main()