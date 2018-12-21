from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains



# logs into Web UI ====================================================================================================
driver = webdriver.Chrome()
driver.get("https://pim.genpt.net/webui/cda_attribute_portal")
wait = WebDriverWait(driver, 20)


user = wait.until(EC.presence_of_element_located((By.ID, 'username-input')))
user.send_keys('407427')

password = wait.until(EC.presence_of_element_located((By.ID, 'password-input')))
password.send_keys('GPCN@P@10')

driver.find_element_by_id('login-button').click()

# Search PROD PCC =====================================================================================================

prodPCC = 'PRODPCC_899_8996_5'

driver.get('https://pim.genpt.net/webui/cda_attribute_portal#contextID=GL&workspaceID=''Main&selection=' + prodPCC +
           '&nodeType=product')
driver.maximize_window()

link_attribute = wait.until(EC.element_to_be_clickable((By.XPATH, '//div[@id = "toolbar_button_Create_attribute_link"]')))
link_attribute.click()

search_tab = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[.='Search']"))).click()

attribute_id = 'GPC_material'
search_attribute_id = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[7]/div/table/tbody/tr[2]/'
                                                                          'td[2]/div/table/tbody/tr/td/table/tbody/tr/'
                                                                          'td/div/table/tbody/tr[2]/td/div/div[2]/div/'
                                                                          'table/tbody/tr[1]/td/table/tbody/tr/td[1]/'
                                                                          'input')))
search_attribute_id.send_keys(attribute_id)

search = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[.='Search']"))).click()

attribute_description = 'Material'
select_result = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[.='" + attribute_description + "']"))).click()

ok = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[.='OK']"))).click()





#-------------add Y to attribute---------------------------------------------------------------------------------------

attribute_id = 'GPC_material'
#
# find_attribute_id = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[.='" + attribute_id + "']"))).click()

table = wait.until(driver.find_element(By.XPATH, "//tr/td[@class ='readonly-cell cell-selected cell-selected-primary sheet-coll']"))


print(table)

# id = table.find_element(By.XPATH("//tr/td[contains(text(), 'GPC_material')]"))
#
#
# print(id, " Found it")
#
# id.click()
