import requests
import hashlib
from datetime import datetime, timedelta, timezone


api_url = 'https://recruitment.fastprint.co.id/tes/api_tes_programmer'

def generate_password():
    current_date = datetime.now().strftime('%d-%m-%y')
    password = f'bisacoding-{current_date}'
    print(f"password: {password}")

    hashed_password = hashlib.md5(password.encode()).hexdigest()
    print(f"hashed_password: {hashed_password}")
    return hashed_password

def generate_username():
    # server_time = get_server_time(api_url)
    # print(f"server time: {server_time}")

    # current_time = server_time.strftime('%H%M%S')
    # current_time = (server_time.strftime('%H%M%S')+timedelta(seconds=1)).strftime('%H%M%S')
    now=datetime.now()
    current_time = (now).strftime('%d%m%y')
    next_hour=now+timedelta(hours=1)
    username = f'tesprogrammer{current_time}C{next_hour.strftime("%H")}'
    print(f"username: {username}")
    return username

def get_server_time(api_url):
    try:
        response = requests.head(api_url)  # Using a HEAD request to minimize data transfer
        if 'Date' in response.headers:
            server_time_str = response.headers['Date']
            server_time = datetime.strptime(server_time_str, '%a, %d %b %Y %H:%M:%S GMT')
            # Adding one second to the server time
            adjusted_server_time = server_time + timedelta(seconds=1)
            return adjusted_server_time
            # return server_time
        else:
            print('Server time not available in response headers.')
            return None
    except Exception as e:
        print(f'Error while getting server time: {e}')
        return None

def main():
    password = generate_password()
    username = generate_username()
    data = {
        'username': username,  # Sesuaikan dengan data yang diperlukan oleh API
        'password': password  # Sesuaikan dengan data yang diperlukan oleh API
    }

    try:
        print("=======================================")
        response = requests.post(api_url, data=data)

        if response.status_code == 200:
            print('Berhasil mengakses API dengan metode POST.')
            print('Response:', response.text)
        else:
            print(f'Gagal mengakses API. Status code: {response.status_code}')
            print('Response:', response.text)
            print('header:', response.headers)
    except Exception as e:
        print(f'Error: {e}')

if __name__ == '__main__':
    main()