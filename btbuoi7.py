from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()

driver.get('https://phatnguoixe.vn/')

css_selector_img = 'tracuu > ul > li: nth-child(2) >label>img'
element_ing = driver.find_element(By.css_SELECTOR, css_selector_img)
element_ing.click()

id_bs = 'bienso'
element_bs= driver.find_element(By.ID, id_bs)
element_bs.click()
value_bs = '76B1-86.552'
element_bs.send_keys('76B1-86.552')

xpath_btn = '//*[@id="submit-pn*]'
element_btn = driver.find_element(By.XPATH, xpath_btn)
element_btn.click()



id_result = 'ketqua'
element_result = driver.find_element(By.ID, id_result)
text_result = element_result.text
print(text_result)
if "chuc mung ban k co loi vi pham " in text_result:
     print("k co loi")
else:
     print("co loi vi pham")