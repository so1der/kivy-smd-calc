from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.properties import StringProperty
from kivy.core.window import Window
from kivy.lang.builder import Builder
import re

index = {"01": 100, "02": 102, "03": 105, "04": 107, "05": 110, "06": 113,
         "07": 115, "08": 118, "09": 121, "10": 124, "11": 127, "12": 130,
         "13": 133, "14": 137, "15": 140, "16": 143, "17": 147, "18": 150,
         "19": 154, "20": 158, "21": 162, "22": 165, "23": 169, "24": 174,
         "25": 178, "26": 182, "27": 187, "28": 191, "29": 169, "30": 200,
         "31": 205, "32": 210, "33": 215, "34": 221, "35": 226, "36": 232,
         "37": 237, "38": 243, "39": 249, "40": 255, "41": 261, "42": 267,
         "43": 274, "44": 280, "45": 287, "46": 294, "47": 301, "48": 309,
         "49": 316, "50": 324, "51": 332, "52": 340, "53": 348, "54": 357,
         "55": 365, "56": 374, "57": 383, "58": 392, "59": 402, "60": 412,
         "61": 422, "62": 432, "63": 442, "64": 453, "65": 464, "66": 475,
         "67": 487, "68": 499, "69": 511, "70": 523, "71": 536, "72": 549,
         "73": 562, "74": 576, "75": 590, "76": 604, "77": 619, "78": 634,
         "79": 649, "80": 665, "81": 681, "82": 698, "83": 715, "84": 732,
         "85": 750, "86": 768, "87": 787, "88": 806, "89": 825, "90": 845,
         "91": 866, "92": 887, "93": 909, "94": 931, "95": 953, "96": 976,
         "97": 0, "98": 0, "99": 0}

multipler = {"Z": 0.001, "Y": 0.01, "R": 0.01, "X": 0.1, "S": 0.1, "A": 1,
             "B": 10, "H": 10, "C": 100, "С": 100, "D": 1000, "E": 10000,
             "F": 100000}

Window.clearcolor = (.1, .1, .1, .24)

KV = """
<CalcGridLayout>:

    rows: 9
    padding: 10
    spacing: 10

    FloatLayout:
        id: top
        Label:
            font_size: 45
            text: root.upper_text
            markup: True
            pos: top.pos
        Image:
            id: resistor_image
            pos: this_one.pos
            source: 'resistor.png'
            size: this_one.texture_size


    BoxLayout:
        orientation: 'vertical'
        Label:
            id: this_one
            font_size: 45
            text: root.label_entry_text


    BoxLayout:
        Label:
            font_size: 35
            text: root.summary

    BoxLayout:
        Widget:

    BoxLayout:
        spacing: 10
        orientation: 'horizontal'

        Button:
            text: "Calculate"
            font_size: 35
            background_color: root.button_color
            size_hint: .6, 1
            on_press: root.calculate()
        Button:
            text: "Clear"
            font_size: 35
            background_color: root.button_color
            size_hint: .2, 1
            on_press: root.entryClear()
        Button:
            text: "Del"
            font_size: 35
            background_color: root.button_color
            size_hint: .2, 1
            on_press: root.entryDel()

    BoxLayout:
        spacing: 10
        Button:
            text: "7"
            background_color: root.button_color
            on_press: root.callback('7')
            font_size: 35
        Button:
            text: "8"
            background_color: root.button_color
            on_press: root.callback('8')
            font_size: 35
        Button:
            text: "9"
            background_color: root.button_color
            on_press: root.callback('9')
            font_size: 35
        Button:
            text: "D"
            background_color: root.button_color
            on_press: root.callback('D')
            font_size: 35
        Button:
            text: "E"
            background_color: root.button_color
            on_press: root.callback('E')
            font_size: 35
        Button:
            text: "F"
            background_color: root.button_color
            on_press: root.callback('F')
            font_size: 35

    BoxLayout:
        spacing: 10
        Button:
            text: "4"
            background_color: root.button_color
            on_press: root.callback('4')
            font_size: 35
        Button:
            text: "5"
            background_color: root.button_color
            on_press: root.callback('5')
            font_size: 35
        Button:
            text: "6"
            background_color: root.button_color
            on_press: root.callback('6')
            font_size: 35
        Button:
            text: "H"
            background_color: root.button_color
            on_press: root.callback('H')
            font_size: 35
        Button:
            text: "B"
            background_color: root.button_color
            on_press: root.callback('B')
            font_size: 35
        Button:
            text: "C"
            background_color: root.button_color
            on_press: root.callback('C')
            font_size: 35

    BoxLayout:
        spacing: 10
        Button:
            text: "1"
            background_color: root.button_color
            on_press: root.callback('1')
            font_size: 35

        Button:
            text: "2"
            background_color: root.button_color
            on_press: root.callback('2')
            font_size: 35

        Button:
            text: "3"
            background_color: root.button_color
            on_press: root.callback('3')
            font_size: 35
        Button:
            text: "X"
            background_color: root.button_color
            on_press: root.callback('X')
            font_size: 35
        Button:
            text: "S"
            background_color: root.button_color
            on_press: root.callback('S')
            font_size: 35
        Button:
            text: "A"
            background_color: root.button_color
            on_press: root.callback('A')
            font_size: 35

    BoxLayout:
        spacing: 10
        Widget:

        Button:
            text: "0"
            background_color: root.button_color
            on_press: root.callback('0')
            font_size: 35
        Widget:

        Button:
            text: "Z"
            background_color: root.button_color
            on_press: root.callback('Z')
            font_size: 35
        Button:
            text: "Y"
            background_color: root.button_color
            on_press: root.callback('Y')
            font_size: 35
        Button:
            text: "R"
            background_color: root.button_color
            on_press: root.callback('R')
            font_size: 35
"""


class CalcGridLayout(GridLayout):
    upper_text_list = ['[color=FFFFFF]Enter Resistor Code:[/color]',
                       '[color=C52626]Wrong Resistor Code![/color]']
    upper_text = StringProperty(upper_text_list[0])
    label_entry_text = StringProperty('')
    summary = StringProperty('')
    button_color = '#AFADFF'
    Builder.load_string(KV)

    def callback(self, text):
        if len(self.label_entry_text) < 4:
            self.label_entry_text += text
            self.upper_text = self.upper_text_list[0]

    def entryClear(self):
        self.label_entry_text = ''
        self.summary = ''
        self.upper_text = self.upper_text_list[0]

    def entryDel(self):
        self.label_entry_text = self.label_entry_text[:-1]
        self.upper_text = self.upper_text_list[0]
        self.summary = ''

    def calculate(self):
        r_code = self.label_entry_text
        r_type = self.resistorCodeTypeCheker(r_code)
        if r_type is None:
            self.upper_text = self.upper_text_list[1]
            self.summary = ''
            return
        resistance = self.resistanceСalculate(r_type, r_code)

        if resistance == 0 and r_type == 'EIA-96':
            self.upper_text = self.upper_text_list[1]
            self.summary = ''
            return
        resistance_value = self.unitAbbreviationsHandler(round(resistance, 3))
        self.summary = f"Resistance: {resistance_value}"

    def resistorCodeTypeCheker(self, r_code):
        patterns = ['^\d{4}$', '^\d{3}$', '^[R]+\d{1,3}$',
                    '^\d{,2}[R]\d{1,3}$', '^\d{2}[A-F H R-S X-Z]$', '^[0]$']

        types = ['4digits', '3digits', 'R+digits',
                 'digitsRdigits', 'EIA-96', 'zero']

        for index, pattern in enumerate(patterns):
            if re.match(pattern, r_code):
                return types[index]

    def resistanceСalculate(self, r_type, r_code):
        if r_type == '3digits':
            value = r_code[0] + r_code[1]
            power = r_code[2]
            resistance = int(value)*(10**int(power))
            return resistance
        elif r_type == '4digits':
            value = r_code[0] + r_code[1] + r_code[2]
            power = r_code[3]
            resistance = int(value)*(10**int(power))
            return resistance
        elif r_type == 'EIA-96':
            value = index[r_code[0] + r_code[1]]
            power = str(r_code[2])
            resistance = int(value)*multipler[power]
            return resistance
        elif r_type == 'R+digits':
            value = r_code.replace('R', '.')
            resistance = f"0{str(value)}"
            return float(resistance)
        elif r_type == 'digitsRdigits':
            value = r_code.replace('R', '.')
            return float(value)
        elif r_type == 'zero':
            return 0

    def unitAbbreviationsHandler(self, value):
        if value < 1000:
            answer = f"{str(value)} Ω"
            return(answer)
        value = value/1000
        answer = f"{str(value)} kΩ"
        if value >= 1000:
            value = value/1000
            answer = f"{str(value)} MΩ"
        return(answer)


class ResistorCalcApp(App):
    def build(self):
        return CalcGridLayout()

ResistorCalcApp().run()
