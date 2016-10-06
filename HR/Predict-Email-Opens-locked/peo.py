import numpy as np
import pandas as pd
import math
import csv
import MySQLdb

def loadsql_testdataset(file_path):
    mydb = MySQLdb.connect(host='localhost',
        user='root', passwd='pwd1', db='hackerank')
    cursor = mydb.cursor()

    csv_data = csv.reader(file(file_path))
    
    for row in csv_data:

          cursor.execute('INSERT INTO predict_email_opens_testdata(user_id, mail_id, \
            mail_category, mail_type, sent_time, last_online, hacker_created_at, hacker_timezone, \
            contest_login_count, contest_login_count_1_days, contest_login_count_30_days, \
            contest_login_count_365_days, contest_login_count_7_days, \
            contest_participation_count, contest_participation_count_1_days, \
            contest_participation_count_30_days, contest_participation_count_365_days, \
            contest_participation_count_7_days, forum_comments_count, forum_count, \
            forum_expert_count, forum_questions_count, hacker_confirmation, \
            ipn_count, ipn_count_1_days, ipn_count_30_days, ipn_count_365_days, ipn_count_7_days, \
            ipn_read, ipn_read_1_days, ipn_read_30_days, ipn_read_365_days, ipn_read_7_days, \
            submissions_count, submissions_count_1_days, submissions_count_30_days, \
            submissions_count_365_days, submissions_count_7_days, \
            submissions_count_contest, submissions_count_contest_1_days, submissions_count_contest_30_days, \
            submissions_count_contest_365_days, submissions_count_contest_7_days, submissions_count_master, \
            submissions_count_master_1_days, submissions_count_master_30_days, \
            submissions_count_master_365_days, submissions_count_master_7_days)' \
              'VALUES(%s, %s, \
            %s, %s, %s, %s, %s, %s, \
            %s, %s, %s, \
            %s, %s, \
            %s, %s, \
            %s, %s, \
            %s, %s, %s, \
            %s, %s, %s, \
            %s, %s, %s, %s, %s, \
            %s, %s, %s, %s, %s, \
            %s, %s, %s, \
            %s, %s, \
            %s, %s, %s, \
            %s, %s, %s, \
            %s, %s, \
            %s, %s)', 
          row)
        #close the connection to the database.
    mydb.commit()
    cursor.close()
    '''
    update hackerank.predict_email_opens set opened = replace(opened,"'","")
    '''

def loadsql(file_path):
    mydb = MySQLdb.connect(host='localhost',
        user='root', passwd='pwd1', db='hackerank')
    cursor = mydb.cursor()

    csv_data = csv.reader(file(file_path))
    
    for row in csv_data:
        cursor.execute('INSERT INTO predict_email_opens(opened, user_id, mail_id, \
            mail_category, mail_type, sent_time, last_online, hacker_created_at, hacker_timezone, \
            contest_login_count, contest_login_count_1_days, contest_login_count_30_days, \
            contest_login_count_365_days, contest_login_count_7_days, \
            contest_participation_count, contest_participation_count_1_days, \
            contest_participation_count_30_days, contest_participation_count_365_days, \
            contest_participation_count_7_days, forum_comments_count, forum_count, \
            forum_expert_count, forum_questions_count, hacker_confirmation, \
            ipn_count, ipn_count_1_days, ipn_count_30_days, ipn_count_365_days, ipn_count_7_days, \
            ipn_read, ipn_read_1_days, ipn_read_30_days, ipn_read_365_days, ipn_read_7_days, \
            submissions_count, submissions_count_1_days, submissions_count_30_days, \
            submissions_count_365_days, submissions_count_7_days, \
            submissions_count_contest, submissions_count_contest_1_days, submissions_count_contest_30_days, \
            submissions_count_contest_365_days, submissions_count_contest_7_days, submissions_count_master, \
            submissions_count_master_1_days, submissions_count_master_30_days, \
            submissions_count_master_365_days, submissions_count_master_7_days)' \
              'VALUES("%s", "%s", "%s", \
            "%s", "%s", "%s", "%s", "%s", "%s", \
            "%s", "%s", "%s", \
            "%s", "%s", \
            "%s", "%s", \
            "%s", "%s", \
            "%s", "%s", "%s", \
            "%s", "%s", "%s", \
            "%s", "%s", "%s", "%s", "%s", \
            "%s", "%s", "%s", "%s", "%s", \
            "%s", "%s", "%s", \
            "%s", "%s", \
            "%s", "%s", "%s", \
            "%s", "%s", "%s", \
            "%s", "%s", \
            "%s", "%s")', 
          row)
        #close the connection to the database.
    mydb.commit()
    cursor.close()
    '''
    update hackerank.predict_email_opens set opened = replace(opened,"'","")
    '''
    
def attributes(file_path):
    ou_file = open('data_set_out.txt', 'a')
    predictions = {}
    df = pd.read_csv(file_path)
    total_count = 0
    total_count_true = 0
    total_count_false = 0
    ##print df.head()
    ##print df.dtypes

    '''mail_categorys = df.groupby('mail_category')
    print mail_categorys['user_id'].count(),mail_categorys['user_id'].count()/total_count
    print df.user_id[df.mail_category=="mail_category_1"].count()
    print df.user_id[df.mail_category.isnull()].count()
    '''
    #print math.isnan(mail_categorys[18])
    ##print df.mail_category.isnull()

    col_names = list(df.columns.values)
    total = df.user_id.count()
    total_true = df.user_id[df.opened == True].count()
    total_false = df.user_id[df.opened == False].count()
    print>>ou_file,'Total-TT\tTotal True-TTT\tTotal False-TTF'
    print>>ou_file,total,'\t',total_true,'\t',total_false
    print>>ou_file,''
    
    for col_name in col_names:
        if (col_name!='opened' and col_name!='user_id' and \
            col_name!='mail_id' and col_name!='sent_time' and \
            col_name!='last_online' and col_name!='hacker_created_at'):
            col_name_values = df[col_name].unique()

            headers=['Col Value-1','CV Count-2','CVT Count-3',\
                             'CVF Count-4', '3 D 2','4 D 2','3 D TTT', \
                             '4 D TTF','2 D TT','3 D TT']
            #print headers
            row_list=[]
            for cn_value in col_name_values:
                cnv_count = df.user_id[df[col_name]==cn_value].count()
                cnv_true_count =df.user_id[(df[col_name]==cn_value) & (df.opened == True)].count()
                cnv_false_count =df.user_id[(df[col_name]==cn_value) & (df.opened == False)].count()
                row_list.append([cn_value, cnv_count, cnv_true_count, cnv_false_count, \
                    (cnv_true_count*1.0)/cnv_count, \
                    (cnv_false_count*1.0)/cnv_count, \
                    (cnv_true_count*1.0)/total_true,
                    (cnv_false_count*1.0)/total_false, \
                    (cnv_count*1.0)/total, (cnv_true_count*1.0)/total])
                
            cn_value ='Empty'
            cnv_count = df.user_id[df[col_name].isnull()].count()
            cnv_true_count =df.user_id[(df[col_name].isnull()) & (df.opened == True)].count()
            cnv_false_count =df.user_id[(df[col_name].isnull()) & (df.opened == False)].count()
            row_list.append([cn_value, cnv_count, cnv_true_count, cnv_false_count, \
                    (cnv_true_count*1.0)/cnv_count, \
                    (cnv_false_count*1.0)/cnv_count, \
                    (cnv_true_count*1.0)/total_true,
                    (cnv_false_count*1.0)/total_false, \
                    (cnv_count*1.0)/total, (cnv_true_count*1.0)/total])
            dfc = pd.DataFrame(data = row_list, columns=headers)
            dfcs = dfc.sort_index(by=['3 D TT'], ascending=[False])
            dft = pd.DataFrame(columns=[col_name, df[col_name].count()])
            #with open(r'data_set_out.txt', 'a') as f:
            print>>ou_file, col_name,'\t',df[col_name].count()
            dfcs.to_csv(ou_file, index=None,sep='\t')
            print>>ou_file, ''
            print>>ou_file, ''
           
            '''print>>ou_file, col_name,'\t',df[col_name].count()
            for cn_value in col_name_values:
                cnv_count = df.user_id[df[col_name]==cn_value].count()
                cnv_true_count =df.user_id[(df[col_name]==cn_value) & (df.opened == True)].count()
                cnv_false_count =df.user_id[(df[col_name]==cn_value) & (df.opened == False)].count()
                print>>ou_file, cn_value,'\t', cnv_count, '\t',\
                    cnv_true_count, '\t',cnv_false_count, '\t',\
                    (cnv_true_count*1.0)/cnv_count , '\t',(cnv_false_count*1.0)/cnv_count, '\t',\
                    (cnv_true_count*1.0)/total_true, '\t',(cnv_false_count*1.0)/total_false, '\t',\
                    (cnv_count*1.0)/total, '\t', (cnv_true_count*1.0)/total

            cn_value ='Empty'
            cnv_count = df.user_id[df[col_name].isnull()].count()
            cnv_true_count =df.user_id[(df[col_name].isnull()) & (df.opened == True)].count()
            cnv_false_count =df.user_id[(df[col_name].isnull()) & (df.opened == False)].count()
            print>>ou_file, cn_value,'\t', cnv_count, '\t',\
                cnv_true_count, '\t',cnv_false_count, '\t',\
                (cnv_true_count*1.0)/cnv_count , '\t',(cnv_false_count*1.0)/cnv_count, '\t',\
                (cnv_true_count*1.0)/total_true, '\t',(cnv_false_count*1.0)/total_false, '\t',\
                (cnv_count*1.0)/total, '\t', (cnv_true_count*1.0)/total
            print>>ou_file, ''
            print>>ou_file, ''
            '''

def attributes_all(file_path):
    ou_file = open('data_set_out_all.txt', 'a')
    predictions = {}
    df = pd.read_csv(file_path)
    total_count = 0
    total_count_true = 0
    total_count_false = 0
   
    col_names = list(df.columns.values)
    total = df.user_id.count()
    total_true = df.user_id[df.opened == True].count()
    total_false = df.user_id[df.opened == False].count()
    
    for col_name in col_names:
        if (col_name!='opened' and col_name!='user_id' and \
            col_name!='mail_id' and col_name!='sent_time' and \
            col_name!='last_online' and col_name!='hacker_created_at'):
            col_name_values = df[col_name].unique()

            headers=['Col Value-T','Col Value-1','CV Count-2','CVT Count-3',\
                             'CVF Count-4', '3 D 2','4 D 2','3 D TTT', \
                             '4 D TTF','2 D TT','3 D TT']
            #print headers
            row_list=[]
            for cn_value in col_name_values:
                cnv_count = df.user_id[df[col_name]==cn_value].count()
                cnv_true_count =df.user_id[(df[col_name]==cn_value) & (df.opened == True)].count()
                cnv_false_count =df.user_id[(df[col_name]==cn_value) & (df.opened == False)].count()
                row_list.append([col_name,cn_value, cnv_count, cnv_true_count, cnv_false_count, \
                    (cnv_true_count*1.0)/cnv_count, \
                    (cnv_false_count*1.0)/cnv_count, \
                    (cnv_true_count*1.0)/total_true,
                    (cnv_false_count*1.0)/total_false, \
                    (cnv_count*1.0)/total, (cnv_true_count*1.0)/total])
                
            cn_value ='Empty'
            cnv_count = df.user_id[df[col_name].isnull()].count()
            cnv_true_count =df.user_id[(df[col_name].isnull()) & (df.opened == True)].count()
            cnv_false_count =df.user_id[(df[col_name].isnull()) & (df.opened == False)].count()
            row_list.append([col_name,cn_value, cnv_count, cnv_true_count, cnv_false_count, \
                    (cnv_true_count*1.0)/cnv_count, \
                    (cnv_false_count*1.0)/cnv_count, \
                    (cnv_true_count*1.0)/total_true,
                    (cnv_false_count*1.0)/total_false, \
                    (cnv_count*1.0)/total, (cnv_true_count*1.0)/total])
            dfc = pd.DataFrame(data = row_list, columns=headers)
            dfcs = dfc.sort_index(by=['3 D TT'], ascending=[False])
            dft = pd.DataFrame(columns=[col_name, df[col_name].count()])
            dfcs.to_csv(ou_file, index=None,sep='\t')
            
#.41
def predict_email_opens_result_0(file_path):
    predictions = {}
    df = pd.read_csv(file_path)
    predictions_file = open("prediction.csv", "wb")
    predictions_file_object = csv.writer(predictions_file)
    for user_index, user in df.iterrows():
        user_id = user['user_id']
        mc = user['mail_category']
        if (mc == 'mail_category_1' or  mc == 'mail_category_4' or \
           mc == 'mail_category_13' or  mc == 'mail_category_3' or \
           mc == 'mail_category_15' or  mc == 'mail_category_7'):
            predictions_file_object.writerow("1")	
        else:
            predictions_file_object.writerow("0")
    predictions_file.close()

def predict_email_opens_result(file_path):
    predictions = {}
    df = pd.read_csv(file_path)
    #predictions_file = open("prediction.csv", "wb")
    #predictions_file_object = csv.writer(predictions_file)

    mail_category = []
    mail_type = []
    hacker_timezone = []
    
    contest_login_count = []
    contest_login_count_1_days = []
    contest_login_count_30_days = []
    contest_login_count_365_days = []
    contest_login_count_7_days = []
    
    contest_participation_count = []
    contest_participation_count_1_days = []
    contest_participation_count_30_days = []
    contest_participation_count_365_days = []
    contest_participation_count_7_days = []
    
    forum_comments_count = []
    forum_count = []
    forum_expert_count = []
    forum_questions_count = []
    hacker_confirmation = []
    
    ipn_count = []
    ipn_count_1_days = []
    ipn_count_30_days = []
    ipn_count_365_days = []
    ipn_count_7_days = []
    
    ipn_read = []
    ipn_read_1_days = []
    ipn_read_30_days = []
    ipn_read_365_days = []
    ipn_read_7_days = []
    
    submissions_count = [606,743,855]
    submissions_count_1_days = []
    submissions_count_30_days = []
    submissions_count_365_days = [646,815,743,789,874,690,568]
    submissions_count_7_days = []
    
    submissions_count_contest = [906,448]
    submissions_count_contest_1_days = []
    submissions_count_contest_30_days = []
    submissions_count_contest_365_days = []
    submissions_count_contest_7_days = [74]
    
    submissions_count_master = [624]
    submissions_count_master_1_days = []
    submissions_count_master_30_days = []
    submissions_count_master_365_days = []
    submissions_count_master_7_days = []
    
    for user_index, user in df.iterrows():
        user_id = user['user_id']
        mc = user['mail_category']
        mt = user['mail_type']
        ht = user['hacker_timezone']

        clc = user['contest_login_count']
        clc1d   = user['contest_login_count_1_days']
        clc30d  = user['contest_login_count_30_days']
        clc365d = user['contest_login_count_365_days']
        clc7d = user['contest_login_count_7_days']

        cpc = user['contest_participation_count']
        cpc1d = user['contest_participation_count_1_days']
        cpc30d = user['contest_participation_count_30_days']
        cpc365d = user['contest_participation_count_365_days']
        cpc7d = user['contest_participation_count_7_days']

        fcc = user['forum_comments_count']
        fc = user['forum_count']
        fec = user['forum_expert_count']
        fqc = user['forum_questions_count']
        hc = user['hacker_confirmation']

        ic = user['ipn_count']
        ic1d = user['ipn_count_1_days']
        ic30d = user['ipn_count_30_days']
        ic365d = user['ipn_count_365_days']
        ic7d = user['ipn_count_7_days']

        ir = user['ipn_read']
        ir1d = user['ipn_read_1_days']
        ir30d = user['ipn_read_30_days']
        ir365d = user['ipn_read_365_days']
        ir7d = user['ipn_read_7_days']

        sc = user['submissions_count']
        sc1d = user['submissions_count_1_days']
        sc30d = user['submissions_count_30_days']
        sc365d = user['submissions_count_365_days']
        
        sc7d = user['submissions_count_7_days']

        scc = user['submissions_count_contest']
        scc1d = user['submissions_count_contest_1_days']
        scc30d = user['submissions_count_contest_30_days']
        scc365d = user['submissions_count_contest_365_days']
        scc7d = user['submissions_count_contest_7_days']

        scm = user['submissions_count_master']
        scm1d = user['submissions_count_master_1_days']
        scm30d = user['submissions_count_master_30_days']
        scm365d = user['submissions_count_master_365_days']
        scm7d = user['submissions_count_master_7_days']

        if (sc365d in submissions_count_365_days):
            print user_id
        '''if (clc1d == 0) or (cpc1d == 0) or (fec == 0) or\
           (fqc==0) or (hc==True) or (ir1d==0) or \
           (ir7d==0) or (scm1d==0) or \
           (sc1d==0) or (scc7d==0) or (scc1d==0):
            predictions_file_object.writerow("1")	
        else:
            predictions_file_object.writerow("0")'''
    #predictions_file.close()
    

print 'Start'
file_path = "C:\\DNS\\Course\\hackerrank\\Predict Email Opens\\dataset\\"
tra_file_path= file_path+"training_dataset.CSV"
#loadsql(tra_file_path)
test_file_path= file_path+"test_dataset.CSV"
loadsql_testdataset(test_file_path)

#attributes(tra_file_path)
#attributes_all(tra_file_path)

test_file_path= file_path+"test_dataset.csv"
#predict_email_opens_result(test_file_path)

print 'End'
