-- SELECT
SELECT * FROM airports
SELECT airport_code FROM airports

-- SELECT + WHERE
SELECT * FROM airports WHERE timezone = 'Europe/Moscow'
SELECT * FROM airports WHERE timezone = 'Europe/Moscow' AND city = 'Москва'
SELECT * FROM airports WHERE city = 'Москва' OR  city = 'Санкт-Петербург'
SELECT * FROM airports WHERE city IN ('Москва', 'Санкт-Петербург');
SELECT * FROM bookings WHERE total_amount < 5000
select flight_id, actual_arrival from flights where actual_arrival IS NULL;

-- SELECT + LIKE
SELECT * FROM airports WHERE city LIKE ('Красно%');
SELECT * FROM airports WHERE city NOT LIKE ('Красно%');
SELECT * FROM airports WHERE city LIKE ('%-%');
SELECT * FROM airports WHERE city LIKE ('_ренбург');

-- SELECT + DISTINCT
SELECT DISTINCT city FROM airports

-- SELECT + LIMIT/OFFSET
SELECT * FROM airports limit 2
SELECT * FROM airports limit 2 offset 1
SELECT + ORDER BY
SELECT * FROM seats WHERE aircraft_code = '319';
SELECT * FROM seats WHERE aircraft_code = '319' ORDER BY seat_no;
SELECT * FROM seats WHERE aircraft_code = '319' ORDER BY seat_no ASC;
SELECT * FROM seats WHERE aircraft_code = '319' ORDER BY seat_no DESC;
SELECT * FROM seats WHERE aircraft_code = '319' ORDER BY fare_conditions, seat_no;
SELECT * FROM seats WHERE aircraft_code = '319' ORDER BY fare_conditions ASC, seat_no DESC;

-- UPDATE
UPDATE bookings SET total_amount = 6200 WHERE  book_ref = '06B046'

-- DELETE
DELETE from aircrafts  where aircraft_code  = '733';