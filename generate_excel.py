import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side

wb = openpyxl.Workbook()

# Setup sheets
ws_summary = wb.active
ws_summary.title = 'Test Summary & Overview'
ws_testcases = wb.create_sheet(title='Manual Test Cases')
ws_defects = wb.create_sheet(title='Defect Log (Bugs)')

# Fonts & Fills
font_title = Font(name='Segoe UI', size=16, bold=True, color='1B365D')
font_subtitle = Font(name='Segoe UI', size=11, italic=True, color='4A607A')
font_section = Font(name='Segoe UI', size=12, bold=True, color='1B365D')
font_header = Font(name='Segoe UI', size=10, bold=True, color='FFFFFF')
font_data = Font(name='Segoe UI', size=9.5)
font_bold = Font(name='Segoe UI', size=9.5, bold=True)
font_pass = Font(name='Segoe UI', size=9.5, bold=True, color='006100')
font_fail = Font(name='Segoe UI', size=9.5, bold=True, color='9C0006')

fill_header = PatternFill(start_color='1F4E79', end_color='1F4E79', fill_type='solid')
fill_sub_header = PatternFill(start_color='2C5E8A', end_color='2C5E8A', fill_type='solid')
fill_alt = PatternFill(start_color='F4F7FA', end_color='F4F7FA', fill_type='solid')
fill_pass = PatternFill(start_color='C6EFCE', end_color='C6EFCE', fill_type='solid')
fill_fail = PatternFill(start_color='FFC7CE', end_color='FFC7CE', fill_type='solid')
fill_card = PatternFill(start_color='E9F1F7', end_color='E9F1F7', fill_type='solid')

thin_border_side = Side(border_style='thin', color='D9D9D9')
border_cell = Border(left=thin_border_side, right=thin_border_side, top=thin_border_side, bottom=thin_border_side)
border_header = Border(left=thin_border_side, right=thin_border_side, top=thin_border_side, bottom=Side(border_style='medium', color='1F4E79'))

# -------------------------------------------------------------
# SHEET 1: Test Summary & Overview
# -------------------------------------------------------------
ws_summary.views.sheetView[0].showGridLines = True
ws_summary['B2'] = 'THE OPEN UNIVERSITY OF SRI LANKA (OUSL)'
ws_summary['B2'].font = Font(name='Segoe UI', size=14, bold=True, color='1B365D')
ws_summary['B3'] = 'Activity: Learning Manual Testing — Simple Calculator Project'
ws_summary['B3'].font = Font(name='Segoe UI', size=12, bold=True, color='2C5E8A')
ws_summary['B4'] = 'Comprehensive Test Execution Summary, Defect Analysis & Version Upgrading'
ws_summary['B4'].font = font_subtitle

# Project Info Table
info_data = [
    ('Project Name', 'Simple Calculator Application'),
    ('Programming Language', 'Python 3.11'),
    ('Interface Type', 'CLI (Command Line Interface) with Menu-driven Operations'),
    ('GitHub Repository URL', 'https://github.com/numair-it/simple-calculator'),
    ('Author / Student GitHub', 'numair-it (numairking4712@gmail.com)'),
    ('Initial Version Tested', 'v1.0.0 (Baseline release with intentional defects)'),
    ('Upgraded Version', 'v2.0.0 (Refactored with defect fixes and robust validation)'),
    ('Testing Methodology', 'Black-Box Manual Testing (BVA, Equivalence Partitioning, Error Guessing)'),
    ('Testing Completion Date', 'September 2026'),
    ('Activity Due Date', '28.09.2026')
]

ws_summary['B6'] = 'Project & Environment Details'
ws_summary['B6'].font = font_section

row_idx = 7
for label, val in info_data:
    ws_summary.cell(row=row_idx, column=2, value=label).font = font_bold
    ws_summary.cell(row=row_idx, column=2).fill = fill_card
    ws_summary.cell(row=row_idx, column=2).border = border_cell
    
    val_cell = ws_summary.cell(row=row_idx, column=3, value=val)
    val_cell.font = font_data
    val_cell.border = border_cell
    if label == 'GitHub Repository URL':
        val_cell.hyperlink = val
        val_cell.font = Font(name='Segoe UI', size=9.5, bold=True, color='0563C1', underline='single')
    row_idx += 1

# Metrics Comparison Table
row_idx += 2
ws_summary.cell(row=row_idx, column=2, value='Test Execution Metrics (v1.0.0 vs v2.0.0)').font = font_section

row_idx += 1
headers_metric = ['Metric Name', 'Version 1.0.0 (Initial)', 'Version 2.0.0 (Upgraded)', 'Improvement / Status']
for c_idx, h in enumerate(headers_metric, start=2):
    c = ws_summary.cell(row=row_idx, column=c_idx, value=h)
    c.font = font_header
    c.fill = fill_header
    c.alignment = Alignment(horizontal='center', vertical='center')
    c.border = border_header

metrics = [
    ('Total Test Cases Executed', '20', '20', '100% Executed'),
    ('Total Passed', '15', '20', '+5 Test Cases (+25%)'),
    ('Total Failed', '5', '0', '-5 Defects Resolved'),
    ('Test Pass Percentage', '75.0%', '100.0%', '+25.0% Overall Quality'),
    ('Defects / Bugs Detected', '5', '0 Open', '100% Bugs Fixed & Closed'),
    ('System Stability & Exception Handling', 'Poor (5 unhandled crashes)', 'Excellent (Zero crashes)', 'All exceptions handled safely')
]

for row_data in metrics:
    row_idx += 1
    for c_idx, val in enumerate(row_data, start=2):
        c = ws_summary.cell(row=row_idx, column=c_idx, value=val)
        c.font = font_data
        c.border = border_cell
        if c_idx in (3, 4, 5):
            c.alignment = Alignment(horizontal='center', vertical='center')
        if val == '75.0%':
            c.fill = fill_fail
            c.font = font_fail
        elif val == '100.0%':
            c.fill = fill_pass
            c.font = font_pass

# Key Defects Summary in Overview
row_idx += 2
ws_summary.cell(row=row_idx, column=2, value='Summary of Defects Detected and Resolved').font = font_section

row_idx += 1
defect_headers = ['Defect ID', 'Severity', 'Defect Summary', 'Root Cause (v1.0.0)', 'Resolution in v2.0.0']
for c_idx, h in enumerate(defect_headers, start=2):
    c = ws_summary.cell(row=row_idx, column=c_idx, value=h)
    c.font = font_header
    c.fill = fill_header
    c.alignment = Alignment(horizontal='center', vertical='center')
    c.border = border_header

defect_briefs = [
    ('BUG-001', 'Critical', 'Division by Zero causes application crash', 'No denominator check before division (ZeroDivisionError)', 'Added denominator validation; returns clear warning message'),
    ('BUG-002', 'High', 'Modulus by Zero causes unhandled crash', 'No zero check in modulus operation (ZeroDivisionError)', 'Added zero check; returns descriptive error message'),
    ('BUG-003', 'High', 'Negative number square root causes crash', 'math.sqrt() called on negative number (ValueError)', 'Added input check for num < 0 before calling square root'),
    ('BUG-004', 'Medium', 'Alphabetic/String input causes immediate crash', 'Direct float(input()) conversion without try-except', 'Implemented get_valid_number() with loop & try-except block'),
    ('BUG-005', 'Medium', 'Empty/Blank Enter causes crash', 'float(\'\') raises unhandled ValueError', 'Added empty input check & re-prompting user')
]

for d in defect_briefs:
    row_idx += 1
    for c_idx, val in enumerate(d, start=2):
        c = ws_summary.cell(row=row_idx, column=c_idx, value=val)
        c.font = font_data
        c.border = border_cell
        if c_idx in (2, 3):
            c.alignment = Alignment(horizontal='center', vertical='center')

ws_summary.column_dimensions['A'].width = 4
ws_summary.column_dimensions['B'].width = 32
ws_summary.column_dimensions['C'].width = 42
ws_summary.column_dimensions['D'].width = 45
ws_summary.column_dimensions['E'].width = 45

# -------------------------------------------------------------
# SHEET 2: Manual Test Cases (Full Table)
# -------------------------------------------------------------
ws_testcases.views.sheetView[0].showGridLines = True
ws_testcases['A1'] = 'SIMPLE CALCULATOR - MANUAL TEST CASES & EXECUTION RESULTS'
ws_testcases['A1'].font = font_title
ws_testcases['A2'] = 'Course: Learning Manual Testing (OUSL) | GitHub: https://github.com/numair-it/simple-calculator'
ws_testcases['A2'].font = font_subtitle

tc_headers = [
    'Test Case ID',
    'Module / Feature',
    'Test Scenario / Description',
    'Pre-Conditions',
    'Test Steps',
    'Test Data (Inputs)',
    'Expected Result',
    'Actual Result (v1.0.0)',
    'Status (v1.0.0)',
    'Defect ID',
    'Bug Description & Root Cause',
    'Fix Implementation in v2.0.0',
    'Actual Result (v2.0.0)',
    'Status (v2.0.0)'
]

for col_idx, h in enumerate(tc_headers, start=1):
    c = ws_testcases.cell(row=4, column=col_idx, value=h)
    c.font = font_header
    c.fill = fill_header
    c.alignment = Alignment(horizontal='center', vertical='center', wrap_text=True)
    c.border = border_header
ws_testcases.row_dimensions[4].height = 32

test_cases_data = [
    (
        'TC_CALC_001', 'Addition', 'Addition of two positive integers',
        'Calculator is running and menu displayed',
        '1. Select option 1 (Addition)\n2. Enter first number\n3. Enter second number\n4. Observe result',
        'num1 = 15\nnum2 = 25',
        'Displays: Result: 15.0 + 25.0 = 40.0',
        'Displayed: Result: 15.0 + 25.0 = 40.0',
        'PASS', 'None', 'N/A', 'N/A',
        'Displayed: Result: 15.0 + 25.0 = 40.0',
        'PASS'
    ),
    (
        'TC_CALC_002', 'Addition', 'Addition of positive and negative number',
        'Calculator is running and menu displayed',
        '1. Select option 1 (Addition)\n2. Enter negative number\n3. Enter positive number\n4. Observe result',
        'num1 = -10\nnum2 = 30',
        'Displays: Result: -10.0 + 30.0 = 20.0',
        'Displayed: Result: -10.0 + 30.0 = 20.0',
        'PASS', 'None', 'N/A', 'N/A',
        'Displayed: Result: -10.0 + 30.0 = 20.0',
        'PASS'
    ),
    (
        'TC_CALC_003', 'Addition', 'Addition with floating-point decimal numbers',
        'Calculator is running and menu displayed',
        '1. Select option 1 (Addition)\n2. Enter decimal numbers\n3. Observe result',
        'num1 = 12.35\nnum2 = 7.65',
        'Displays: Result: 12.35 + 7.65 = 20.0',
        'Displayed: Result: 12.35 + 7.65 = 20.0',
        'PASS', 'None', 'N/A', 'N/A',
        'Displayed: Result: 12.35 + 7.65 = 20.0',
        'PASS'
    ),
    (
        'TC_CALC_004', 'Subtraction', 'Subtraction of two positive integers',
        'Calculator is running and menu displayed',
        '1. Select option 2 (Subtraction)\n2. Enter first number\n3. Enter second number\n4. Observe result',
        'num1 = 50\nnum2 = 20',
        'Displays: Result: 50.0 - 20.0 = 30.0',
        'Displayed: Result: 50.0 - 20.0 = 30.0',
        'PASS', 'None', 'N/A', 'N/A',
        'Displayed: Result: 50.0 - 20.0 = 30.0',
        'PASS'
    ),
    (
        'TC_CALC_005', 'Subtraction', 'Subtraction resulting in negative number',
        'Calculator is running and menu displayed',
        '1. Select option 2 (Subtraction)\n2. Enter smaller first number\n3. Enter larger second number\n4. Observe result',
        'num1 = 10\nnum2 = 45',
        'Displays: Result: 10.0 - 45.0 = -35.0',
        'Displayed: Result: 10.0 - 45.0 = -35.0',
        'PASS', 'None', 'N/A', 'N/A',
        'Displayed: Result: 10.0 - 45.0 = -35.0',
        'PASS'
    ),
    (
        'TC_CALC_006', 'Subtraction', 'Subtraction with decimal numbers',
        'Calculator is running and menu displayed',
        '1. Select option 2 (Subtraction)\n2. Enter decimal values\n3. Observe result',
        'num1 = 25.75\nnum2 = 10.25',
        'Displays: Result: 25.75 - 10.25 = 15.5',
        'Displayed: Result: 25.75 - 10.25 = 15.5',
        'PASS', 'None', 'N/A', 'N/A',
        'Displayed: Result: 25.75 - 10.25 = 15.5',
        'PASS'
    ),
    (
        'TC_CALC_007', 'Multiplication', 'Multiplication of two positive numbers',
        'Calculator is running and menu displayed',
        '1. Select option 3 (Multiplication)\n2. Enter first number\n3. Enter second number\n4. Observe result',
        'num1 = 12\nnum2 = 8',
        'Displays: Result: 12.0 * 8.0 = 96.0',
        'Displayed: Result: 12.0 * 8.0 = 96.0',
        'PASS', 'None', 'N/A', 'N/A',
        'Displayed: Result: 12.0 * 8.0 = 96.0',
        'PASS'
    ),
    (
        'TC_CALC_008', 'Multiplication', 'Multiplication by zero (Boundary Value)',
        'Calculator is running and menu displayed',
        '1. Select option 3 (Multiplication)\n2. Enter any number and 0\n3. Observe result',
        'num1 = 45\nnum2 = 0',
        'Displays: Result: 45.0 * 0.0 = 0.0',
        'Displayed: Result: 45.0 * 0.0 = 0.0',
        'PASS', 'None', 'N/A', 'N/A',
        'Displayed: Result: 45.0 * 0.0 = 0.0',
        'PASS'
    ),
    (
        'TC_CALC_009', 'Multiplication', 'Multiplication of two negative numbers',
        'Calculator is running and menu displayed',
        '1. Select option 3 (Multiplication)\n2. Enter two negative numbers\n3. Observe result',
        'num1 = -6\nnum2 = -7',
        'Displays: Result: -6.0 * -7.0 = 42.0',
        'Displayed: Result: -6.0 * -7.0 = 42.0',
        'PASS', 'None', 'N/A', 'N/A',
        'Displayed: Result: -6.0 * -7.0 = 42.0',
        'PASS'
    ),
    (
        'TC_CALC_010', 'Division', 'Division of two valid positive numbers',
        'Calculator is running and menu displayed',
        '1. Select option 4 (Division)\n2. Enter dividend\n3. Enter non-zero divisor\n4. Observe result',
        'num1 = 100\nnum2 = 4',
        'Displays: Result: 100.0 / 4.0 = 25.0',
        'Displayed: Result: 100.0 / 4.0 = 25.0',
        'PASS', 'None', 'N/A', 'N/A',
        'Displayed: Result: 100.0 / 4.0 = 25.0',
        'PASS'
    ),
    (
        'TC_CALC_011', 'Division', 'Division resulting in recurring float',
        'Calculator is running and menu displayed',
        '1. Select option 4 (Division)\n2. Enter 10 and 3\n3. Observe result',
        'num1 = 10\nnum2 = 3',
        'Displays: Result: 10.0 / 3.0 = 3.3333333333333335',
        'Displayed: Result: 10.0 / 3.0 = 3.3333333333333335',
        'PASS', 'None', 'N/A', 'N/A',
        'Displayed: Result: 10.0 / 3.0 = 3.3333333333333335',
        'PASS'
    ),
    (
        'TC_CALC_012', 'Division', 'Division by Zero (Negative / Error Guessing)',
        'Calculator is running and menu displayed',
        '1. Select option 4 (Division)\n2. Enter dividend = 50\n3. Enter divisor = 0\n4. Observe application response',
        'num1 = 50\nnum2 = 0',
        'Displays clean error: "Error: Division by zero is not allowed." without crashing',
        'Application CRASHED with unhandled exception: ZeroDivisionError: float division by zero',
        'FAIL', 'BUG-001', 'Lack of divisor validation before performing division operator (/)',
        'Added check if b == 0: return Error message string instead of executing division',
        'Displays: "Error: Division by zero is not allowed."',
        'PASS'
    ),
    (
        'TC_CALC_013', 'Modulus', 'Modulus of two integers',
        'Calculator is running and menu displayed',
        '1. Select option 5 (Modulus)\n2. Enter 29\n3. Enter 5\n4. Observe result',
        'num1 = 29\nnum2 = 5',
        'Displays: Result: 29.0 % 5.0 = 4.0',
        'Displayed: Result: 29.0 % 5.0 = 4.0',
        'PASS', 'None', 'N/A', 'N/A',
        'Displayed: Result: 29.0 % 5.0 = 4.0',
        'PASS'
    ),
    (
        'TC_CALC_014', 'Modulus', 'Modulus by Zero (Negative / Error Guessing)',
        'Calculator is running and menu displayed',
        '1. Select option 5 (Modulus)\n2. Enter 20\n3. Enter 0\n4. Observe response',
        'num1 = 20\nnum2 = 0',
        'Displays clean error: "Error: Modulo by zero is not allowed." without crashing',
        'Application CRASHED with unhandled exception: ZeroDivisionError: float modulo',
        'FAIL', 'BUG-002', 'Lack of divisor validation before performing modulus operator (%)',
        'Added check if b == 0: return Error message string instead of executing modulo',
        'Displays: "Error: Modulo by zero is not allowed."',
        'PASS'
    ),
    (
        'TC_CALC_015', 'Power', 'Power operation with positive base and exponent',
        'Calculator is running and menu displayed',
        '1. Select option 6 (Power)\n2. Enter base = 2\n3. Enter exponent = 8\n4. Observe result',
        'num1 = 2\nnum2 = 8',
        'Displays: Result: 2.0 ^ 8.0 = 256.0',
        'Displayed: Result: 2.0 ^ 8.0 = 256.0',
        'PASS', 'None', 'N/A', 'N/A',
        'Displayed: Result: 2.0 ^ 8.0 = 256.0',
        'PASS'
    ),
    (
        'TC_CALC_016', 'Power', 'Power operation with exponent 0 (Boundary)',
        'Calculator is running and menu displayed',
        '1. Select option 6 (Power)\n2. Enter base = 99\n3. Enter exponent = 0\n4. Observe result',
        'num1 = 99\nnum2 = 0',
        'Displays: Result: 99.0 ^ 0.0 = 1.0',
        'Displayed: Result: 99.0 ^ 0.0 = 1.0',
        'PASS', 'None', 'N/A', 'N/A',
        'Displayed: Result: 99.0 ^ 0.0 = 1.0',
        'PASS'
    ),
    (
        'TC_CALC_017', 'Square Root', 'Square root of a valid perfect square',
        'Calculator is running and menu displayed',
        '1. Select option 7 (Square Root)\n2. Enter number = 64\n3. Observe result',
        'num = 64',
        'Displays: Result: sqrt(64.0) = 8.0',
        'Displayed: Result: sqrt(64.0) = 8.0',
        'PASS', 'None', 'N/A', 'N/A',
        'Displayed: Result: sqrt(64.0) = 8.0',
        'PASS'
    ),
    (
        'TC_CALC_018', 'Square Root', 'Square root of a negative number (Negative Test)',
        'Calculator is running and menu displayed',
        '1. Select option 7 (Square Root)\n2. Enter number = -25\n3. Observe response',
        'num = -25',
        'Displays clean error: "Error: Cannot calculate square root of a negative number."',
        'Application CRASHED with unhandled exception: ValueError: math domain error',
        'FAIL', 'BUG-003', 'math.sqrt() called directly on negative number without check',
        'Added check if a < 0: return descriptive error message string',
        'Displays: "Error: Cannot calculate square root of a negative number."',
        'PASS'
    ),
    (
        'TC_CALC_019', 'Input Validation', 'Entering alphabetic string characters as operand',
        'Calculator is running and prompts for number',
        '1. Select option 1 (Addition)\n2. Enter "abc" at number prompt\n3. Observe response',
        'num1 = "abc"',
        'Displays error: "Invalid input! Please enter a valid number." and re-prompts',
        'Application CRASHED with unhandled exception: ValueError: could not convert string to float: \'abc\'',
        'FAIL', 'BUG-004', 'Direct float(input()) conversion without try-except block',
        'Created get_valid_number() function wrapping input in while-loop and try-except ValueError block',
        'Displays: "Invalid input! Please enter a valid number." and re-prompts',
        'PASS'
    ),
    (
        'TC_CALC_020', 'Input Validation', 'Submitting empty/blank enter at number prompt',
        'Calculator is running and prompts for number',
        '1. Select option 1 (Addition)\n2. Press Enter without typing any digits\n3. Observe response',
        'num1 = "" (Empty String)',
        'Displays error: "Input cannot be empty. Please enter a valid number." and re-prompts',
        'Application CRASHED with unhandled exception: ValueError: could not convert string to float: \'\'',
        'FAIL', 'BUG-005', 'Empty string passed to float() raises unhandled ValueError',
        'Added strip() and empty string check inside get_valid_number() with descriptive re-prompting',
        'Displays: "Input cannot be empty. Please enter a number." and re-prompts',
        'PASS'
    )
]

for row_idx, tc in enumerate(test_cases_data, start=5):
    for col_idx, val in enumerate(tc, start=1):
        c = ws_testcases.cell(row=row_idx, column=col_idx, value=val)
        c.font = font_data
        c.border = border_cell
        c.alignment = Alignment(vertical='top', wrap_text=True)
        
        # Center align ID, Module, Statuses, Defect ID
        if col_idx in (1, 2, 9, 10, 14):
            c.alignment = Alignment(horizontal='center', vertical='top', wrap_text=True)
            
        # Color coding for status v1.0.0
        if col_idx == 9:
            if val == 'PASS':
                c.fill = fill_pass
                c.font = font_pass
            else:
                c.fill = fill_fail
                c.font = font_fail
                
        # Color coding for status v2.0.0
        if col_idx == 14:
            if val == 'PASS':
                c.fill = fill_pass
                c.font = font_pass
            else:
                c.fill = fill_fail
                c.font = font_fail
                
    ws_testcases.row_dimensions[row_idx].height = 48

# Column widths
tc_col_widths = {
    'A': 16, 'B': 18, 'C': 32, 'D': 25, 'E': 30, 'F': 20,
    'G': 32, 'H': 35, 'I': 16, 'J': 14, 'K': 35, 'L': 38, 'M': 35, 'N': 16
}
for col_letter, width in tc_col_widths.items():
    ws_testcases.column_dimensions[col_letter].width = width

# -------------------------------------------------------------
# SHEET 3: Defect Log (Bugs)
# -------------------------------------------------------------
ws_defects.views.sheetView[0].showGridLines = True
ws_defects['A1'] = 'DEFECT REPORTING & BUG TRACKING LOG'
ws_defects['A1'].font = font_title
ws_defects['A2'] = 'Course: Learning Manual Testing (OUSL) | Project: Simple Calculator (v1.0.0 -> v2.0.0)'
ws_defects['A2'].font = font_subtitle

defect_log_headers = [
    'Bug ID',
    'Related Test Case',
    'Severity',
    'Priority',
    'Defect Title',
    'Steps to Reproduce',
    'Observed Result (v1.0.0 Crash)',
    'Expected Result',
    'Resolution & Code Fix in v2.0.0',
    'Resolution Status'
]

for col_idx, h in enumerate(defect_log_headers, start=1):
    c = ws_defects.cell(row=4, column=col_idx, value=h)
    c.font = font_header
    c.fill = fill_header
    c.alignment = Alignment(horizontal='center', vertical='center', wrap_text=True)
    c.border = border_header
ws_defects.row_dimensions[4].height = 28

defects_data = [
    (
        'BUG-001', 'TC_CALC_012', 'Critical', 'High',
        'Application crashes with ZeroDivisionError when dividing by zero',
        '1. Launch calculator.py v1.0.0\n2. Select option 4 (Division)\n3. Enter num1 = 50\n4. Enter num2 = 0',
        'ZeroDivisionError: float division by zero (Terminal aborts application execution)',
        'Display user-friendly message: "Error: Division by zero is not allowed." and return to main menu',
        'Added conditional check in divide(a, b): if b == 0 return error string. Prevented unhandled arithmetic exception.',
        'CLOSED (Verified in v2.0.0)'
    ),
    (
        'BUG-002', 'TC_CALC_014', 'High', 'High',
        'Application crashes with ZeroDivisionError when performing modulo by zero',
        '1. Launch calculator.py v1.0.0\n2. Select option 5 (Modulus)\n3. Enter num1 = 20\n4. Enter num2 = 0',
        'ZeroDivisionError: float modulo (Application process terminates abnormally)',
        'Display user-friendly message: "Error: Modulo by zero is not allowed." and return to menu',
        'Added condition in modulus(a, b): if b == 0 return error string. Safely handled modulus arithmetic.',
        'CLOSED (Verified in v2.0.0)'
    ),
    (
        'BUG-003', 'TC_CALC_018', 'High', 'Medium',
        'Application crashes with math domain error when calculating square root of negative number',
        '1. Launch calculator.py v1.0.0\n2. Select option 7 (Square Root)\n3. Enter num = -25',
        'ValueError: math domain error (Raised by standard math.sqrt module)',
        'Display user-friendly message: "Error: Cannot calculate square root of a negative number."',
        'Added validation in square_root(a): if a < 0 return descriptive domain error string.',
        'CLOSED (Verified in v2.0.0)'
    ),
    (
        'BUG-004', 'TC_CALC_019', 'Medium', 'High',
        'Entering string/alphabetic characters causes unhandled ValueError crash',
        '1. Launch calculator.py v1.0.0\n2. Choose any arithmetic option (1-7)\n3. Enter text string e.g. "abc"',
        'ValueError: could not convert string to float: \'abc\' (Terminal crashes)',
        'Application should validate user input, inform user with a clear error prompt, and allow re-entering numbers',
        'Implemented get_valid_number(prompt) helper function utilizing while-loop and try-except ValueError block.',
        'CLOSED (Verified in v2.0.0)'
    ),
    (
        'BUG-005', 'TC_CALC_020', 'Medium', 'Medium',
        'Pressing Enter without input (empty string) causes ValueError crash',
        '1. Launch calculator.py v1.0.0\n2. Choose any arithmetic option (1-7)\n3. Press Enter key with blank input',
        'ValueError: could not convert string to float: \'\' (Immediate crash)',
        'Display prompt: "Input cannot be empty. Please enter a valid number." and prompt again',
        'Added strip() and empty string length check in get_valid_number() before float conversion.',
        'CLOSED (Verified in v2.0.0)'
    )
]

for row_idx, df in enumerate(defects_data, start=5):
    for col_idx, val in enumerate(df, start=1):
        c = ws_defects.cell(row=row_idx, column=col_idx, value=val)
        c.font = font_data
        c.border = border_cell
        c.alignment = Alignment(vertical='top', wrap_text=True)
        if col_idx in (1, 2, 3, 4, 10):
            c.alignment = Alignment(horizontal='center', vertical='top', wrap_text=True)
        if col_idx == 3:
            if val == 'Critical':
                c.font = font_fail
            elif val == 'High':
                c.font = Font(name='Segoe UI', size=9.5, bold=True, color='B9770E')
        if col_idx == 10:
            c.font = font_pass
            c.fill = fill_pass
    ws_defects.row_dimensions[row_idx].height = 55

def_col_widths = {
    'A': 14, 'B': 18, 'C': 14, 'D': 14, 'E': 34,
    'F': 32, 'G': 35, 'H': 35, 'I': 38, 'J': 24
}
for col_letter, width in def_col_widths.items():
    ws_defects.column_dimensions[col_letter].width = width

wb.save('Manual_Testing_Test_Cases_Calculator.xlsx')
print('EXCEL_CREATED_SUCCESSFULLY')
