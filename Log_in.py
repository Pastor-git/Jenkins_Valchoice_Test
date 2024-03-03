from selenium import webdriver
from selenium.webdriver.common import by
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
import time

# intro
password = "Softprodukt23$"
login = "maciej.pastor@softprodukt.com.pl"
web = "https://www.valchoice.com"
print(login + " " + password + " " + web + " webdriver_path")

# initialisation
driver = webdriver.Chrome()
driver.get(web)
time.sleep(2)

# elements
element0 = driver.find_element(By.ID, "menu-item-link-login-my-account")

element_list = [element0]
# element0.click()

# MAIN_PAGE
element = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "menu-item-link-login-my-account"))
)
driver.execute_script("arguments[0].click();", element)
time.sleep(2)

# LOGIN
element_username = driver.find_element(By.ID, "username")
element_password = driver.find_element(By.ID, "password")

element_username.send_keys(login)
element_password.send_keys(password)

element_log_in_button = WebDriverWait(driver, 4).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="customer_login"]/div/form/p[3]/button'))
)
driver.execute_script("arguments[0].click();", element_log_in_button)

target_url = "https://www.valchoice.com/my-account/agent_dashboard/"

if driver.current_url == target_url:
    print(f"Currently on the correct webpage: {target_url}")
else:
    print(f"Not on the expected webpage. Current URL: {driver.current_url}")




driver.quit()