import numpy as np
import pandas as pd
import math
import csv

def mail_category(file_path):
    predictions = {}
    df = pd.read_csv(file_path)
    total_count = 0
    total_count_true = 0
    total_count_false = 0
    ##print df.head()
    ##print df.dtypes

    tc = df.user_id.count()
    tc_true = df.user_id[df.opened == True].count()
    tc_false = df.user_id[df.opened == False].count()
    print tc,total_count_false,total_count
    print (tc_true*1.0)/tc,(tc_false*1.0)/tc

    '''mail_categorys = df.groupby('mail_category')
    print mail_categorys['user_id'].count(),mail_categorys['user_id'].count()/total_count
    print df.user_id[df.mail_category=="mail_category_1"].count()
    print df.user_id[df.mail_category.isnull()].count()
    '''
    mail_categorys = df.mail_category.unique()
    #print math.isnan(mail_categorys[18])
    print df.mail_category.count()
    for mc in mail_categorys:
        mcc = df.user_id[df.mail_category==mc].count()
        mctc =df.user_id[(df.mail_category==mc) & (df.opened == True)].count()
        mcfc =df.user_id[(df.mail_category==mc) & (df.opened == False)].count()
        print mc,'\t', mcc, '\t',mctc, '\t',mcfc, '\t',\
              (mctc*1.0)/mcc , '\t',(mcfc*1.0)/mcc, '\t',\
              (mctc*1.0)/tc_true, '\t',(mcfc*1.0)/tc_false,  '\t',(mcc*1.0)/tc

    mc ='Empty'
    mcc = df.user_id[df.mail_category.isnull()].count()
    mctc =df.user_id[(df.mail_category.isnull()) & (df.opened == True)].count()
    mcfc =df.user_id[(df.mail_category.isnull()) & (df.opened == False)].count()
    print mc,'\t', mcc, '\t',mctc, '\t',mcfc, '\t',\
              (mctc*1.0)/mcc , '\t',(mcfc*1.0)/mcc, '\t',\
              (mctc*1.0)/tc_true, '\t',(mcfc*1.0)/tc_false,  '\t',(mcc*1.0)/tc

    ##print df.mail_category.isnull()

def mail_type(file_path):
    predictions = {}
    df = pd.read_csv(file_path)
    total_count = 0
    total_count_true = 0
    total_count_false = 0

    tc = df.user_id.count()
    tc_true = df.user_id[df.opened == True].count()
    tc_false = df.user_id[df.opened == False].count()
 

    mail_types = df.mail_type.unique()
    
    print df.mail_type.count()
    for mc in mail_types:
        mcc = df.user_id[df.mail_type==mc].count()
        mctc =df.user_id[(df.mail_type==mc) & (df.opened == True)].count()
        mcfc =df.user_id[(df.mail_type==mc) & (df.opened == False)].count()
        print mc,'\t', mcc, '\t',mctc, '\t',mcfc, '\t',\
              (mctc*1.0)/mcc , '\t',(mcfc*1.0)/mcc, '\t',\
              (mctc*1.0)/tc_true, '\t',(mcfc*1.0)/tc_false,  '\t',(mcc*1.0)/tc

    mc ='Empty'
    mcc = df.user_id[df.mail_type.isnull()].count()
    mctc =df.user_id[(df.mail_type.isnull()) & (df.opened == True)].count()
    mcfc =df.user_id[(df.mail_type.isnull()) & (df.opened == False)].count()
    print mc,'\t', mcc, '\t',mctc, '\t',mcfc, '\t',\
              (mctc*1.0)/mcc , '\t',(mcfc*1.0)/mcc, '\t',\
              (mctc*1.0)/tc_true, '\t',(mcfc*1.0)/tc_false,  '\t',(mcc*1.0)/tc


def predict_email_opens_result0(file_path):
    predictions = {}
    df = pd.read_csv(file_path)
    predictions_file = open("prediction.csv", "wb")
    predictions_file_object = csv.writer(predictions_file)
    #predictions_file_object.writerow(["user_id"])
    for user_index, user in df.iterrows():
        user_id = user['user_id']
        mc = user['mail_category']
        mt = user['mail_type']

        if (mc == 'mail_category_1' or  mc == 'mail_category_4' or \
           mc == 'mail_category_13' or  mc == 'mail_category_3' or \
           mc == 'mail_category_15' or  mc == 'mail_category_7') or \
           (mt == 'mail_type_1' or mt == 'mail_type_2'):
            predictions_file_object.writerow("1")	
            #predictions[user_id] = 1
        else:
            #predictions[user_id] = 0
            predictions_file_object.writerow("0")
    predictions_file.close()
    #return predictions

def predict_email_opens_result(file_path):
    predictions = {}
    df = pd.read_csv(file_path)
    predictions_file = open("prediction.csv", "wb")
    predictions_file_object = csv.writer(predictions_file)
    #predictions_file_object.writerow(["user_id"])
    for user_index, user in df.iterrows():
        user_id = user['user_id']
        mc = user['mail_category']
        mt = user['mail_type']
        htz = user['hacker_timezone']
        clc = user['contest_login_count']

        if (mc == 'mail_category_1' or  mc == 'mail_category_4' or \
            mc == 'mail_category_13' or  mc == 'mail_category_3' or \
            mc == 'mail_category_15' or  mc == 'mail_category_7') and \
           (htz == -25200 or  htz == -14400 or htz == -10800 or \
            htz == 7200 or htz == 10800 or htz == 18000):
            predictions_file_object.writerow("1")	
            #predictions[user_id] = 1
        else:
            #predictions[user_id] = 0
            predictions_file_object.writerow("0")
    predictions_file.close()
    #return predictions    
    

file_path = "E:\\hackerrank\\Predict Email Opens\\dataset\\"
##file_path = "C:\\DNS\\Course\\hackerrank\\Predict Email Opens\\dataset\\"
tra_file_path= file_path+"training_dataset.CSV"
#mail_category(tra_file_path)
#mail_type(tra_file_path)

test_file_path= file_path+"test_dataset.csv"
predict_email_opens_result(test_file_path)
