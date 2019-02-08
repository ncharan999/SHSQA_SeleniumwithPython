class homePage():

    def __init__(self, driver):
        self.driver = driver
        self.validurl        = "https://shs:thegreatproject@www.armadillo.xyz/"
        self.repairLink      = "//nav[@class='nav-main']/ul/li[1]/a"
        self.improveLink     = "//nav[@class='nav-main']/ul/li[2]/a"
        #Write all the locators in home page

    def validUrl(self,validurl):
        self.driver.get(self.validurl)

    # def repair(self):
    #      self.driver.find_element_by_xpath(self.repairLink).click()



