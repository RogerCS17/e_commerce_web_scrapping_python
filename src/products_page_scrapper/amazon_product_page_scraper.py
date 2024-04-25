from bs4 import BeautifulSoup
from products_page_scrapper.product import Product
from products_page_scrapper.products_page_scrapper import ProductsPageScrapper
from time import sleep


class AmazonProductPageScraper(ProductsPageScrapper):

    def __init__(self, driver) -> None:
        self.driver = driver

    def get_html(self, url: str) -> BeautifulSoup:
        self.driver.get(url)
        self.driver.refresh()
        self.driver.get(url)
        sleep(5)
        content = self.driver.page_source
        html = BeautifulSoup(content, "html.parser")
        self.driver.close()
        return html

    def get_products(self, html_content: BeautifulSoup) -> list[Product]:
        products: list[Product] = []
        products_divs_list = html_content.find_all("div", {"class": "s-result-item"})
        for index, item in enumerate(products_divs_list):
            try:
                item_name = item.find(
                    "span", {"class": "a-size-medium a-color-base a-text-normal"}
                ).text
                item_price = (
                    item.find("span", {"class": "a-price-whole"}).text.replace(",", "")
                    + item.find("span", {"class": "a-price-fraction"}).text
                )
                item_url = item.find(
                    "a", {"class": "a-link-normal s-no-outline"}
                ).attrs["href"]
                products.append(
                    Product(
                        id=index + 1,
                        name=item_name,
                        price=float(item_price),
                        url=item_url,
                    )
                )
            except Exception as e:
                pass
        return products
