# 세단, 10월대여, 자동차 ID리스트 출력, 중복없이, 자동차ID 기준 내림차순
SELECT CAR_ID
FROM CAR_RENTAL_COMPANY_CAR
WHERE CAR_TYPE = '세단' AND CAR_ID IN (SELECT CAR_ID
                                        FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
                                        WHERE START_DATE LIKE '____-10-__')
ORDER BY CAR_ID DESC