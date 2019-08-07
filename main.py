from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import time
import random

driver_1 = webdriver.Chrome()
driver_1.implicitly_wait(0)
url_1 = 'https://mirrors.tuna.tsinghua.edu.cn/pypi/web/packages/'
driver_1.get(url_1)
tr_list_1=driver_1.find_elements_by_tag_name("tr")
for tr_1 in tr_list_1:
    td_list_1 = tr_1.find_elements_by_tag_name("td")
    if(len(td_list_1)>0):
        text_1=tr_1.find_elements_by_tag_name("td")[0].text
        if(len(text_1)==3):
            url_2 = url_1+str(text_1)  
            #'https://mirrors.tuna.tsinghua.edu.cn/pypi/web/packages/00/'
            driver_2  = webdriver.Chrome()
            time_2 = random.randint(1,10)
            driver_2.get(url_2)
            tr_list_2=driver_2.find_elements_by_tag_name("tr")
            for tr_2 in tr_list_2:
                td_list_2 = tr_2.find_elements_by_tag_name("td")
                if(len(td_list_2)>0):
                    text_2=tr_2.find_elements_by_tag_name("td")[0].text
                    if(len(text_2)==3):
                        url_3 = url_2+str(text_2)  
#'https://mirrors.tuna.tsinghua.edu.cn/pypi/web/packages/00/00/'
                        driver_3 = webdriver.Chrome()
                        time_3 = random.randint(1,10)
                        driver_3.get(url_3)
                        # tr_list_3=driver_3.find_elements_by_tag_name("tr")
                        # print(tr_list_3)
                        # for tr_3 in tr_list_3:
                        #     td_list_3 = tr_3.find_elements_by_tag_name("td")
                        #     if(len(td_list_3)>0):
                        #         text_3=tr_3.find_elements_by_tag_name("td")[0].text
                        #         if(len(text_3)>17):
                        for link_3 in driver_3.find_elements_by_xpath("//*[@href]"):
                            if(len(str(link_3.get_attribute('href')))>110):
                                url_4 = str(link_3.get_attribute('href'))
                                driver_4 = webdriver.Chrome()
                                time_4 = random.randint(1,10)
                                driver_4.get(url_4)
                                for link_4 in driver_4.find_elements_by_xpath("//*[@href]"):
                                    check_txt = str(link_4.get_attribute('href'))
                                    if(len(check_txt)>130):

                                        f_file = open('tsinghua_url.txt','a')
                                        f_file.write(check_txt+'\n')
                                        

# https://mirrors.tuna.tsinghua.edu.cn/pypi/web/packages/00/02/167a1d7be500797b57a6db0c628ac81f5dd646291e624a8b3e7a9cef2417/
                                    # button_3 = tr_3.find_elements_by_tag_name("td")[0]
                                    # b_temp = tr_3.title
                                    # # a_tmp = button_3.click()
                                    # print(b_temp)
                                    # driver_3.switch_to.window(driver_3.window_handles[0])
                                    # print(driver_3.window_handles[0])

                                    # driver_4 = webdriver.Chrome()
                                    # time_4 = random.randint(1,10)
                                    # driver_4.get(url_4)
                                    # tr_list_4=driver_3.find_elements_by_tag_name("tr")
                                    # for tr_4 in tr_list_4:
                                    #     td_list_4 = tr_4.find_elements_by_tag_name("td")
                                    #     if(len(td_list_4)>0):
                                           
                                    #         text_4=tr_4.find_elements_by_tag_name("td")[0].text
                                    #         if(len(text_4)>13):
                                    #             button_4 = tr_4.find_elements_by_tag_name("td")[0]
                                    #             button_4.click()
                                    #             url_5 = url_4+str(text_4) 
                                    #             print(url_5)
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
