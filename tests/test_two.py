# ✔ Without type hint
#better test_one file code only

def test_justredirection(page):
    page.goto("https://www.saucedemo.com/")
    print(page.title())
    
