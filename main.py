from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.properties import StringProperty
from kivy.uix.widget import Widget
from kivy.core.window import Window
import re

# importing EIA-96 codes from EIA96.py:
from EIA96 import index, multipler


Window.clearcolor = (.1, .1, .1, .24)


class CalcGridLayout(GridLayout):
    upper_text_list = ['[color=FFFFFF]Enter Resistor Code:[/color]',
                       '[color=C52626]Wrong Resistor Code![/color]']
    upper_text = StringProperty(upper_text_list[0])
    label_entry_text = StringProperty('')
    summary = StringProperty('')
    button_color = '#AFADFF'

    def callback(self, text):
        if len(self.label_entry_text) < 4:
            self.label_entry_text += text
            self.upper_text = self.upper_text_list[0]

    def entry_clear(self):
        self.label_entry_text = ''
        self.summary = ''
        self.upper_text = self.upper_text_list[0]

    def entry_del(self):
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
        match r_type:
            case '3digits':
                value = r_code[0] + r_code[1]
                power = r_code[2]
                resistance = int(value)*(10**int(power))
                return resistance
            case '4digits':
                value = r_code[0] + r_code[1] + r_code[2]
                power = r_code[3]
                resistance = int(value)*(10**int(power))
                return resistance
            case 'EIA-96':
                value = index[r_code[0] + r_code[1]]
                power = str(r_code[2])
                resistance = int(value)*multipler[power]
                return resistance
            case 'R+digits':
                value = r_code.replace('R', '.')
                resistance = f"0{str(value)}"
                return float(resistance)
            case 'digitsRdigits':
                value = r_code.replace('R', '.')
                return float(value)
            case 'zero':
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
        Window.size = (500, 816)
        return CalcGridLayout()

ResistorCalcApp().run()
