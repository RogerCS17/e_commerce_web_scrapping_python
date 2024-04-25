from abc import ABC, abstractmethod
from bs4 import BeautifulSoup
from .product import Product


class ProductsPageScrapper(ABC):

    @abstractmethod
    def get_html(self, url: str) -> BeautifulSoup: ...

    @abstractmethod
    def get_products(self, html_content: BeautifulSoup) -> list[Product]: ...
