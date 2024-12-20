from schemas.customer_info import CustomerInfo
from schemas.currency import Currency
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


if __name__ == "__main__":
    print("\nTesting Checkout Create...")
    test_checkout_create()
