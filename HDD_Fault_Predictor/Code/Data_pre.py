import pandas as pd
import hdd_fault_predictor as r
import numpy as np

class Data_Process:

    def __init__(self, data_csv):
        #read train data
        self.df = pd.read_csv(data_csv,usecols=['serial_number', 'manufacturer', 'model', 'dt','smart_5_normalized','smart_187_normalized','smart_188_normalized','smart_197_normalized','smart_198_normalized','smart_9_normalized','smart_193_normalized','smart_194_normalized','smart_241_normalized','smart_242_normalized'],keep_default_na=False, na_values=[""])

        self.df.fillna(0, inplace=True)


    def update_failure_tag(self,fault_time):
        #read fault data from fault-time
        self.fault_tag=pd.read_csv(fault_time,keep_default_na=False, na_values=[""])




    def tag(self,n):
         # extract faulty datarows from train data using faultTag data
        self.merged_inner = pd.merge(left=self.df, right=self.fault_tag)
        #the faulty one....
         # tag faulty as 1 if fault_time - (minus) sample time<=n (n=10 so 10 din er kome jegulo fault hobe segulo 1 ,bakigulo 0)
        self.merged_inner['faulty']=np.where(self.merged_inner['fault_time'].str.replace(r'\D+', '').astype(int)-self.merged_inner['dt']<= n,1,0)
        #extract faulty sample
        self.fault=self.merged_inner[self.merged_inner['faulty']==1]
        #filtering coloumns
        self.f_n = self.fault.filter(['serial_number', 'manufacturer', 'model', 'dt','smart_5_normalized','smart_187_normalized','smart_188_normalized','smart_197_normalized','smart_198_normalized','smart_9_normalized','smart_193_normalized','smart_194_normalized','smart_241_normalized','smart_242_normalized'])

        self.f_n.fillna(0, inplace=True)
        #concat the main dataset and the fault values
        self.temp = pd.concat([self.df, self.f_n])


#the good_one
#Extract duplicates values
        self.good_one = self.temp.drop_duplicates(keep=False)
        r=self.good_one.copy()
        r['faulty'] = 0
        self.good_one.reset_index(inplace=True, drop=True)


        self.f_n['faulty']=1

        self.data=pd.concat([r, self.f_n])
        self.data = self.data.sample(frac=1).reset_index(drop=True)

        self.data.fillna(0,inplace=True)








        return self.df.to_csv('../Data/Features.csv'),self.data.to_csv('../Data/Final.csv'),self.good_one.to_csv('../Data/GoodHDD.csv'),self.f_n.to_csv('../Data/FaultyHDD.csv')

    def convert_fill(self,dfr):
        return dfr.stack().apply(pd.to_numeric, errors='ignore').fillna(0).unstack()




d=Data_Process('../Data/disk_sample_smart_log_201707.csv')
p=r.Process_Fault_time()
p.data_processing_fault_time('2017-10-20')

d.update_failure_tag('../Data/fault_time.csv')
d.tag(30)


