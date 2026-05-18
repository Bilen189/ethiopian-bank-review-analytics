import pandas as pd
from sqlalchemy import create_engine
print("Starting script...")


# PostgreSQL connection
username = "postgres"
password = "Ehkttmea3?"
host = "localhost"
port = "5432"
database = "bank_reviews"


engine = create_engine(
    f"postgresql://{username}:{password}@{host}:{port}/{database}"
)
print("Connected to PostgreSQL...")
from sqlalchemy import text

with engine.connect() as conn:
    conn.execute(text("DELETE FROM reviews;"))
    conn.execute(text("DELETE FROM banks;"))
    conn.commit()

print("Old data cleared...")


# Load dataset
df = pd.read_csv("data/processed/task2_sentiment_themes.csv")
print("CSV loaded successfully...")

# Rename bank column
df = df.rename(columns={"bank": "bank_name"})


# Create banks table data
banks_df = pd.DataFrame({
    "bank_name": ["CBE", "BOA", "Dashen"],
    "app_name": [
        "Commercial Bank of Ethiopia",
        "Bank of Abyssinia",
        "Dashen Bank"
    ]
})


# Insert banks
banks_df.to_sql(
    "banks",
    engine,
    if_exists="append",
    index=False
)
print("Banks inserted...")


# Read bank IDs
banks = pd.read_sql("SELECT * FROM banks", engine)


# Merge bank IDs
df = df.merge(
    banks,
    on="bank_name",
    how="left"
)


# Rename columns
df = df.rename(columns={
    "review": "review_text",
    "theme": "identified_theme",
    "sentiment": "sentiment_label"
})



# Add source column
df["source"] = "Google Play"


# Select final columns
df = df[
    [
        "review_id",
        "bank_id",
        "review_text",
        "rating",
        "review_date",
        "sentiment_label",
        "identified_theme",
        "source"
    ]
]


# Insert reviews
df.to_sql(
    "reviews",
    engine,
    if_exists="append",
    index=False
)

print("Data inserted successfully.")
print("Reviews inserted...")