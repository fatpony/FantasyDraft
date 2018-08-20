from bokeh.layouts import column
from bokeh.models import CustomJS, ColumnDataSource
from bokeh.plotting import Figure, output_file, show

from bokeh.io import curdoc
curdoc().clear()

from bokeh.models.widgets import Button
output_file("button.html")


x = [x*0.05 for x in range(0, 200)]
y = x

source = ColumnDataSource(data=dict(x=x, y=y))

plot = Figure(plot_width=400, plot_height=400)
plot.line('x', 'y', source=source, line_width=3, line_alpha=0.6)

callback = CustomJS(args=dict(source=source), code="""
    var data = source.data;
    x = data['x']
    y = data['y']
    for (i = 0; i < x.length; i++) {
        y[i] = Math.pow(x[i], 4)
    }
    source.trigger('change');
""")


toggle1 = Button(label="Change Graph", callback=callback, name="1")
layout = column(toggle1 , plot)

show(layout)
