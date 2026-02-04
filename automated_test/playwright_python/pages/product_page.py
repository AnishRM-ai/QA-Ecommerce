from pages.base_page import BasePage

class ProductPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

        self.add_to_cart_button = page.get_by_role("button", name="Add to cart")
        self.cart_icon = page.locator("a[href='/cart']")
        self.cart_count = page.locator(".cart-count-bubble")

    def add_to_cart(self):
        self.add_to_cart_button.wait_for(state="visible")
        self.add_to_cart_button.click()

    def is_product_added(self):
        self.cart_count.wait_for(state="visible")
        return self.cart_count.text_content().strip() == "1"

    def go_to_cart(self):
        self.cart_icon.click()