
#Playwright expect:
#expect(page.get_by_text("Products")).to_be_visible()

# Rules
# Rule 1: Always import expect from Playwright — it's separate from Page:
# from playwright.sync_api import Page, expect




# Rule 2: expect() wraps a locator — not a value:
# ✅ correct
# expect(page.get_by_text("Products")).to_be_visible()

# ❌ wrong
# expect("Products").to_be_visible()





# Rule 3: Playwright expect() auto-waits — keeps checking until assertion passes or times out. No manual waits needed.




# Rule 4: assert vs expect:
# plain Python assert — no auto-wait, fails immediately
# assert "inventory" in page.url

# Playwright expect — auto-waits, better for UI elements
# expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
# Use expect for UI elements. assert is fine for simple URL/title checks.




# Rule 5: A test with no assertions is useless — it always passes even if the page is broken! Always assert something meaningful.

# Assertions Task
# Create tests/test_assertions.py and write these 3 tests:
# Test 1 — After login, assert page heading "Products" is visible
# Test 2 — Assert the URL after login is inventory.html
# Test 3 — Assert exactly 6 products are on the inventory page

from playwright.sync_api import Page, expect
def test_loginProduct(page: Page):
    page.goto("https://www.saucedemo.com")
    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_placeholder("Password").fill("secret_sauce")
    page.get_by_role("button",name = "Login").click()
    print(page.title())
    #assertion
    expect(page.get_by_text("Products")).to_be_visible()
    #page.title() returns a string, not a locator.  Wrap a locator inside expect

def test_loginURL(page: Page):
    page.goto("https://www.saucedemo.com")
    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_placeholder("Password").fill("secret_sauce")
    page.get_by_role("button",name = "Login").click()
     #assertion
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")


def test_loginProductCount(page: Page):
    page.goto("https://www.saucedemo.com")
    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_placeholder("Password").fill("secret_sauce")
    page.get_by_role("button",name = "Login").click()
     #assertion
    expect(page.locator(".inventory_item")).to_have_count(6)
    # CSS class needs a dot! Dot before class name.


