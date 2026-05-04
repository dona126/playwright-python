def test_justredirection(page):
    page.goto("https://www.saucedemo.com/")
    print(page.title())
    
