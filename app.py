import streamlit as st
st.title("Streamlit Learning by Taofik Khris")
st.header("this is the header")
st.markdown("this is the markdown")
st.subheader("this is the subheader")
st.caption("this is the caption")
st.code("x=2021")
st.latex(r''' a+a r^1+a r^2+a r^3 ''')
st.code("st.text()", language='python')
st.text('Neptune AI Blog')
st.code("st.markdown()", language='python')
st.markdown('# This is Heading 1 in Markdown')
st.code("st.title()", language='python')
st.title('This is a title')
st.code("st.header()", language='python')
st.header('Header')
st.code("st.subheader()", language='python')
st.subheader('Sub Header')
st.code("st.latex()", language='python')
st.latex(r'''
...     a + ar + a r^2 + a r^3 + cdots + a r^{n-1} =
...     sum_{k=0}^{n-1} ar^k =
...     a left(frac{1-r^{n}}{1-r}right)
...     ''')
st.code("st.write()", language='python')

st.write('Display Image')
st.code('st.image("gambar.png")', language='python')
st.image("gambar.png")

st.write('Display Audio')
st.code('st.audio("anaba.mp3")', language='python')
st.audio("anaba.mp3")

st.write('Display Video')
st.code('st.video("video.mp4")', language='python')
st.video("video.mp4")

import pandas as pd
df = pd.read_csv("data.csv")

st.write('Display Dataframe')
st.code('st.dataframe(df)', language='python')
st.dataframe(df)
#st.table(df)

st.checkbox('yes')
st.button('Click')
st.radio('Pick your gender',['Male','Female'])
st.selectbox('Pick your gender',['Male','Female'])
st.multiselect('choose a planet',['Jupiter', 'Mars', 'neptune'])
st.select_slider('Pick a mark', ['Bad', 'Good', 'Excellent'])
st.slider('Pick a number', 0,50)

st.number_input('Pick a number', 0,10)
st.text_input('Email address')
st.date_input('Travelling date')
st.time_input('School time')
st.text_area('Description')
st.file_uploader('Upload a photo')
st.color_picker('Choose your favorite color')

import time

st.balloons()
st.progress(5)
with st.spinner('Wait for it...'):
    time.sleep(5)

st.success("You did it !")
st.error("Error")
st.warning("Warning")
st.info("It's easy to build a streamlit app")
st.exception(RuntimeError("RuntimeError exception"))

import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
rand=np.random.normal(1, 2, size=20)
fig, ax = plt.subplots()
ax.hist(rand, bins=15)
st.pyplot(fig)

import streamlit as st
import pandas as pd
import numpy as np
df= pd.DataFrame(    
    np.random.randn(10, 2),    
    columns=['x', 'y'])
st.line_chart(df)

import streamlit as st
import pandas as pd
import numpy as np
df= pd.DataFrame(    
    np.random.randn(10, 2),    
    columns=['x', 'y'])
st.bar_chart(df)

import streamlit as st
import pandas as pd
import numpy as np
df= pd.DataFrame(    
    np.random.randn(10, 2),    
    columns=['x', 'y'])
st.area_chart(df)

import streamlit as st
import numpy as np
import pandas as pd
import altair as alt

df = pd.DataFrame(   
    np.random.randn(500, 3),   
    columns=['x','y','z'])
c = alt.Chart(df).mark_circle().encode(   
    x='x' , y='y' , size='z', color='z', tooltip=['x', 'y', 'z'])
st.altair_chart(c, use_container_width=True)

import streamlit as st
import graphviz as graphviz
st.graphviz_chart('''    
                     digraph {        
                     Big_shark -> Tuna        
                     Tuna -> Mackerel        
                     Mackerel -> Small_fishes        
                     Small_fishes -> Shrimp    
                     }
                     '''
                     )

import pandas as pd
import numpy as np
import streamlit as st
df = pd.DataFrame(np.random.randn(500, 2) / [50, 50] + [37.76, -122.4],
                  columns=['lat', 'lon'])
st.map(df)