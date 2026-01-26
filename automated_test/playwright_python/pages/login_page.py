from pages.base_page import BasePage

class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        
        #Locators
        self.username_input = page.locator("#customer_email")
        self.password_input = page.locator("#customer_password")
        self.login_button = page.locator("input[value='Sign In']")
        
    def navigate(self):
        self.page.goto("https://sauce-demo.myshopify.com/account/login")
            
    def login(self, username, password):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()
        
    def is_login_successful(self):
        return "/account" in self.page.url
        