select count(*) from predict_email_opens_testdata as p where p.predictions = 1 
union all
select count(*) from predict_email_opens_testdata as p

select predictions from predict_email_opens_testdata as p limit 207424

update predict_email_opens_testdata set predictions= 0 ;

update predict_email_opens_testdata set predictions= 1 
where  
mail_category in ('mail_category_15','mail_category_1')
#mail_category in ('mail_category_1', 'mail_category_4' ,
#           'mail_category_13' , 'mail_category_3' ,'mail_category_15', 'mail_category_7')
or 
mail_type in ('mail_type_3')
or contest_login_count_30_days ='1' or ipn_count_30_days in  ('0','1')
or contest_participation_count_7_days	='1'
or contest_participation_count	='2'  or
contest_login_count	='2' or
ipn_count_1_days	='1' or
ipn_count_7_days	='1' or
contest_participation_count_365_days	='2' or
ipn_read	='1' or
ipn_read_365_days	='1' or
contest_login_count_365_days	='2' or
ipn_count_365_days	='1' or
ipn_count	='1' or
submissions_count_master_365_days	='0'

update predict_email_opens_testdata set predictions= 0
#select *  from predict_email_opens_testdata where  
where 
#contest_login_count_1_days in ('0')
contest_login_count   
#not in ('1','3','5','2','53','11','4')
not in ('1','3','2')

