import plotly.figure_factory as ff
import plotly.graph_objects as go
import numpy as np
import statistics as s
import csv
import pandas as pd

df = pd.read_csv('./data.csv')
scores = df['reading score'].to_list()
def data(dat):
  mode = s.mode(dat)
  mean = s.mean(dat)
  median = s.median(dat)
  sd = s.stdev(dat)
  print("Mode - ", mode, "\nMean - ", mean, "\nMedian - ", median, "\nStandard Deviation - ", sd)
  first_sd_start, first_sd_end = mean-sd, mean+sd
  second_sd_start, second_sd_end = mean-(2*sd), mean+(2*sd)
  third_sd_start, third_sd_end = mean-(3*sd), mean+(3*sd)
  first_list_of_data = [result for result in dat if result>first_sd_start and result<first_sd_end]
  second_list_of_data = [result for result in dat if result>second_sd_start and result<second_sd_end]
  third_list_of_data = [result for result in dat if result>third_sd_start and result<third_sd_end]
  print("{}% of data lies within first standard deviation".format(len(first_list_of_data)*100/len(dat)))
  print("{}% of data lies within second standard deviation".format(len(second_list_of_data)*100/len(dat)))
  print("{}% of data lies within third standard deviation".format(len(third_list_of_data)*100/len(dat)))

  fig = ff.create_distplot([dat], ['Result'])
  fig.show()

data(scores)
