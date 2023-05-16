import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

x = st.slider('Select a value')
st.write(x,'squared is', x*x)
rand=np.random.normal(1,2,size=20)
fig, ax = plt.subplots()
ax.hist(rand,bins=15)
st.sidebar.pyplot(fig)
st.sidebar.button("Click")
