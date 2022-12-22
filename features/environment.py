from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from app.application import Application
from selenium.webdriver.chrome.options import Options

opt = Options()
opt.add_argument("--headless")


def browser_init(context, test_name):
    """
    :param context: Behave context
    """

    context.driver = webdriver.Chrome(executable_path='../../chromedriver.exe', chrome_options=opt)
    # context.browser = webdriver.Safari()
    # context.browser = webdriver.Firefox(executable_path="../geckodriver.exe")

    #for browserstack ##
    desired_cap = {
        'browser': 'Chrome',
        'os_version': '108',
        'name': test_name
    }
    bs_user = "fawziamasud_kNC9b3"
    bs_key = "ditULBsjzAEVyAJEhyHJ"
    url = f'http://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'
    context.driver = webdriver.Remote(url, desired_capabilities=desired_cap)

    context.driver.maximize_window()
    context.driver.implicitly_wait(4)
    context.driver.wait = WebDriverWait(context.driver, 10)
    context.app = Application(context.driver)


def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context, scenario.name)


def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)


def after_scenario(context, feature):
    context.driver.delete_all_cookies()
    context.driver.quit()
