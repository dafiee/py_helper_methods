from enum import Enum


class FieldType(Enum):
    INPUT = 1
    SELECT = 0


# class Validator():
#     def __init__(self, field: str, validator: list) -> None:
#         self.field = field
#         self.validator = validator

#     def get_validator(self):
#         '''Generates field validators'''
#         seperator = "|"
#         return f'"{self.field}" => "{seperator.join(self.validator)}"'


class Field():
    def __init__(self, label: str, input_name: str, validator: list[str] = list, field_type: FieldType = FieldType.INPUT, options: list[str] = list):
        self.label = label
        self.input_name = input_name
        self.validator = validator
        self.seperator = "|"
        self.field_type = field_type
        self.options = options

    # def __str__(self) -> str:
    #     return self.create_field()

    def create_input(self):
        """Function returns form-group div"""
        return f"""<div class="col-sm-6">
            <div class="form-group">
                <label for="{self.input_name}-id">{self.label}</label>
                <input type="text" class="form-control @error('{self.input_name}') is-invalid @enderror"
                    id="{self.input_name}-id" placeholder="Enter ..." name="{self.input_name}" value="{{ old('{self.input_name}') }}">
                @error('{self.input_name}')
                    <span class="error invalid-feedback">
                    {{ $message }}
                    </span>
                @enderror
            </div>
        </div>"""

    def create_select_input(self):
        """Function returns form-group div"""
        return f"""<div class="col-sm-6">
            <div class="form-group">
                <label for="{self.input_name}-id">{self.label}</label>
                <input type="text" class="form-control @error('{self.input_name}') is-invalid @enderror"
                    id="{self.input_name}-id" placeholder="Enter ..." name="{self.input_name}" value="{{ old('{self.input_name}') }}">
                @error('{self.input_name}')
                    <span class="error invalid-feedback">
                    {{ $message }}
                    </span>
                @enderror
            </div>
        </div>"""

    def create_validators(self):
        '''Funtion to create validators for form inputs'''
        return f'"{self.input_name}"=>"{self.seperator.join(self.validator)}"'

    def create_field(self):
        '''Funtion to create field for form input elements'''
        if self.field_type == FieldType.INPUT:
            return self.create_input()
        return self.create_select_input()


class Form():
    def __init__(self, name: str, fields: list[Field]):
        self.name = name
        self.fields = fields

    def create_form(self, elements: str):
        '''Funtion to enclose form with information'''
        return f"""<form method="POST" action="">@csrf{elements}</form>"""

    def generate_html_string(self) -> str:
        '''Generates HTML string'''
        html_string = ""

        for field in self.fields:
            html_string += field.create_field()

        html_string = html_string.replace("{", '{{')
        html_string = html_string.replace("}", "}}")

        return self.create_form(html_string)

    def generate_validators(self) -> str:
        '''Generates validator string'''
        validator_string = ""

        for field in self.fields:
            validator_string += field.create_validators() + ",\n"

        return validator_string

    def create_html_file(self):
        '''Funtion to create html file'''
        with open(f'{self.name}.html', 'w', encoding='utf-8') as form_html:
            form_html.write(self.generate_html_string())

    def create_validator_file(self):
        '''Funtion to create validators for laravel'''
        with open(f'{self.name}.php', 'w', encoding='utf-8') as form_validators:
            form_validators.write(self.generate_validators())
