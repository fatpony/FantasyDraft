from datetime import date
from random import randint

from bokeh.plotting import figure
from bokeh.io import output_file, show, curdoc
from bokeh.layouts import widgetbox, column, row
from bokeh.models import ColumnDataSource, CustomJS
from bokeh.models.widgets import DataTable, DateFormatter, TableColumn, Dropdown, Button, CheckboxButtonGroup, Panel, Tabs, TextInput, StringFormatter
from bokeh.palettes import Category20b

import pandas as pd
import numpy as np

excel_file = r'NFL_Players_2017.xlsx'
player_list = pd.read_excel(excel_file, sheetname = 'Players', parse_cols = 'A:C', header = 0)
fantasy_teams = pd.read_excel(excel_file, sheetname = 'Teams', parse_cols = 'B:F', header = 0)
fantasy_teams.set_index('Fantasy Team', inplace=True)
fantasy_teams.dropna(inplace = True)

COLORS = Category20b

#output_file('draft_layout.html')

sauces = []
sauces.append(fantasy_teams.to_dict(orient='list'))
temp =

def draft():
    fantasy_teams.set_value('Team 1', 'Player', player_list['Player'][2], takeable=False)
    fantasy_teams.set_value('Team 1', 'Position', player_list['Position'][2], takeable=False)
    fantasy_teams.set_value('Team 1', 'Team', player_list['Team'][2], takeable=False)
    fantasy_teams.set_value('Team 1', 'Amount ($)', 5, takeable=False)
    #source_teams = ColumnDataSource(fantasy_teams)
    #teams_table = DataTable(source = source_teams, columns = columns_teams, width=1000, height=800)

def do_something():
    print 'worked'


source_teams = ColumnDataSource(fantasy_teams)
print source_teams
columns_teams = [TableColumn(field = 'Fantasy Team', title = 'Fantasy Team', formatter = StringFormatter(font_style = 'bold')), \
                TableColumn(field='Player', title='Player'), \
                TableColumn(field = 'Position', title = 'Position'), TableColumn(field = 'Team', title = 'Team'), \
                TableColumn(field = 'Amount ($)', title = 'Amount ($)')]

teams_table = DataTable(source = source_teams, columns = columns_teams, width=1000, height=800)
draft()

source_players = ColumnDataSource(player_list)
columns_players = [TableColumn(field = 'Player', title = 'Player'), \
                TableColumn(field = 'Position', title = 'Position'), TableColumn(field = 'Team', title = 'Team')]
players_table = DataTable(source = source_players, columns = columns_players, width=1100, height=800)

menu = [('Item 1', 'item_1'), ('Item 2', 'item_2'), None, ('Item 3', 'item_3')]
dropdown = Dropdown(label = 'Dropdown button', button_type = 'warning', menu = menu)

button = Button(label='Foo', button_type='success')
button.on_click(do_something)


#source_parent =

p = figure()
p.line(source=source_teams, x='Fantasy Team', y='Player')


callback = CustomJS(args=dict(source=source_teams, source2=source_players), code="""
        var data = source.get('data');
        var data2 = source2.get('data');
        data['x'] = data2['x' + cb_obj.get("name")];
        data['y'] = data2['y' + cb_obj.get("name")];
        source.trigger('change');
    """)
toggle1 = Button(label="Load data file 1", callback=callback, name="1")
toggle2 = Button(label="Load data file 2", callback=callback, name="2")


draft_button = Button(label='Draft')
button.on_click(draft)


checkbox_button_group = CheckboxButtonGroup(
        labels=['Option 1', 'Option 2', 'Option 3'], active=[0, 1])

tinput = TextInput(value = '', title = 'Label:')

tab1 = Panel(child = row(column(toggle1, toggle2, draft_button), teams_table), title = 'Teams')
#tab1 = Panel(child = fantasy_teams, title = 'Teams')
tab2 = Panel(child = players_table, title = 'Players')
tab3 = Panel(child = button, title = 'button')
#tab4 = Panel(child = tinput, title = 'input')
tabs = Tabs(tabs = [ tab1, tab2 ])

layout = widgetbox(tabs)
curdoc().add_root(tabs)
