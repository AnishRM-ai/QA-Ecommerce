from pages.login_page import LoginPage

def test_valid_login(page):
    login_page = LoginPage(page)

    login_page.navigate()
    login_page.login("mindpixel168@gmail.com", "Password1!")

    assert login_page.is_login_successful()


def test_invalid_login(page):
    login_page = LoginPage(page)

    login_page.navigate()
    login_page.login("wrong@email.com", "wrongpassword")

    assert "/account/login" in page.url