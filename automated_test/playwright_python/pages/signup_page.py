from pages.base_page import BasePage

class SignupPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        
        #Locators
        self.first_name = page.locator("input[name='customer[first_name]']")
        self.last_name = page.locator("input[name='customer[last_name]']")
        self.email = page.locator("input[name='customer[email]']")
        self.password = page.locator("input[name='customer[password]']")
        self.signup_button = page.locator("input[value='Create']")
        
    def navigate(self):
        self.page.goto("https://sauce-demo.myshopify.com/account/register")
        self.wait_for_page_load()
        
    def signup(self, first, last, email, password):
        self.wait_for_element(self.first_name)
        
        self.first_name.fill(first)
        self.last_name.fill(last)
        self.email.fill(email)
        self.password.fill(password)
        
        self.signup_button.click()
        self.page.wait_for_load_state("networkidle")
        
    def is_signup_successful(self):
        return "/account" in self.page.url
    
        
    