#from realbrowserlocusts import FirefoxLocust, ChromeLocust, PhantomJSLocust
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


from locust import TaskSet, task, HttpLocust


class LocustUserBehavior(TaskSet):

    def open_locust_homepage(self):
        self.client.get("/")
        #self.client.wait.until(EC.visibility_of_element_located((By.XPATH, '//a[text()="Documentation"]')), "documentation link is visible")

    def click_through_to_result(self):
        self.client.get("/vn/insurance/travel/quote-online/")
        #self.client.find_element_by_xpath('//a[text()="Documentation"]').click()
        #self.client.wait.until(EC.visibility_of_element_located((By.XPATH, '//h1[text()="Locust Documentation"]')), "documentation is visible")

    @task(1)
    def homepage_and_docs(self):
        #self.client.timed_event_for_locust("Go to", "homepage", self.open_locust_homepage)
        #self.client.timed_event_for_locust("Click to", "documentation", self.click_through_to_result)
        self.open_locust_homepage


    @task(2)
    def homepage_and_docs2(self):
        #self.client.timed_event_for_locust("Go to", "homepage", self.open_locust_homepage)
        #self.client.timed_event_for_locust("Click to", "documentation", self.click_through_to_result)
        self.click_through_to_result

#class LocustUser(FirefoxLoc--ust):
#class LocustUser(ChromeLocust):
#class LocustUser(PhantomJSLocust):
class LocustUser(HttpLocust):
    #host = "https://www.gobear.com/"
    timeout = 30 #in seconds in waitUntil thingies
    min_wait = 100
    max_wait = 1000
    #screen_width = 1200
    #screen_height = 600
    task_set = LocustUserBehavior
