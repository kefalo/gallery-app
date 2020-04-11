from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class Registation():
    driver = webdriver.Firefox()
    webPage = "https://gallery-app.vivifyideas.com/"

    def __init__(self):
        print("Inicializing")

    def openPage(self):
        self.driver.maximize_window()
        self.driver.get(self.webPage)
        #print("Web Page Loaded Successfully")

    def register(self):
        self.driver.find_element(By.XPATH, "//html//body//div[1]//div[1]//nav//div//ul[2]//li[2]//a").click()
        #print("Register Form Loaded Successfully")

    def enter_the_data(self):
        first_Name = "first-name"
        last_Name = "last-name"
        Email = "email"
        Password = "password"
        confirmed_Password = "password-confirmation"
        accept_Checkbox = "//html//body//div[1]//div[2]//div//form//div[6]//input"
        submit_button = "//html//body//div[1]//div[2]//div//form//button"

        self.driver.find_element(By.ID, first_Name).send_keys("test1")
        self.driver.find_element(By.ID, last_Name).send_keys("test1")
        self.driver.find_element(By.ID, Email).send_keys("testemail@email.com")
        self.driver.find_element(By.ID, Password).send_keys("PasswordTest1")
        self.driver.find_element(By.ID, confirmed_Password).send_keys("PasswordTest1")
        self.driver.find_element(By.XPATH, accept_Checkbox).click()
        self.driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/form/button").click()


ff = Registation()

ff.openPage()
print("Web Page Loaded Successfully")
ff.register()
print("Register Form Loaded Successfully")
ff.enter_the_data()
print("You've entered all the data, now proceed.. By clicking on Submit")