from pages.base_page import BasePage

class CartPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

        self.cart_items = page.locator(".cart-item")
        self.checkout_button = page.get_by_role("button", name="Check out")

    def is_cart_not_empty(self):
        self.cart_items.first.wait_for(state="visible")
        return self.cart_items.count() > 0

    def proceed_to_checkout(self):
        self.checkout_button.click()
        self.page.wait_for_url("**/checkout**")