# Develop vmgabriel

"""Route for send email data"""

# Libraries
import os
from flask import Blueprint, jsonify, request

# Configuration orf Server
from config.server import configuration

# Email Sender
from utils.middlewares.email_sender import EmailSender


def get_blueprint(email_sender: EmailSender) -> Blueprint:
    """Define Get Blueprint"""
    mod = Blueprint('api/email', __name__);

    @mod.route('/alerts', methods=['POST'])
    def send_alert():
        """Route that send Alerts for email"""

        data = request.get_json(force=True)

        print(data)

        if not ('title_alert' in data):
            return jsonify({ 'error': 'title_alert not found.' }), 400
        if not ('measure_name' in data):
            return jsonify({ 'error': 'measure_name not found.' }), 400
        if not ('controller_name' in data):
            return jsonify({ 'error': 'controller_name not found.' }), 400
        if not ('description' in data):
            return jsonify({ 'error': 'description not found.' }), 400
        if not ('is_hot' in data):
            return jsonify({ 'error': 'is_hot not found.' }), 400

        email_sender.send_alert(
            title_alert=data['title_alert'],
            metric_name=data['measure_name'],
            controller_name=data['controller_name'],
            detail_alert=data['description'],
            title=data['title_alert'],
            is_hot=data['is_hot']
        )
        return jsonify({ 'message': 'Done Correctly.' }), 200

    @mod.route('/notifications', methods=['POST'])
    def send_notification():
        """Route that send Notifications for email"""

        data = request.get_json(force=True)

        if not ('title_alert' in data):
            return jsonify({ 'error': 'title_alert not found.' }), 400
        if not ('measure_name' in data):
            return jsonify({ 'error': 'measure_name not found.' }), 400
        if not ('controller_name' in data):
            return jsonify({ 'error': 'controller_name not found.' }), 400
        if not ('description' in data):
            return jsonify({ 'error': 'description not found.' }), 400

        email_sender.send_notification(
            title_alert=data['title_alert'],
            metric_name=data['measure_name'],
            controller_name=data['controller_name'],
            detail_alert=data['description'],
            title=data['title_alert'],
            is_hot=data['is_hot']
        )
        return jsonify({ 'message': 'Done Correctly.' }), 200

    return mod
