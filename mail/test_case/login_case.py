#!/usr/bin/python3
# -*- coding:utf-8 -*-
from time import sleep
import unittest,random,sys
from mail.test_case.model import myunit,function
from mail.test_case.page_object.login_page import LoginPage
from mail.test_case.page_object.mail_page import MailPage
sys.path.append('./model')
sys.path.append('./page_object')

class LoginTest(myunit.MyTest):

    def test_login_user_pwd_null(self):
        '''用户名、密码为空登录'''
        po = LoginPage(self.driver)
        po.open()
        po.login_action('','')
        sleep(2)
        self.assertEqual(po.login_error_hint(),'请输入帐号')
        function.insert_img(self.driver,'user_pwd_null.png')

    def test_login_pwd_null(self):
        '''密码为空登录'''
        po = LoginPage(self.driver)
        po.open()
        po.login_action('abc','')
        sleep(2)
        self.assertEqual(po.login_error_hint(),'请输入密码')
        function.insert_img(self.driver,'pwd_null.png')

    def test_login_user_pwd_error(self):
         '''用户名或密码错误'''
         po = LoginPage(self.driver)
         po.open()
         character = random.choice('zyxwvutsrqponmlkjihgfedcba')
         username = "test" + character
         po.login_action(username,"$#%#")
         sleep(2)
         #print(po.login_error_hint())
         self.assertEqual(po.login_error_hint(),'帐号或密码错误')
         function.insert_img(self.driver, "user_pwd_error.png")

    def test_login_success(self):
        '''用户名、密码正确,登录成功'''
        po = LoginPage(self.driver)
        po.open()
        user = "zb194236"
        po.login_action(user,"zhb194236")
        sleep(2)
        po2 = MailPage(self.driver)
        #print(po2.login_success_user())
        self.assertEqual(po2.login_success_user(),user+"@163.com")
        function.insert_img(self.driver, "success.png")
