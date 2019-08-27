import pandas as pd

file = 'VBD2019_A1.xls'
positions = ['QB', 'RB', 'WR', 'TE', 'PK']
#players = pd.read_excel(file, sheet_name = ['QB', 'RB', 'WR', 'TE', 'PK', 'Def'], usecols = [0, 1, 2] )
players_unformatted = pd.read_excel(file, sheet_name = positions, header = 1, usecols = [0, 1, 2])

i = 0
for key in players_unformatted:
	temp_df = str(positions[i])
	temp_df = pd.DataFrame(players_unformatted[key])
	i += 1

print(QB)
#players_formatted = pd.Series((players['First'] + players['Last']))