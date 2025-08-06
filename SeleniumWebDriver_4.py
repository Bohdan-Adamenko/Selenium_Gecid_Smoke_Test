import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import datetime
from selenium.webdriver.chrome.options import Options

stamp = datetime.now().strftime("%Y.%m.%d.%H;%M;%S")

opts = Options()
opts.add_argument("--headless=new")
opts.add_argument("--window-size=1920,1080")
driver = webdriver.Chrome(options=opts)

driver.get("https://ru.gecid.com/")


assert "GECID.com - обзоры и новости мира IT." in driver.title, \
       f"Ожидался title, содержащий 'GECID.com', а получен '{driver.title}'"
print("✅ Title проверен: ", driver.title)


try:
    driver.find_element(By.CSS_SELECTOR, 'a[title="Новости"]')
    print("✅ Ссылка 'Новости' найдена на главной странице")
except:
    print("❌ ")

try:
    driver.find_element(By.CSS_SELECTOR, 'label[class="articles_button"]')
    print("✅ Элемент 'Обзоры' найдена на главной странице")
except:
    print("❌ ")

try:
    driver.find_element(By.CSS_SELECTOR, 'a[title="Видео"]')
    print("✅ Ссылка 'Видео' найдена на главной странице")
except:
    print("❌ ")


try:
    driver.find_element(By.CSS_SELECTOR, 'label[for="lang_toggle"]')
    print("✅ Элемент смены языка найден на главной странице")
except:
    print("❌ ")


try:
    driver.find_element(By.CSS_SELECTOR, 'img[src="./img/search.png"]')
    print("✅ Поиск найден на главной странице")
except:
    print("❌ ")

try:
    driver.find_element(By.CSS_SELECTOR, 'img[src="./img/ln2.png"]')
    print("✅ Элемент смены темы сайта найден на главной странице")
except:
    print("❌ ")


try:
    driver.find_element(By.CSS_SELECTOR, 'a[href="./info.php?v=a"]')
    print("FOOTER ✅ Элемент 'О нас' сайта найден на главной странице")
except:
    print("❌ ")

try:
    driver.find_element(By.CSS_SELECTOR, 'a[href="./ittech/"]')
    print("FOOTER ✅ Элемент 'Цифровая индустрия' сайта найден на главной странице")
except:
    print("❌ ")

try:
    driver.find_element(By.CSS_SELECTOR, 'a[href="./storag/"]')
    print("FOOTER ✅ Элемент 'Накопители' сайта найден на главной странице")
except:
    print("❌ ")

try:
    driver.find_element(By.CSS_SELECTOR, 'a[href="./nouts/"]')
    print("FOOTER ✅ Элемент 'Ноутбуки и Планшеты' сайта найден на главной странице")
except:
    print("❌ ")

try:
    driver.find_element(By.XPATH, "//div[@class='footer_div']//footer//nav//li[normalize-space(text())='Наши партнеры']")
    print("FOOTER ✅ Элемент 'Наши партнеры' сайта найден на главной странице")
except:
    print("❌ ")


try:
    driver.save_screenshot(f"X:/all/qa/screenshots/gecid_home{stamp}.png")
    print("✅ Скриншот сохранён 'Main page' -> gecid_home.png")
except:
    print("❌ ")


try:
    driver.find_element(By.CSS_SELECTOR, "img[id='SearchImg']").click()
    print("✅ Нажата кнопка Search")
except:
    print("❌ ")

try:
    driver.find_element(By.NAME, "s").send_keys("CPU")
    print("✅ В поле Search написан текст 'CPU'")
except:
    print("❌ ")

try:
    driver.find_element(By.CSS_SELECTOR, "img[src='./img/search2.png']").click()
    print("✅ Нажата кнопка Submit (Search)")
except:
    print("❌ ")

time.sleep(1)
try:
    driver.find_element(By.CSS_SELECTOR, 'button[aria-label="Соглашаюсь"]').click()
    print("✅ Нажата кнопка 'Соглашаюсь' (Согласие на использование ваших данных)")
except:
    print("❌ ")
    time.sleep(100)


expected = "CPU. GECID.com - обзоры и новости мира IT."
if driver.title == expected:
    print("✅ Титл правильный")
else:
    print("❌ ")


url = 'https://ru.gecid.com/search.php?s=CPU'
if driver.current_url == url:
    print("✅ URL правильный")

else:
    print("❌ ")


try:
    driver.find_element(By.CSS_SELECTOR, 'button[class="gsc-search-button gsc-search-button-v2"]').click()
    print("✅ Найдена кнопка 'Google Search'")
except:
    print("❌ ")

try:
    driver.save_screenshot(f"X:/all/qa/screenshots/Search_CPU{stamp}.png")
    print("✅ Скриншот сохранён 'Search' -> Search_CPU.png")
except:
    print("❌ ")