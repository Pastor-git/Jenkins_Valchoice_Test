from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time


def test_login_to_website():
    password = "Softprodukt23$"
    login = "maciej.pastor@softprodukt.com.pl"
    web = "https://www.valchoice.com"

    options = Options()
    options.headless = True
    driver = webdriver.Chrome(options=options)
    driver.get(web)
    time.sleep(2)

    element0 = driver.find_element(By.ID, "menu-item-link-login-my-account")
    element0.click()

    element_username = driver.find_element(By.ID, "username")
    element_password = driver.find_element(By.ID, "password")

    element_username.send_keys(login)
    element_password.send_keys(password)

    element_log_in_button = WebDriverWait(driver, 4).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="customer_login"]/div/form/p[3]/button'))
    )
    element_log_in_button.click()

    target_url = "https://www.valchoice.com/my-account/agent_dashboard/"

    assert driver.current_url == target_url, f"Login failed. Expected URL: {target_url}, Actual URL: {driver.current_url}"

    driver.quit()
