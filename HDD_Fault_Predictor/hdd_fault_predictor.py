import pandas as pd


def data_processing_fault_time(cur_date):
    df = pd.read_csv("../HDD_Fault_Predictor/Dataset/disk_sample_fault_tag.csv", skiprows=1)
    df.columns = ["manufacturer", "model", "serial_number", "fault_time", "tag"]

    # selecting rows based on condition
    rslt_df = df[df['fault_time'] <= cur_date]

    print('\nResult dataframe :\n', rslt_df)


# let say today's date 2017-10-20
data_processing_fault_time('2017-10-20')
