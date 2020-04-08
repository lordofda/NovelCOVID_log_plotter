import json
from urllib.request import Request,urlopen
import pandas
import matplotlib.pyplot as plt
import argparse

#Parse argument -c
parser = argparse.ArgumentParser()
parser.add_argument("-c", "--country", help="Country to plot the data for, see https://github.com/NovelCOVID/API", type=str, default="Poland")
args = parser.parse_args()

#Request data
req = Request('https://corona.lmao.ninja/v2/historical/{}'.format(args.country), headers={'User-Agent': 'Mozilla/5.0'})
data = urlopen(req).read()
output = json.loads(data)

#Make panda dataframe
df = pandas.DataFrame(output['timeline']['cases'], index=[0])
df = df.transpose()
df.columns = ['A']

#Calculate new cases
df['B'] = df['A'] - df['A'].shift(1)

#Make a plot
plt.title('Corona trend for {}'.format(args.country))
plt.xscale('log')
plt.yscale('log')
plt.xlabel('Total Cases')
plt.ylabel('New Cases')
plt.plot('A', 'B', '.-g', data=df.ewm(alpha=0.3).mean(), label="Smoothed")
plt.plot('A', 'B', '.--b', data=df, label="Raw")
plt.legend()
plt.show()

