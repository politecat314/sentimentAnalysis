import plotly.graph_objs as go

def draw_bar_chart(x_list, y_list, x_label="", y_label="", title="", colors=['steelblue', 'forestgreen','crimson','lightslategray']):
    data = [go.Bar(
       x = x_list,
       y = y_list,
       marker_color=colors
    )]
    fig = go.Figure(data=data)
    
    fig.update_layout(
        title=title,
        xaxis_title=x_label,
        yaxis_title=y_label,
    )
    
    fig.show()