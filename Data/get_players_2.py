import pandas as pd

def get_format_players(df, p):
	for row, data in df.iterrows():
		for r, d in team_codes.iterrows():
			if d[0] in data[2]:
				df[2][row] = d[1]
	formatted_players = pd.DataFrame({'Player': (df[1] + ' ' + df[0]), 'Team': df[2], 'Position': p})
	return formatted_players


file = 'Players_Unformatted.xlsx'
team_cf = 'team_codes.csv'
output_file = 'Players_Formatted.xlsx'
positions = ['QB', 'RB', 'WR', 'TE', 'K']
cols1 = {0: 'Last', 1: 'First', 2: 'Team'}
players_collection = {'QB': '', 'RB': '', 'WR': '', 'TE': '', 'K': '', 'Def': ''}

team_codes = pd.read_csv(team_cf, header = None)
players_collection['Def'] = pd.DataFrame({'Player': team_codes[2], 'Team': team_codes[1], 'Position': 'Def'})

for pos in positions:
	temp_df = pd.read_excel(file, sheet_name = pos, header = None)
	players_collection[pos] = get_format_players(temp_df, pos)

all_formatted_players = pd.concat([players_collection['QB'], players_collection['RB'], players_collection['WR'],
						players_collection['TE'], players_collection['K'], players_collection['Def']], ignore_index = 1)

all_formatted_players.to_excel(output_file, sheet_name = 'Players')