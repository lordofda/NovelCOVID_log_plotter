import json
from urllib.request import Request,urlopen
import pandas
import matplotlib.pyplot as plt
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-c", "--country", help="Country to plot the data for, see https://github.com/NovelCOVID/API", type=str, default="Poland")
args = parser.parse_args()

req = Request('https://corona.lmao.ninja/v2/historical/{}'.format(args.country), headers={'User-Agent': 'Mozilla/5.0'})
data = urlopen(req).read()
output = json.loads(data)


#print(output['timeline']['cases'])
df = pandas.DataFrame(output['timeline']['cases'], index=[0])
df = df.transpose()
df.columns = ['A']
df['B'] = df['A'] - df['A'].shift(1)



#fig = df.plot.line(x='A', y='B', loglog=True).get_figure()
#fig.savefig('test.pdf')
#print(df)
#df.plot()

#df.ewm(alpha=0.5).mean().plot.line(style= 'r--' x='A', y='B', loglog=True, label = 'Smoothed')
#df.plot.line(x='A', y='B', loglog=True, label = 'Raw')
plt.title('Corona trend for {}'.format(args.country))
plt.xscale('log')
plt.yscale('log')
#plt.plot('A', 'B', '.--g', data=df.ewm(alpha=0.8).mean())
plt.plot('A', 'B', '.-g', data=df.ewm(alpha=0.3).mean(), label="Smoothed")
plt.plot('A', 'B', '.--b', data=df, label="Raw")
plt.legend()
plt.show()

