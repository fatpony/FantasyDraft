import pandas as pd
import numpy as np

excel_file = r'NFL_Players_2017.xlsx'
player_list = pd.read_excel(excel_file, sheetname = 'Players', parse_cols = 'A:C', header = 0)
fantasy_teams = pd.read_excel(excel_file, sheetname = 'Teams', parse_cols = 'B', header = 0)
#player_list.set_index('Player', inplace=True)
fantasy_teams.set_index('Fantasy Team', inplace=True)
fantasy_teams.dropna(inplace = True)
teamz = [fantasy_teams.index]
print teamz
fantasy_teamz = pd.DataFrame(columns = ['Player', 'Position', 'Team', 'Amount ($)'])
print fantasy_teamz

'''fantasy_teams.set_value('Team 1', 'Player', player_list['Player'][2], takeable=False)
fantasy_teams.set_value('Team 1', 'Position', player_list['Position'][2], takeable=False)
fantasy_teams.set_value('Team 1', 'Team', player_list['Team'][2], takeable=False)
fantasy_teams.set_value('Team 1', 'Amount ($)', 5, takeable=False)'''

#print fantasy_teams['Player']['Team 1']
#n = 'Drew Brees'
#print player_list.Player[player_list.Player == n].index[0]
#print player_list['Player'][player_list.Player[player_list.Player == n].index[0]]
#x = player_list.loc[player_list['Player'] == 'Trevone Boykin']['Player']
#y = player_list.loc[player_list['Player'] == n]['Player']
#print "player_list[i]: %s" %player_list['Player'][2]
#print x
#print y

def info(draft_player):
    info_string = []
    info_string.append(player_list['Player'][player_list.Player[player_list['Player'] == draft_player].index[0]])
    info_string.append(player_list['Position'][player_list.Player[player_list['Player'] == draft_player].index[0]])
    info_string.append(player_list['Team'][player_list.Player[player_list['Player'] == draft_player].index[0]])
    return info_string

'''def draft(draft_team, draft_player, value):
    #print player_list['Player'][player_list.Player[player_list['Player'] == 'Blake Bortles']].index[0]
    fantasy_teams.set_value(draft_team, 'Player', info(draft_player)[0])
    fantasy_teams.set_value(draft_team, 'Position', info(draft_player)[1])
    fantasy_teams.set_value(draft_team, 'Team', info(draft_player)[2])
    fantasy_teams.set_value(draft_team, 'Amount ($)', float(value))
    player_list.drop(player_list.Player[player_list['Player'] == draft_player].index[0], inplace=True)'''

def draft(draft_team, draft_player, value):
    draft_temp = pd.DataFrame([[info(draft_player)[0], info(draft_player)[1], info(draft_player)[2], float(value)]], index = [draft_team], columns = ['Player', 'Position', 'Team', 'Amount ($)'])
    print draft_temp
    player_list.drop(player_list.Player[player_list['Player'] == draft_player].index[0], inplace=True)
    return draft_temp

#def nominate(nominee):

#class auction:
#    def __init__(self):
#
#    def nominate(nominee,)

#print info('Tom Savage')[0]
#fantasy_teams = pd.concat([fantasy_teams, draft('Team 3', 'Blake Bortles', 10)])
#print player_list.head(5)

excel_out_file = 'Draft_Results.xlsx'
write_to_excel = pd.ExcelWriter(excel_out_file)

while True:
    print '-------------'
    selection = raw_input('Nominate Player (1), Draft Player (2), Print Board (3), Save (8), Quit (9): ')
    print '-------------'
    if selection == '1':
        raw_input('Nominated Player: ')
    elif selection == '2':
        #fantasy_teams = pd.concat([fantasy_teams, draft(raw_input('Drafted By: '), raw_input('Drafted Player: '), raw_input('Drafted For: '))])
        fantasy_teamz = pd.concat([fantasy_teamz, draft(raw_input('Drafted By: '), raw_input('Drafted Player: '), raw_input('Drafted For: '))])
    elif selection == '3':
        #print fantasy_teams
        print fantasy_teamz
    elif selection == '8':
        fantasy_teams.to_excel(write_to_excel, 'Teams')
    elif selection == '9':
        write_to_excel.save()
        break
