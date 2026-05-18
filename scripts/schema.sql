CREATE TABLE banks (
    bank_id SERIAL PRIMARY KEY,
    bank_name VARCHAR(100) UNIQUE NOT NULL,
    app_name VARCHAR(150)
);

CREATE TABLE reviews (
    review_id TEXT PRIMARY KEY,
    bank_id INTEGER REFERENCES banks(bank_id),
    review_text TEXT,
    rating INTEGER,
    review_date TIMESTAMP,
    sentiment_label VARCHAR(50),
    sentiment_score FLOAT,
    identified_theme VARCHAR(100),
    source VARCHAR(50)
);
