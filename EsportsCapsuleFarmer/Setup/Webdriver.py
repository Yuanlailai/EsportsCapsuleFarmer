from selenium import webdriver
from selenium_driver_updater import DriverUpdater
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.service import Service as EdgeService

class Webdriver:
    def __init__(self, browser, headless) -> None:
        self.browser = browser
        self.headless = headless

    def createWebdriver(self):
        """
        Creates the web driver which is automatically controlled by the program
        """
        match self.browser:
            case "chrome":
                # choose driverPath automatically to manually
                driverPath = "D:\EsportsCapsuleFarmer-master\chromedriver107.exe"
                # driverPath = DriverUpdater.install(path=".", driver_name=DriverUpdater.chromedriver, upgrade=False, check_driver_is_up_to_date=True, old_return=False)
                options = self.addWebdriverOptions(webdriver.ChromeOptions())
                # force chrome path
                options.binary_location = r"D:\\Chrome107\\App\\Chrome-bin\\chrome.exe"
                # force chromedata path
                # edit website settings at lolesports.com. change sound auto to enable
                options.add_argument("user-data-dir=D:\\EsportsCapsuleFarmer-master\\ChromeData")
                # options.add_argument("user-data-dir=D:\\Chrome107\\Data\\profile")
                service = ChromeService(driverPath)
                print(driverPath)
                return webdriver.Chrome(service=service, options=options)            
            case "firefox":
                driverPath = DriverUpdater.install(path=".", driver_name=DriverUpdater.geckodriver, upgrade=True, check_driver_is_up_to_date=True, old_return=False)
                options = self.addWebdriverOptions(webdriver.FirefoxOptions())
                service = FirefoxService(driverPath)
                return webdriver.Firefox(service=service, options=options)
            case "edge":  # NO CURRENT DRIVER AVAILABLE
                driverpath = "D:\EsportsCapsuleFarmer-master\msedgedriver.exe"
                # driverPath = DriverUpdater.install(path=".", driver_name=DriverUpdater.edgedriver, upgrade=True, check_driver_is_up_to_date=True, old_return=False)
                options = self.addWebdriverOptions(webdriver.EdgeOptions())
                service = EdgeService(driverPath)
                print(driverPath)
                return webdriver.Edge(service=service, options=options)

    def addWebdriverOptions(self, options):
        options.add_argument("log-level=3")
        options.add_experimental_option('useAutomationExtension', False)
        options.add_experimental_option("excludeSwitches", ['enable-automation'])
        if self.headless:
            options.add_argument("--headless")
            user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"
            options.add_argument(f'user-agent={user_agent}')
        return options
