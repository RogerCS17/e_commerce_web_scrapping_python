from time import sleep
from bs4 import BeautifulSoup
from products_page_scrapper.product import Product
from products_page_scrapper.products_page_scrapper import ProductsPageScrapper


class MeliProductPageScraper(ProductsPageScrapper):
    def __init__(self, driver) -> None:
        self.driver = driver

    def get_html(self, url: str) -> BeautifulSoup:
        self.driver.get(url)
        sleep(5)
        content = self.driver.page_source
        html = BeautifulSoup(content, "html.parser")
        self.driver.close()
        return html

    def get_products(self, html_content: BeautifulSoup) -> list[Product]:
        products: list[Product] = []
        products_divs_list = html_content.find_all(
            "div", {"class": "ui-search-result__wrapper"}
        )
        for index, item in enumerate(products_divs_list):
            try:
                item_name = item.find("h3", {"class": "ui-search-item__title"}).text
                item_price = item.find(
                    "span", {"class": "andes-money-amount__fraction"}
                ).text.replace(".", "")
                item_url = item.find(
                    "a",
                    {
                        "class": "ui-search-item__group__element ui-search-link__title-card ui-search-link"
                    },
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
