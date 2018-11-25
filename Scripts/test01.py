# self.find_element(by=By.XPATH, value=xpath)
from selenium.webdriver.common.by import By

# loc=(By.XPATH,"//*[contains(@text,'WLAN')]")


loc=By.XPATH,"//*[contains(@text,'WLAN')]"

print(type(loc))
print(loc)

print("解包后的值：",*loc)