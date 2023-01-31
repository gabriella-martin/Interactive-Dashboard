import pandas as pd

df = pd.read_csv('Database.csv')
number_of_entries = len(df)

class ImportantMetrics:

    def __init__(self, metric_list):
        self.metric_list = metric_list

        
        time_period_percent_change = []

    def get_time_period_metric(self, date_range=int):
        time_period_averages = []
        for i in self.metric_list:
            time_period_metric = 0
            for a in range(1,date_range+1):
                time_period_metric += df.iloc[number_of_entries-a][i]
            time_period_averages.append(round(time_period_metric/date_range))
        return time_period_averages

    def get_time_period_percent_change(self,date_range=int):
        time_period_averages = self.get_time_period_metric(date_range)
        time_period_before_averages = []
        time_period_percent_change = []
        for i in self.metric_list:
            time_period_before_metric = 0
            for a in range(1 +date_range,(date_range*2)+1):
                time_period_before_metric += df.iloc[number_of_entries-a][i]
            time_period_before_averages.append(round(time_period_before_metric/date_range))

        for index, value in enumerate(time_period_averages):
            percent_change = round(((value - time_period_before_averages[index])/time_period_before_averages[index])*100)
            time_period_percent_change.append(percent_change)

        return time_period_percent_change




