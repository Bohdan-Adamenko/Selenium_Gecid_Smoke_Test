import time
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
timestamp = time.strftime("%Y.%m.%d-%H;%M;%S")


# --- HELPER FUNCTIONS ---
def take_screenshot(driver, name):
    screenshot_path = f"{name}-{timestamp}.png"
    try:
        driver.save_screenshot(screenshot_path)
        print(f"📸 Screenshot saved to '{screenshot_path}'")
    except Exception as e:
        print(f"Could not save screenshot: {e}")

def handle_critical_failure(driver, step_description, error):
    print(f"🔥 CRITICAL FAILURE at step: '{step_description}'")
    take_screenshot(driver, "critical_failure" )
    print(f"⚠️ Error details: {error}")
    sys.exit(1)

def find_element(driver, by, value, element_name,):
    try:
        driver.find_element(by, value)
        print(f'✅ Verification PASSED: Element "{element_name}" found.')
        return True
    except:
        print(f'❌ Verification FAILED: Element "{element_name}" was NOT found.')
        return False

def assert_title(driver, title):
    try:
        assert title in driver.title
        print('✅ Verification PASSED: Initial "Title" matches')
        return True
    except:
        print('❌ Verification FAILED: "Title" does not match')
        return False

def handle_click(driver, a, text):
    try:
        driver.find_element(By.CSS_SELECTOR, a).click()
        print(f'✅ Assertion PASSED: Button "{text}" is clicked')
    except Exception as e:
        handle_critical_failure(driver, f'Button "{text}" is clicked', e)


# --- MAIN TEST FUNCTION ---
def run_test(driver):
    overall_result = True

    # --- STEP 1: NAVIGATION & INITIAL CHECKS ---
    try:
        driver.get("https://ru.gecid.com/")
        print('✅ Assertion PASSED: Navigated to "gecid.com" homepage')
    except Exception as e:
        handle_critical_failure(driver, 'Navigated to "gecid.com" homepage', e)

    assert_title(driver, 'GECID.com - обзоры и новости мира IT.')

    print("\n--- Verifying elements on homepage ---")

    overall_result &= find_element(driver, By.CSS_SELECTOR, 'a[title="Новости"]', "Header Link: Новости")
    overall_result &= find_element(driver, By.CSS_SELECTOR, 'a[title="Видео"]', "Header Link: Видео")
    overall_result &= find_element(driver, By.CSS_SELECTOR, 'label[class="articles_button"]', "Header Element: Обзоры")
    overall_result &= find_element(driver, By.CSS_SELECTOR, 'label[for="lang_toggle"]', "Header Element: Change language")
    overall_result &= find_element(driver, By.CSS_SELECTOR, 'img[alt="Search"]', "Header Element: Search")
    overall_result &= find_element(driver, By.CSS_SELECTOR, 'img[alt="Dark theme"]', "Header Element: Change site theme")
    overall_result &= find_element(driver, By.CSS_SELECTOR, 'a[href="./info.php?v=a"]', "Footer Link: О нас")
    overall_result &= find_element(driver, By.CSS_SELECTOR, 'a[href="./ittech/"]', "Footer Link: Цифровая индустрия")
    overall_result &= find_element(driver, By.CSS_SELECTOR, 'a[href="./storag/"]', "Footer Link: Накопители")
    overall_result &= find_element(driver, By.CSS_SELECTOR, 'a[href="./nouts/"]', "Footer Link: Ноутбуки и Планшеты")
    overall_result &= find_element(driver, By.XPATH,"//div[@class='footer_div']//footer//nav//li[normalize-space(text())='Наши партнеры']","Footer Text: Наши партнеры")

    take_screenshot(driver, "gecid_home")


    # --- STEP 2: SEARCH FUNCTIONALITY ---
    print("\n--- Verifying search functionality ---")

    handle_click(driver, "img[id='SearchImg']", "Search")

    try:
        driver.find_element(By.NAME, "s").send_keys("CPU")
        print('✅ Assertion PASSED: Text "CPU" is written in the "Search" text field')
    except Exception as e:
        handle_critical_failure(driver, 'Text "CPU" is written in the "Search" text field', e)

    handle_click(driver, "img[src='./img/search2.png']", "Submit")

    time.sleep(1)

    try:
        driver.find_element(By.CSS_SELECTOR, 'button[aria-label="Соглашаюсь"]').click()
        print('✅ Verification PASSED: Cookie consent accepted.')
    except:
        print('ℹ️ Cookie consent pop-up not found, continuing...')


    # --- STEP 3: VERIFY SEARCH RESULTS ---
    print("\n--- Verifying search results page ---")

    overall_result &= assert_title(driver, 'CPU. GECID.com - обзоры и новости мира IT.')

    try:
        assert "https://ru.gecid.com/search.php?s=CPU" in driver.current_url
        print('✅ Verification PASSED: "URL" matches')
    except:
        print('❌ Verification FAILED: "URL" does not match')
        overall_result = False

    overall_result &= find_element(driver, By.CSS_SELECTOR, 'button[class="gsc-search-button gsc-search-button-v2"]', "Body Element: Google Search")

    take_screenshot(driver, "Search_CPU")

    return overall_result


# --- EXECUTION BLOCK ---
def main():
    opts = Options()
    opts.add_argument("--headless=new")
    opts.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome(options=opts)

    final_status = False

    try:
        final_status = run_test(driver)
    except SystemExit:
        final_status = False
    except Exception as e:
        print(f"\n🔥 AN UNEXPECTED CRITICAL ERROR OCCURRED: {e}")
        final_status = False
    finally:
        print("\n" + "=" * 40)
        if final_status:
            print("🎉 OVERALL TEST RESULT: PASSED 🎉")
        else:
            print("🔥 OVERALL TEST RESULT: FAILED 🔥")
        print("=" * 40)

        driver.quit()
        print("\nBrowser closed.")

if __name__ == "__main__":
    main()
