update 
	hackerank.predict_email_opens_testdata as upeo
	inner join 
	(
		select 
			distinct peo.user_id 
		from 
			hackerank.predict_email_opens_testdata as peo
		where 
			peo.submissions_count_master_365_days  in 
			(
				'293',
'295',
'307',
'308',
'323',
'341',
'342',
'345',
'346',
'358',
'359',
'361',
'376',
'383',
'409',
'416',
'420',
'429',
'434',
'444',
'468',
'472',
'473',
'474',
'479',
'480',
'488',
'493',
'495',
'496',
'505',
'512',
'518',
'530',
'574',
'582',
'590',
'596',
'605',
'606',
'656',
'659',
'691',
'725',
'740',
'744',
'849',
'907'
			)
	) tupeo on tupeo.user_id = upeo.user_id
set 
	predictions = 1
	