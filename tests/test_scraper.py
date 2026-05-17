from scripts.scrape_reviews import clean_text


def test_clean_text():

    sample = "Hello!!! 123"

    cleaned = clean_text(sample)

    assert cleaned == "hello"