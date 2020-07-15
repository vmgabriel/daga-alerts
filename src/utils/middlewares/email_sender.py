#!/usr/bin/pýthon3
# Develop: vmgabriel

# Libraries
from typing import List
from flask import Flask, render_template
from flask_mail import Mail, Message

# Configuration of Server
from config.server import configuration as conf

class EmailSender:
    """Class that define method for send"""

    def __init__(self, app: Flask):
        app.config['MAIL_SERVER']   = conf['mail_sender']
        app.config['MAIL_PORT']     = conf['mail_port']
        app.config['MAIL_USERNAME'] = conf['mail_username']
        app.config['MAIL_PASSWORD'] = conf['mail_password']
        app.config['MAIL_USE_TLS']  = conf['mail_use_tls']
        app.config['MAIL_USE_SSL']  = conf['mail_use_ssl']

        self.url_cold = conf['url_image_cold']
        self.url_hot = conf['url_image_hot']
        self.url_notification = conf['header_notification']
        self.url_alert = conf['header_alert']
        self.list_notification = conf['notifications_emails_list']
        self.list_alert = conf['alert_emails_list']
        self.mail = Mail(app)

    def send_alert(
            self,
            title_alert: str,
            metric_name: str,
            controller_name: str,
            detail_alert: str,
            title: str,
            is_hot: bool = True
    ):
        """Send Alert Email"""
        name_template = 'alert.html'
        rendered = render_template(
            name_template,
            title_alert = title_alert,
            metric_name = metric_name,
            controller_name = controller_name,
            detail_alert = detail_alert,
            url_photo_icon = self.url_hot if is_hot else self.url_cold,
            url_header = self.url_alert
        )
        self.send_message(title, self.list_alert, rendered)

    def send_notification(
            self,
            title_alert: str,
            metric_name: str,
            controller_name: str,
            detail_alert: str,
            title: str,
            is_hot: bool = True
    ):
        """Send Notification Email"""
        name_template = 'alert.html'
        rendered = render_template(
            name_template,
            title_alert = title_alert,
            metric_name = metric_name,
            controller_name = controller_name,
            detail_alert = detail_alert,
            url_photo_icon = self.url_hot if is_hot else self.url_cold,
            url_header = self.url_notification
        )
        self.send_message(title, self.list_notification, rendered)

    def send_message(self, title: str, destiny: List[str], body: str):
        """With title, destiny and body HTML send email."""
        msg = Message(
            title,
            sender = conf['mail_username'],
            recipients = destiny
        )
        msg.html = body
        self.mail.send(msg)
