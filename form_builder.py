"""Creates forms from list/dict of names"""

from form_items import *
from form_model import Form, Field, FieldType

# sample form field data
staff = {
    'First Appoinment Date': 'first_appointment_date',
    'Appointment Duration': 'appointment_duration',
}

form = Form("bio_data", fields=[
    Field('Surname', 'surname', ['required']),
    Field('Other name(s)', 'other_names', ['required']),
    Field('Nationality', 'nationality', ['required']),
    Field('Gender', 'gender', ['required', 'boolean']),
    Field('Languages Spoken', 'languages_spoken', ['required']),
    Field('Marital Status', 'marital_status', ['required']),
    Field('Religion', 'religion', ['required']),
    Field('Date of Birth', 'dob', ['required', 'date']),
    Field('Place of Birth', 'place_of_birth', ['required']),
    Field('Sub County', 'sub_county', ['required']),
    Field('County', 'county', ['required']),
    Field('District', 'district', ['required']),
    Field('Village/LC1', 'village', ['required']),
    Field('Town', 'town', ['required']),
    Field('Telephone', 'telephone', ['required']),
    Field('Email', 'email', ['required', 'email']),
    Field('Profile Picture', 'profile_picture', ['required']),
    # father details
    Field('Father\'s Name', 'father_name', ['required']),
    Field('Address', 'father_address', ['required']),
    Field('Phone Number', 'father_phone', ['required']),
    # mother details
    Field('Mother\'s Name', 'mother_name', ['required']),
    Field('Address', 'mother_address', ['required']),
    Field('Phone Number', 'mother_phone', ['required']),
    # next of kin details
    Field('Next of Kin\'s Name', 'next_of_kin_name', ['required']),
    Field('Place of Origin', 'place_of_origin', ['required']),
    Field('Address', 'next_of_kin_address', ['required']),
    Field('Relationship', 'next_of_kin_relationship', ['required']),
    # spouse
    Field('Name of Spouse', 'spouse_name', ['required']),
    Field('Place of Birth', 'spouse_place_of_birth', ['required']),
    Field('Number of Children', 'no_of_children', ['required', 'number']),
    # children
    Field('Name of Child', 'name_of_child[]', ['required']),
    Field('Gender', 'child_gender[]', ['required']),
    Field('Date of Birth', 'child_dob', ['required', 'date']),
    # bank details
    Field('NSSF Number', 'nssf', ['required', 'number']),
    Field('Account Number', 'acc_no', ['required']),
    Field('Bank', 'bank_name', ['required']),
    Field('Tin Number', 'tin_no', ['required', 'number']),
    Field('Driver License', 'driver_license', ['required']),
    Field('Passport Number/NIN', 'nin', ['required']),
    Field('Job Title / Designation', 'job_title', ['required']),
    Field('Monthly Salary', 'salary', ['required', 'number']),
    Field('Date of First Appointment', 'first_appointment_date', ['required']),
    Field('Date of Present Appointment',
          'present_appointment_date', ['required']),
    Field('Department/Section', 'department', ['required']),
    Field('Duty Station', 'duty_station', ['required']),
    Field('Membership to: Societies, Clubs and other Organizations',
          'memberships', ['required']),

])


form.create_html_file()
form.create_validator_file()
