from lib import *
from chart_utilities import *
from analysis_utilities import *
from csv_utilities import *
from daywise_utilities import *
import plotly.figure_factory as ff

hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden;}
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)

with st.container():
    df = px.data.gapminder().query("country == 'Canada'")
    fig = px.bar(df, x='year', y='pop', height = 200, width=600)
    fig.update_layout(showlegend = False)
    fig.update_layout(
        margin=dict(l=0, r=0, t=0, b=0)
    )
    config = {'displayModeBar': False}
    st.plotly_chart(fig, use_container_width=False, config = config)
    st.plotly_chart(fig, use_container_width=False, config = config)
