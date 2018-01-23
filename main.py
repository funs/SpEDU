# -*-coding=UTF-8-*-

import kivy
kivy.require('1.10.0')

from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.app import App
from kivy.properties import ObjectProperty, StringProperty


class SpeduWidget(FloatLayout):

    pass


class SpeduApp(App):

    def build(self):
        return SpeduWidget()


if __name__ == '__main__':
    SpeduApp().run()
