# src/stripe_client.py
import stripe
from .config import STRIPE_SECRET_KEY

stripe.api_key = STRIPE_SECRET_KEY

def create_charge(amount, currency="usd", source="tok_visa"):
    # Create a Stripe charge
    return stripe.Charge.create(
        amount=amount,
        currency=currency,
        source=source,
        description="Purchase credits"
    )
