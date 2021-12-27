from kivy.lang import Builder
from kivy.properties import StringProperty
from kivymd.app import MDApp
from kivymd.uix.list import IRightBodyTouch, OneLineAvatarIconListItem



KV = '''
<Name>:

    IconLeftWidget:
        icon: root.icon


BoxLayout:

    ScrollView:

        MDList:
            id: scroll
'''


class Name(OneLineAvatarIconListItem):
    '''Custom list item.'''

    icon = StringProperty(None)


class MainApp(MDApp):
    def build(self):
        return Builder.load_string(KV)

    def on_start(self):
        icons = "train_details.png"
        for i in range(30):
            self.root.ids.scroll.add_widget(
                Name(text=str(i), icon=icons)
            )


MainApp().run()