# This file includes functionalities that we might use in the future

from lib import *

st.header("Your Sleep Through The Year")
#progress_bar = st.sidebar.progress(0)
#status_text = st.sidebar.empty()
last_rows = np.random.randn(1, 1)
chart = st.line_chart(last_rows)

#initially 1, 101
for i in range(1, 5):
    new_rows = last_rows[-1, :] + np.random.randn(5, 1).cumsum(axis=0)
    #status_text.text("%i%% Complete" % i)
    chart.add_rows(new_rows)
    #progress_bar.progress(i)
    last_rows = new_rows
    time.sleep(0.05)

#progress_bar.empty()

st.button("Re-run")

progress_bar = st.progress(0)
status_text = st.empty()
chart = st.line_chart(np.random.randn(10, 2))

#initially 100
for i in range(10):
    # Update progress bar.
    progress_bar.progress(i + 1)

    new_rows = np.random.randn(10, 2)

     #Update status text.
    status_text.text(
        'The latest random number is: %s' % new_rows[-1, 1])

     #Append data to the chart.
    chart.add_rows(new_rows)

  #   Pretend we're doing some computation that takes time.
    time.sleep(0.1)

status_text.text('Done!')
st.balloons()

st.header("Timings Over The Last Two Months")
chart_data = pd.DataFrame(
     np.random.randn(50, 3),
     columns=["a", "b", "c"])

st.bar_chart(chart_data)

st.header("Indicating Factors")
chart_data = pd.DataFrame(
     np.random.randn(10, 3),
     columns=['Total Connections', 'Device 1 Unique AP', 'Device 2 Unique AP'])

st.line_chart(chart_data)


st.header("Variations in Sleeping Hours")
chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.area_chart(chart_data)


# CSV file upload, use the data in real time to plot a graph
# Extract day from date to make the pie chart
# Focus on pie chart 
# Find sleep duration from csv and keep in new csv
# Pie chart blacked out if day hasn't come
# Inter chart interactivity

#Testing how bar graphs look
data_canada = px.data.gapminder().query("country == 'Canada'")
fig = px.bar(data_canada, x='year', y='pop')
st.plotly_chart(fig)

df = px.data.wind()
st.write(df)
fig = px.bar_polar(df, r="frequency", theta="direction",
                   color="strength", 
                   #template="plotly_dark",
                   color_discrete_sequence= px.colors.sequential.Plasma_r)
st.plotly_chart(fig) 


 num_slices = 7
    theta = [(i + 1.5) * 360 / num_slices for i in range(num_slices)]
    width = [360 / num_slices for _ in range(num_slices)]

    color_seq = px.colors.qualitative.Pastel
    color_indices = range(0, len(color_seq), len(color_seq) // num_slices)
    colors = [color_seq[i] for i in color_indices]
    fig = go.Figure(go.Barpolar(
        r = df['Hours'],
        name = 'Someday',
        theta=theta,
        width=width, 
        marker_color=px.colors.diverging.Spectral,
        #["#F96167", '#FCE77D', '#8A307F', '#EE4E34', '#FFAA70', '#FFDF70', '#B6FFB4'], 
        marker_line_color="black",
        marker_line_width=2, 
        opacity = 0.7
        ))
  
    angular_tickvals = [(i + 1) * 360 / 7 for i in range(7)]

    fig.update_layout(
        polar_angularaxis_tickvals=angular_tickvals,
        #template="plotly_dark",
        polar = dict(
            radialaxis = dict(range=[4, 8], showticklabels=False, ticks=''),
            angularaxis = dict(showticklabels=False, ticks='')
        )
    )
    st.plotly_chart(fig)


 def make_ring_chart(file_name):
    df = pd.read_csv(file_name)
    print(df.head())
    startingRadius = 0.7 + (0.3* (len(df)-1))
    for index, row in df.iterrows():
        scenario = row["Day"]
        percentage = row["Hours"]
        textLabel = scenario 
        percentage = df.at[index, 'Hours'] * 100 / 8
        remainingPie = 100 - percentage
        donut_sizes = [remainingPie, percentage]
        plt.text(0.01, startingRadius + 0.07, textLabel, 
                horizontalalignment='center', verticalalignment='center')
        plt.pie(donut_sizes, radius=startingRadius, startangle=90, colors=['#d5f6da', '#5cdb6f'],
            wedgeprops={"edgecolor": "white", 'linewidth': 1})
        startingRadius-=0.3
        index = index + 1 

         plt.axis('equal')
    circle = plt.Circle(xy=(0, 0), radius=0.35, facecolor='white')
    plt.gca().add_artist(circle)
    st.pyplot(plt)   