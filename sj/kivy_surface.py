# -*- coding: utf-8 -*-
# Author @yangxiaodong
# Description @ kivy_surface.py
# CreatTime @ 2019-06-23 16:42:56

import kivy

from kivy.app import App
from kivy.uix.label import Label


class SJApp(App):

    def build(self):
        return Label(text='Hello world')

if __name__ == '__main__':
        SJApp().run()
