# pages/login_page.py
class LoginPage:
    def __init__(self, page):
        self.page = page
        
        # ✅ Locators defined inside the class
        self.username = page.get_by_placeholder("Username")
        self.password = page.get_by_placeholder("Password")
        self.login_btn = page.get_by_role("button", name="Login")
        self.error_msg = page.locator("[data-test='error']")

    def goto(self):
        self.page.goto("https://www.saucedemo.com")

    def login(self, username, password):
        self.username.fill(username)
        self.password.fill(password)
        self.login_btn.click()

    def get_error(self):
        return self.error_msg.inner_text()
    






# tests/test_login.py
from playwright.sync_api import Page, expect
from pages.login_page import LoginPage

def test_valid_login(page: Page):
    login = LoginPage(page)
    login.goto()
    login.login("standard_user", "secret_sauce")
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")

def test_invalid_login(page: Page):
    login = LoginPage(page)
    login.goto()
    login.login("wrong_user", "wrong_pass")
    error = login.get_error()
    print(error) 


# 📏 Rules — Real Project
# Rule 1: One page = one file in pages/ folder.
# Rule 2: Locators defined in __init__ as self. variables.
# Rule 3: Actions are methods — goto(), login(), get_error().
# Rule 4: Test file imports the page class and just calls methods.
# Rule 5: pages/ folder must have empty __init__.py file.
# Rule 6: requirements.txt lists all packages — so anyone can clone and run!


