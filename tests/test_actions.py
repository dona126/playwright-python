# 📏 Rules
# Rule 1: Always find the element first (locator) → then act on it.
# Rule 2: Playwright auto-waits before every action — it waits for the element to be visible and ready. No manual waits needed.
# Rule 3: Use fill() for inputs — it clears first then types. Use type() only if you need keystroke by keystroke.
# Rule 4: click() works on buttons, links, checkboxes — anything clickable.

#1️⃣ page.goto() — navigate to URL
page.goto("https://www.saucedemo.com")
page.goto("https://playwright.dev")


#2️⃣ locator.fill() — type into input
# Clears the field first, then types
page.get_by_placeholder("Username").fill("standard_user")
page.get_by_placeholder("Password").fill("secret_sauce")


#3️⃣ locator.click() — click anything
page.get_by_role("button", name="Login").click()
page.get_by_text("Add to cart").click()


#4️⃣ page.keyboard.press() — press a key
page.keyboard.press("Enter")
page.keyboard.press("Tab")
page.keyboard.press("Escape")

#5️⃣ page.go_back() / page.go_forward()
page.go_back()     # like clicking browser back button
page.go_forward()  # like clicking browser forward button