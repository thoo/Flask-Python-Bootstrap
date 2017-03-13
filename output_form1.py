from flask_wtf import FlaskForm
from wtforms.validators import DataRequired
from wtforms import SelectField, SelectMultipleField, SubmitField
from wtforms_components import SelectMultipleField as SelectMultipleField1
import json

dict_label=json.load(open('dict_data/plot_dict.txt'))
tuple_label=zip(tuple(dict_label.keys()),tuple(dict_label.keys()))
state_label=json.load(open('dict_data/country_dict.txt'))
tuple_state_label=zip(tuple(state_label.keys()),tuple(state_label.keys()))
tuple_state_label=('List of States',(tuple_state_label))

label = [tuple_state_label]



plot_label = [('GDP per capita (current US$)','GDP per capita (current US$)'),
            ('GDP growth (annual %)','GDP growth (annual %)')]

class Select2MultipleField(SelectMultipleField1):

    def pre_validate(self, form):
        # Prevent "not a valid choice" error
        pass

    def process_formdata(self, valuelist):
        if valuelist:
            self.data=valuelist
            #self.data = ",".join(valuelist)
        else:
            self.data = ""




class DemoForm(FlaskForm):
    dropdown_label = label
    dropdown_plot_label = tuple_label
    multi_select_plot = Select2MultipleField(u"Development Indicators", [],
            choices=dropdown_plot_label,
            description=u" ",
            render_kw={"multiple": "multiple"})

    multi_select = Select2MultipleField(u"States", [],
            choices=dropdown_label,
            description=u" ",
            render_kw={"multiple": "multiple"})

    submit = SubmitField()


'''

label = [
        ('Group', (
            ('ASEAN', 'ASEAN'),
            ('APTA','Asia-Pacific Trade Agreement')
           # ('APEC','Asia-Pacific Economic Cooperation')
        )),

        ('ASEAN Member States', (
            ('Brunei Darussalam', 'Brunei Darussalam'),
            ('Cambodia', 'Cambodia'),
            ('Indonesia', 'Indonesia'),
            ('Lao PDR', 'Lao PDR'),
            ('Malaysia', 'Malaysia'),
            ('Myanmar', 'Myanmar'),
            ('Philippines', 'Philippines'),
            ('Singapore', 'Singapore'),
            ('Thailand', 'Thailand'),
            ('Vietnam', 'Vietnam')
        )),

        ('Asia-Pacific Trade Agreement States',(
            ('Bangladesh', 'Bangladesh'),
            ('China', 'China'),
            ('India', 'India'),
            ('Korea, Rep.', 'Korea, Rep.'),
            ('Lao PDR', 'Lao PDR'),
            ('Sri Lanka', 'Sri Lanka')
        )),

        ('Asia-Pacific Economic Cooperation States',(
            (u'Namibia', u'Namibia'),
            (u'Korea, Rep.', u'Korea, Rep.'),
            (u'Philippines', u'Philippines'),
            (u'Hong Kong SAR, China', u'Hong Kong SAR, China'),
            (u'United States', u'United States'),
            (u'Russian Federation', u'Russian Federation'),
            (u'China', u'China'),
            (u'Korea, Dem. Rep.', u' Korea, Dem. Rep.'),
            (u'Australia', u'Australia'),
            (u'Brunei Darussalam', u'Brunei Darussalam '),
            (u'Canada', u'Canada'),
            (u'Chile', u'Chile'),
            (u'Indonesia', u'Indonesia'),
            (u'Japan', u'Japan'),
            (u'Malaysia', u'Malaysia'),
            (u'Mexico', u'Mexico'),
            (u'New Zealand', u'New Zealand'),
            (u'Papua New Guinea', u'Papua New Guinea'),
            (u'Peru', u'Peru'),
            (u'Singapore', u'Singapore'),
            (u'Thailand', u'Thailand')
            )),

        tuple_state_label
        ]



        '''
