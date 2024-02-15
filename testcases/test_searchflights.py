#Session 48
import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions

@pytest.mark.usefixtures("setup")   #It will call the function fixture from conftest file   #Use of conftest file is It allows you to define fixtures and other configurations that are common across multiple test files or directories within your project
class TestSearchFlights():
    def test_flights(self):
        #Launching the webdriver and opening the travel website
        #It will automatically launch the browser using conftest file as source file


        #Providing from location
        depart=self.wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,"#BE_flight_origin_city")))
        depart.click()
        time.sleep(2)
        depart.send_keys('Mumbai')
        depart.send_keys(Keys.ENTER)

        # Providing going to location
        arrival=self.wait.until(expected_conditions.element_to_be_clickable((By.ID,"BE_flight_arrival_city")))
        arrival.click()
        time.sleep(2)
        arrival.send_keys("New York")
        time.sleep(2)
        arr1=self.wait.until(expected_conditions.presence_of_all_elements_located((By.XPATH,"//div[@class='viewport']//div//div/li")))
        for ar in arr1:
            if "New York (JFK)" in ar.text:
                ar.click()
                break

        #To resolve sync issue
        self.wait.until(expected_conditions.element_to_be_clickable((By.ID,"BE_flight_origin_date"))).click()
        all_dates=self.wait.until(expected_conditions.element_to_be_clickable((By.XPATH,"//div[@id='monthWrapper']//tbody//td[@class!='inActiveTD'][@class!='inActiveTD weekend']"))).\
            find_elements(By.XPATH,"//div[@id='monthWrapper']//tbody//td[@class!='inActiveTD'][@class!='inActiveTD weekend']")

        #To select depature date
        for dt in all_dates:
            if dt.get_attribute('data-date')=="19/09/2024":
                dt.click()
                break

        #click on flight search button
        self.wait.until(expected_conditions.element_to_be_clickable((By.XPATH,"(//input[@id='BE_flight_flsearch_btn'])[1]"))).click()
        time.sleep(3)

        #Selects the filter 1 stop
        self.wait.until(expected_conditions.element_to_be_clickable((By.XPATH, "(//p[normalize-space()='1'])[1]"))).click()
        time.sleep(4)

        #TO scroll to the bottom of the page
        # Get initial page height
        last_height = self.driver.execute_script("return document.body.scrollHeight")

        while True:
            # Scroll to the bottom of the page
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            # Wait for some time to let new content load
            time.sleep(2)

            # Calculate new scroll height and compare with last scroll height
            new_height = self.driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                # If the scroll height hasn't changed, we've reached the bottom
                break
            last_height = new_height
        time.sleep(2)

        all_stops=self.wait.until(expected_conditions.presence_of_all_elements_located((By.XPATH,"//span[contains(text(),'Non Stop') or contains(text(),'1 Stop') or contains(text(),'2 Stop')]")))
        # alternate xpath for 1 stop -
        # all_stops=driver.find_elements(By.XPATH,"//div//div//div//div//div//div//span[@class='dotted-borderbtm']")
        print(len(all_stops))

        #Verify that the filtered results show flights having only 1 stop
        for stop in all_stops:
            if stop.text=="1 Stop":
                print("The stop is: "+stop.text)
                assert stop.text=="1 Stop"
                print("assert pass")

#Since we are using the pytest framework we need to call the class obj
