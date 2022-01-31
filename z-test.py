import csv
import pandas as pd
import plotly.graph_objects as go
import plotly.figure_factory as ff
import random
import statistics as s

df = pd.read_csv("studentMarks.csv")
data = df["Math_score"].to_list()
# fig = ff.create_distplot([data],["math scores"],show_hist = False)
# fig.show()

mean1 = s.mean(data)
stdev = s.stdev(data)
print(mean1)
print(stdev)

def random_set_of_mean(counter):
    data_set = []
    for i in range(0,counter):
        random_index = random.randint(0,len(data)-1)
        value = data[random_index]
        data_set.append(value)
    mean = s.mean(data_set)
    return mean
mean_list = []
for i in range(0,1000):
    set_of_means = random_set_of_mean(100)
    mean_list.append(set_of_means)
mean = s.mean(mean_list)
print(mean)
fig = ff.create_distplot([mean_list],["Student marks"],show_hist = False)
fig.add_trace(go.Scatter(x = [mean,mean],y = [0,0.2],mode = 'lines', name = "MEAN"))
fig.show()
mean2 = s.mean(mean_list)
stdev2 = s.stdev(mean_list)
print(mean2)
print(stdev2)

