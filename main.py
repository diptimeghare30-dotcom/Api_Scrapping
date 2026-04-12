print("Main is running...")
from scraper.fetcher import fetch_page
from scraper.parser import parse_page
from scraper.paginator import get_all_urls
from utils.saver import save_to_csv, save_to_json
import time
from utils.logger import setup_logger

logger = setup_logger()

def run_pipeline():
    logger.info("Scraping started")

    all_data = []
    urls = get_all_urls()

    for url in urls:
        try:
            logger.info(f"Processing URL: {url}")

            html = fetch_page(url)
            page_data = parse_page(html)

            all_data.extend(page_data)

            logger.info(f"Extracted {len(page_data)} records")

            time.sleep(1)

        except Exception as e:
            logger.error(f"Error processing {url}: {e}")

    save_to_csv(all_data, "data/processed/books.csv")
    save_to_json(all_data, "data/processed/books.json")

    logger.info("Scraping completed successfully")

if __name__ == "__main__":
    run_pipeline()