from schemas.customer_info import CustomerInfo
from schemas.currency import Currency
from schemas.payment_intent import PaymentIntent
from schemas.payment_method_type import PaymentMethodType
import fenanpay

API_KEY = "98Orwr1bw1Uwk1zHl67nYF8AWmB2Od7cEwngJuJq/2eUNOyvwIVsEAzIPHd94ICIeqlnyZ0bREeEZm0OhMr69w=="
fenan_pay = fenanpay.Fenanpay(apikey=API_KEY)


def test_express_pay():

    try:
        express_pay = fenan_pay.express_pay
        payment_intent = PaymentIntent(
            amount=3.0,
            currency=Currency.ETB,
            payment_intent_unique_id="KiOdIGua4AdIlOooxx43gxR1qwe456y7890oDiuy6yhbvcds1",
            method_type=[PaymentMethodType.TELE_BIRR],
            return_url="https://returnurl",
            expire_in=3600,
            callback_url="https://callbacllurl",
            commission_paid_by_customer=True,
            customer_info=CustomerInfo(
                name="Bereket",
                email="bereket125@gmail.com",
                phone="0955516005"
            ),
        )

        response = express_pay.pay(payment_intent)
        print("Express Pay Response:", response)
    except Exception as e:
        print("Express Pay Error:", e)


if __name__ == "__main__":
    print("Testing Exppress Pay...")
    test_express_pay()
