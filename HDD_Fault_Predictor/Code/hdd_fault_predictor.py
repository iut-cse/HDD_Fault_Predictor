import pandas as pd

class Process_Fault_time:



    def data_processing_fault_time(self,cur_date):
        self.df = pd.read_csv("../Data/disk_sample_fault_tag.csv", skiprows=1)

        self.df.columns = ["manufacturer", "model", "serial_number", "fault_time", "tag"]

    # selecting rows based on condition
        self.df = self.df[self.df['fault_time'] <= cur_date]
        self.df.reset_index(inplace=True,drop = True)


        return  self.df.to_csv('../Data/fault_time.csv')


# let say contestants want to get the failure prediction results of 20171020,

p=Process_Fault_time()
p.data_processing_fault_time('2017-10-20')
