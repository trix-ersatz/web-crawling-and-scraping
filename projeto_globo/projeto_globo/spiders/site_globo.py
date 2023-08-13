import scrapy
from scrapy_selenium import SeleniumRequest
from projeto_globo.items import ProjetoGloboItem

class SiteGloboSpider(scrapy.Spider):
    name = "site_globo"
    allowed_domains = ["www.globo.com"]
    start_urls = ["https://www.globo.com/busca/?q=Seguran%C3%A7a+da+Informa%C3%A7%C3%A3o&order=recent&from=2018-01-01T00%3A00%3A00-0200&to=2022-12-31T23%3A59%3A59-0200"]

    def parse(self, response):
        div_noticias = response.css('li.widget.widget--card.widget--info')

        for div in div_noticias:
            link = div.css('.widget--info__text-container > a::attr(href)').extract_first()
            title = div.css('.widget--info__text-container > a > div.widget--info__title.product-color::text').extract_first()
            #date = div.css('.widget--info__text-container > a > div.widget--info__meta > font > font ::text').extract_first()
            date = div.css('.widget--info__meta ::text').extract_first().strip()
            #newspaper_section = div.css('.widget--info__text-container > div > font > font ::text').extract_first()
            newspaper_section = div.css('.widget--info__text-container > div ::text').extract_first()
            subtitle = div.css('.widget--info__text-container > a > p ::text').extract_first()
            
            notice = ProjetoGloboItem(link=link, title=title, date=date, newspaper_section=newspaper_section, subtitle=subtitle)
            yield notice

        # Encontrar e clicar no botão "Veja mais"
        next_page_button = response.css('a.fundo-cor-produto.pagination__load-more')
        if next_page_button:
            yield SeleniumRequest(
                url=response.urljoin(next_page_button.attrib['href']),
                callback=self.parse
            )
