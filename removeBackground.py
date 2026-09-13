import requests

response = requests.post(
    'https://api.remove.bg/v1.0/removebg',
    # تم وضع اسم الصورة الحقيقي هنا في المدخلات
    files={'image_file': open('صور-جميلة-رائعة.jpg', 'rb')},
    data={'size': 'auto'},
    headers={'X-Api-Key': '8A4rvKMNWvCvkeqhWcj3XXXX'},
)

if response.status_code == requests.codes.ok:
    # تم تصحيح طريقة كتابة دالة الحفظ وموضع وضع الكتابة الثنائي ('wb')
    with open('no-bg.png', 'wb') as out:
        out.write(response.content)
    print("تمت إزالة الخلفية بنجاح وحفظ الصورة باسم no-bg.png!")
else:
    print("Error:", response.status_code, response.text)