#!/usr/bin/python3

# Develop Vmgabriel

"""Define the Configuration base of all service, this get data"""

# Libraries
import os
from pathlib import Path
from dotenv import load_dotenv
load_dotenv()


def mbToBytes(byte_data: int) -> int:
    """Convert byte number data and this convert to mb"""
    return byte_data * 1048576

def get_public_path() -> str:
    """Get Public Path"""
    return str(Path(__file__).resolve().parent.parent.parent)

print('Public Path - {}'.format(get_public_path()))

configuration = {
    'host': '0.0.0.0',
    'port': 7204,

    'debug': True,

    'files_path_upload': get_public_path() + '/public/',
    'files_path_images_upload': get_public_path() + '/public/images/',
    'max_length_files': mbToBytes(5),

    'cookie_secret': os.getenv('COOKIE_SECRET'),
    'cookie_name': os.getenv('COOKIE_NAME'),

    'jwt_location': ['cookies'],
    'jwt_secret': os.getenv('JWT_SECRET'),

    'verify_ip': False,  # True | False
    'mail_sender': os.getenv('MAIL_SERVER'),
    'mail_port': 465,
    'mail_use_tls': False,
    'mail_use_ssl': True,
    'mail_username': os.getenv('MAIL_USERNAME'),
    'mail_password': os.getenv('MAIL_PASSWORD'),

    'header_notification': 'https://gitlab.com/vmgabriel/img-public/-/raw/master/rdp/logo-image.jpg',
    'header_alert': 'https://gitlab.com/vmgabriel/img-public/-/raw/master/rdp/broke.jpg',
    'url_image_cold': 'https://gitlab.com/vmgabriel/img-public/-/raw/master/rdp/cold.jpg',
    'url_image_hot': 'https://gitlab.com/vmgabriel/img-public/-/raw/master/rdp/hot.jpg',

    'alert_emails_list': ['timdx.2ei@gmail.com', 'vmgabriel96@gmail.com'],
    'notifications_emails_list': ['timdx.2ei@gmail.com', 'vmgabriel96@gmail.com']
}
