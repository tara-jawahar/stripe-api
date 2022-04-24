# Set your secret key. Remember to switch to your live secret key in production.
# See your keys here: https://dashboard.stripe.com/apikeys
import stripe
import os
stripe.api_key = os.environ['STRIPE_API_KEY_TEST']

stripe.Customer.create(description="My First Test Customer")

stripe.PaymentIntent.create(
  customer='{{CUSTOMER_ID}}',
  currency="usd",
  amount=2000,
  payment_method_types=["card"],
  setup_future_usage="on_session",
)
