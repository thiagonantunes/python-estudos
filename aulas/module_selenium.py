from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://youtube.com')
searchbox = driver.find_element_by_xpath('//*[@id="search"]')
searchbox.send_keys('Corey Schafer')
searchButton = driver.find_element_by_xpath('//*[@id="search-icon-legacy"]/yt-icon')
searchButton.click()
