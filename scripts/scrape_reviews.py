import pandas as pd
from google_play_scraper import reviews, Sort
import re


def scrape_reviews(app_id, bank_name, count=2000):

    try:
        result, continuation_token = reviews(
            app_id,
            lang="en",
            country="et",
            sort=Sort.NEWEST,
            count=count
        )

        df = pd.DataFrame(result)

        df["bank"] = bank_name

        return df

    except Exception as e:
        print(f"Error scraping {bank_name}: {e}")
        return pd.DataFrame()


def clean_text(text):

    try:
        text = str(text).lower()

        text = re.sub(r"http\\S+", "", text)

        text = re.sub(r"[^a-zA-Z\\s]", "", text)

        text = re.sub(r"\\s+", " ", text).strip()

        return text

    except Exception as e:
        print(f"Error cleaning text: {e}")
        return ""


# App IDs
cbe_app_id = "com.combanketh.mobilebanking"
boa_app_id = "com.boa.boaMobileBanking"
dashen_app_id = "com.dashen.dashensuperapp"


# Scrape reviews
cbe_reviews = scrape_reviews(cbe_app_id, "CBE")
boa_reviews = scrape_reviews(boa_app_id, "BOA")
dashen_reviews = scrape_reviews(dashen_app_id, "Dashen")


# Combine datasets
all_reviews = pd.concat(
    [cbe_reviews, boa_reviews, dashen_reviews],
    ignore_index=True
)


# Keep important columns
all_reviews = all_reviews[
    [
        "reviewId",
        "userName",
        "content",
        "score",
        "thumbsUpCount",
        "at",
        "bank"
    ]
]


# Rename columns
all_reviews.columns = [
    "review_id",
    "user_name",
    "review",
    "rating",
    "thumbs_up",
    "review_date",
    "bank"
]


# Remove missing values
all_reviews.dropna(subset=["review", "rating"], inplace=True)


# Remove duplicates
all_reviews.drop_duplicates(subset=["review"], inplace=True)


# Clean reviews
all_reviews["clean_review"] = all_reviews["review"].apply(clean_text)


# Convert dates
all_reviews["review_date"] = pd.to_datetime(
    all_reviews["review_date"]
)


# Save dataset
all_reviews.to_csv(
    "data/processed/all_bank_reviews.csv",
    index=False
)

print("Dataset saved successfully.")