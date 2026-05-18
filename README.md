Task 1: Data Collection & Preprocessing
Project Overview

This project is part of the 10 Academy Artificial Intelligence Mastery Program (Week 2 Challenge).
The goal of Task 1 is to collect, clean, and prepare Google Play Store reviews for Ethiopian banking mobile applications for further sentiment and thematic analysis.

The banks analyzed include:

Commercial Bank of Ethiopia (CBE)
Bank of Abyssinia (BOA)
Dashen Bank


Scraping Methodology
Data Source

All data was collected from the Google Play Store using the google-play-scraper Python library.

 Tools Used
google-play-scraper → for extracting user reviews
pandas → for data manipulation and cleaning
numpy → for numerical operations
 Extraction Process

For each banking application:

The unique Google Play package ID (app ID) was identified.
The reviews() function from google-play-scraper was used to extract user reviews.
Reviews were collected in English language (lang='en') and filtered by country (country='et').
A maximum of 2000 reviews per app was requested to ensure sufficient data coverage.
 Data Fields Collected

For each review, the following attributes were extracted:

Review ID
User name
Review text
Rating (1–5 stars)
Number of thumbs up
Review date
Bank/app name
 Date Range Used

The dataset includes reviews collected across the full available historical range returned by the Google Play Store API at the time of extraction.

Start Date: Earliest available reviews in Google Play Store dataset
End Date: Latest available reviews up to the scraping date (May 2026)

Note: The dataset is dynamic and reflects the most recent available reviews at the time of scraping.

 Data Preprocessing Steps

The raw dataset was cleaned using the following steps:

Column Selection
Retained only relevant fields for analysis
Renaming Columns
Standardized column names for consistency:
review_id, review, rating, review_date, bank
Missing Value Handling
Removed rows with missing review text or ratings
Duplicate Removal
Removed duplicate reviews based on review text
Text Cleaning
Converted text to lowercase
Removed URLs, special characters, and numbers
Removed extra whitespace
Date Formatting
Converted review dates to YYYY-MM-DD format using pandas datetime
Final Dataset Structure
A cleaned and merged dataset was created for all three banks


 Limitations Encountered

While collecting and processing the data, the following limitations were observed:

API Rate Limits
The Google Play Store scraper may return fewer reviews than requested due to internal rate limiting.
Incomplete Historical Coverage
Some older reviews may not be accessible depending on app availability and Play Store restrictions.
Language Filtering
Non-English reviews were excluded, which may result in partial loss of user feedback diversity.
Dynamic Data Source
Google Play reviews are continuously updated, meaning repeated scraping may produce slightly different datasets.
Review Volume Variation
Some apps returned fewer than the target 400 reviews per bank depending on availability.


 Output Files

The final outputs generated in this task include:

cbe_reviews_clean.csv
boa_reviews_clean.csv
dashen_reviews_clean.csv
all_bank_reviews.csv (combined dataset)

Note: All raw and processed datasets are excluded from GitHub using .gitignore to maintain repository cleanliness.


 Summary

This task successfully built a structured data pipeline that:

Extracts real user feedback from mobile banking apps
Cleans and standardizes textual data for NLP tasks
Produces a unified dataset ready for sentiment and thematic analysis

## Task 3: PostgreSQL Integration

### Database Setup
- Database name: bank_reviews
- Tables: banks, reviews

### Data Insertion
Data was inserted using SQLAlchemy in `scripts/load_to_postgres.py`

### Verification Queries

#### Total reviews
```sql
SELECT COUNT(*) FROM reviews;

Reviews per bank
SELECT b.bank_name, COUNT(*) 
FROM reviews r
JOIN banks b ON r.bank_id = b.bank_id
GROUP BY b.bank_name;

Average rating
SELECT b.bank_name, AVG(r.rating)
FROM reviews r
JOIN banks b ON r.bank_id = b.bank_id
GROUP BY b.bank_name;
