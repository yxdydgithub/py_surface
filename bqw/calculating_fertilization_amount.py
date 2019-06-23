# -*- coding: utf-8 -*-
# Author @yangxiaodong
# Description @ calculating_fertilization_amount.py
# CreatTime @ 2019-06-16 20:56:54

import wx
from math import sqrt
import bqw


# 计算施肥量
class CalcFrame(bqw.MyFrame1):
    def __init__(self, parent):
        bqw.MyFrame1.__init__(self, parent)

    def FertilizerCalculation(self, event):
        self.m_textCtrl2.Clear()
        self.m_textCtrl3.Clear()
        fertilizationAmount = float(self.m_textCtrl1.GetValue())

        params = [{'a': -0.0381, 'b': 109.82, 'volume': 110.2, 'vol_name': '体积1'},
                  {'a': -0.0534, 'b': 92.552, 'volume': 91.5, 'vol_name': '体积2'},
                  {'a': -0.0855, 'b': 74.595, 'volume': 72.8, 'vol_name': '体积3'},
                  {'a': -0.0276, 'b': 48.577, 'volume': 49.2, 'vol_name': '体积4'},
                  {'a': -0.0833, 'b': 36.584, 'volume': 32.1, 'vol_name': '体积5'},
                  {'a': -0.0171, 'b': 14.305, 'volume': 14.8, 'vol_name': '体积6'}]
        paramsLen = len(params)
        for i in range(paramsLen):
            a = params[i]['a']
            b = params[i]['b']
            volume = params[i]['volume']
            vol_name = params[i]['vol_name']
            nu = 5/3.6
            condition_1 = fertilizationAmount/volume
            condition_2 = b*b-(-20*a*fertilizationAmount*nu)
            condition_3 = (-b+sqrt(condition_2))/(2*a)
            if condition_1 > 3 and condition_2 > 0 and 0 < condition_3 <= 120:
                self.m_textCtrl2.AppendText(vol_name + '\n')
            else:
                self.m_textCtrl3.AppendText(vol_name + '\n')


app = wx.App()
frame = CalcFrame(None)
frame.Show(True)
app.MainLoop()
