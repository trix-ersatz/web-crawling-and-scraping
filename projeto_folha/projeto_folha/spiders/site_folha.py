import scrapy
from projeto_folha.items import ProjetoFolhaItem

class FolhaSpider(scrapy.Spider):
   name = "folha"
   allowed_domains = ["folha.com", "search.folha.uol.com.br"]
   start_urls = ["https://search.folha.uol.com.br/search?q=%22Seguran%C3%A7a+da+Informa%C3%A7%C3%A3o%22"]
  
   n = 1

   def parse(self, response):

       for div in response.css("#view-view"):
           link = div.css("div.c-headline__wrapper > div > a::attr(href)").extract_first()
           title = div.css("div.c-headline__wrapper > div > a > h2::text").extract_first()
           date = div.css("div.c-headline__wrapper > div > a > div > time::text").extract_first()
           newspaper_section = div.css("#view-view > div.c-headline__head > h3::text").extract_first()

           notice = ProjetoFolhaItem(link=link, title=title, date=date, newspaper_section=newspaper_section)
           yield notice
    
       
       next_page = response.css(f'a[aria-label="Ir para pgina {self.n+1}"]::attr(href)').extract_first()
       if next_page is not None:
        self.n += 1
        yield response.follow(next_page, self.parse)

