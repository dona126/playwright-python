# Playwright Python

## What This Repo Covers
Playwright test automation using Python and pytest,
practiced on [SauceDemo](https://www.saucedemo.com/).

## Topics Covered
- Setup & first browser automation
- Locators - finding elements (get_by_role, get_by_placeholder, get_by_text)
- Actions - fill, click, navigate, keyboard
- Assertions - expect, to_be_visible, to_have_url, to_have_count
- Page Object Model (POM)

## Tech Stack
- Python 3.12
- Playwright
- Pytest


## How to Run
# Create virtual env
python -m venv venv
venv\Scripts\activate

# Install dependencies
pip install pytest-playwright

python -m playwright install chromium

# To Run tests
pytest tests/filenamee -v --headed
