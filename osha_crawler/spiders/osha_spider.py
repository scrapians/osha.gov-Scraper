import scrapy


class OshaSpider(scrapy.Spider):
    name = "osha"
    allowed_domains = ["www.osha.gov"]
    start_urls = ["https://www.osha.gov/ords/imis/industry.search?p_logger=1&sic=&naics=&State=All&officetype=All&Office=All&endmonth=02&endday=16&endyear=2021&startmonth=02&startday=16&startyear=2024&owner=&scope=&FedAgnCode="]

    def parse(self, response):
        breakpoint()
        last_table = response.xpath("//table")[-1]
        headings = last_table.xpath(".//th/text()").extract()
        rows_element = last_table.xpath(".//tr")[1:]

        for i,row_element in enumerate(rows_element):
            item = dict()
            headling
            rows_data = row_element.xpath(".//td//text()").extract()
            yeild 
