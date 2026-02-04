from pages.home_page import HomePage
from pages.product_page import ProductPage
from pages.cart_page import CartPage

def test_product_add_to_cart_and_checkout(page):
    home = HomePage(page)
    product = ProductPage(page)
    cart = CartPage(page)

    # Step 1: Product listing
    home.navigate()
    assert home.get_product_count() > 0

    # Step 2: Product detail
    home.click_first_product()
    product.add_to_cart()
    assert product.is_product_added()

    # Step 3: Cart & checkout
    product.go_to_cart()
    assert cart.is_cart_not_empty()

    cart.proceed_to_checkout()
    assert "/checkout" in page.url