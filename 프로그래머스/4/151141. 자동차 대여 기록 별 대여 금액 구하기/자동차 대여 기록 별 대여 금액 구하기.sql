SELECT DISTINCT HISTORY_ID, FEE
FROM
    (SELECT CH.history_id as HISTORY_ID,
       DATEDIFF(end_date, start_date) AS 'DATE_DIFF',
           CASE 
                WHEN (DATEDIFF(end_date, start_date)+1 BETWEEN 7 AND 29) AND duration_type = '7일 이상' THEN ROUND(daily_fee * (DATEDIFF(end_date, start_date)+1) * (100 - discount_rate) * 0.01)
                WHEN (DATEDIFF(end_date, start_date)+1 BETWEEN 30 AND 89) AND duration_type = '30일 이상' THEN ROUND(daily_fee * (DATEDIFF(end_date, start_date)+1) * (100 - discount_rate) * 0.01)
                WHEN (DATEDIFF(end_date, start_date)+1 >= 90) AND duration_type = '90일 이상' THEN ROUND(daily_fee *(DATEDIFF(end_date, start_date)+1) * (100 - discount_rate) * 0.01)
                WHEN (DATEDIFF(end_date, start_date) < 7)  THEN ROUND(daily_fee * (DATEDIFF(end_date, start_date)+1))
                ELSE NULL
           END AS 'FEE'
    FROM CAR_RENTAL_COMPANY_CAR AS CR
         LEFT JOIN CAR_RENTAL_COMPANY_RENTAL_HISTORY AS CH ON CR.car_id = CH.car_id
         LEFT JOIN CAR_RENTAL_COMPANY_DISCOUNT_PLAN AS CP ON CR.car_type = CP.car_type
    WHERE CR.car_type = '트럭') AS TEMP
WHERE FEE IS NOT NULL
ORDER BY FEE DESC, history_id DESC