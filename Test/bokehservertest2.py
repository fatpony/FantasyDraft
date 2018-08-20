from random import random

from bokeh.layouts import column
from bokeh.models import Button
from bokeh.palettes import RdYlBu3
from bokeh.plotting import figure, curdoc

default_minutes = 5
default_seconds = 0
seconds_left = default_minutes*60 + default_seconds
# ColumnDataSource data values must be iterable,
# so the values below are placed inside single-element lists
color = ['#78c400']
text_color = ['#ffffff']
start_time = [default_minutes*60 + default_seconds]
time_remaining = list(start_time)
time_string = ['%02d:%02d' % (default_minutes, default_seconds)]
# Create data source for timer plot
s=ColumnDataSource(data=dict(x=[0],
                                  y=[0],
                                  start_time=start_time,
                                  start_mins=[default_minutes],
                                  start_secs=[default_seconds],
                                  time_remaining=time_remaining,
                                  time_string=time_string,
                                  fill_color=color,
                                  text_color=text_color,
                                  interval_id=[0]))

p1 = figure(x_range=(-8, 8), y_range=(-5, 5),
                  plot_width=900, plot_height=600,
                  title=None, tools=tools)
p1.rect(x='x', y='y',
        width=16, height=10,
        fill_color='fill_color',
        line_color=None,
        name='block',
        source=source)
p1.text(x='x', y='y',
        text='time_string',
        text_color='text_color',
        alpha=0.75,
        text_font_size='128pt',
        text_baseline='middle',
        text_align='center',
        name='timer',
        source=source)
# create a plot and style its properties
p = figure(x_range=(0, 100), y_range=(0, 100), toolbar_location=None)
p.border_fill_color = 'black'
p.background_fill_color = 'black'
p.outline_line_color = None
p.grid.grid_line_color = None

# add a text renderer to our plot (no data yet)
r = p.text(x=[], y=[], text=[], text_color=[], text_font_size="20pt",
           text_baseline="middle", text_align="center")

i = 0

ds = r.data_source

# create a callback that will add a number in a random location
def callback():
    global i

    # BEST PRACTICE --- update .data in one step with a new dict
    new_data = dict()
    new_data['x'] = ds.data['x'] + [random()*70 + 15]
    new_data['y'] = ds.data['y'] + [random()*70 + 15]
    new_data['text_color'] = ds.data['text_color'] + [RdYlBu3[i%3]]
    new_data['text'] = ds.data['text'] + [str(i)]
    ds.data = new_data

    i = i + 1

# add a button widget and configure with the call back
button = Button(label="Press Me")
button.on_click(callback)

# put the button and plot in a layout and add to the document
curdoc().add_root(column(button, p))
