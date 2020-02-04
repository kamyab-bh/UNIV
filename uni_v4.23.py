import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import threading 






# import time
# start_time = time.time()
print('\nv 0.4.1')
print('-' * 20," * R A H N A M A * ",'-' * 20,"\n")
print('1. # Shomare daneshjooyito vared kon Enter bezan # --> Shomare Daneshjooyi ')
print('2. #        Ramzeto vared kon Enter bezan        # --> Ramz')
print('3. # Har dafe ye shenase darseto vared kon Enter bezan #')
print('4. # Agar dg nemikhay darsion ezafe koni "ok" vared kon Enter bezan  #\n')
print('-' * 20," * R A H N A M A * ",'-' * 20,"\n\n")

print('#' * 45)
print('# Welcome To UNIV PLUGIN by "Neo Data" Team #')
print("#      Rahnamaye bala ro motale'e konid     #")
print('#' * 45)
print("              .: Good Luck :.               ","\n")

### python code
doros = []
UID = input("Shomare Daneshjooyi:\n")
PASS = input("Ramz:\n")


item = "no"
while item!="ok":
    item = input('shenase dars ro vared konid, agar nemikhahid darse digari ezafe konid benevisid "ok"\n')
    if item =="ok":
        continue
    if item in doros:
        continue
    doros.append(item)
    print("dorose entekhab shode: " ,doros,"\n")

print("dorose entekhab shode: " ,doros)
### python code

k = len(doros)

# def En_v():
# for browser in doros[0]:
def En_v():
    browser = webdriver.Chrome(executable_path=r'chromedriver.exe')
    # browser.maximize_window()
    # browser.set_window_size(3000,2000)
    browser.set_window_position(0,0)
    sleep(1)


    ### LOGIN
    browser.get("http://edu1.iau-tnb.ac.ir")


    browser.find_element_by_id("txtUserName").send_keys(UID)
    browser.find_element_by_id("txtPassword").send_keys(PASS)
    browser.find_element_by_id("btn_ent_stu").click()
    sleep(1)
    ### LOGIN

    # pick = doros.pop()
    picked = []
    # picked_c = []

    ### ENTEKHAB_VAHED
    browser.refresh()
    browser.get("http://edu1.iau-tnb.ac.ir/SelectCourse.aspx")


    browser.find_element_by_id("ContentPlaceHolder1_txtCourseId").send_keys(doros[0])
    browser.find_element_by_id("ContentPlaceHolder1_lnkBtnSelectCourse").click()
    sleep(3)

    x = False
    x = browser.find_elements_by_xpath("//*[contains(text(), 'ثبت شد')]")
    
    

    # for dars in doros[0]:
        
    if x:
        print(doros[0] + " akhz shod\n")
        picked.append(doros[0])

    while not x:
        browser.refresh()
        browser.find_element_by_id("ContentPlaceHolder1_txtCourseId").send_keys(doros[0])
        browser.find_element_by_id("ContentPlaceHolder1_lnkBtnSelectCourse").click()
        sleep(3)

        if x:
            print(doros[0] + " akhz shod\n")
            picked.append(doros[0])
            # picked.append(doros.remove(doros[0]))
            break
        else:
            browser.refresh()

    sleep(5)
    ### ENTEKHAB_VAHED




# -----------------
# for browser in doros[1]:
def En_v2():
    browser = webdriver.Chrome(executable_path=r'chromedriver.exe')
    # browser.maximize_window()
    # browser.set_window_size(3000,2000)
    browser.set_window_position(0,0)
    sleep(1)


    ### LOGIN
    browser.get("http://edu1.iau-tnb.ac.ir")

    # UID = input("ID\n")
    browser.find_element_by_id("txtUserName").send_keys(UID)
    # PASS = input("ramz\n")
    browser.find_element_by_id("txtPassword").send_keys(PASS)
    browser.find_element_by_id("btn_ent_stu").click()
    ### LOGIN

    # pick = doros.pop()
    picked = []
    # picked_c = []

    ### ENTEKHAB_VAHED
    browser.refresh()
    browser.get("http://edu1.iau-tnb.ac.ir/SelectCourse.aspx")
        

    browser.find_element_by_id("ContentPlaceHolder1_txtCourseId").send_keys(doros[1])
    browser.find_element_by_id("ContentPlaceHolder1_lnkBtnSelectCourse").click()
    sleep(3)

    x = False
    x = browser.find_elements_by_xpath("//*[contains(text(), 'ثبت شد')]")


    # for dars in doros[0]:
        
    if x:
        print(doros[1] + " akhz shod\n")
        picked.append(doros[1])

    while not x:
        browser.refresh()
        browser.find_element_by_id("ContentPlaceHolder1_txtCourseId").send_keys(doros[1])
        browser.find_element_by_id("ContentPlaceHolder1_lnkBtnSelectCourse").click()
        sleep(3)

        if x:
            print(doros[1] + " akhz shod\n")
            picked.append(doros[1])
            # picked.append(doros.remove(doros[0]))
            break
        else:
            browser.refresh()

    sleep(5)
    ### ENTEKHAB_VAHED

# -------------------

# -----------------
for browser in doros:
    def En_v3():
        browser = webdriver.Chrome(executable_path=r'chromedriver.exe')
        # browser.maximize_window()
        # browser.set_window_size(3000,2000)
        browser.set_window_position(0,0)
        sleep(1)


        ### LOGIN
        browser.get("http://edu1.iau-tnb.ac.ir")

        # UID = input("ID\n")
        browser.find_element_by_id("txtUserName").send_keys(UID)
        # PASS = input("ramz\n")
        browser.find_element_by_id("txtPassword").send_keys(PASS)
        browser.find_element_by_id("btn_ent_stu").click()
        ### LOGIN

        # pick = doros.pop()
        picked = []
        # picked_c = []
        ### ENTEKHAB_VAHED
        browser.refresh()
        browser.get("http://edu1.iau-tnb.ac.ir/SelectCourse.aspx")

        browser.find_element_by_id("ContentPlaceHolder1_txtCourseId").send_keys(doros)
        browser.find_element_by_id("ContentPlaceHolder1_lnkBtnSelectCourse").click()
        sleep(3)

        x = False
        x = browser.find_elements_by_xpath("//*[contains(text(), 'ثبت شد')]")
    

        for dars in doros:
            
            if x:
                print(dars + " akhz shod\n")
                picked.append(dars)

            while not x:
                browser.refresh()
                browser.find_element_by_id("ContentPlaceHolder1_txtCourseId").send_keys(dars)
                browser.find_element_by_id("ContentPlaceHolder1_lnkBtnSelectCourse").click()
                sleep(3)

                if x:
                    print(dars + " akhz shod\n")
                    picked.append(dars)
                    picked.append(doros.remove(dars))
                    break
                else:
                    browser.refresh()

            sleep(5)
        ### ENTEKHAB_VAHED

# -------------------

t1 = threading.Thread(target=En_v) 
t2 = threading.Thread(target=En_v2) 
t3 = threading.Thread(target=En_v3) 

if k==1:
    t1.start()

    t1.join() 
elif k==2:
    t1.start()
    t2.start()

    t1.join()
    t2.join() 
elif k==3:
    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join() 
    t3.join() 


# t1.start() 
# t2.start() 
# t3.start() 

# t1.join() 
# t2.join() 
# t3.join() 

print("dars haye zir baraye shoma bardashte shod:\n")
print(picked)
sleep(4)
print("My program took", time.time() - start_time, "to run")