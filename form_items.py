"""Creates forms from list/dict of names"""

client_personal_information = {
    'Title': 'title',
    "Applicant's Name": 'name',
    "National ID Number": 'nin',
    "Passport Number": 'passport',
    "Marital Status": 'passport',  # single, married, widower, divorced
    "Date of Birth": 'passport',
    "Gender": 'gender',  # male, female
    "Nationality": 'nationality',
    "Number of dependants": 'no_of_dependants',
    "Post Address Box": 'po_box',
    "Code": 'post_code',
    "Postal Address": 'postal_address',
    "Postal Code": 'postal_code',
    "Phone": 'phone',
    "Spouse's name": 'spouse_name',
    "Residence": 'residence_id_no',
    "Estate": 'estate',
    "Town": 'town',
    "House No.": 'house_no',
    "Status": 'house_no',  # rented, owned
    "Length of stay": 'length_of_stay',
    "Name of Landlord": 'landlord_name',
    "Landlord Phone": 'landlord_phone',
}

business_particulars = {
    "Name of Entity": "name_of_entity",
    "Registration number": "reg_no",
    "Business Activity Type": "business_activity_type",
    "Liscence Number": "liscence_no",
    "Pin Number": "pin_no",
    "Value Added Tax (V.A.T)": "vat",
    "Type of Entity": "type_of_entity",
    "Business Email Address": "business_email",
    "Postal Status": "postal_status",  # current, permanent
    "Postal Address": "postal_address",
    "Telephone Number": "business_phone",
    "Physical Location": "physical_location",
    "Town": "town",
    "Street/Area": "street",
    "Building": "building",
    "Business Premises (status)": "premises_status",  # rented, owned
    "Lease Period": "lease_period",
    "Remaining Period": "remaining_period",
    "Rent Payable": "rent_payable",
}

exposure_particulars = {
    "Name": "name",
    "ID Number": "proprietors_id",
    "PIN Number": "proprietors_pin",
    "Telephone Number": "proprietors_phone",
    "Mobile Number": "proprietors_mobile",
    "Postal Address": "proprietors_postal_address",
}

exposure_particulars = {
    "Loan Amount Requested": "loan_requested",
    "Specific Purpose": "loan_requested",
    "Cost of Project": "cost_of_project",
    "Own Contribution": "own_contribution",
    "Repayment Period": "repayment_period",
    "Monthly Installments": "monthly_installments",
}

accounts_in_other_banks = {
    "Bank/Financial Institution": "institution",
    "Branch": "branch",
    "Balance (DR/CR)": "balance",
    "Amount Recorded": "amount_recorded",
}

other_ecogreen_loans = {
    "Branch Name": "eco_branch_name",
    "Amount Advanced": "eco_amount_advanced",
    "Data Advanced": "eco_data_advanced",
    "Loan Period": "eco_loan_period",
    "Installment": "eco_installment",
    "Balance (DR/CR)": "eco_balance",
    "Repayment Record": "eco_repayment_record",
}

other_banks_loans = {
    "Branch Name": "branch_name",
    "Amount Advanced": "amount_advanced",
    "Data Advanced": "data_advanced",
    "Loan Period": "loan_period",
    "Installment": "installment",
    "Balance (DR/CR)": "balance",
    "Repayment Record": "repayment_record",
}

refrees = {
    "Name": "refree_name",
    "Address": "refree_address",
    "Telephone": "refree_phone",
    "Relationship": "refree_relationship",
}

profit = {
    "Income": "profit_income",
    "Actual": "profit_actual",
    "Projected": "profit_projected",
}

expenses = {
    # Prchases, Rents, Salaries/Wages, Transport, Water/Phone/Electricity, Others
    "Expenses": "expense_income",
    "Actual": "expense_actual",
    "Projected": "expense_projected",
}

# balance_sheet
assets = {
    "Cash at hand/Bank": "cash_at_hand",  # hint: (Ecogreen or other Bank)
    "Debtors": "debtors",
    "Inventory": "Inventory",
    "Total Fixed Assets": "total_aixed_assets",
    "Other Assets": "other_assets",
}

liabilities = {
    "Creditors": "Creditors",
    "Bank Loans/Overdrafts": "bank_loans_overdrafts",
    "Other Liabilities": "other_liabilities",
    "Long Term Loans": "long_term_loans",
    "Capital": "capital",
}

# net_household_budget
mothly_income = {
    # e.g salary from other sources
    "Borrower's other income ": "borrowers_other_income",
    # e,g salary etc
    "Spouce income from other sources": "spouce_income",
    "Business income/profit": "business_income_profit",
    "Pension/ Farm proceeds": "pension_farm_proceeds",
    "Other Business Income": "other_business_income",
}

monthly_expenses = {
    "Rent": "rent",
    "School Fees": "school_fees",
    "Transport": "transport",
    "Water, phone, electricity": "water_phone_electricity",
    "Food": "food",
    "Other Loan Repayment": "other_loan_repayment",
}

proposed_guarantors = {
    "Name": "proposed_guarantors_name",
    "Address": "proposed_guarantors_address",
    "Telephone": "proposed_guarantors_phone",
    "Relationship": "proposed_guarantors_relationship",
}

security_collateral_details = {
    "Cash Collateral": "cash",
    "Address": "proposed_guarantors_address",
    "Telephone": "proposed_guarantors_phone",
    "Relationship": "proposed_guarantors_relationship",
}
