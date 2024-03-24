import socket
import json
import random
import time 
from datetime import datetime
import threading
import queue
import requests

concatenated_values_queue = queue.Queue()
concatenated_values_queue_4 = queue.Queue()

def slep():
    time.sleep(60)

def notify_server(data):
    server_url = 'http://localhost:6000/api/iot/data'  
     
    # print(jdata)
    # ddata = json.loads(jdata)
    # print(ddata)
    response = requests.get(server_url, params=data, timeout= 2)

def concat_values_thread():
    while True:
        try:
            # Get values ID the queue
            digit = concatenated_values_queue.get()
            letter = concatenated_values_queue.get()

            # Concatenate and print
            concatenated_value = str(digit) + letter
            current_timestamp = datetime.now().strftime('%Y-%m-%dT%H:%M:%S')
            data = {"ID": "concat_2_values",
                    "Time": f"{current_timestamp}",
                    "Data": f"{concatenated_value}"}
            notify_server(data)
        except Exception as e:
            pass

def concat_values_4_thread():
    while True:
        try:
            # Get values ID the queue
            digit = concatenated_values_queue_4.get()
            letter = concatenated_values_queue_4.get()

            # Concatenate and print
            concatenated_value = str(str(digit)[-2:] + letter[-2:])
            current_timestamp = datetime.now().strftime('%Y-%m-%dT%H:%M:%S')
            data = {"ID": "concat_4_values",
                    "Time": f"{current_timestamp}",               
                    "Data": f"{concatenated_value}"}
            notify_server(data)
        except Exception as e:
            pass

def generate_2_digit_number():
    number =  random.randint(10, 99)
    concatenated_values_queue.put(number)
    return number

def generate_3_digit_number():
    return random.randint(100, 999)

def generate_4_digit_number():
    number =  random.randint(1000, 9999)
    concatenated_values_queue_4.put(number)
    return number

def generate_2_letters():
    value =  ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=2))
    concatenated_values_queue.put(value)
    return value

def generate_4_letters():
    value =  ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=4))
    concatenated_values_queue_4.put(value)
    return value

def generate_2_digit_number_thread():
    while True:
        try:
            number = generate_2_digit_number()
            current_timestamp = datetime.now().strftime('%Y-%m-%dT%H:%M:%S')
            data = {"ID": "2_digit_number",
                    "Time": f"{current_timestamp}",
                    "Data": f"{number}"}
            notify_server(data)
        except Exception as e:
            pass # Adjust sleep time as needed
        slep()

def generate_3_digit_number_thread():
    while True:
        try:
            number = generate_3_digit_number()
            current_timestamp = datetime.now().strftime('%Y-%m-%dT%H:%M:%S')
            data = {"ID": "3_digit_number",
                    "Time": f"{current_timestamp}",
                    "Data": f"{number}"}
            notify_server(data)
        except Exception as e:
            pass # Adjust sleep time as needed
        slep()


def generate_4_digit_number_thread():
    while True:
        try:
            number = generate_4_digit_number()
            current_timestamp = datetime.now().strftime('%Y-%m-%dT%H:%M:%S')
            data = {"ID": "4_digit_number",
                    "Time": f"{current_timestamp}",
                    "Data": f"{number}"}
            notify_server(data)
        except Exception as e:
            pass # Adjust sleep time as needed
        slep()


def generate_2_letters_thread():
    while True:
        try:
            number = generate_2_letters()
            current_timestamp = datetime.now().strftime('%Y-%m-%dT%H:%M:%S')
            data = {"ID": "2_digit_letters",
                    "Time": f"{current_timestamp}",
                    "Data": f"{number}"}
            notify_server(data)

        except Exception as e:
            pass # Adjust sleep time as needed
        slep()


def generate_4_letters_thread():
    while True:
        try:
            number = generate_4_letters()
            current_timestamp = datetime.now().strftime('%Y-%m-%dT%H:%M:%S')
            data = {"ID": "4_digit_letters",
                    "Time": f"{current_timestamp}",
                    "Data": f"{number}"}
            notify_server(data)
        except Exception as e:
            pass # Adjust sleep time as needed
        slep()


if __name__ == "__main__":
    thread_2_digit = threading.Thread(target=generate_2_digit_number_thread)
    thread_3_digit = threading.Thread(target=generate_3_digit_number_thread)
    thread_4_digit = threading.Thread(target=generate_4_digit_number_thread)
    thread_2_letters = threading.Thread(target=generate_2_letters_thread)
    thread_4_letters = threading.Thread(target=generate_4_letters_thread)
    concat_thread = threading.Thread(target=concat_values_thread)
    concat_thread4 = threading.Thread(target=concat_values_4_thread)

    thread_2_digit.start()
    time.sleep(1)
    thread_3_digit.start()
    time.sleep(1)
    thread_4_digit.start()
    time.sleep(1)
    thread_2_letters.start()
    time.sleep(1)
    thread_4_letters.start()
    concat_thread.start()
    concat_thread4.start()
    

    thread_2_digit.join()
    thread_3_digit.join()
    thread_4_digit.join()
    thread_2_letters.join()
    thread_4_letters.join()
    concat_thread.join()
    concat_thread4.join()