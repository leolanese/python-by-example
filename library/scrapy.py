# scrapy
# An open source and collaborative framework for extracting the data you need from websites.
# In a fast, simple, yet extensible way.

# pip install scrapy
# cat > myspider.py <<EOF

#####################################################################

# Build and run your web spiders
class BlogSpider(scrapy.Spider):
    name = 'blogspider'
    start_urls = ['https://blog.scrapinghub.com']

    def parse(self, response):
        for title in response.css('.post-header>h2'):
            yield {'title': title.css('a ::text').extract_first()}

        for next_page in response.css('div.prev-post > a'):
            yield response.follow(next_page, self.parse)
EOF
scrapy runspider myspider.py
