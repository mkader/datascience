select
	distinct 
	concat('''',sc365d.contest_login_count_1_days,''',')
from (
		select 
			contest_login_count_1_days, count(*) count
		from 
			hackerank.predict_email_opens
		group by
			contest_login_count_1_days
	)as sc365d left join
	(
		select 
			contest_login_count_1_days, count(*) count
		from 
			hackerank.predict_email_opens
		where
			opened='FALSE'
		group by
			contest_login_count_1_days
	) as sc365d_f on sc365d.contest_login_count_1_days = sc365d_f.contest_login_count_1_days left join
	(
		select 
			contest_login_count_1_days, count(*) count
		from 
			hackerank.predict_email_opens
		where
			opened='TRUE'
		group by
			contest_login_count_1_days
	) as sc365d_t on sc365d_t.contest_login_count_1_days  = sc365d.contest_login_count_1_days
where
	sc365d_t.count/sc365d.count >= .10
			


