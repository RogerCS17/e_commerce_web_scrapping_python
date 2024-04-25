from selenium import webdriver
from products_page_scrapper.amazon_product_page_scraper import AmazonProductPageScraper
from products_page_scrapper.meli_produict_page_scraper import MeliProductPageScraper


def init():

    print("1. Amazon")
    print("2. Mercado Libre")
    print("0. SALIR")
    opc = int(input("Seleccione donde desea buscar: "))
    match opc:
        case 1:
            item = input("Ingrese el nombre del producto a buscar: ")
            amazon_search_result_url = f"https://www.amazon.com/s?k={item}"
            amazon_products_page_scraper = AmazonProductPageScraper(
                driver=webdriver.Edge()
            )
            amazon_search_result_html = amazon_products_page_scraper.get_html(
                amazon_search_result_url
            )
            amazon_products = amazon_products_page_scraper.get_products(
                html_content=amazon_search_result_html
            )

            for item in amazon_products:
                print(
                    f"{item.id}. Producto: {item.name} Precio: {item.price}", end="\n\n"
                )
        case 2:
            item = input("Ingrese el nombre del producto a buscar: ")
            meli_search_result_url = f"https://listado.mercadolibre.com.pe/{item}"
            meli_products_page_scraper = MeliProductPageScraper(driver=webdriver.Edge())
            meli_search_result_html = meli_products_page_scraper.get_html(
                meli_search_result_url
            )
            meli_products = meli_products_page_scraper.get_products(
                html_content=meli_search_result_html
            )

            for item in meli_products:
                print(
                    f"{item.id}. Producto: {item.name} Precio: {item.price}", end="\n\n"
                )
        case 0:
            exit()
        case _:
            print("No existe esa opción")


if __name__ == "__main__":
    init()
