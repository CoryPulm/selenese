from selenese.testcases import TestRunner
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium import webdriver


# Start setting up the webdriver
dcap = dict(DesiredCapabilities.PHANTOMJS)
dcap["phantomjs.page.settings.userAgent"] = ("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/53 (KHTML, like Gecko) Chrome/15.0.87")
driver = webdriver.PhantomJS(desired_capabilities=dcap, service_args=['--ignore-ssl-errors=true','--ssl-protocol=any'])
driver.set_window_size(1360, 768)
driver.is_manual = True

testrunner = TestRunner.from_file('test.html')
results = testrunner.run(driver)


