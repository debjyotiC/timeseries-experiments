import requests as r

data_url = ("https://consentiuminc.online/api/board/getdata/recent?receivekey=d46549f155ec2f887066c0ace65b86f2&boardkey"
            "=b0953b10042e1094")

data = r.get(data_url).json()['sensors']

print(data)
