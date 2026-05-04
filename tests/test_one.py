from playwright.sync_api import Page

def test_browser_opens(page: Page):
    page.goto("https://playwright.dev")
    print(page.title())
    assert "Playwright" in page.title()

# Page → represents your browser tab
# page.goto() → opens the URL
# page.title() → reads the tab title
# assert → test passes only if this is True

# RUN

# # See the result in terminal
# pytest tests/test_first.py -v --headed
#-v → see test names
# -s → see print output
# --headed → see browser



