import time
from django.test import SimpleTestCase
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class AuthTestCase(SimpleTestCase):

    allow_database_queries = True

    def setUp(self):
        self.selenium = webdriver.Remote(command_executor="http://selenium:4444/wd/hub",
                                         desired_capabilities=DesiredCapabilities.CHROME)
        self.selenium.implicitly_wait(10)
        self.selenium.get("http://django:9000")
        time.sleep(1)

    def tearDown(self):
        self.selenium.stop_client()

    def test_login_successful(self):
        print("Q"*34)
        EXPECTED_URL = "http://django:9000/user/login/"

        # usermame_input = self.selenium.find_elements_by_id("username")
        # usermame_input.send_keys('fatima')
        usermame_input = self.selenium.find_element_by_xpath('//*[@id="username"]')
        usermame_input.send_keys("fatima")
        time.sleep(3)
        # password_input = self.selenium.find_elements_by_id("password")
        # password_input.send_keys("nikitinoleg24335")
        password_input =self.selenium.find_element_by_id("password")
        password_input.send_keys("nikitinoleg24335")
        time.sleep(3)

        submit_button = self.selenium.find_element_by_xpath("//*[@id='content']/div/form/p/button")
        submit_button.click()
        time.sleep(3)

        # if not test:
        #     enter_button = self.selenium.find_element_by_xpath("//a[@href='/']/button")
        #     enter_button.click()
        #     time.sleep(1)
        # with self.assertRaises(TimeoutException):
        #     WebDriverWait(self.selenium, 5).until(EC.url_changes(self.selenium.current_url))
        # self.assertNotEqual(self.selenium.current_url, EXPECTED_URL)
