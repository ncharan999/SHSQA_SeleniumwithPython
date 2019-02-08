class repairLink():

    def __init__(self,driver):
        self.driver = driver
        self.repair_element = "//nav[@class='nav-main']/ul/li[1]/a"
        self.scheduleButton_element = "(//span[contains(text(),'Schedule now')])[3]"
        self.dishWasher_element = "//*[@id='scheduler-appliance-info-top-selection-appliance-name-dishwasher']"
        self.boschBrand_element = "//*[@id='scheduler-appliance-info-top-selection-appliance-brand-bosch']"
        self.coverage_element = "//label[@id='scheduler-appliance-info-top-selection-no-coverage']"
        self.problemDropDownBox_element = "//*[@id='scheduler-appliance-problem-field']"
        self.problem_element = "//*[@value='Displaying error code']"
        self.next_element = "//span[contains(text(),'Next')]"
        self.streetNumber_element = "//*[@id='scheduler-contact-address-i-field']"
        self.unitNumber_element = "//*[@id='scheduler-contact-address-ii-field']"
        self.city_element = "//*[@id='scheduler-contact-city-field']"
        self.cityDropDown_element = "//*[@value='DE']"
        self.zipCode_element = "//*[@id='scheduler-contact-zip-code-field']"
        self.AvilabilityError_element = "//*[contains(text(),'We’re sorry but we’re unable to schedule your service online.')]"
        self.Failure_message1 = "//*[@class='notice-message']"
        self.Failure_message2 = "//*[@class='call-message']"
        self.AvilabilityError = "We’re sorry but we’re unable to schedule your service online."
        self.AvilabilityDatePage_element = "//*[contains(text(),'Choose a date and time')]"
        self.AvilabilityErrorCloseButton_element = "//*[contains(text(),'Close')]"
        self.AvilabilityDate_element = "(//*[contains(text(),'8am-12pm')])[2]"
        self.FirstName_element = "//*[@id='scheduler-contact-first-name-field']"
        self.LastName_element = "//*[@id='scheduler-contact-last-name-field']"
        self.PhoneNumber_element = "//*[@id='scheduler-contact-phone-number-field']"
        self.Email_element = "//*[@id='scheduler-contact-email']"
        self.ConfirmEmail_element = "//*[@id='scheduler-contact-confirm-email']"
        self.repairBookButton_element = "(//span[contains(text(),'Book')])[2]"
        self.SOSuccessMessage = "//*[@class='successful-book-text']"
        self.WrongAddressMessage_element = "//*[@class='error-message']"


    def repairPageTest(self):
        driver=self.driver
        driver.find_element_by_xpath(self.repair_element).click()
        driver.find_element_by_xpath(self.scheduleButton_element).click()
        driver.find_element_by_xpath(self.dishWasher_element).click()
        driver.find_element_by_xpath(self.boschBrand_element).click()
        driver.find_element_by_xpath(self.coverage_element).click()
        driver.find_element_by_xpath(self.problemDropDownBox_element).click()
        driver.find_element_by_xpath(self.problem_element).click()
        driver.find_element_by_xpath(self.next_element).click()


    def repairPageAddress(self,StreetNumber):
        driver=self.driver
        driver.find_element_by_xpath(self.streetNumber_element).clear()
        driver.find_element_by_xpath(self.streetNumber_element).send_keys(StreetNumber)

    def repairPageUnit(self, unitNumber):
        driver = self.driver
        #driver.find_element_by_xpath(self.unitNumber_element).clear()
        driver.find_element_by_xpath(self.unitNumber_element).send_keys(unitNumber)

    def repairPageCity(self,city):
        driver = self.driver
        #driver.find_element_by_xpath(self.city_element).clear()
        driver.find_element_by_xpath(self.city_element).send_keys(city)

    def repairPageCityDropdown(self):
        driver = self.driver
        driver.find_element_by_xpath(self.cityDropDown_element).click()

    def repairPageZipcode(self,Zipcode):
        driver = self.driver
        driver.find_element_by_xpath(self.zipCode_element).clear()
        driver.find_element_by_xpath(self.zipCode_element).send_keys(Zipcode)

    def repairPageNext(self):
        driver = self.driver
        driver.find_element_by_xpath(self.next_element).click()
        # if driver.find_element_by_xpath(self.WrongAddressMessage_element).is_enabled():
        #     print(driver.find_element_by_xpath(self.WrongAddressMessage_element).text)
        #
        # else :
        #     print("I dont have any issues at the address page")



    def repairAvilability(self):
        driver = self.driver
        driver.implicitly_wait(3000)
        # if (driver.find_element_by_xpath(self.AvilabilityError_element).is_displayed()):
        #     driver.find_element_by_xpath(self.AvilabilityErrorCloseButton_element).click()
        # else :
        # print('Before I am here at erro page')
        if driver.find_element_by_xpath(self.AvilabilityDate_element).is_enabled():
           driver.find_element_by_xpath(self.AvilabilityDate_element).click()
           # RepairSOSuccessMessage=driver.find_element_by_xpath(self.SOSuccessMessage).text
           # print(RepairSOSuccessMessage)
           # driver.find_element_by_xpath(self.next_element).click()
        else :
            driver.find_element_by_xpath(self.AvilabilityErrorCloseButton_element).is_enabled()
            driver.find_element_by_xpath(self.AvilabilityErrorCloseButton_element).click()
            return driver.title

        # try:
        #     print
        #     "Hello World"
        # except:
        #     print
        #     "This is an error message!"

    def customerFirstName(self,FirstName):
        driver = self.driver
        driver.find_element_by_xpath(self.FirstName_element).clear()
        driver.find_element_by_xpath(self.FirstName_element).send_keys(FirstName)

    def customerLastName(self,LastName):
        driver = self.driver
        driver.find_element_by_xpath(self.LastName_element).clear()
        driver.find_element_by_xpath(self.LastName_element).send_keys(LastName)

    def customerPhoneNumber(self,PhoneNumber):
        driver = self.driver
        #driver.find_element_by_xpath(self.PhoneNumber_element).clear()
        driver.find_element_by_xpath(self.PhoneNumber_element).send_keys(PhoneNumber)

    def customerEmail(self, Email):
        driver = self.driver
        #driver.find_element_by_xpath(self.Email_element).clear()
        driver.find_element_by_xpath(self.Email_element).send_keys(Email)
        driver.implicitly_wait(3000)

    def customerConfirmEmail(self, Email):
        driver = self.driver
        #driver.find_element_by_xpath(self.ConfirmEmail_element).clear()
        driver.find_element_by_xpath(self.ConfirmEmail_element).send_keys(Email)
        driver.implicitly_wait(3000)

    def repairBookButton(self):
        driver = self.driver
        driver.find_element_by_xpath(self.repairBookButton_element).click()

    def repairSuccessMessage(self):
        driver = self.driver
        RepairSOSuccessMessage = driver.find_element_by_xpath(self.SOSuccessMessage).text
        print(RepairSOSuccessMessage)
    #Test function just for running more tests
    def test_sumSO(x,y):
        sum=x+y
        print("Sum of ",x,"& ",y," is: ",sum)
