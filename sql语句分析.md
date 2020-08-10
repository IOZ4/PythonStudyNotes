##basic应用##
> select  
>
> industry_code_2 
> 
> from 
> 
> tcompany_industry 
> 
> where 
> 
> comp_code in(select comp_code from tcompany where comp_code = corp_code or comp_name = corp_code)
>
> and 
>
> industry_source='xquantdata(integrate)' 
>
> and 
>
> isexist=1 
>
> order by 
>
> beg_date desc

#从tcompany\_industry表中筛选符合where条件的industry\_code\_2字段的数据然后再通过beg\_date进行降序排序##
> where中有三个条件
> 

1. comp\_code 必须在 tcompany表中comp\_code字段等于corp\_code字段 或者 comp\_name字段等于corp\_code字段的comp\_code字段的数据的 列子查询中
2. 在tcompany\_industry表中 industry\_source字段等于'xquantdata(integrate)' 
3. 在tcompany\_industry表中 isexist字段等于1

----------

> SELECT 
> 
> comp_name 
> 
> FROM 
> 
> tcompany 
> 
> WHERE 
> 
> comp_code = :corp_code
##在tcompany表中选取符合comp_code等于corp_code的comp_name字段的数据##
corp\_code是参数传参进来的

----------
    WITH the_result AS (
	SELECT
	CASE
			
		WHEN
			t.area IN ( '地级市', '省直辖县级' ) THEN
				(
				SELECT
					a1.name 
				FROM
					tregion a1 
				WHERE
					a1.code = ( SELECT a2.p_code FROM tregion a2 WHERE a2.code = t.region ) 
				) --'地级市','省直辖县级'
				
				WHEN t.area IN ( '县级' ) THEN
				(
				SELECT
					name 
				FROM
					tregion a2 
				WHERE
					a2.code = (
					SELECT
						a1.p_code 
					FROM
						tregion a1 
					WHERE
						a1.code = ( SELECT a2.p_code FROM tregion a2 WHERE a2.code = t.region ) 
					) 
				) -- '县级'
				ELSE 区域名称 
			END AS 区域,
			t.* 
		FROM
			(
			SELECT
				a.comp_code,
				a.comp_name,
				a.regaddr,
				a.region,
				e.code 区域代码,
				e.area,
				e.name 区域名称 
			FROM
				tcompany a
				LEFT JOIN tregion e ON a.region = e.code 
			WHERE
				a.comp_code =: corp_code 
			) t 
		) SELECT DISTINCT
		b.comp_code COMP_CODE,
		a.L_CODE STOCK_CODE,
		b.comp_name FULL_NAME,
		b.sname ABBR_NAME,
		b.ENNAME EN_NAME,
		(
		CASE
				
				WHEN ( SELECT area FROM the_result ) = '地级市' THEN
				( SELECT 区域名称 FROM the_result ) ELSE ( --select (select name from tregion g where g.code = h.p_code) 上级区域名称
    --from tregion h where h.area in ('县级','省直辖县级') and code=(SELECT region FROM  the_result)
				SELECT 区域 FROM the_result ) 
			END 
			) region,
			b.TEL,
			b.WEBSITE,
			b.LEGALREP,
			b.REGCAPITAL CAPITAL,
			( SELECT name FROM tindustry_class WHERE code = c.industry_code_1 AND grade = 1 AND std = 'xQuantdata(integrate)' ) INDUSTRY 
		FROM
			TCOMPANY b
			LEFT JOIN tstk a ON a.ISSUER_CODE = b.comp_code 
			AND a.isexist = '1' 
			AND a.m_type <> 'X_NEEQ' 
			AND a.status <> '5'
			LEFT JOIN v_company_industry c ON c.comp_code = b.comp_code 
			AND c.industry_source = 'xQuantdata(integrate)' 
			AND c.isexist = '1' 
			AND c.end_date >= TO_CHAR( SYSDATE, 'YYYY-MM-DD' )
			LEFT JOIN TREGION d ON d.CODE = b.REGION 
		WHERE
			b.isexist = '1' 
			AND b.comp_code =: corp_code
##创建临时表the\_result先tcompany 别名为a 与tregion表左连接别名为 e 连接条件为a.region = e.code通过a.comp_code =: corp\_code进行筛选 选取需要的a表和e表属性作为一个表别名为t##
##在主查询select里的case中根据t.area的不同条件执行不同的then后面的语句最后得到区域和t.*的the\_result的临时表##
##在第二段sql语句中TCOMPANY表别名为b和tstk表别名为a和v_company_industry表别名为c和TREGION表别名为d全为左连接拿取b.isexist = '1' AND b.comp_code =: corp_code的符合条件的表取需要的字段与select的子查询拼接为需要的表region字段是通过临时表the\_result的case-when-then语句生成##

----------
    SELECT
	q1.*,
	(
	CASE
			
			WHEN q1.score >= 90 THEN
			'高' ELSE ( CASE WHEN q1.score >= 75 THEN '中' ELSE ( CASE WHEN q1.score >= 60 THEN '低' ELSE '无' END ) END ) 
			END 
			) risk 
		FROM
			(
			SELECT
				asource.*,
			( CASE WHEN ann.score_announce IS NULL THEN 0 ELSE ann.score_announce END ) score 
    FROM
	(
	SELECT
		t0.FILE_CODE,
		t0.BONDS,
		t1.name TYPE1,
		t2.name TYPE2,
		d.issue_name TITLE,
		d.pub_date PUB_DATE,
	CASE
			
			WHEN d.suffix IS NULL THEN
			'-' ELSE d.file_path || '\\' || d.file_code || d.suffix 
		END AS file_loc 
	FROM
		(
		SELECT
			wmsys.wm_concat ( a.b_name ) BONDS,
			b.file_code FILE_CODE 
		FROM
			( SELECT d_code, b_name FROM saconfig.TBND WHERE b_issuer_code = : corp_code ) a
			LEFT JOIN saconfig.TBND_FILE_RELATION b ON a.d_code = b.d_code 
		WHERE
			b.file_code IS NOT NULL 
		GROUP BY
			b.file_code 
		) t0
		LEFT JOIN saconfig.TBND_MAIN_EVENT c ON t0.file_code = c.file_code
		LEFT JOIN saconfig.TFINANCE_FILE d ON t0.file_code = d.file_code
		LEFT JOIN ( SELECT * FROM saconfig.TSYSTEMCONST WHERE TYPE = 313 ) t1 ON c.event_classify_code1 = t1.code
		LEFT JOIN ( SELECT * FROM saconfig.TSYSTEMCONST WHERE TYPE = 313 ) t2 ON c.event_classify_code2 = t2.code 
	ORDER BY
		d.pub_date DESC 
	) asource
	LEFT JOIN saconfig.SA_ANNOUNCE_SCORE ann ON asource.TITLE = ann.pdftitle 
	AND asource.PUB_DATE = ann.cal_date 
	) q1
##这个sql语句先从最里面的from( SELECT d\_code, b_name FROM saconfig.TBND WHERE b_issuer\_code = : corp\_code )别名为a经过where的筛选按照b.file\_code分组和select选取相应的字段得到别名为t0的表t0，t0又和c、d、t1、t2左连接经过条件筛选通过d.pub_date降序排序选取需要字段生成asource表asource表与ann左连接经过筛选操作得到q1最后选取q1的所有字段和经过case语句的筛选的rick字段生成需要的表##

----------
    SELECT
    	* 
    FROM
    	(
    	SELECT
    		q1.*,
    		(
    		CASE
    				
    				WHEN q1.score >= 90 THEN
    				'高' ELSE ( CASE WHEN q1.score >= 75 THEN '中' ELSE ( CASE WHEN q1.score >= 60 THEN '低' ELSE '无' END ) END ) 
    				END 
    				) risk 
    			FROM
    				(
    				SELECT
    					asource.*,
    				( CASE WHEN ann.score_announce IS NULL THEN 0 ELSE ann.score_announce END ) score 
    FROM
    	(
    	SELECT
    		t0.FILE_CODE,
    		t0.BONDS,
    		t1.name TYPE1,
    		t2.name TYPE2,
    		d.issue_name TITLE,
    		d.pub_date PUB_DATE,
    	CASE
    			
    			WHEN d.suffix IS NULL THEN
    			'-' ELSE d.file_path || '\\' || d.file_code || d.suffix 
    		END AS file_loc 
    	FROM
    		(
    		SELECT
    			wmsys.wm_concat ( a.b_name ) BONDS,
    			b.file_code FILE_CODE 
    		FROM
    			( SELECT d_code, b_name FROM saconfig.TBND WHERE b_issuer_code = : corp_code ) a
    			LEFT JOIN saconfig.TBND_FILE_RELATION b ON a.d_code = b.d_code 
    		WHERE
    			b.file_code IS NOT NULL 
    		GROUP BY
    			b.file_code 
    		) t0
    		LEFT JOIN saconfig.TBND_MAIN_EVENT c ON t0.file_code = c.file_code
    		LEFT JOIN saconfig.TFINANCE_FILE d ON t0.file_code = d.file_code
    		LEFT JOIN ( SELECT * FROM saconfig.TSYSTEMCONST WHERE TYPE = 313 ) t1 ON c.event_classify_code1 = t1.code
    		LEFT JOIN ( SELECT * FROM saconfig.TSYSTEMCONST WHERE TYPE = 313 ) t2 ON c.event_classify_code2 = t2.code 
    	ORDER BY
    		d.pub_date DESC 
    	) asource
    	LEFT JOIN saconfig.SA_ANNOUNCE_SCORE ann ON asource.TITLE = ann.pdftitle 
    	AND asource.PUB_DATE = ann.cal_date 
    	) q1 
    	) pr 
    ORDER BY
    	pub_date DESC --where pub_date>='pre_date' and pub_date<='now_date'
##首先最内层的( SELECT d\_code, b_name FROM saconfig.TBND WHERE b\_issuer_code = : corp\_code )生成a表与b表左连接通过where条件和分组选取需要的字段生成t0表，t0与c、d、t1、t2表左连接通过d.pub_date进行分组降序排序选取需要的字段生成asource表，asource表与ann表进行左连接选取需要的字段生成q1表，对q1表选取需要的字段生成pr表通过pub_date的排序选取需要的字段生成目标数据##