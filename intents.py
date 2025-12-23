from products import products

def detect_intent(message):
    msg = message.lower()
    if any(w in msg for w in ["hi", "hello", "hey"]):
        return "greeting"
    if any(p in msg for p in products):
        if "price" in msg:
            return "price"
        if "stock" in msg or "available" in msg:
            return "stock"
        if any(w in msg for w in ["buy", "order", "purchase"]):
            return "order"
        return "product_only"

    if "price" in msg:
        return "price"
    if "stock" in msg or "available" in msg:
        return "stock"
    if any(w in msg for w in ["buy", "order"]):
        return "order"

    if any(w in msg for w in ["thanks", "thank you"]):
        return "thanks"

    return "info"
