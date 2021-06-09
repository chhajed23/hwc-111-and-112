import pandas as pd
import statistics
import plotly.express as px
import numpy as np
import csv
import plotly.figure_factory as ff
import seaborn as sns
df=pd.read_csv("savings_data.csv")
fig=px.scatter(df,y="quant_saved",color="highschool_completed")
fig.show()
df.head()
df.highschool_completed.value_counts()

with open("savings_data.csv",newline="") as f:
  reader=csv.reader(f)
  savings_data=list(reader)
savings_data.pop(0)
total_enteries=len(savings_data)
total_people_given_reminder=0
for data in savings_data:
  if int(data[3])==1:
    total_people_given_reminder+=1
import plotly.graph_objects as go
fig=go.Figure(go.Bar(x=["reminded","not Reminded"],y=[total_people_given_reminder,(total_enteries-total_people_given_reminder)]))
fig.show()
print("Mean of Savings ",df.quant_saved.mean())
print("Mode of Savings ",df.quant_saved.mode())
print("Median of Savings ",df.quant_saved.median())
df_reminded=df[df["highschool_completed"]==1]
df_reminded
print("People who are reminded")
print("Mean of Savings  ",df_reminded.quant_saved.mean())
print("Mode of Savings ",df_reminded.quant_saved.mode())
print("Median of Savings ",df_reminded.quant_saved.median())
print("Standard Deviation of Savings ",df_reminded.quant_saved.std())
df_not_reminded=df[df["highschool_completed"]==0]
df_not_reminded
print("People who are not reminded")
print("Mean of Savings  ",df_not_reminded.quant_saved.mean())
print("Mode of Savings ",df_not_reminded.quant_saved.mode())
print("Median of Savings ",df_not_reminded.quant_saved.median())
print("Standard Deviation of Savings: ",df.quant_saved.std())
print("Standard Deviation of Savings with reminder: ",df_reminded.quant_saved.std())
print("Standard Deviation of Savings without reminder: ",df_not_reminded.quant_saved.std())

age=[]
savings=[]
with open("savings_data.csv",newline="") as f:
  reader=csv.reader(f)
  savings_data=list(reader)
savings_data.pop(0)
for data in savings_data:
  if float(data[4])!=0:
    age.append(float(data[3]))
    savings.append(float(data[0]))
correlation=np.corrcoef(age,savings)
print("Correlation between the age of the person and their saving is: ",correlation[0,1])
df.corr()
fig=ff.create_distplot([df["quant_saved"].tolist()],["savings"],show_hist=False)
fig.show()
sns.boxplot(data=df,x=df["quant_saved"])

q1=df["quant_saved"].quantile(0.25)
q3=df["quant_saved"].quantile(0.75)
iqr=q3-q1
print("Q1= ",q1)
print("Q3= ",q3)
print("iqr= ",iqr)
lowerWhisker=q1-1.5*iqr
upperWhisker=q3+1.5*iqr
print("lower Whisker= ",lowerWhisker)
print("upper Whisker= ",upperWhisker)
new_df=df[df["quant_saved"]<upperWhisker]
new_df
print("mean is= ",new_df.quant_saved.mean())
print("mode is= ",new_df.quant_saved.mode())
print("median is= ",new_df.quant_saved.median())
print("sd is= ",new_df.quant_saved.std())
fig=ff.create_distplot([new_df["quant_saved"]],["savings"],show_hist=False)
fig.show()
import random
sampling_mean_list=[]
for i in range(1000):
  temp_list=[]
  for j in range(100):
    temp_list.append(random.choice(new_df["quant_saved"].tolist()))
  sampling_mean_list.append(statistics.mean(temp_list))
mean_sampling=statistics.mean(sampling_mean_list)
fig=ff.create_distplot([sampling_mean_list],["savings_sampling"],show_hist=False)
fig.add_trace(go.Scatter(x=[mean_sampling,mean_sampling],y=[0,0.1],mode="lines",name="mean"))
fig.show()
ssd=statistics.stdev(sampling_mean_list)
print("ssd is ",ssd)
pop_mean=new_df.quant_saved.mean()
print("Mean of population ",pop_mean)
print("Mean of smpling distribution ",mean_sampling)
print("sd of population ",new_df.quant_saved.std())
print("sd of sampling data ",ssd)
temp_df=new_df[new_df.age!=0]
age=temp_df["age"].tolist()
savings=temp_df["quant_saved"].tolist()
correlation=np.corrcoef(age,savings)
print("Correlation between the age of the person and their saving is: ",correlation[0,1])
df_reminded=new_df[new_df["highschool_completed"]==1]
df_not_reminded=new_df[new_df["highschool_completed"]==0]
fig=ff.create_distplot([df_not_reminded["quant_saved"]],["Savings(not reminded)"],show_hist=False)
fig.show()

sampling_mean_list_notReminded=[]
for i in range(1000):
  temp_list=[]
  for j in range(100):
    temp_list.append(random.choice(df_not_reminded["quant_saved"].tolist()))
  sampling_mean_list_notReminded.append(statistics.mean(temp_list))
mean_sampling_not_reminded=statistics.mean(sampling_mean_list_notReminded)
fig=ff.create_distplot([sampling_mean_list_notReminded],["savings_sampling"],show_hist=False)
fig.add_trace(go.Scatter(x=[mean_sampling_not_reminded,mean_sampling_not_reminded],y=[0,0.1],mode="lines",name="mean"))
fig.show()
sd_not_reminded=statistics.stdev(sampling_mean_list_notReminded)
print(f"mean of not reminded sampling {mean_sampling_not_reminded}\nsd of not reminded sampling {sd_not_reminded}")
fsds,fsde=mean_sampling_not_reminded-sd_not_reminded,mean_sampling_not_reminded+sd_not_reminded
ssds,ssde=mean_sampling_not_reminded-(2*sd_not_reminded),mean_sampling_not_reminded+(2*sd_not_reminded)
tsds,tsde=mean_sampling_not_reminded-(3*sd_not_reminded),mean_sampling_not_reminded+(3*sd_not_reminded)
print(f"first(Start) = {fsds} and first(end)= {fsde}")
print(f"Second(Start) = {ssds} and Second(end)= {ssde}")
print(f"Third(Start) = {tsds} and Third(end)= {tsde}")
sampling_mean_list_Reminded=[]
for i in range(1000):
  temp_list=[]
  for j in range(100):
    temp_list.append(random.choice(df_reminded["quant_saved"].tolist()))
  sampling_mean_list_Reminded.append(statistics.mean(temp_list))
mean_sampling_reminded=statistics.mean(sampling_mean_list_Reminded)
fig=ff.create_distplot([sampling_mean_list_Reminded],["savings_sampling"],show_hist=False)
fig.add_trace(go.Scatter(x=[mean_sampling_reminded,mean_sampling_reminded],y=[0,0.1],mode="lines",name="mean"))
fig.show()
sd_reminded=statistics.stdev(sampling_mean_list_Reminded)
print(f"mean of reminded sampling {mean_sampling_reminded}\nsd of reminded sampling {sd_reminded}")
fsds,fsde=mean_sampling_reminded-sd_reminded,mean_sampling_reminded+sd_reminded
ssds,ssde=mean_sampling_reminded-(2*sd_reminded),mean_sampling_reminded+(2*sd_reminded)
tsds,tsde=mean_sampling_reminded-(3*sd_reminded),mean_sampling_reminded+(3*sd_reminded)
print(f"first(Start) = {fsds} and first(end)= {fsde}")
print(f"Second(Start) = {ssds} and Second(end)= {ssde}")
print(f"Third(Start) = {tsds} and Third(end)= {tsde}")
zscore=(mean_sampling_reminded-mean_sampling_not_reminded)/sd_not_reminded
print("the zscore is ",zscore)



