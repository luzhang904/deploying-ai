conversation_history = []


def add_memory(user, assistant):

    conversation_history.append(
        {
            "role":"user",
            "content":user
        }
    )

    conversation_history.append(
        {
            "role":"assistant",
            "content":assistant
        }
    )


def get_memory():

    return conversation_history