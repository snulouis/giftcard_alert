from selenium import webdriver

driver = webdriver.Chrome('./chromedriver')

driver.get('http://prod.danawa.com/info/?pcode=5232151&keyword=%ED%95%B4%ED%94%BC%EB%A8%B8%EB%8B%88&cate=19231551')
elements = driver.find_elements_by_css_selector('#blog_content > div.summary_info > div.detail_summary > div.summary_left > div.lowest_area > div.lowest_top > div > span.lwst_prc > a > em')
print(elements[0].text)

driver.quit()
