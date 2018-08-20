import pandas as pd
import numpy as np

from bokeh.models import ColumnDataSource, CustomJS, TextInput, Paragraph, Button
from bokeh.models.widgets import DataTable, TableColumn, Tabs, Panel
from bokeh.plotting import curdoc
from bokeh.layouts import widgetbox, column, row
from bokeh.io import show

from threading import Thread

excel_file = r'NFL_Players_2017.xlsx'
player_list = pd.read_excel(excel_file, sheetname = 'Players', parse_cols = 'A:C', header = 0)
team_balances = pd.read_excel(excel_file, sheetname = 'Teams', parse_cols = 'B:C', header = 0)
#player_list.set_index('Player', inplace=True)
team_balances.set_index('Fantasy Team', inplace=True)
draft_results = pd.DataFrame(columns = ['Player', 'Position', 'Team', 'Amount ($)'])

def check_team(team_to_check):
    try:
        team_balances.loc[team_to_check]
        return team_to_check
    except KeyError:
        print 'No such team, try again!'
        print '-------------'
        return check_team(raw_input('Drafted By: '))

def check_player(player_to_check):
    if player_to_check in player_list.Player.values:
        return player_to_check
    else:
        print 'No such player, try again!'
        print '-------------'
        return check_player(raw_input('Drafted Player: '))

def check_bid(bid_to_check):
    try:
        if float(bid_to_check) > 0 and float(bid_to_check) < 200:
            return bid_to_check
        else:
            print 'Weird entry, try again!'
            print '-------------'
            return check_bid(raw_input('Drafted For: '))
    except ValueError:
        print 'Weird entry, try again!'
        print '-------------'
        return check_bid(raw_input('Drafted For: '))

def availability(player_avail_check):
    if player_avail_check in player_list.Player.values:
        print '-------------'
        print 'Still Available.'
    else:
        print '-------------'
        print 'Not Available.'

def info(draft_player):
    info_string = []
    info_string.append(player_list['Player'][player_list.Player[player_list['Player'] == draft_player].index[0]])
    info_string.append(player_list['Position'][player_list.Player[player_list['Player'] == draft_player].index[0]])
    info_string.append(player_list['Team'][player_list.Player[player_list['Player'] == draft_player].index[0]])
    return info_string

def draft(draft_team, draft_player, value):
    draft_temp = pd.DataFrame([[info(draft_player)[0], info(draft_player)[1], info(draft_player)[2], \
                float(value)]], index = [draft_team], columns = ['Player', 'Position', 'Team', 'Amount ($)'])
    player_list.drop(player_list.Player[player_list['Player'] == draft_player].index[0], inplace=True)
    sell_val = float(team_balances.loc[draft_team][0]) - float(value)
    team_balances.set_value(draft_team, 'Money ($)', sell_val)
    return draft_temp

### Bokeh ###

text_banner_draft = Paragraph(text='Press Button', width=200, height=100)
def callback_draft(text_banner=text_banner_draft):
    button_temp = 'Buttom Pressed'
    text_banner_draft.text = button_temp

source_balances = ColumnDataSource(team_balances)
columns_balances = [TableColumn(field = 'Fantasy Team', title = 'Fantasy Team'),\
                    TableColumn(field = 'Money ($)', title = 'Money ($)')]

table_balances = DataTable(source = source_balances, columns = columns_balances, width = 300, height = 8000)

source_players = ColumnDataSource(player_list)
columns_players = [TableColumn(field = 'Player', title = 'Player'), \
                    TableColumn(field = 'Position', title = 'Position'), \
                    TableColumn(field = 'Team', title = 'Team')]

table_players = DataTable(source = source_players, columns = columns_players, width = 800, height = 800)

draft_button = Button(label="Draft")
draft_button.on_click(callback_draft)

tables = Panel(child = row(table_players, text_banner_draft, column(draft_button, table_balances)), title = 'RBB 2017')
tabs = Tabs(tabs = [ tables ] )
layout = widgetbox(tabs)

doc = curdoc().add_root(layout)
thread = Thread(target=doc)
thread.start()
### Bokeh ###
    #####
