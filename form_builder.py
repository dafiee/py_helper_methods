"""Creates forms from list/dict of names"""

from form_items import *

# sample form field data


def create_input(label: str, input_name: str):
    """Function returns form-group div"""
    return f"""<div class="col-sm-6">
        <div class="form-group">
            <label for="{input_name}-id">{label}</label>
            <input type="text" class="form-control @error('{input_name}') is-invalid @enderror"
                id="{input_name}-id" placeholder="Enter ..." name="{input_name}" value="{{ old('{input_name}') }}">
            @error('{input_name}')
                <span class="error invalid-feedback">
                {{ $message }}
                </span>
            @enderror
        </div>
    </div>"""


def create_select_input(label: str, input_name: str, options: list):
    """Function returns form-group div"""
    return f"""<div class="col-sm-6">
        <div class="form-group">
            <label for="{input_name}-id">{label}</label>
            <input type="text" class="form-control @error('{input_name}') is-invalid @enderror"
                id="{input_name}-id" placeholder="Enter ..." name="{input_name}" value="{{ old('{input_name}') }}">
            @error('{input_name}')
                <span class="error invalid-feedback">
                {{ $message }}
                </span>
            @enderror
        </div>
    </div>"""


def create_form(elements: str):
    '''Funtion to enclose form with information'''
    return f"""<form method="POST" action="">@csrf{elements}</form>"""


def generate_html_string():
    '''Generates HTML string'''
    html_string = ""

    for key, value in client_personal_information.items():
        my_string = create_input(key, value).replace('{', "{{")
        my_string = my_string.replace('}', "}}")

        html_string += my_string

    html_string = create_form(html_string)

    with open('client_personal_information.html', 'w', encoding='utf-8') as form_html:
        form_html.write(html_string)


generate_html_string()
