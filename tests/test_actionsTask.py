# Write a new test in tests/test_actions.py:

# Go to https://www.saucedemo.com
# Fill username → standard_user
# Fill password → secret_sauce
# Click Login button
# Print the URL after login
# Assert URL contains inventory — meaning login was successful!
from playwright.sync_api import Page
def test_actionTask(page: Page):
    page.goto("https://www.saucedemo.com")
    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_placeholder("Password").fill("secret_sauce")
    page.get_by_role("button",name = "Login").click()
    # print current URL after login
    print(page.url)

    assert "inventory" in page.url
