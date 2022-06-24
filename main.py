from lib import *
from chart_utilities import *
from analysis_utilities import *
from csv_utilities import *
from daywise_utilities import *
import plotly.figure_factory as ff
import sqlite3 
import hashlib
import string
import random
import sqlite3 

hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden;}
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)

x = ['Product A', 'Product B', 'Product C']
y = [20, 14, 23]

df = px.data.gapminder().query("country == 'Canada'")
fig = go.Figure(data=[go.Bar(
            x=x, y=y,
            marker_color = 'firebrick',
            text="""<a href="http://localhost:8501/link">{}</a>""".format("Text"),
            
            textposition='auto',
        )])

st.plotly_chart(fig)  


x = ['Product A', 'Product B', 'Product C']
y = [20, 14, 23]

df = px.data.gapminder().query("country == 'Canada'")
fig = go.Figure(data=[go.Bar(
            x=x, y=y,
            marker_color = 'firebrick',
            text="""<a href="http://localhost:8501/#section-1">{}</a>""".format("Text"),
            textposition='auto',
        )])

st.plotly_chart(fig)   

df = px.data.gapminder().query("country == 'Canada'")
fig = px.bar(df, x='year', y='pop',  height = 300, width=600)
fig.update_layout(showlegend = False, xaxis_range = [1980,2010])

fig.update_traces(textposition='inside')

config = {'displayModeBar': False}

for idx in df.index:
    url="<a href='http://localhost:8501/link"+"' target='_blank'>"+str(df['year'][idx])+"</a>"
    fig.add_annotation(dict(
                            showarrow=False,
                            text=url,
                            xanchor='auto',
                            yanchor='auto'
                            )
    )


st.plotly_chart(fig, use_container_width=True, config = config)







