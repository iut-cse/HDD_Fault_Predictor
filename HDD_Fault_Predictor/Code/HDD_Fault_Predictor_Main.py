import Fault_time_processor as f
import Data_preprocessing  as d
import PCA as pca
import Logistic_Regression as logisticRegression
import Naive_Bayes as naive_bayes
import logisticRegression_using_library as lr_library
import naive_bayes_using_library as nb_libary
date ='2017-10-20'
days = 30
# Data Preprocessing
#data= d.Data_Process('../Data/disk_sample_smart_log_201707.csv')
#faulty=f.Process_Fault_time()

#faulty.data_processing_fault_time(date)#
#data.update_failure_tag('../Data/fault_time.csv')

#data.tag(days) # to predict failure upto next 30 days
# PCA

pca.PCA('../Data/Final.csv')

#Logistic Regression
print("Logistic Regression (Manually) :")
print("\n")
logisticRegression.accuracy_result()
print("\n")
print("Logistic Regression (Using library): ")
print("\n")

lr_library.logistic_Regression_library()
print("\n")
print("Naive Bayes (Manually) :")
print("\n")
naive_bayes.accuracy_result()
print("\n")
print("Naive Bayes (Using library):")
print("\n")
nb_libary.run()



