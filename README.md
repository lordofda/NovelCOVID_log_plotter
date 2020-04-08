# NovelCOVID_log_plotter
Simple Python3 script that plots historical data on Novel Coronavirus on log-log scale
It takes data from https://github.com/NovelCOVID/API and creates a plot of new cases against total cases
This should show the trend of spread of the virus based on MinutePhysics video - https://www.youtube.com/watch?v=54XLXg4fYsc

Usage:

'python3 corona2.py -c <Country Name>'
or
'python corona2.py -c <Country Name>'
Depending on your setup

Dependencies:
Pandas, Matplotlib, Json
If they are not in your system try:
'pip3 install pandas matplotlib json'
