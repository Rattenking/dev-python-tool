import time
from selenium import webdriver
from datetime import datetime
from apscheduler.schedulers.blocking import BlockingScheduler

def is_element_exist(driver, element):
  flag = True
  try:
    driver.find_element_by_xpath(element)
  except:
    flag = False
  finally:
    return flag

def auto_sign_in_csdn():
  driver = webdriver.Chrome()
  print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
  try:
    driver.maximize_window()
    driver.get("https://i.csdn.net/#/user-center/draw")
    
    driver.find_element_by_xpath('//div[@class="main-select"]/ul/li/a[text()="账号密码登录"]').click()
    driver.find_element_by_id("all").send_keys("18684006650")
    driver.find_element_by_id("password-number").send_keys("stone18684006650")
    driver.find_element_by_xpath("//button[@class='btn btn-primary']").click()
    time.sleep(3)
    if is_element_exist(driver,"//div[@class='handle_box to_sign']"):
      driver.find_element_by_xpath("//div[@class='handle_box to_sign']").click()
  except Exception as e:
    print(e)
  finally:
    driver.quit()

if __name__ == '__main__':
  scheduler = BlockingScheduler()
  scheduler.add_job(auto_sign_in_csdn, 'cron', day_of_week='0-6', hour=9, minute=10)
  scheduler.start()