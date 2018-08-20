import pandas as pd
import numpy as np

excel_file = r'NFL_Players_2017.xlsx'
player_list = pd.read_excel(excel_file, sheetname = 'Players', parse_cols = 'A:C', header = 0)
team_balances = pd.read_excel(excel_file, sheetname = 'Teams', parse_cols = 'B:C', header = 0)
team_balances.set_index('Fantasy Team', inplace=True)
#draft_results = pd.DataFrame(columns = ['Player', 'Position', 'Team', 'Amount ($)'])
draft_results = pd.DataFrame()

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

excel_out_file = 'Draft_Results.xlsx'
write_to_excel = pd.ExcelWriter(excel_out_file)

while True:
    print '-------------'
    selection = raw_input('Check Availability (1), Draft Player (2), Last 5 Picks (3), Print Balances (4), Save (8), Quit (9): ')
    print '-------------'
    if selection == '1':
        availability(raw_input('Player: '))
    elif selection == '2':
        draft_results = pd.concat([draft_results, draft(check_team(raw_input('Drafted By: ')), \
                        check_player(raw_input('Drafted Player: ')), check_bid(raw_input('Drafted For: ')) ) ])
    elif selection == '3':
        print draft_results.head()
    elif selection == '4':
        print team_balances
    elif selection == '8':
        draft_results.to_excel(write_to_excel, 'Teams')
        team_balances.to_excel(write_to_excel, 'Balances')
        write_to_excel.save()
    elif selection == '9':
        write_to_excel.save()
        break
