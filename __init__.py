from mycroft import MycroftSkill, intent_file_handler


class IntentOpen(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('open.intent.intent')
    def handle_open_intent(self, message):
        self.speak_dialog('open.intent')


def create_skill():
    return IntentOpen()

