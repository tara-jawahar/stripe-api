# Set your secret key. Remember to switch to your live secret key in production.
# See your keys here: https://dashboard.stripe.com/apikeys
import stripe
stripe.api_key = "sk_test_4eC39HqLyjWDarjtT1zdp7dc"

stripe.Price.create(
  currency="usd",
  unit_amount=120000,
  product_data={"name": "stand up paddleboard"},
)