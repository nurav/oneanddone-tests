from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()

# 1. Open the home page
driver.get("https://oneanddone.mozilla.org/")

# 2. Click the first task in the Suggested Tasks list
elem = driver.find_element_by_xpath("//ol[@class=\"task-list\"]/li[1]//p//a")
task_url = elem.get_attribute("href")
elem.click()

# 3. Verify that the browser is on the Task Detail page for that task.
assert driver.current_url == task_url

# 4. Verify that the Get Started button is visible.
elem = driver.find_element_by_id("get-started")
assert elem.is_displayed()

# 5. Verify that a team for the task is visible.
elem = driver.find_element_by_xpath("//div[@class=\"three-fields\"]//a")
team_url = elem.get_attribute("href")
assert elem.is_displayed()

# 6. Click the link for the team.
elem.click()

# 7. Verify that the browser is on the Team Detail page for that team.
assert driver.current_url == team_url


