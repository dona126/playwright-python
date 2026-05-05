#  write locators for 4 elements on https://www.saucedemo.com:

# Username input field
# Password input field
# Login button
# "Swag Labs" heading


from playwright.sync_api import Page

def test_find_elements(page: Page):
    page.goto("https://www.saucedemo.com")

    username = page.get_by_placeholder("Username")
    password = page.get_by_placeholder("Password")
    login_btn = page.get_by_role("Button",name = "Login")
    heading = page.get_by_text("Swag Labs", exact = True)

    print(username)
    print(password)
    print(login_btn)
    print(heading)