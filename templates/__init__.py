class MessageData:
    def __init__(self, text, kb=None, parse_mode='HTML'):
        self.text = text
        self.reply_markup = kb
        self.parse_mode = parse_mode
