from stripe import StripeClient
from config.settings import STRIPE_SECRET_KEY
from django.urls import reverse

client = StripeClient(STRIPE_SECRET_KEY)

def create_stripe_product(payment):
    if payment.course:
        product = client.v1.products.create({"name": payment.course.name})
        return product
    elif payment.lesson:
        product = client.v1.products.create({"name": payment.lesson.name})
        return product
    raise ValueError("Не выбран урок или курс для оплаты")

def create_stripe_price(payment, product):
    if payment.course:
        price = client.v1.prices.create({
          "currency": "rub",
          "unit_amount": payment.course.price * 100,
          "product": product.id,
        })
        return price
    elif payment.lesson:
        price = client.v1.prices.create({
          "currency": "rub",
          "unit_amount": payment.lesson.price * 100,
          "product": product.id,
        })
        return price
    return None

def create_stripe_session(price):
    session = client.v1.checkout.sessions.create({
        "success_url": f"http://127.0.0.1:8000/{reverse('users:payment_success')}",
        "line_items": [{"price": price.id, "quantity": 1}],
        "mode": "payment",
    })
    return session.id, session.url
