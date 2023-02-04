import pandas as pd

df = pd.read_csv('Database.csv')
number_of_entries = len(df)

class ImportantMetrics:

    def __init__(self, metric_list):
        self.metric_list = metric_list



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

    def commits_per_hour(self,date_range=int):
        total_commits=0
        total_hours_coding=0
        for i in range(1,date_range+1):
            total_commits += df.iloc[number_of_entries -i]['GitHub Contributions']
            total_hours_coding += df.iloc[number_of_entries -i]['Coding Hours']
        commits_per_hour = round(total_commits/total_hours_coding, 2)
        return commits_per_hour

    def get_work_reading_coding_split(self, date_range=int):
        average_time_working = 0
        average_time_coding =0
        average_time_reading=0

        for i in range(1, date_range+1):
            average_time_working += df.iloc[number_of_entries - i]['Work Hours']
            average_time_coding += df.iloc[number_of_entries - i]['Coding Hours']
            average_time_reading += df.iloc[number_of_entries - i]['Reading Hours']
        
        percent_of_working_spent_coding = round((float(average_time_coding) / float(average_time_working))*100)
        
        average_time_working_not_coding = average_time_working - average_time_coding
        total_time_spent = average_time_working_not_coding + average_time_coding + average_time_reading
        split_list = [average_time_working_not_coding, average_time_coding,  average_time_reading]
        for index,value in enumerate(split_list):
            split_list[index] =round((value/total_time_spent)*100)
            

        return percent_of_working_spent_coding, split_list