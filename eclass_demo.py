import os
from tkinter import E
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

option = webdriver.ChromeOptions()
option.add_argument('headless')
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=option)
driver.get('http://eclass.inha.ac.kr/login.php')
os.system('clear')

try:
    username = driver.find_element(by=By.NAME, value='username')
    input_username = input('Enter your username: ')
    username.send_keys(input_username)
    password = driver.find_element(by=By.NAME, value='password')
    input_password = input('Enter your password: ')
    password.send_keys(input_password)
    login = driver.find_element(by=By.NAME, value='loginbutton').click()
    course_titles = driver.find_elements(by=By.CLASS_NAME, value='course-title')
except Exception:
    raise Exception

for index, course_title in enumerate(course_titles, start=1):
    print('-'*50)
    course_name = course_title.find_element(by=By.TAG_NAME, value='h3').text
    name = course_name.split('[')[0]
    print('\n',index, name, '\n')

def get_course_name():
        assignment_link = driver.find_element(by=By.LINK_TEXT, value='Assignment')
        assignment_link.click()
        deadlines = driver.find_elements(by=By.CLASS_NAME, value='c0')
        assignments = driver.find_elements(by=By.CLASS_NAME, value='c1')
        no_submissions = driver.find_elements(by=By.CLASS_NAME, value='c3')
        for date, assignment, homework in zip(deadlines, no_submissions, assignments):
            print('\n', date.text, '               | ', homework.text,'          | ', assignment.text, '\n')

input_course = input('Enter the course number: ')
os.system('clear')
if input_course == '1':
    course_title = course_titles[0].click()
    get_course_name()
elif input_course == '2':
    course_title = course_titles[1].click()
    get_course_name()
elif input_course == '3':
    course_title = course_titles[2].click()
    get_course_name()
elif input_course == '4':
    course_title = course_titles[3].click()
    get_course_name()
elif input_course == '5':
    course_title = course_titles[4].click()
    get_course_name()

driver.quit()
 
