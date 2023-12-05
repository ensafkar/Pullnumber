import requests

def get_orders(page, per_page=100):
    url = "https://senindomainadresinburayagelecek/wp-json/wc/v3/orders"
    params = {
        "consumer_key": "YENI_CONSUMER_KEY",
        "consumer_secret": "YENI_CONSUMER_SECRET",
        "per_page": per_page,
        "page": page
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Hata: {response.status_code}, Mesaj: {response.text}")
        return None

# Sayfalama için döngü
page = 1
while True:
    orders = get_orders(page)
    if not orders:
        break  # Veri kalmadığında döngüyü kır

    for order in orders:
        customer_id = order.get('customer_id', None)
        first_name = order['billing'].get('first_name', 'İsim yok')
        last_name = order['billing'].get('last_name', 'Soyisim yok')
        phone = order['billing'].get('phone', 'Telefon numarası yok')
        print(f"Müşteri ID: {customer_id}, İsim: {first_name} {last_name}, Telefon: {phone}")

    page += 1  # Sonraki sayfaya geç
