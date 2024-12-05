from schemas.product_type import ProductType
from schemas.payment_item import PaymentItem
from schemas.customer_info import CustomerInfo
from schemas.currency import Currency
from schemas.payment_intent import PaymentIntent
from schemas.payment_method_type import PaymentMethodType
from schemas.fenanpay_options import FenanpayOptions
from schemas.fenanpay_checkout_request import FenanpayCheckoutRequest
from core.fenanpay_direct_pay import FenanpayDirectPay
from core.direct_pay import DirectPay
from core import fenanpay_checkout
import fenanpay
import os
import sys
import django
import traceback

# Add the project directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Initialize Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fenan_django.settings')
django.setup()

API_KEY = "davlUdgCd/zZkQ/LaoFw9DtUPCEwn+LC3v931oIyiAdm39qxpt7FYb4eruIbi6UXmUkDQ69FFMUjMZq1or4LLQ=="

# Initialize Fenanpay
fenanpay = fenanpay.Fenanpay(apikey=API_KEY)

# Initialize Checkout and Direct Pay
checkout = fenanpay_checkout.FenanpayCheckout(fenanpay.http_client)
direct_pay = FenanpayDirectPay(fenanpay.http_client)


def test_checkout_create():
    print("Running test_checkout_create...")

    payment_items = [
        PaymentItem(
            name="Item 1",
            description="This is a description for Item 1",
            image="https://example.com/image1.png",
            quantity=1,
            type=ProductType.PRODUCT,
            price=10.0
        ),
        PaymentItem(
            name="Item 2",
            description="This is a description for Item 2",
            image="https://example.com/image2.png",
            quantity=2,
            type=ProductType.PRODUCT,
            price=5.0
        ),
    ]

    customer_info = CustomerInfo(
        name="Bereket",
        email="bereket@gmail.com",
        phone="0934160075"
    )

    # Prepare FenanpayCheckoutRequest
    checkout_request = FenanpayCheckoutRequest(
        amount=100.0,
        items=payment_items,
        currency=Currency.ETB,
        payment_intent_unique_id="wZq23dOfMiAuLqM9STF3utnwa",
        payment_type=PaymentMethodType.TELE_BIRR,
        payment_link_unique_id=None,
        split_payment=None,
        return_url="https://gemini.google.com/app",
        expire_in=3600,
        callback_url="https://gemini.google.com/app",
        commission_paid_by_customer=True,
        customer_info=customer_info,
    )

    try:
        response = checkout.create(
            checkout_request, FenanpayOptions(sandbox=True))
        print("Checkout created successfully:", response)
    except Exception as e:
        print("Error during checkout creation:", e)
        traceback.print_exc()
    print("Running test_checkout_create...")


def test_direct_pay():
    print("Running test_direct_pay...")

    payment_intent = PaymentIntent(
        amount=150.0,
        items=[
            {"name": "Item 1", "description": "Sample Item 1",
                "quantity": 1, "price": 50.0, "type": "PRODUCT"},
            {"name": "Item 2", "description": "Sample Item 2",
                "quantity": 2, "price": 25.0, "type": "PRODUCT"},
        ],
        currency=Currency.ETB,
        payment_intent_unique_id="KiOpO07U4MdOdIGua4AdIlOoogxR",
        payment_link_unique_id=None,
        method_type=[PaymentMethodType.CBE],
        split_payment=[],
        return_url="https://gemini.google.com/app",
        expire_in=3600,
        callback_url="https://gemini.google.com/app",
        commission_paid_by_customer=False,
        customer_info=CustomerInfo(
            name="Bereket",
            email="bereket@gmail.com",
            phone="0934160075"
        ),
    )

    try:
        cbe_payment = DirectPay(fenanpay.http_client, PaymentMethodType.CBE)
        response = cbe_payment.pay(payment_intent)
        print("Direct payment successful (CBE):", response)
    except Exception as e:
        print("Error during direct payment (CBE):", e)
        traceback.print_exc()

    try:
        telebirr_payment = DirectPay(
            fenanpay.http_client, PaymentMethodType.TELE_BIRR)
        response = telebirr_payment.pay(payment_intent)
        print("Direct payment successful (TeleBirr):", response)
    except Exception as e:
        print("Error during direct payment (TeleBirr):", e)
        traceback.print_exc()


if __name__ == "__main__":
    test_checkout_create()
    test_direct_pay()
