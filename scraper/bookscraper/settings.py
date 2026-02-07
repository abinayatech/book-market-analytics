BOT_NAME = 'bookscraper'

SPIDER_MODULES = ['bookscraper.spiders']
NEWSPIDER_MODULE = 'bookscraper.spiders'

# Crawl responsibly
ROBOTSTXT_OBEY = True
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (HTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 16

# Configure a delay for requests for the same website (default: 0)
DOWNLOAD_DELAY = 1

# Enable and configure the AutoThrottle extension (disabled by default)
AUTOTHROTTLE_ENABLED = True
AUTOTHROTTLE_START_DELAY = 5
AUTOTHROTTLE_MAX_DELAY = 60

# Configure item pipelines
ITEM_PIPELINES = {
   'bookscraper.pipelines.CleanDataPipeline': 300,
   'bookscraper.pipelines.SaveToSQLitePipeline': 400,
}
