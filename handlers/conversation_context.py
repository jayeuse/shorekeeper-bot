
conversation_context = {}
conversation_context_limit = 16

def store_chat(server, channel, message, role):
    if server not in conversation_context:
        conversation_context[server] = {}

    if channel not in conversation_context[server]:
        conversation_context[server][channel] = []

    chat = conversation_context[server][channel]

    if len(chat) >= conversation_context_limit:
        chat.pop(0)

    chat.append({"role": role, "content": message})

def get_chat(server, channel):
    if server not in conversation_context:
        return []
    return conversation_context.get(server, {}).get(channel, [])
