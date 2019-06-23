# -*- coding: utf-8 -*-
# Author @yangxiaodong
# Description @ kivy_surface.py
# CreatTime @ 2019-06-23 16:42:56

from kivy.app import App

from kivy.uix.scatter import Scatter
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout


class ScatterTextWidget(BoxLayout):
    pass

class SJApp(App):

    def build(self):
        return ScatterTextWidget()

if __name__ == '__main__':
        SJApp().run()
