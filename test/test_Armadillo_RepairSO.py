from selenium import webdriver
import pytest
from pages.homePage_armadillo import homePage
from pages.repairPage_armadillo import repairLink
from testdata import Credentials as C

class TestcreateRepairSO():

    @pytest.fixture(scope="class")
    def test_setup(self):
        global driver
        chromeOptions = webdriver.ChromeOptions()
        chromeOptions.add_experimental_option('useAutomationExtension', False)
        chromeOptions.add_argument('--disable-extensions')
        driver = webdriver.Chrome(options=chromeOptions, desired_capabilities=chromeOptions.to_capabilities(),
                                  executable_path='C:/Users/cnallan/PycharmProjects/Python_Selenium/drivers/chromedriver.exe')
        driver.implicitly_wait(10)
        driver.maximize_window()
        yield
        driver.close()
        driver.quit()
        print("TestCompleted")

    def test_createSO(self, test_setup):
        # driver = self.driver
        HomePage = homePage(driver)
        HomePage.validUrl(C.URL)
        RepairLinkPage = repairLink(driver)
        RepairLinkPage.repairPageTest()
        RepairLinkPage.repairPageAddress(C.Street_Number_and_Name)
        RepairLinkPage.repairPageUnit(C.Unit_Number)
        RepairLinkPage.repairPageCity(C.City)
        RepairLinkPage.repairPageCityDropdown()
        RepairLinkPage.repairPageZipcode(C.Zipcode)
        RepairLinkPage.repairPageNext()
        # driver.set_page_load_timeout(10000)
        # RepairLinkPage = repairLink(driver)
        RepairLinkPage.repairAvilability()
        RepairLinkPage.customerFirstName(C.First_Name)
        RepairLinkPage.customerLastName(C.Last_Name)
        RepairLinkPage.customerPhoneNumber(C.Phone_Number)
        RepairLinkPage.customerEmail(C.Email)
        RepairLinkPage.customerConfirmEmail(C.Email)
        # RepairLinkPage.repairPageNext()
        RepairLinkPage.repairBookButton()
        RepairLinkPage.repairSuccessMessage()
    #test testcase for testing
    def test_sumSO1(self):
        test_sumSO=repairLink.test_sumSO(1,2)