from pages.base_page import BasePage

class HomePage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        
        #locators
        self.product_cards = page.locator(".grid__item")
        self.product_titles = page.locator(".card__heading")
        
    def navigate(self):
        self.page.goto("https://sauce-demo.myshopify.com")
        self.wait_for_page_load()
        
    def get_product_count(self):
        self.product_cards.first.wait_for(state="visible")
        return self.product_cards.count()
    
    def click_first_product(self):
        self.product_titles.first.click()
        