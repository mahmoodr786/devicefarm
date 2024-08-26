import boto3
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver import Remote


devicefarm_client = boto3.client("devicefarm", region_name="us-west-2")

testgrid_url_response = devicefarm_client.create_test_grid_url(
    projectArn= "arn:aws:devicefarm:us-west-2:**********:testgrid-project:0c727dc8-7a2f-4326-b364-0aa0331258bf", # Your ARN here
    expiresInSeconds=300
)

options = webdriver.ChromeOptions()
driver = Remote(testgrid_url_response['url'], options=options)

driver.get("https://a3xz565riq3kyzdhkqobhjlsni0nnwsm.lambda-url.us-east-1.on.aws") # Update your website URL here

# Fill out the form
driver.find_element(By.ID, "firstName").click()
driver.find_element(By.ID, "firstName").send_keys("hello")

driver.find_element(By.ID, "lastName").click()
driver.find_element(By.ID, "lastName").send_keys("hi")

driver.find_element(By.ID, "username").click()
driver.find_element(By.ID, "username").send_keys("myusername")

driver.find_element(By.ID, "email").click()
driver.find_element(By.ID, "email").send_keys("someemail@example.com")

driver.find_element(By.ID, "address").click()
driver.find_element(By.ID, "address").send_keys("1234 main st")

# Select country
driver.find_element(By.ID, "country").click()
Select(driver.find_element(By.ID, "country")).select_by_visible_text("United States")

# Select state
driver.find_element(By.ID, "state").click()
Select(driver.find_element(By.ID, "state")).select_by_visible_text("California")

driver.find_element(By.ID, "zip").click()
driver.find_element(By.ID, "zip").send_keys("345678")

# Handle checkboxes/radio buttons
driver.find_element(By.CSS_SELECTOR, ".needs-validation > .form-check:nth-child(3) > .form-check-label").click()
driver.find_element(By.CSS_SELECTOR, ".form-check:nth-child(4) > .form-check-label").click()
driver.find_element(By.CSS_SELECTOR, ".form-check:nth-child(2) > .form-check-label").click()

# Fill out credit card information
driver.find_element(By.ID, "cc-name").click()
driver.find_element(By.ID, "cc-name").send_keys("fadfadf")

driver.find_element(By.ID, "cc-number").click()
driver.find_element(By.ID, "cc-number").send_keys("fadfasd")

driver.find_element(By.ID, "cc-expiration").click()
driver.find_element(By.ID, "cc-expiration").send_keys("05/20/2024")

driver.find_element(By.ID, "cc-cvv").click()
driver.find_element(By.ID, "cc-cvv").send_keys("123")

# Submit the form
driver.find_element(By.CSS_SELECTOR, ".w-100").click()

driver.quit()

