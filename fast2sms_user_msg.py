import requests

r=requests.get('https://www.fast2sms.com/dev/bulk?authorization=PGmSojzFqKwhN45ti0D1dpBUuAnr3xRMb7CQagce6f2XYJsZWVXU1SZuCABYlaoNE7x46sczHPgpGb0O&sender_id=FSTSMS&message=This%20is%20test%20message&language=english&route=p&numbers=9789744893')

print(r.status_code) 
