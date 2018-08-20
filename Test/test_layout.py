from bokeh.layouts import widgetbox
from bokeh.models import CustomJS, TextInput, Paragraph, Button
from bokeh.plotting import output_file, show, curdoc

# PREP DATA
welcome_message = 'You have selected: (none)'
welcome_2 = 'Draft Example:'

# TAKE ONLY OUTPUT
text_banner = Paragraph(text=welcome_message, width=200, height=100)
text_banner_draft = Paragraph(text=welcome_2, width=200, height=100)

# CALLBACKS
def callback_print(text_banner=text_banner):
    user_input = str(cb_obj.value)
    welcome_message = 'You have selected: ' + user_input
    text_banner.text = welcome_message

def callback_draft(text_banner=text_banner):
    welcome_2 = 'Button Press'
    text_banner_draft.text = welcome_2

# USER INTERACTIONS
text_input = TextInput(value="", title="Enter row number:", callback=CustomJS.from_py_func(callback_print))

button = Button(label="Press Me")
button.on_click(callback_draft)

# LAYOUT
widg = widgetbox(text_input, text_banner, button, text_banner_draft)
curdoc().add_root(widg)
