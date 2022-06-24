from lib import *
from chart_utilities import *
from analysis_utilities import *
from csv_utilities import *
from daywise_utilities import *
import plotly.figure_factory as ff

import math

hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden;}
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)


df = px.data.gapminder()
df.groupby(['year'])['country'].agg([('CountryCount', 'count')])
df = px.data.gapminder().query("year==2007 and continent=='Asia'")
fig = px.scatter(df, x="gdpPercap", y="lifeExp", color="lifeExp", \
        size="pop",log_x=True, size_max=60)
fig.update_layout(
    height=600,width=1000,
    title_text='GDP and Life Expectancy (Asia, 2007)'
)

fig = px.scatter(df, x="gdpPercap", y="lifeExp", color="lifeExp", \
        size="pop",log_x=True, size_max=60, hover_data=['country'])

fig = px.scatter(df, x='gdpPercap', y='lifeExp', color='lifeExp', \
        size='pop', text='country', log_x=True, size_max=60)
#                   ^^^^^^^^^^^^^^
fig.update_traces(textposition='top center')


fig = px.scatter(df, x="gdpPercap", y="lifeExp", color="lifeExp", \
        size="pop", log_x=True, size_max=60)
fig.update_layout(
    height=600,width=1000,
    title_text='GDP and Life Expectancy (Asia, 2007)'
)
for idx in df.index:
    url="<a href='http://localhost:8501/1"+"' >"+df['country'][idx]+"</a>"

    fig.add_annotation(dict(x=math.log10(df['gdpPercap'][idx]),
                            y=df['lifeExp'][idx],
                            showarrow=False,
                            text=url,
                            xanchor='auto',
                            yanchor='auto'))

st.plotly_chart(fig)

#df = px.data.tips()
#fig = px.scatter(df, x="total_bill", y="tip", facet_col="sex",
                 #width=800, height=400)

#fig.update_layout(
    #margin=dict(l=20, r=20, t=20, b=20),
    #paper_bgcolor="LightSteelBlue",
#)
#with st.container():
#    st.plotly_chart(fig, use_container_width=True)


#st.header('Welcome to SleepMore.')
#link = '[GitHub](http://github.com)'
#st.markdown(link, unsafe_allow_html=True)



#chart_data = pd.DataFrame(
#     np.random.randn(25, 3),
#     columns=["a", "b", "c"])

#st.bar_chart(chart_data)

#with st.expander("See explanation"):
#    df = pd.DataFrame(
#    np.random.randn(5, 5),
#    columns=('col %d' % i for i in range(5)))
#    st.dataframe(df)
     
     
 #   df = px.data.tips()
 #   fig = px.pie(df, values='tip', names='day', width=300, height=300)
 #   st.plotly_chart(fig, use_container_width=True)









