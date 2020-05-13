from base.Selenium_Drivers import SeleniumDrivers
import logging
import utilities.Custom_Logger as cl


class TestStatus(SeleniumDrivers):
    log = cl.customLogger(logging.INFO)
    def __init__(self ,driver):
        super(TestStatus,self).__init__(driver)
        self.resultList=[]

    def setResult(self,result,resultMessage):
        if result is not None:
            if result:
                self.resultList.append("PASS")
                self.log.info(("******** Verification Sucesssfull******", resultMessage))
            else:
                self.resultList.append("FAIL")
                self.log.error(("******** Verification Failed******", resultMessage))
                self.screenshot(resultMessage)
        else:
            self.resultList.append("FAIL")
            self.log.error(("******** Verification Failed******", resultMessage))
            self.screenshot(resultMessage)


    def mark(self,result,resultMessage):
        self.setResult(result,resultMessage)

    def markFinal(self, testName, result, resultMessage):
        self.setResult(result,resultMessage)
        if "FAIL" in self.resultList:
            self.log.error(testName + "FAILED")
            self.resultList.clear()
            assert True == False
        else:
            self.log.info(testName + "PASSED")
            self.resultList.clear()
            assert True == True


