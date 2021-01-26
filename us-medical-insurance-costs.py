#!/usr/bin/env python
# coding: utf-8

# # U.S. Medical Insurance Costs

# 
# As the smoking is a practice that affects many people even young people and could have some health effects, is important to point out some aspects related with smoking and the cost of an insurance. 
# 
# According that the objective to achive is revelated some aspects of the life of smoker people based in the given information , so according with that the points to be checked are as follow:
# 
# * Find out the average age of the smokers patients in the dataset.
# * Analyze where the most of the smokers are from.
# * Look at the different costs between smokers vs non-smokers average.
# * Discover if there a realtion between being a smoker and the BMI.
# 
# The project is provided for  data that describes insurance cost depending diferents variables as age, sex, bmi, number of children, if the person is smoker or not, region. It counts with a poblation of 1338 persons.
# The Data is obtained from [Insurance Data](https://www.kaggle.com/mirichoi0218/insurance).

# ***
# ## Implementation Process
# ### Importing libreries
# 
# First at all, the necessaries libraries are going to be imported. In this particular project:
# 
# * csv
# 

# In[1]:


import csv


# ### Importing data 
# 
# The data will be stored in lists object that lives inside a Class, the contrcutor is in charge of build one list for each of the filed inside de csv file:
# 
# * age
# * sex
# * bmi
# * children
# * smoker
# * region
# * charges
# 

# In[11]:


class Medata:
    age = []
    sex = []
    bmi = []
    children = []
    smoker = []
    region = []
    charges = []
    def __init__(self):
        with open('insurance.csv', newline = '') as med_file:
            med_dic = csv.DictReader(med_file)
            for row in med_dic:
                self.age.append(int(row['age']))
                self.sex.append(row['sex'])
                self.bmi.append(float(row['bmi']))
                self.children.append(row['children'])
                self.smoker.append(row['smoker'])
                self.region.append(row['region'])
                self.charges.append(float(row['charges']))


# #### Creating the class object
# 
# In order to finnish the data importing a class object has to be defined, in this case the object is going to be  **country**

# In[15]:


country = Medata()


# ***
# ### Findings Answers
# #### Average age of the smokers patients
# 
# To answer this question a function is defined as follows:

# In[4]:


def average_age(country):
    smoker_list = []
    total_smoker = 0
    for i in range(len(country.smoker)):
        if country.smoker[i] == 'yes':
            smoker_list.append(country.age[i])
    for i in smoker_list:
        total_smoker += i
    average_smoker = total_smoker/len(smoker_list)
    print('The average smoker age is {}'.format(average_smoker))
# Calling the function
average_age(country)


# According with the calculation the average smoker age is 38.51459854014598.
# 
# #### Where the most of the smokers are from
# 
# To answer this question a function is defined as follows:

# In[5]:


def mostsmoker(country):
    smoker_list = []
    for i in range(len(country.smoker)):
        if country.smoker[i] == 'yes':
            smoker_list.append(country.region[i])
    northeast_smokers = smoker_list.count('northeast')
    northwest_smokers = smoker_list.count('northwest')
    southeast_smokers = smoker_list.count('southeast')
    southwest_smokers = smoker_list.count('southwest')
    if northeast_smokers >  northwest_smokers and northeast_smokers > southeast_smokers and northeast_smokers > southwest_smokers:
        most_smokers = 'northeast'
    elif northwest_smokers > southeast_smokers and northwest_smokers > southwest_smokers:
        most_smokers = 'northwest'
    elif southeast_smokers > southwest_smokers:
        most_smokers = 'southeast'
    else:
        most_smokers = 'southwest'
    print('The most of the smokers are in {}'.format(most_smokers))
# Calling the function
mostsmoker(country)
    


# According with the calculation the most the smokers are in southeast.
# 
# #### Different costs between smokers vs non-smokers
# 
# To answer this question a function is defined as follows:
# 

# In[ ]:


def difcost(country):
    smoker_list = []
    no_smoker_list = []
    for i in range(len(country.smoker)):
        if country.smoker[i] == 'yes':
            smoker_list.append(country.charges[i])
        else:
            no_smoker_list.append(country.charges[i])
    total_smoker = 0
    no_total_smoker = 0
    for i in smoker_list:
        total_smoker += i
    for i in no_smoker_list:
        no_total_smoker += i
    av_smoker = total_smoker/len(smoker_list)
    av_no_smoker = no_total_smoker / len(no_smoker_list)
    dif = av_smoker - av_no_smoker
    if dif > 0:
        print('The average insurance cost is bigger for smokers persons by {}'.format(abs(dif)))
    elif dif == 0:
        print('There is no differences between the insurance cost of smokers and non-smokers persons')
    else:
        print('The average insurance cost is bigger for non-smokers persons by {}'.format(abs(dif)))
# Calling function
difcost(country)


# According with the calculation an smoker person pay in average 23615.96353367665 more than a non-smoker person.
# 
# #### Realtion between being a smoker and the BMI
# 
# To answer this question a function is defined as follows:
# 

# In[16]:


def smokerbmi(country):
    total = 0
    smoker_total = 0
    smoker_list = []
    for i in range(len(country.smoker)):
        if country.smoker[i] == 'yes':
            smoker_list.append(country.bmi[i])
    for i in country.bmi:
        total += i
    for i in smoker_list:
        smoker_total += i
    av_total = total / len(country.smoker)
    av_total_smoker = smoker_total / len(smoker_list)
    dif = av_total_smoker - av_total
    if dif > 0 :
        print('In average the smoker person has an higher BMI')
    elif dif == 0:
        print('There is no differences between the BMI of smokers and non-smokers persons ')
    else:
        print('In average the non-smoker person has an higher BMI')
#Calling the function
smokerbmi(country)


# According with the calculation an smoker person has higher BMI.
# ***
# ## Conclusions
# 
# After built the function and once the calcualtion have donde the conclusion are:
# 
# * The average age of the smokers are 38.51, that means that for this poblation the smoker in young people should not be a problem.
# * The most of the smokers are from southeast, it is necesarie further information and analisys to find why it is.
# * A smoker person pay in average 23615.96353367665 more than a non-smoker person, normally smoking add risk to the health itself and as effect of it, the cost in insurance increase.
# * It seems that in average the smoker person has an higher BMI, however that does not mean that it is healhty risk indicator because an higher BMI depends of differents aspect that could vari in each person. So, BMI could be high for one person but good for another one. So, it is needed futher investagation including if BMI is higher, lower or healhty  for each person.
