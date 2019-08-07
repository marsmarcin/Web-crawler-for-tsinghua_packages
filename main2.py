from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import time
import numpy as np 
import random

driver_1 = webdriver.Chrome()
driver_1.implicitly_wait(0)
url_1 = 'https://mirrors.tuna.tsinghua.edu.cn/pypi/web/packages/'
driver_1.get(url_1)

for link_1 in driver_1.find_elements_by_xpath("//*[@href]"):
    
    text_1=str(link_1.get_attribute('href'))
    # print(text_1)
    if(len(text_1)==58 and text_1[-1]=='/'):
        url_2 = text_1
#'https://mirrors.tuna.tsinghua.edu.cn/pypi/web/packages/00/'
        driver_2  = webdriver.Chrome()
        # time_2 = random.randint(1,5)
        time_2 = np.random.rand()
        driver_2.get(url_2)
        
        for link_2 in driver_2.find_elements_by_xpath("//*[@href]"):
            text_2=str(link_2.get_attribute('href'))
            # print(text_2)
            if(len(text_2)==61 and text_2[-1]=='/'):
                url_3 = text_2 
#'https://mirrors.tuna.tsinghua.edu.cn/pypi/web/packages/00/00/'
                driver_3 = webdriver.Chrome()
                # time_3 = random.randint(1,5)
                time_3 = np.random.rand()
                driver_3.get(url_3)
                for link_3 in driver_3.find_elements_by_xpath("//*[@href]"):
                    text_3=str(link_3.get_attribute('href'))
                    if(len(text_3)==122):
                        url_4 = text_3
                        driver_4 = webdriver.Chrome()
                        # time_4 = random.randint(1,5)
                        time_4 = np.random.rand()
                        # try:

                        #     driver_4.get(url_4)
                        
                        # except Exception,e:
                        #     print(Exception,":",e)
                        try: 
                            driver_4.get(url_4)
                        except ZeroDivisionError as e:
                            print('except:', e)
                        finally:
                            driver_4.refresh()

                        for link_4 in driver_4.find_elements_by_xpath("//*[@href]"):
                            check_txt = str(link_4.get_attribute('href'))
                            if(len(check_txt)>130):
                                f_file = open('tsinghua_url.txt','a')
                                f_file.write(check_txt+'\n')
# https://mirrors.tuna.tsinghua.edu.cn/pypi/web/packages/00/02/167a1d7be500797b57a6db0c628ac81f5dd646291e624a8b3e7a9cef2417/
                        time.sleep(time_4)
                        driver_4.close()
                        driver_4.quit()
                time.sleep(time_3)
                driver_3.close()
                driver_3.quit()
        time.sleep(time_2)
        driver_2.close()
        driver_2.quit()
time.sleep(1)
driver_1.close()
driver_1.quit()
