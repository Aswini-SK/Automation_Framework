class CheckoutLocators:

    ACCEPT_TERMS_AD_SERVICES = "input[id='termsofservice']"

    CHECKOUT_BUTTON = "button[id='checkout']"
    EXISTING_BILLING_ADDRESS="div[id='checkout-step-billing']"
    EXISTING_CONTINUE_BUTTON="//input[@onclick='Billing.save()']"

    COUNTRY = "#BillingNewAddress_CountryId"

    CITY = "#BillingNewAddress_City"

    ADDRESS = "#BillingNewAddress_Address1"

    ZIP = "#BillingNewAddress_ZipPostalCode"

    PHONE = "#BillingNewAddress_PhoneNumber"

    CONTINUE = "input[value='Continue']"

    # CONFIRM_ORDER = "//input[@onclick='Billing.save()']"

    PICKUP="//input[@onclick='Shipping.togglePickUpInStore(this)']"

    SHIPPING="//input[@onclick='Shipping.save()']"
    PAYMENT_TYPE="//input[@onclick='PaymentMethod.save()']"
    PAYMENT_INFO="//input[@onclick='PaymentInfo.save()']"
    CONFIRM_ORDER="//input[@onclick='ConfirmOrder.save()']"
    CONTINUE_FURTHER=".order-completed-continue-button"