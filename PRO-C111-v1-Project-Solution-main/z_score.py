import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import random
import pandas as pd
import csv

df = pd.read_csv("medium_data.csv")
data = df["reading_time"].tolist()



def random_set_of_mean(counter):
    dataset = []
    for i in range(0,counter):
        random_index = random.randint(0,len(data)-1)
        value = data[random_index]
        dataset.append(value)
    mean=statistics.mean(dataset)
    return mean

def show_fig(mean_list):
  df = mean_list
  fig = ff.create_distplot([df], ["means"], show_hist=False)
  fig.add_trace(go.Scatter(x=[mean,mean],y=[0,1],mode="lines"))
  fig.show()


mean_list=[]

for i in range(0,1000):
    set_of_means = random_set_of_mean(100)
    mean_list.append(set_of_means)
    

mean=statistics.mean(mean_list)
std_deviation=statistics.stdev(mean_list)

print(mean)
print(std_deviation)

   
first_std_deviation_start, first_std_deviation_end = mean - std_deviation, mean + std_deviation
second_std_deviation_start, second_std_deviation_end = mean - (std_deviation*2), mean + (std_deviation*2)
third_std_deviation_start, third_std_deviation_end = mean - (std_deviation*3), mean + (std_deviation*3)



df=pd.read_csv("sample_1.csv")

data=df["reading_time"].tolist()
meanofsample1=statistics.mean(data)
print(meanofsample1)

fig=ff.create_distplot([mean_list],["readingtime"],show_hist=False)

fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 0.17], mode="lines", name="MEAN"))
fig.add_trace(go.Scatter(x=[meanofsample1, meanofsample1], y=[0, 0.17], mode="lines", name="MEAN OF READING TIME IN SAMPLE1"))
fig.add_trace(go.Scatter(x=[first_std_deviation_end, first_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1 END"))
fig.add_trace(go.Scatter(x=[second_std_deviation_end, second_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2 END"))
fig.add_trace(go.Scatter(x=[third_std_deviation_end, third_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 3 END"))
fig.show()

df=pd.read_csv("sample_2.csv")

data=df["reading_time"].tolist()
meanofsample2=statistics.mean(data)
print(meanofsample2)

fig=ff.create_distplot([mean_list],["readingtime"],show_hist=False)

fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 0.17], mode="lines", name="MEAN"))
fig.add_trace(go.Scatter(x=[meanofsample2, meanofsample2], y=[0, 0.17], mode="lines", name="MEAN OF READING TIME IN SAMPLE2"))
fig.add_trace(go.Scatter(x=[first_std_deviation_end, first_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1 END"))
fig.add_trace(go.Scatter(x=[second_std_deviation_end, second_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2 END"))
fig.add_trace(go.Scatter(x=[third_std_deviation_end, third_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 3 END"))
fig.show()

df=pd.read_csv("sample_3.csv")

data=df["reading_time"].tolist()
meanofsample3=statistics.mean(data)
print(meanofsample3)

fig=ff.create_distplot([mean_list],["readingtime"],show_hist=False)

fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 0.17], mode="lines", name="MEAN"))
fig.add_trace(go.Scatter(x=[meanofsample3, meanofsample3], y=[0, 0.17], mode="lines", name="MEAN OF READING TIME IN SAMPLE3"))
fig.add_trace(go.Scatter(x=[first_std_deviation_end, first_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1 END"))
fig.add_trace(go.Scatter(x=[second_std_deviation_end, second_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2 END"))
fig.add_trace(go.Scatter(x=[third_std_deviation_end, third_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 3 END"))
fig.show()

zscore1= (mean - meanofsample1) / std_deviation
print(zscore1)

zscore2= (mean - meanofsample2) / std_deviation
print(zscore2)

zscore3= (mean - meanofsample3) / std_deviation
print(zscore3)


