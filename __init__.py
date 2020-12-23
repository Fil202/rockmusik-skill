from mycroft import MycroftSkill, intent_file_handler


class Rockmusik(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('rockmusik.intent')
    def handle_rockmusik(self, message):
        self.speak_dialog('rockmusik')


def create_skill():
    return Rockmusik()

