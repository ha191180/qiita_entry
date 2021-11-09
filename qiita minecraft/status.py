#!/usr/bin/env python3
import sys

sys.path.append('/home/ubuntu/.local/lib/python3.8/site-packages')

import boto3
from datetime import datetime
from datetime import timedelta
from matplotlib import pyplot
import pandas
import seaborn as sns

def make_statistics_file():
  client = boto3.client('lightsail')


  responce = client.get_instance_metric_data( instanceName='Minecraft1',
                                              metricName='BurstCapacityPercentage',
                                              period=120,
                                              startTime=datetime.now() + timedelta(days=-2),
                                              endTime=datetime.now(),
                                              unit='Percent',
                                              statistics=['Maximum'])

  df = pandas.DataFrame(columns=['Capacity','Time'])


  for h,i in enumerate(responce['metricData']):
    df.loc[h] = [(i['maximum']),i['timestamp']]
  df.set_index('Time',inplace=True)
  sns.set()
  sns.set_style(style='dark')
  df.plot(grid=True)
  pyplot.tick_params(labelsize=9)
  pyplot.ylim(-1, 101)
  pyplot.title(datetime.now().strftime('%m/%d %H:%M') + " created.")
  pyplot.savefig('/home/ubuntu/tmppictures/stat.png')
  pyplot.close('all')




if __name__=='__main__':
  make_statistics_file()
