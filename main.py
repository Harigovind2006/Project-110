import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import random
import pandas as pd
import csv

df = pd.read_csv('Data.csv')
data = df['average'].tolist()
def random_set_of_mean(counter):
    dataSet = []
    for i in range(0,counter):
        random_index = random.randint(0,len(data)-1)
        value = data[random_index]
        dataSet.append(value)
    mean = statistics.mean(dataSet)
    return mean

def show_fig(mean_list):
    df = mean_list
    mean = statistics.mean(df)
    fig = ff.create_distplot([df],['average'],show_hist=False)
    fig.add_trace(go.Scatter(x=[mean,mean],y = [0,1],mode = 'lines',name = 'mean'))
    fig.show()

def setup():
    mean_list=[]
    for i in range(0,1000):
        set_of_mean = random_set_of_mean(100)
        mean_list.append(set_of_mean)
    show_fig(mean_list)
    mean = statistics.mean(mean_list)
    print('mean of sample distribution',mean)

setup()

population_mean = statistics.mean(data)
print('mean of the population',population_mean)
def standard_deviation():
    mean_list = []
    for i in range(0,1000):
        set_of_mean = random_set_of_mean(100)
        mean_list.append(set_of_mean)
    standard_deviation = statistics.stdev(mean_list)
    print('this is the standard deviation',standard_deviation)
