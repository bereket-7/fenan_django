from schemas.customer_info import CustomerInfo
from schemas.currency import Currency
from schemas.payment_intent import PaymentIntent
from schemas.payment_method_type import PaymentMethodType
from schemas.fenanpay_options import FenanpayOptions
from schemas.fenanpay_checkout_request import FenanpayCheckoutRequest
import fenanpay
import traceback

API_KEY = "98Orwr1bw1Uwk1zHl67nYF8AWmB2Od7cEwngJuJq/2eUNOyvwIVsEAzIPHd94ICIeqlnyZ0bREeEZm0OhMr69w=="
fenan_pay = fenanpay.Fenanpay(apikey=API_KEY)


def test_checkout_create():
    check_out = fenan_pay.checkout
    customer_info = CustomerInfo(
        name="Bereket",
        email="bereket7089@gmail.com",
        phone="0933457900")

    checkout_request = FenanpayCheckoutRequest(
        amount=4.0,
        currency=Currency.ETB,
        payment_intent_unique_id="w5g6c8x28q6608qa200mkgjkoxx0trxld5op00fcx9er8uj2adf",
        payment_type=PaymentMethodType.TELE_BIRR,
        return_url="https://gemini.google.com/app",
        expire_in=3600,
        callback_url="https://gemini.google.com/app",
        commission_paid_by_customer=True,
        customer_info=customer_info,
    )

    try:
        response = check_out.create(
            checkout_request, FenanpayOptions(sandbox=False))
        print("Checkout created successfully:", response)
    except Exception as e:
        print("Error during checkout creation:", e)
        traceback.print_exc()
    print("Running test_checkout_create...")


def test_direct_pay():

    try:
        direct_pay = fenan_pay.direct_pay
        payment_intent = PaymentIntent(
            amount=3.0,
            currency=Currency.ETB,
            payment_intent_unique_id="KiOdIGua4AdIlOooxx43gxR1qwe456y7890oDiuy6yhbvcds1",
            method_type=[PaymentMethodType.TELE_BIRR],
            return_url="https://gemini.google.com/app",
            expire_in=3600,
            callback_url="https://gemini.google.com/app",
            commission_paid_by_customer=True,
            customer_info=CustomerInfo(
                name="Bereket",
                email="bereket125@gmail.com",
                phone="0955516005"
            ),
        )

        response = direct_pay.pay(payment_intent)
        print("Direct Pay Response:", response)
    except Exception as e:
        print("Direct Pay Error:", e)


if __name__ == "__main__":
    print("\nTesting Checkout Create...")
    test_checkout_create()
    print("Testing Direct Pay...")
    test_direct_pay()
