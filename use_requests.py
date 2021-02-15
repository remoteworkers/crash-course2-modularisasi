import requests

requests.get('https://detik.com')

print('ATAU')
url = 'https://detik.com'
requests.get(url)

print('ATAU')
url = 'https://detik.com'
try:
    requests.get(url)
    print('Success!')

except Exception as e:
    print('There is an error', e)

print('Program Ended!')

print('ATAU')
url = 'https://detik.com'
try:
    response = requests.get(url)
    if response.status_code == 200 :
        print(f'Success! Response = {response.status_code}')
        print(f'content {response.text}')
    else :
        print(f'ups, ada kesalahan request {response.status_code}')
except Exception as e:
    print(f'There is an error {e}')