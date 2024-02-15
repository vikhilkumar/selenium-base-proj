import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions

class LaunchPage():
    def __init__(self,driver,wait):
        self.driver=driver
        self.wait=wait

    def departfrom(self,departFromlocation):
        depart = self.wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, "#BE_flight_origin_city")))
        depart.click()
        time.sleep(2)
        depart.send_keys('Mumbai')
        depart.send_keys(Keys.ENTER)

    def goingTo(self,goingTolocation):
        arrival = self.wait.until(expected_conditions.element_to_be_clickable((By.ID, "BE_flight_arrival_city")))
        arrival.click()
        time.sleep(2)
        arrival.send_keys("New York")
        time.sleep(2)
        arr1 = self.wait.until(
            expected_conditions.presence_of_all_elements_located((By.XPATH, "//div[@class='viewport']//div//div/li")))
        for ar in arr1:
            if "New York (JFK)" in ar.text:
                ar.click()
                break

    def journyDate(self,date):
        self.wait.until(expected_conditions.element_to_be_clickable((By.ID, "BE_flight_origin_date"))).click()
        all_dates = self.wait.until(expected_conditions.element_to_be_clickable((By.XPATH, "//div[@id='monthWrapper']//tbody//td[@class!='inActiveTD'][@class!='inActiveTD weekend']"))). \
                            find_elements(By.XPATH,"//div[@id='monthWrapper']//tbody//td[@class!='inActiveTD'][@class!='inActiveTD weekend']")

        for dt in all_dates:
            if dt.get_attribute('data-date')=="19/09/2024":
                dt.click()
                break

    def clickSearchbtn(self):
        self.wait.until(expected_conditions.element_to_be_clickable((By.XPATH, "(//input[@id='BE_flight_flsearch_btn'])[1]"))).click()
        time.sleep(3)

