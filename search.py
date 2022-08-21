from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class Search:

    def search(self):

        driver = webdriver.Firefox()

        driver.get("https://www.avito.ru")

        input_tag = driver.find_element(By.XPATH, "//div[@class='suggest-root-NysQD suggest-searchFormDesign-PpmeM']//div//div[@class='suggest-inputWrap-n4VgP']//label[@class='input-layout-input-layout-_HVr_ input-layout-size-s-COZ10 input-layout-text-align-left-U2OZJ width-width-12-_MkqF suggest-input-X6pqt js-react-suggest']//input")
        input_tag.send_keys('Машины', Keys.ENTER)

        # enter_tag = driver.find_element(by='class')
        # enter_tag.click()


if __name__ == '__main__':
    search = Search()
    search.search()
