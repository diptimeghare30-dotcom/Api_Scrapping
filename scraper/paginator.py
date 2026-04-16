from config import BASE_URL, TOTAL_PAGES

def get_all_urls():
    return [BASE_URL.format(i) for i in range(1, TOTAL_PAGES + 1)]