import scrapy


class OshaSpider(scrapy.Spider):
    name = "osha"
    allowed_domains = ["www.osha.gov"]
    start_urls = ["https://www.osha.gov/ords/imis/industry.search?p_logger=1&sic=&naics=&State=All&officetype=All&Office=All&endmonth=02&endday=16&endyear=2021&startmonth=02&startday=16&startyear=2024&owner=&scope=&FedAgnCode="]

    def parse(self, response):
        breakpoint()
        last_table = response.xpath("//table")[-1]
        headings = last_table.xpath(".//tbody/tr/th")