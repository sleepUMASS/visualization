from lib import *
from daywise_utilities import *

config = {'displayModeBar': False}


# takes a file name (string) and makes a pie chart using the file's data
def make_pie_chart(file_name):
    # creating DataFrame from CSV file
    df = pd.read_csv(file_name)
    df['Hours'] = df['Hours'].round(1)
    fig = px.pie(df, values='Hours', names='Day', hole=0.5, title='Your Sleep Distribution By Day', 
    width = 450, 
    height = 450,
    template="plotly_dark")
    #fig.update_layout(coloraxis_colorbar_x=-0.3)
    #fig.update_layout(coloraxis_colorbar_orientation='h')
    fig.update_layout(legend=dict(
    orientation="h"
    ))
    with st.container():
        st.plotly_chart(fig, use_container_width=False, config = config)

# takes a file name (string) and makes a polar bar chart using the file’s data, according to frequency of hours of sleep
def make_freq_chart(file_name):
    df = pd.read_csv(file_name)
    df['Hours'] = df['Hours'].round(1)
    df.rename(columns = {'Category':'You slept'}, inplace = True)
    fig = px.bar_polar(df, theta='Day', r='Hours', color="You slept", 
                       color_discrete_sequence = ['rgb(210, 43, 43)', 'rgb(80, 200, 120)', 'rgb(255, 195, 0)'],
                       category_orders = {'You slept': ['Too less', 'Just right', 'Too much']},
                       hover_data = {'Hours': True, 'You slept': True, 'Day': False},
                       title="Your Sleep Over Time", 
                       #template="plotly_dark"
                       )
    fig.update_layout(coloraxis_colorbar_x=-0.3)
    fig.update(layout_showlegend=False)
    fig.update_traces(showlegend=False)
    #fig.update_coloraxes(colorbar_orientation="h")
    #fig.update_coloraxes(colorbar_thickness=15)   
    with st.container():
        st.plotly_chart(fig, use_container_width=True, config = config)
        

# takes a file name (string) and makes a polar bar chart using the file’s data, according to uncertainty rate
def make_pred_chart(file_name):
    df = pd.read_csv(file_name)
    df['Hours'] = df['Hours'].round(1)
    df.rename(columns = {'Category':'uncertain_rate'}, inplace = True)
    df = df.sort_values(by='uncertain_rate', ascending=False)
   
    fig = px.bar_polar(df, theta='Day', r='Hours', 
                        #color="uncertain_rate", 
                       title="Your Sleep Over Time", 
                       hover_data = {'Hours': True, 'uncertain_rate': True, 'Day': False},
                       #template="plotly_dark"
                       )
    fig.update_layout(coloraxis_colorbar_x=-0.3)                   
    fig.update(layout_showlegend=False)
    fig.update_traces(showlegend=False)
    with st.container():
        st.plotly_chart(fig, use_container_width=True, config = config)

# takes a file name (string) and makes a polar bar chart using the file’s data
def make_polar_bar_chart(file_name):
    df = pd.read_csv(file_name)
    df['Hours'] = df['Hours'].round(1)
    confidence = df['uncertain_rate']
    df['uncertain_rate'] = confidence
    fig = px.bar_polar(df, r="Hours", theta="Day",
                       #color="uncertain_rate", 
                       #template="plotly_dark",
                       hover_data = {'Hours': True,'Day': False},
                       #color_discrete_sequence= px.colors.diverging.Spectral,
                       title='Hours of Sleep Each Night')
    fig.update_layout(coloraxis_colorbar_x=-0.3)
    fig.update(layout_showlegend=False)
    fig.update_traces(marker_line_color = 'black', 
                      marker_line_width=2,  
                      selector=dict(type='barpolar'))    
    fig.update_traces(showlegend=False)          
    with st.container():
        st.plotly_chart(fig, use_container_width=True, config = config) 

      


       
    
    
    
