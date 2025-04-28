from selenium import webdriver 



driver = webdriver.Chrome()
driver.get("https://sinhvien.dau.edu.vn/sinh-vien-dang-nhap.html")
print()
id_menu = 'menu'
element_menu= driver.find_element(By.id,id_menu)
print(element_menu)

name_input = 'pIDmenu_input'
element_input = driver.find_element(By.name, name_input)


css_selector_btn = 'body> div.bg-search .div> form>div >div:nth-child(3)>button'
element_btn = driver.find_element(By.css_SELECTOR, css_selector_btn)


xpath_input_nganh = 'html/body/div[3]/div/form/div/div[2]/span/span/input'
element_input_nganh = driver.find_element(By.XPATH, xpath_input_nganh)