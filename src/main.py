from selenium import webdriver
from products_page_scrapper.amazon_product_page_scraper import AmazonProductPageScraper


def init():
    item = input("Ingrese el nombre del producto a busar: ")
    options = webdriver.EdgeOptions()

    amazon_search_result_url = f"https://www.amazon.com/s?k={item}"
    mercadolibre_search_result_url = f"https://listado.mercadolibre.com.pe/{item}"

    amazon_products_page_scraper = AmazonProductPageScraper(driver=webdriver.Edge())
    amazon_search_result_html = amazon_products_page_scraper.get_html(
        amazon_search_result_url
    )
    amazon_products = amazon_products_page_scraper.get_products(
        html_content=amazon_search_result_html
    )

    for item in amazon_products:
        print(f"{item.id}. Producto: {item.name} Precio: {item.price}", end="\n\n")


if __name__ == "__main__":
    init()
