import pandas as pd
import csv 
import statistics
import plotly.figure_factory as ff
import plotly.graph_objects as go

df=pd.read_csv("StudentsPerformance.csv")
data=df["reading score"].tolist()

mean=statistics.mean(data)
median=statistics.median(data)
mode=statistics.mode(data)
stdD=statistics.stdev(data)

first_standard_deviation_start, first_standard_deviation_end=mean-stdD, mean+stdD
second_standard_deviation_start, second_standard_deviation_end=mean-(2*stdD), mean+(2*stdD)
third_standard_deviation_start, third_standard_deviation_end=mean-(3*stdD), mean+(3*stdD)

fig=ff.create_distplot([data],["reading score"], show_hist=False)
fig.show()

list_data_within_1_stdd=[result for result in data if result>first_standard_deviation_start and result<first_standard_deviation_end]
list_data_within_2_stdd=[result for result in data if result>second_standard_deviation_start and result<second_standard_deviation_end]
list_data_within_3_stdd=[result for result in data if result>third_standard_deviation_start and result<third_standard_deviation_end]

print("mean=", mean)
print("median=", median)
print("mode=", mode)
print("standard deviation=", stdD)
print("{}% of data lies within 1 standard deviation", format(len(list_data_within_1_stdd)*100.0/len(data)))
print("{}% of data lies within 2 standard deviations", format(len(list_data_within_2_stdd)*100.0/len(data)))
print("{}% of data lies within 3 standard deviations", format(len(list_data_within_3_stdd)*100.0/len(data)))


