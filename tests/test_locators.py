# Rule 1: Locators are lazy — they don't search the page until you actually DO something with them (click, fill, assert).

# Rule 2: Playwright auto-waits up to 30 seconds for an element to appear. No time.sleep() ever.

# Rule 3: Always prefer locators in this order:
# get_by_role → get_by_label → get_by_placeholder → get_by_text → locator(css)
# Top = best practice. Bottom = last resort.

# 1. Role
#Finds by HTML role — button, heading, textbox, link.
page.get_by_role("button", name="Login")
page.get_by_role("heading", name="Products")
page.get_by_role("link", name="Sign up")


# 2. Label
#Finds input by its label text.
page.get_by_label("Username")
page.get_by_label("Password")


# 3. Placeholder
page.get_by_placeholder("Username")
page.get_by_placeholder("Password")


# 4. Text
page.get_by_text("Swag Labs")
page.get_by_text("Login", exact=True)


# 5. locator(css)
page.locator("#user-name")
page.locator(".login-button")
page.locator("[data-test='username']")