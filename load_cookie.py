from http import cookies
import pickle
from scipy.__config__ import show
from selenium import webdriver
from time import sleep

browser  = webdriver.Chrome(executable_path="chromedriver.exe")

browser.get("https://www.facebook.com/")

# Load cookie from file
cookies = pickle.load(open("my_cookie.pkl","rb"))
for cookie in cookies:
    browser.add_cookie(cookie)

# Refresh lại trang Facebook
browser.get("https://www.facebook.com/truongnguoita.vn/posts/pfbid02xMDz6Y6UCp2vcNs4KSRxZ7pbUVbWVo64jDEoCXmj8cEEgAKdhzECizbsTTcaZdgrl?__cft__[0]=AZV262X_3Me7CvPm5P9ZOVRAtz-sQYYueFRw0vT3WIAVqYhWOnZTcguRN3agV_UxlTMdV5c9TYdPcKO1hMtnvOQ3PqizbdP9y9hA4RYype7_DLEdQFO-jlbw4ug7jOYp5EMBpVJsnF34sN_qbtJp_iGaUeFtecgiiAEUzkl-q8TyCZ5brGs7fCqW6A3ZyKJ_o7g&__tn__=%2CO%2CP-R")  
sleep(10)

# Dong trinh duyet
browser.close()