CREATE TABLE users (
    id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    family VARCHAR(255),
    email VARCHAR(50),
    password VARCHAR(255),
    created_at DATETIME DEFAULT current_timestamp
);
