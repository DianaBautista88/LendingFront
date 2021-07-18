from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import unittest 

options = Options()

options.add_argument("--disable-infobars")
options.add_experimental_option("prefs",{
        "profile.default_content_setting_values.notifications" : 1
})


class Test(unittest.TestCase):
	def testName(self):
                driver = webdriver.Chrome(chrome_options=options,executable_path=r'chromedriver.exe')
                driver.get('https://google.com')

                search_input = driver.find_element_by_name("q")
                search_input.click()
                search_input.send_keys("LendingFront")
                driver.save_screenshot('screenshot1.png')
                search_input.submit()
                driver.save_screenshot('screenshot2.png')

                LendingFront_input = driver.find_element_by_xpath("//div[@class='yuRUbf']/h3[text()='LendingFront']")
                 
                LendingFront_input.click()
                titleOfWebPage = driver.title
                # verify title is bing
                self.assertEqual("Bitng", titleOfWebPage, "webpage title is not matching")
                driver.close()
if __name__ == "__main__":
	unittest.main()


#GyAeWb



