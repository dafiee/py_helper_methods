"""Creates forms from list/dict of names"""

# sample form field data
formFields = {
    'Name': 'name',
    'Email Address': 'email',
    'Phone Number': 'phone',
    'Password': 'password',
    'Confirm Password': 'password_confirmation',
}


def create_input(label: str, input_name: str):
    """Function returns form-group div"""
    return f"""<div class="form-group">
        <label for="">{label}</label>
        <input type="text" class="form-control" name="{input_name}" placeholder="Enter ..." />
    </div>"""


def create_form(elements: str):
    '''Funtion to enclose form with information'''
    return f"""<form method="POST" action="">{elements}</form>"""


def generate_html_string():
    '''Generates HTML string'''
    html_string = ""

    for key, value in formFields.items():
        html_string += create_input(key, value)

    html_string = create_form(html_string)

    with open('form1.html', 'w', encoding='utf-8') as form_html:
        form_html.write(html_string)


generate_html_string()
