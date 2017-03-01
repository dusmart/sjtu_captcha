#!/usr/bin/python
# -*- coding:utf-8 -*-

# Author : Steven/Xinqi Zhu
# modified by dusmart
# Copyright © 2016 Steven Zhu

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import getpass
import urllib
import re
import time
import sys
import requests
from lib.predict import predict
from PIL import Image
from io import BytesIO

username = ""
password = ""

if(sys.version_info[0]==2):
    reload(sys) 
    sys.setdefaultencoding('utf8')
    

#----------------------必修课----------------------#
def Time1Election():
    temp = chrome.find_element_by_id("btnBxk")
    temp.click()
    #course_number = input("请输入课程代号（例如输入：CS001，若要重新开始选课请输入大写X）（请自行确保所选课程在本页显示）：")
    course_number = 'CS356'
    if course_number == 'X':
        return 1
    else:
        course_number = course_number.upper()
    temp = chrome.find_element_by_xpath("//input[@value='"+course_number+"']")
    temp.click()
    temp = chrome.find_element_by_id("SpeltyRequiredCourse1_lessonArrange")
    temp.click()
    content = chrome.page_source
    pattern = re.compile(r'<input type="radio" name="myradiogroup" value="(.*?)" /></span>\s*?</td><td style="border-width:1px;border-style:solid;">(.*?)</td><td style="border-width', re.S)
    iterms = re.findall(pattern, content)
    lsTeachers = {}
    for item in iterms:
        lsTeachers[item[1]] = item[0]
    print("\n")
    print(lsTeachers)
    print("\n")
    time.sleep(3)
    #teacher = input("请输入任课老师代号（如上表所示，不加引号，若要重新开始选课请输入大写X）：")
    teacher = '380439'
    if teacher == 'X':
        return 1
    else:
        while teacher not in lsTeachers.values():
            teacher = input("非法输入，请重新输入任课老师代号（如上表所示，不加引号）：")
    temp = chrome.find_element_by_xpath("//input[@value="+teacher+"]")
    temp.click()
    time.sleep(3)
    temp = chrome.find_element_by_id("LessonTime1_btnChoose")
    temp.click()
    time.sleep(3)
    print("已开始选课……")
    while "人数已满" in chrome.page_source or "请勿频繁" in chrome.page_source:
        temp = chrome.find_element_by_id("Button1")
        temp.click()
        time.sleep(3)
        temp = chrome.find_element_by_id("LessonTime1_btnChoose")
        temp.click()
        time.sleep(3)
        if "请勿频繁" in chrome.page_source:
            time.sleep(5)
            continue

    temp = chrome.find_element_by_id("SpeltyRequiredCourse1_Button1")
    temp.click()
    if "冲突" not in chrome.page_source:
        command = input("输入 Y 继续选课，输入其他字符退出此选课程序：")
        if (command != 'Y') and (command != 'y'):
            return 0
    else:
        command = input("你的选课有冲突，请确认后再运行此程序。")
        return 0
    return 1

#----------------------通识课----------------------#
def Time2Election():
    temp = chrome.find_element_by_id("btnTxk")
    temp.click()
    catalogue_list = {"1":"人文学科", "2":"社会科学", "3":"自然科学与工程技术", "4":"数学或逻辑学"}
    field_type = input("请输入所选学科类型（人文、社科、自科、数学 依次输入 1/2/3/4，若要重新开始选课请输入大写X）：")
    if field_type == 'X':
        return 1
    else:
        while field_type not in catalogue_list:
            field_type = input("非法输入，请重新输入所选学科类型：")
    temp = chrome.find_element_by_xpath("//tbody/tr[td='"+catalogue_list[field_type]+"']/child::*[1]")
    temp.click()
    course_number = input("请输入课程代号（例如输入：CS001，若要重新开始选课请输入大写X）（请自行确保所选课程在本页显示）：")
    if course_number == 'X':
        return 1
    else:
        course_number = course_number.upper()
    temp = chrome.find_element_by_xpath("//input[@value='"+course_number+"']")
    temp.click()
    temp = chrome.find_element_by_id("lessonArrange")
    temp.click()
    content = chrome.page_source
    pattern = re.compile(r'<input type="radio" name="myradiogroup" value="(.*?)" /></span>\s*?</td><td style="border-width:1px;border-style:solid;">(.*?)</td><td style="border-width', re.S)
    iterms = re.findall(pattern, content)
    lsTeachers = {}
    for item in iterms:
        lsTeachers[item[1]] = item[0]
    print("\n")
    print(lsTeachers)
    print("\n")
    teacher = input("请输入任课老师代号（如上表所示，不加引号，若要重新开始选课请输入大写X）：")
    if teacher == 'X':
        return 1
    else:
        while teacher not in lsTeachers.values():
            teacher = input("非法输入，请重新输入任课老师代号（如上表所示，不加引号）：")
    temp = chrome.find_element_by_xpath("//input[@value="+teacher+"]")
    temp.click()
    time.sleep(0.1)
    temp = chrome.find_element_by_id("LessonTime1_btnChoose")
    temp.click()
    time.sleep(0.1)
    print("已开始选课……")
    while "人数已满" in chrome.page_source:
        temp = chrome.find_element_by_id("Button1")
        temp.click()
        time.sleep(0.1)
        temp = chrome.find_element_by_id("LessonTime1_btnChoose")
        temp.click()
        time.sleep(0.1)

    temp = chrome.find_element_by_id("OutSpeltyEP1_btnSubmit")
    temp.click()
    if "冲突" not in chrome.page_source:
        command = input("输入 Y 继续选课，输入其他字符退出此选课程序：")
        if (command != 'Y') and (command != 'y'):
            return 0
    else:
        command = input("你的选课有冲突，请确认后再运行此程序。")
        return 0
    return 1

#----------------------任选课----------------------#
def Time3Election():
    print("请耐心等待……")
    temp = chrome.find_element_by_id("btnXuanXk")
    temp.click()

    lsColleges = {'船舶海洋与建筑工程学院':'01000'}
    grade_list = ['2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', 
            '2019', '2020', '2021']
    content = chrome.page_source
    pattern = re.compile(r'<option value="(.*?)">(.*?)</option>', re.S)
    items = re.findall(pattern, content)
    for item in items:
        if item[1] not in grade_list:
            lsColleges[item[1]] = item[0]
    for key, val in lsColleges.items():
        print(key+':'+val)
    college_number = input("请输入学院代号（如上表所示，若要重新开始选课请输入大写X）：")
    if college_number == 'X':
        return 1
    else:
        while college_number not in lsColleges.values():
            college_number = input("非法输入，请重新输入学院代号（如上表所示）：")
    select = Select(chrome.find_element_by_id("OutSpeltyEP1_dpYx"))
    select.select_by_value(college_number)
    grade = input("请输入所选课程的年级（如2014，若要重新开始选课请输入大写X）：")
    if grade == 'X':
        return 1
    else:
        while grade not in grade_list:
            grade = input("非法输入，请重新输入所选课程的年级（如2014）：")
    select = Select(chrome.find_element_by_id("OutSpeltyEP1_dpNj"))
    select.select_by_value(grade)
    temp = chrome.find_element_by_id("OutSpeltyEP1_btnQuery")
    temp.click()

    course_number = input("请输入课程代号（例如输入：CS001，若要重新开始选课请输入大写X）（请自行确保所选课程在本页显示）：")
    if course_number == 'X':
        return 1
    else:
        course_number = course_number.upper()
    temp = chrome.find_element_by_xpath("//input[@value='"+course_number+"']")
    temp.click()
    temp = chrome.find_element_by_id("OutSpeltyEP1_lessonArrange")
    temp.click()
    content = chrome.page_source
    pattern = re.compile(r'<input type="radio" name="myradiogroup" value="(.*?)" /></span>\s*?</td><td style="border-width:1px;border-style:solid;">(.*?)</td><td style="border-width', re.S)
    iterms = re.findall(pattern, content)
    lsTeachers = {}
    for item in iterms:
        lsTeachers[item[1]] = item[0]
    print("\n")
    print(lsTeachers)
    print("\n")
    teacher = input("请输入任课老师代号（如上表所示，不加引号，若要重新开始选课请输入大写X）：")
    if teacher == 'X':
        return 1
    else:
        while teacher not in lsTeachers.values():
            teacher = input("非法输入，请重新输入任课老师代号（如上表所示，不加引号）：")
    temp = chrome.find_element_by_xpath("//input[@value="+teacher+"]")
    temp.click()
    time.sleep(0.1)
    temp = chrome.find_element_by_id("LessonTime1_btnChoose")
    temp.click()
    time.sleep(0.1)
    print("已开始选课……")
    while "人数已满" in chrome.page_source:
        temp = chrome.find_element_by_id("Button1")
        temp.click()
        time.sleep(0.1)
        temp = chrome.find_element_by_id("LessonTime1_btnChoose")
        temp.click()
        time.sleep(0.1)

    temp = chrome.find_element_by_id("OutSpeltyEP1_btnSubmit")
    temp.click()
    if "冲突" not in chrome.page_source:
        command = input("输入 Y 继续选课，输入其他字符退出此选课程序：")
        if (command != 'Y') and (command != 'y'):
            return 0
    else:
        command = input("你的选课有冲突，请确认后再运行此程序。")
        return 0
    return 1


# START HERE
print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
print("**************************************************************************")
print("这是一个帮助你选课的小程序。")
print("请确保安装Chrome浏览器，否则选课失败。")
print("使用本程序招致的任何后果，作者不负任何责任。")
print("如果你想在任何时刻停止此程序，请使用Control+c键退出。")
print("任何时候请在程序内的终端操作而非浏览器页面，即使是验证码也请在终端输入。")
print("碰上任何问题，请退出重新运行试试。若弹出安全对话框，请选择允许访问。")
print("Made by Steven/Xinqi Zhu.")
print("Please head to http://zhuxinqi.space/project.html for more information.")
print("**************************************************************************")


chrome = webdriver.Chrome()
chrome.get("http://electsys.sjtu.edu.cn/edu/login.aspx")
s = requests.Session()
cookie = []
for item in chrome.get_cookies():
    cookie.append(item['name'] + '=' + item['value'])
c = ';'.join(cookie)
s.headers.update({'cookie':c})
img = s.get("https://jaccount.sjtu.edu.cn/jaccount/captcha?"+ str(int(round(time.time() * 1000))))
with open("./tmp.jpg", 'wb') as tmp_img:
        for chunk in img.iter_content(80):
            tmp_img.write(chunk)

usernamebox = chrome.find_element_by_id("user")
usernamebox.clear()
usernamebox.send_keys(username)

passwordbox = chrome.find_element_by_id("pass")
passwordbox.clear()
passwordbox.send_keys(password)

captchabox = chrome.find_element_by_id("captcha")
captcha = predict(Image.open(BytesIO(img.content)).convert("L"))
captchabox.clear
captchabox.send_keys(captcha)
print(captcha)



captchabox.send_keys(Keys.RETURN)

#electionNumber = input("这是第几轮选课（海选、抢选、第三轮 请分别输入 1/2/3）：")
electionNumber = '3'
while electionNumber not in ["1", "2", "3"]:
    electionNumber = input("非法输入，请重新输入（海选、抢选、第三轮 请分别输入 1/2/3）：")
electionUrl = "http://electsys.sjtu.edu.cn/edu/student/elect/warning.aspx?&xklc="+electionNumber+"&lb=1"
chrome.get(electionUrl)
temp = chrome.find_element_by_id("CheckBox1")
temp.click()
temp = chrome.find_element_by_id("btnContinue")
temp.click()
temp = chrome.find_element_by_id("SpeltyRequiredCourse1_btnQxsy")
temp.click()

flag_continue = 1
while flag_continue:
    electionUrl = "http://electsys.sjtu.edu.cn/edu/student/elect/warning.aspx?&xklc="+electionNumber+"&lb=1"
    chrome.get(electionUrl)
    temp = chrome.find_element_by_id("SpeltyRequiredCourse1_btnQxsy")
    temp.click()

    #course_type = input("课程类型（必修课、通识课、任选课 请分别输入 1/2/3）：")
    course_type = '1'
    while course_type not in ["1", "2", "3"]:
        course_type = input("非法输入，请重新输入（必修课、通识课、任选课 请分别输入 1/2/3）：")
    if course_type == "1":
        flag1 = Time1Election()
        if flag1:
            continue
        else:
            break
    elif course_type == "2":
        flag2 = Time2Election()
        if flag2:
            continue
        else:
            break
    else:
        flag3 = Time3Election()
        if flag3:
            continue
        else:
            break

chrome.close()
