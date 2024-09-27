import requests
import pytest
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestIntegration():

    def test_frontend_to_backend(self):
        # Replace this URL with the actual Minikube service URL for the frontend
        frontend_url = 'http://172.24.133.70:30850'
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(frontend_url)

        css = 'body h1'
        front_end_header = driver.find_element(By.CSS_SELECTOR, css).text

        response = requests.get(frontend_url)
        self.assertEqual(response.status_code, 200)
        self.assertIn(front_end_header, response.text)


if __name__ == '__main__':
    unittest.main()
