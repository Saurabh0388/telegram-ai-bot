import os
from openai import OpenAI
from context import get_context, set_context, clear_context
from products import products
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=OPENROUTER_API_KEY
)

def save_lead(data):
    with open("leads.txt", "a") as f:
        f.write(data + "\n")

def get_ai_reply(message, user_id):
    msg = message.lower()
    ctx = get_context(user_id)

    if ctx == "price":
        clear_context(user_id)
        for p in products:
            if p in msg:
                return f"💰 {p.title()} price is {products[p]['price']}"
        return "Product not found."

    if ctx == "stock":
        clear_context(user_id)
        for p in products:
            if p in msg:
                return f"📦 {p.title()} stock status: {products[p]['stock']}"
        return "Product not found."

    if ctx == "order":
        for p in products:
            if p in msg:
                set_context(user_id, f"order_{p}")
                return "Please share your Name and Phone number."
        return "Product not found."

    if ctx and ctx.startswith("order_"):
        product = ctx.replace("order_", "")
        clear_context(user_id)
        save_lead(f"Order | {product} | {message}")
        return "✅ Order received. Our team will contact you."

    if "price" in msg:
        set_context(user_id, "price")
        return "Please tell the product name."

    if "stock" in msg:
        set_context(user_id, "stock")
        return "Please tell the product name."

    if "order" in msg:
        set_context(user_id, "order")
        return "Which product would you like to order?"

    ai_response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": message}],
        temperature=0.7
    )

    return ai_response.choices[0].message.content
