class BasePage:
    def __init__(self, page):
        self.page = page
        
    def wait_for_page_load(self):
        self.page.wait_for_load_state("networkidle")
    
    def wait_for_element(self, locator):
        locator.wait_for(state="visible")
        
    def get_title(self):
        return self.page.title()
    
    def get_url(self):
        return self.page.url
    
    