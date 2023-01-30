import pandas as pd
df = pd.read_csv('Database.csv')
number_of_entries = len(df)

class ImportantMetrics:

    def __init__(self, metric_list):
        self.metric_list = metric_list
        self.yesterdays_metrics = []
        self.yesterday_vs_day_before_yesterday_percent_change = []
        self.three_day_averages = []
        self.current_three_day_vs_past_three_day = [] 
        self.seven_day_averages = []
        self.current_seven_day_vs_past_seven_day = []

    def get_yesterdays_metrics(self):
        for i in self.metric_list:
            yesterday_metric = df.iloc[number_of_entries -1][i]
            self.yesterdays_metrics.append(yesterday_metric)
        return self.yesterdays_metrics

    def get_yesterday_percentage_change(self):
        self.yesterdays_metrics = self.get_yesterdays_metrics()
        for index, value in enumerate(self.yesterdays_metrics):
            percent_change = round((((value - (df.iloc[number_of_entries-2])[self.metric_list[index]]))/((df.iloc[number_of_entries-2])[metric_list[index]]))*100)
            self.yesterday_vs_day_before_yesterday_percent_change.append(percent_change)
        return self.yesterday_vs_day_before_yesterday_percent_change
    
    def get_three_day_averages(self):
        for category in self.metric_list:
            three_day_sum = 0
            for i in range(1,4):
                metric = df.iloc[number_of_entries - i][category]
                three_day_sum = three_day_sum + metric
            three_day_average =round((three_day_sum)/3)
            self.three_day_averages.append(three_day_average)
        return self.three_day_averages

    def get_three_day_percentage_change(self):
        self.three_day_averages = self.get_three_day_averages 
        for index, value in enumerate(self.three_day_averages):
            three_day_earlier_average = ((((df.iloc[number_of_entries-4])[self.metric_list[index]]) + (df.iloc[number_of_entries-5][self.metric_list[index]]) + (df.iloc[number_of_entries-6])[self.metric_list[index]]))/3
            percent_change = round((((value - three_day_earlier_average))/three_day_earlier_average)*100)
            self.current_three_day_vs_past_three_day.append(percent_change)
        return self.current_three_day_vs_past_three_day

    def get_seven_day_averages(self):
        for category in self.metric_list:
            seven_day_sum = 0
            for i in range(1,8):
                metric = df.iloc[number_of_entries - i][category]
                seven_day_sum = seven_day_sum + metric
            seven_day_average =round((seven_day_sum)/7)
            self.seven_day_averages.append(seven_day_average)
        return self.seven_day_averages

    def get_seven_day_percentage_change(self):
        self.seven_day_averages = self.get_seven_day_averages()
        for index, value in enumerate(self.seven_day_averages):
            seven_day_earlier_average = ((((df.iloc[number_of_entries-8])[self.metric_list[index]]) + (df.iloc[number_of_entries-9][self.metric_list[index]]) + (df.iloc[number_of_entries-10])[self.metric_list[index]]) + 
        (df.iloc[number_of_entries-11][self.metric_list[index]]) + (df.iloc[number_of_entries-12][self.metric_list[index]]) + (df.iloc[number_of_entries-13][self.metric_list[index]]) + (df.iloc[number_of_entries-14][self.metric_list[index]]) )/7
            percent_change = round((((value - seven_day_earlier_average))/seven_day_earlier_average)*100)
            self.current_seven_day_vs_past_seven_day.append(percent_change)
        return self.current_seven_day_vs_past_seven_day