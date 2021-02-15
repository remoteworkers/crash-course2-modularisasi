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
    print(f'Success! {response}')
    print(f'content {response.text}')

except Exception as e:
    print(f'There is an error {e}')