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

chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)

data_canada = px.data.gapminder().query("country == 'Canada'")
fig = px.bar(data_canada, x='year', y='pop')
fig.update_layout(showlegend = False)
fig.update_layout(
    margin=dict(l=0, r=0, t=0, b=0)
)

config = {'displayModeBar': False}
st.plotly_chart(fig, use_container_width=True, config = config)

c1, c2 = st.columns(2)

x1 = np.random.randn(200) - 2
x2 = np.random.randn(200)
x3 = np.random.randn(200) + 2

hist_data = [x1, x2, x3]

group_labels = ['Group 1', 'Group 2', 'Group 3']

fig = ff.create_distplot(
         hist_data, group_labels, bin_size=[.1, .25, .5]
      )

fig.update_layout(legend=dict(
    orientation = 'h',
    xanchor= "center",
    yanchor="top",
    y=-0.3, 
    x=0.5 
    ))  

fig.update_layout(
    margin=dict(l=0, r=0, t=0, b=0)
)          

with c1:
    st.plotly_chart(fig, use_container_width=True, config = config)

with c2:
    st.plotly_chart(fig, use_container_width=True, config = config)

files = []
for i in range(1, 8):
	f = open(str(i) +'.csv', 'r')
	files.append(f)

write_pred_csv(files, 'pred.csv')
st.bar_chart({"data": [1, 5, 2, 6, 2, 1]})
with st.expander("See explanation"):
    df = pd.DataFrame(
    np.random.randn(5, 5),
    columns=('col %d' % i for i in range(5)))
    st.dataframe(df)
     
     
    df = px.data.tips()
    fig = px.pie(df, values='tip', names='day', width=300, height=300)
    fig.update_layout(
    margin=dict(l=0, r=0, t=0, b=0)
)
    st.plotly_chart(fig, use_container_width=True, config = config)
     
      

col1, col2= st.columns(2)

with col1:
    #st.write('Hello')
    df = px.data.tips()
    fig = px.pie(df, values='tip', names='day', width=300, height=300)
    st.plotly_chart(fig, use_container_width=True, config = config)
    #st.bar_chart(chart_data)

with col2:
    #st.write('There')
    df = px.data.tips()
    fig = px.pie(df, values='tip', names='day', width=300, height=300)
    st.plotly_chart(fig, use_container_width=True, config = config)
    #st.bar_chart(chart_data)

files = []
for i in range(1, 8):
	f = open(str(i) +'.csv', 'r')
	files.append(f)

write_pred_csv(files, 'pred.csv')
make_freq_chart('raw.csv')

files = []
for i in range(1, 8):
	f = open(str(i) +'.csv', 'r')
	files.append(f)


#uploaded_files4 = st.file_uploader("Choose one or more CS", accept_multiple_files=True)
db = find_day_distribution(files)
write_csv(db, 'hours.csv')
make_pie_chart('hours.csv')

files = []
for i in range(1, 8):
	f = open(str(i) +'.csv', 'r')
	files.append(f)
#uploaded_files2 = st.file_uploader("Choose one or more CSV file", accept_multiple_files=True)
write_pred_csv(files, 'pred.csv')
make_pred_chart('pred.csv')
files = []
for i in range(1, 8):
	f = open(str(i) +'.csv', 'r')
	files.append(f)

#uploaded_files3 = st.file_uploader("Choose one or more CSV ", accept_multiple_files=True)
db = find_day_distribution(files)
write_csv(db, 'hours.csv')
make_pie_chart('hours.csv')
make_polar_bar_chart('pred.csv')


if st.button('Make chart'):
     make_freq_chart('raw.csv')

df = px.data.gapminder().query("country == 'Canada'")
fig = px.bar(df, x='year', y='pop')
fig.update_layout(showlegend = False, xaxis_range = [1980,2010])
fig.update_traces(textposition='inside')

config = {'displayModeBar': False}

for idx in df.index:
    url="<a href='http://localhost:8501"+"' target='_blank'>"+str(df['year'][idx])+"</a>"
    fig.add_annotation(dict(
                            showarrow=False,
                            text=url,
                            xanchor='auto',
                            yanchor='auto'))

st.plotly_chart(fig, use_container_width=True, config = config)
