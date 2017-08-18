import pandas as pd
import numpy as np

excel_file = r'/Users/fatpony/Dropbox/Draft/NFL_Players_2017.xlsx'
player_list = pd.read_excel(excel_file, sheetname = 'Players', parse_cols = 'D:F', header = 0)
fantasy_teams = pd.read_excel(excel_file, sheetname = 'Teams', parse_cols = 'B:F', header = 0)
#player_list.set_index('Player', inplace=True)
fantasy_teams.set_index('Fantasy Team', inplace=True)
fantasy_teams.dropna(inplace = True)

fantasy_teams.set_value('Team 1', 'Player', player_list['Player'][2], takeable=False)
fantasy_teams.set_value('Team 1', 'Position', player_list['Position'][2], takeable=False)
fantasy_teams.set_value('Team 1', 'Team', player_list['Team'][2], takeable=False)
fantasy_teams.set_value('Team 1', 'Amount ($)', 5, takeable=False)

#print fantasy_teams['Player']['Team 1']
#n = 'Drew Brees'
#print player_list.Player[player_list.Player == n].index[0]
#print player_list['Player'][player_list.Player[player_list.Player == n].index[0]]
#x = player_list.loc[player_list['Player'] == 'Trevone Boykin']['Player']
#y = player_list.loc[player_list['Player'] == n]['Player']
#print "player_list[i]: %s" %player_list['Player'][2]
#print x
#print y

def draft(draft_team, draft_player, value):
    #print player_list['Player'][player_list.Player[player_list['Player'] == 'Blake Bortles']].index[0]
    fantasy_teams.set_value(draft_team, 'Player', player_list['Player'][player_list.Player[player_list['Player'] == draft_player].index[0]])
    fantasy_teams.set_value(draft_team, 'Position', player_list['Position'][player_list.Player[player_list['Player'] == draft_player].index[0]])
    fantasy_teams.set_value(draft_team, 'Team', player_list['Team'][player_list.Player[player_list['Player'] == draft_player].index[0]])
    fantasy_teams.set_value(draft_team, 'Amount ($)', value)
    player_list.drop(player_list.Player[player_list['Player'] == draft_player].index[0], inplace=True)

#class auction:
#    def __init__(self):

draft('Team 3', 'Blake Bortles', 10)
print fantasy_teams
print player_list.head(5)
