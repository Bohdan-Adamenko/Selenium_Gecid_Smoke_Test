# Test Project: Smoke Test for Gecid.com with Selenium WebDriver

This educational project demonstrates UI test automation skills using Python and Selenium WebDriver.

## 🚀 What Does This Test Do?

The script performs a basic smoke test for the `ru.gecid.com` website:
1.  Opens the main page.
2.  Asserts the page `title`.
3.  Verifies the presence of key elements in the header (e.g., News, Reviews, Videos, Search).
4.  Verifies the presence of key elements in the footer.
5.  Executes a search for the keyword "CPU".
6.  Asserts the `title` and URL of the search results page.
7.  Saves screenshots of key steps for visual verification.

## 🛠️ How to Run

### Prerequisites:
*   **Python 3.x** installed.
*   **Google Chrome** browser installed.
*   **Selenium** library and the corresponding **ChromeDriver** installed.

### Installation:

pip install selenium

*Note: Please ensure your ChromeDriver version matches your installed Google Chrome browser version.*

### Running the Test:
To run the test, execute the following command from your terminal:

python SeleniumWebDriver_4.py
