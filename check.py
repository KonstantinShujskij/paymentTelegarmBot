from data import config


def is_admin(user_id):
    if user_id not in config.admins_id:
        raise Exception('You not has access!')


def is_moderator(user_id):
    if user_id not in config.moderators_id:
        is_admin(user_id)


def is_private(message):
    user_id = message.from_user.id
    chat_id = message.chat.id

    if not chat_id == user_id:
        raise Exception('Can`t complete in group!')