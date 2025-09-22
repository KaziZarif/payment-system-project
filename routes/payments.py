import os 
import stripe 
from flask import Blueprint, redirect, render_template

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
                    "product_data": {"name": "Stanley Cup"},
                    "unit_amount": 1500, 
                }, 
                "quantity": 1
            }],
            mode="payment",
            success_url="http://localhost:5000/payments/success",
            cancel_url="http://localhost:5000/payments/cancel",
        )
        return redirect(session.url, code=303)
    except Exception as e:
        return {"error": str(e)}, 400
    
@payments_bp.route("/success")
def success():
    return "<h1>Payment successful ✅</h1><p>Thank you for your order!</p>"

@payments_bp.route("/cancel")
def cancel():
    return "<h1>Payment canceled ❌</h1><p>You can try again whenever you’re ready.</p>"
