from bs4 import BeautifulSoup
import requests

headers = {
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:104.0) Gecko/20100101 Firefox/104.0',
    'host': 'maktabkhooneh.org'
}

url = 'https://maktabkhooneh.org/'

session = requests.Session()
res = session.get(url, headers=headers)
res.raise_for_status()
print(headers)
url = 'https://maktabkhooneh.org/auth/check-active-user'
headers['origin'] = 'https://maktabkhooneh.org/'
headers['referer'] = 'https://maktabkhooneh.org/'
headers['X-Requested-With'] = 'XMLHttpRequest'
dom = BeautifulSoup(res.text, 'html.parser')
csrf = dom.select("input[name=csrfmiddlewaretoken]")
print(csrf)
if csrf:
    csrf = csrf[0].attrs['value']

    d = {
        'csrfmiddlewaretoken': csrf,
        'tessera': 'ariyan.eghbal@gmail.com'
    }

    res = session.post(url, headers=headers, data=d)
    res.raise_for_status()
    r = res.json()
    print(r['message'])
    if r['message'] == "get-pass":
        url = 'https://maktabkhooneh.org/auth/login-authentication'
        d = {
            'csrfmiddlewaretoken': csrf,
            'tessera': 'ariyan.eghbal@gmail.com',
            'hidden_username': 'ariyan.eghbal@gmail.com',
            'password': '1sM3dWLrcPdq'
        }
        headers['content-type'] = 'application/x-www-form-urlencoded; charset=UTF-8'
        res = session.post(url, headers=headers, data=d)
        res.raise_for_status()
        print(res.text)
        if 'logined' in res.text:
            print("Done!")
        else:
            print("Undone!")
    else:
        print("Error!")

else:
    print("Fail1!")