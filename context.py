user_context = {}

def set_context(user_id, value):
    user_context[user_id] = value

def get_context(user_id):
    return user_context.get(user_id)

def clear_context(user_id):
    user_context.pop(user_id, None)
