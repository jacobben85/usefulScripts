from selenium import webdriver
import subprocess

driver = webdriver.PhantomJS() # or add to your PATH
driver.set_window_size(1024, 768) # optional
driver.get('https://google.com/')
driver.save_screenshot('screen.png') # save a screenshot to disk

driver.quit()

args = ["phantomjs", "headers.js", "http://www.univision.com"]
result = subprocess.check_output(args)

print result