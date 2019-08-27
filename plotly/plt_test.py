import plotly.plotly as py
import plotly.graph_objs as go
import pandas as pd

excel_file = r'NFL_Players_2018.xlsx'
team_balances = pd.read_excel(excel_file, sheet_name = 'Teams', usecols = 'B:C', header = 0)
#team_balances.set_index('Fantasy Team', inplace=True)

trace0 = go.Scatter(
    x=[1, 2, 3, 4],
    y=[10, 15, 13, 17]
)
trace1 = go.Scatter(
    x=[1, 2, 3, 4],
    y=[1, 2, 3, 10]
)

fig = go.Table( columnwidth = [1, 1],
                header = dict( values = list(team_balances.columns ),
                        fill = dict( color='grey' ), \
                        align = ['center'],
                        font = dict(color = 'white', size = 24),
                        height = 40 ), \
                cells = dict( values = [team_balances['Fantasy Team'], team_balances['Money ($)']],
                        fill = dict( color= ['lightblue', 'lightgrey'] ),
                        align = ['center', 'center'],
                        font = dict(size = 20),
                        height = 30 )
                )
'''def plot_balances():
    fig_balances = go.Table( columnwidth = [1, 1],
                    header = dict( values = ['Fantasy Team', 'Balance ($)'],
                            fill = dict( color='grey' ), \
                            align = ['center'],
                            font = dict(color = 'white', size = 24),
                            height = 40 ), \
                    cells = dict( values = [draft_results['Fantasy Team'], draft_results['Money ($)']],
                            fill = dict( color= ['lightblue', 'lightgrey'] ),
                            align = ['center', 'center'],
                            font = dict(size = 20),
                            height = 30 )
                    )

    data = [fig_balances]

    plot_url = py.plot(data, filename = 'balances', auto_open=False)'''

data = [fig]

plot_url = py.plot(data, filename = 'basic-line', auto_open=False)
