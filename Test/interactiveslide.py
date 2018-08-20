from bokeh.layouts import column, row
from bokeh.models import CustomJS, ColumnDataSource, Slider, Button
from bokeh.plotting import figure, output_file, show

output_file("callback.html")

x = [x*0.005 for x in range(0, 200)]
y = x

source = ColumnDataSource(data=dict(x=x, y=y))

plot = figure(plot_width=400, plot_height=400)
plot.line('x', 'y', source=source, line_width=3, line_alpha=0.6)

callback = CustomJS(args=dict(source=source), code="""
        var data = source.data;
        var f = 2
        x = data['x']
        y = data['y']
        for (i = 0; i < x.length; i++) {
            y[i] = Math.pow(x[i], f)
        }
        source.change.emit();
    """)
start_timer = CustomJS(args=dict(source=source), code="""
    var data = source.get('data');
    interval_id = data['interval_id'];
    function countdown() {
        start_time = data['start_time'];
        time_remaining = data['time_remaining'];
        time_string = data['time_string'];
        text_color = data['text_color'];
        fill_color = data['fill_color'];
        if (time_remaining[0] == 0) {
            if (text_color[0] == '#ffffff') {
                text_color[0] = '#ff0000';
            }else {
                text_color[0] = '#ffffff';
            }
        }else{
            time_remaining[0]--;
            time_string[0] = ('0' + Math.floor(time_remaining[0] / 60)).slice(-2) + ':' + ('0' + Math.floor(time_remaining[0] % 60)).slice(-2);
            if (time_remaining[0] <= start_time[0]/10) {
                fill_color[0] = '#ff0000';
            }
        }
        source.trigger('change');
    }
    if (interval_id[0] == 0) {
        interval_id[0] = setInterval(countdown, 1000);
        source.trigger('change');
    }
""")

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
source=ColumnDataSource(data=dict(x=[0],
                                  y=[0],
                                  start_time=start_time,
                                  start_mins=[default_minutes],
                                  start_secs=[default_seconds],
                                  time_remaining=time_remaining,
                                  time_string=time_string,
                                  fill_color=color,
                                  text_color=text_color,
                                  interval_id=[0]))

# No tools required for this one
tools = ''

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

# Remove axes, labels & tick lines
p1.ygrid.grid_line_color = None
p1.xgrid.grid_line_color = None
p1.axis.axis_line_color  = None
p1.axis.major_label_text_color = None
p1.axis.major_tick_line_color = None
p1.axis.minor_tick_line_color = None

button = Button(label="power", callback=callback)
button_start = Button(label='start', callback=start_timer)

layout = column(row(button, button_start), row(plot), p1)

show(layout)
