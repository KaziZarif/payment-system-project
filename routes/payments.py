import os 
import stripe 
from flask import Blueprint, redirect

payments_bp = Blueprint("payments", __name__)

stripe.api_key = os.getenv("STRIPE_SECRET_KEY")

@payments_bp.route("/create-checkout-session")
def create_checkout_session():
    try:
        session = stripe.checkout.Session.create(
            payment_method_types=["card"],
            line_items=[{
                "price_data": {
                    "currency": "aud",
                    "product_data": {"name": "Cup"},
                    "unit_amount": 1500, 
                }, 
                "quantity": 1
            }],
            mode="payment",
            success_url="http://localhost:5000/success",
            failure_url="http://localhost:5000/cancel",
        )
        return redirect(session.url, code=303)
    except Exception as e:
        return {"error": str(e)}, 400
