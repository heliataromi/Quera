-- Section1
    CREATE TABLE events (
    id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    description TEXT,
    date DATETIME,
    created_at DATETIME DEFAULT NOW()
);

-- Section2
    Create TABLE event_user (
    user_id BIGINT UNSIGNED,
    event_id BIGINT UNSIGNED,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
    FOREIGN KEY (event_id) REFERENCES events(id)
);
