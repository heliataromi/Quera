-- Section1
    SELECT *
    FROM hospitals
    WHERE CONCAT(provider_number, name, address, city, state, zip_code, owner) LIKE '%x%';

-- Section2
    DELETE FROM hospitals
    WHERE CONCAT(provider_number, zip_code) LIKE '%x%';

-- Section3
    UPDATE hospitals
    SET name = 'PROBABLY AN ERROR'
    WHERE name LIKE '%x%';
