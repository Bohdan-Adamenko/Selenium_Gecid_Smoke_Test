# Test Project: Robust Smoke Test for Gecid.com with Selenium WebDriver

This educational project demonstrates how to build a structured and reliable UI test automation script using Python and Selenium WebDriver.

## 🚀 What Does This Test Do?

The script performs a robust smoke test for the `ru.gecid.com` website, incorporating a **"fail fast"** strategy and reusable helper functions.

### Test Logic & Flow:
1.  **Modular Design:** The code is organized into helper functions for actions like taking screenshots, handling failures, and verifying elements, promoting clean and reusable code (D.R.Y. principle).
2.  **Critical Steps:** Core actions like site navigation, search execution, and critical verifications are treated as assertions. A failure in any of these steps will **immediately terminate** the test via `sys.exit(1)` to provide a clear and immediate failure report.
3.  **Non-Critical Verifications:** Simple checks for the presence of various UI elements on the homepage are designed to log their status (found/not found) and update the final test result without stopping the execution.
4.  **Execution Management:** The entire test is managed by a `main()` function that handles driver initialization, execution, final reporting (PASSED/FAILED), and teardown.

### Key Actions Performed:
*   Navigates to the homepage and verifies its title.
*   Performs non-critical checks for header and footer elements.
*   Executes a search for the keyword "CPU".
*   Verifies the title and URL of the search results page.
*   Saves screenshots for key stages.

## 🛠️ How to Run

### Prerequisites:
*   **Python 3.x** installed.
*   **Google Chrome** browser installed.
*   **Selenium** library and a matching **ChromeDriver** for your browser version.

### Installation:
```
pip install selenium
```
### Running the Test:
Execute the following command from your terminal:
```

```
