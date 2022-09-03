# !/usr/anaconda3/bin python
# -*-coding:utf-8-*-
"""
@Project        :   project_manage
@FileName       :   utils.py
@Author         :   tangchaolizi
@Datetime       :   2020-06-16 13:04
@Software       :   PyCharm
@Show           :   邮件发送
"""

from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from email.mime.text import MIMEText
from email.header import Header


class Email(object):
    def __init__(self, send_email):
        self.settings = settings
        self.send_to = ['{}'.format(send_email)]  # 接受邮箱
        self.send_emailer = '「{}」<{}>'.format(self.settings.WEB_NAME, self.settings.DEFAULT_FROM_EMAIL)

    def send_new_question(self, name, username, questionId, url):
        mail_msg = """
        <p>尊敬的用户<strong>「{0}」</strong></p>
        <p>你有一个新问题</p>
        <p>{2}</p>
        <p><a href='http://{3}/question_manage/views_question/?questionId={1}' target='_blank' rel="noopener">
        http://{3}/question_manage/views_question/?questionId={1}</a></p>
        <p>若无法点击请复制以上链接到浏览器访问。</p>
        """.format(username, questionId, name, url)
        subject = '新问题提示'
        msg = EmailMultiAlternatives(subject, mail_msg, self.send_emailer, self.send_to)
        msg.attach_alternative(mail_msg, "text/html")
        msg.send()


    def send_question_over(self, name, username, questionId, successinfo, url):
        mail_msg = """
        <p>尊敬的用户<strong>「{0}」</strong></p>
        <p>你有一个问题已完成</p>
        <p>{2}</p>
        <p><a href='http://{4}/question_manage/views_question/?questionId={1}' target='_blank' rel="noopener">
        http://{4}/question_manage/views_question/?questionId={1}</a></p>
        <p>完成信息:{3}</p>
        <p>若无法点击请复制以上链接到浏览器访问。</p>
        """.format(username, questionId, name, successinfo, url)
        subject = '问题完成提示'
        msg = EmailMultiAlternatives(subject, mail_msg, self.send_emailer, self.send_to)
        msg.attach_alternative(mail_msg, "text/html")
        msg.send()


if __name__ == '__main__':
    pass
