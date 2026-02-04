from pages.signup_page import SignupPage
import time

def test_signup(page):
    signup_page = SignupPage(page)
    
    signup_page.navigate()
    
    signup_page.signup(
        first="Test",
        last="User",
        email="test@gmail.com",
        password="Password123!"
    )
    
    assert signup_page.is_signup_successful()
    