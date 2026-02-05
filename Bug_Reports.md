# Bug Report - SauceDemo Application

## Summary
Total Bugs Found: 4
- Critical: 0
- High: 2
- Medium: 3
- Low: 0

---

## BUG_001

| Field | Description |
|-------|-------------|
| Bug ID | BUG_001 |
| Title | Unclear error message displayed on invalid login credentials |
| Application | SauceDemo E-commerce |
| URL | https://www.saucedemo.com |
| Module | Login |
| Environment | Chrome v120 / Windows 11 |
| Severity | Medium |
| Priority | High |
| Status | Open |
| Reported Date | January 28, 2026 |
| Reported By | Anish Rajan Magar |
| Assigned To | Dev Team |

### Steps to Reproduce
1. Navigate to https://www.saucedemo.com
2. Enter username: "mindpixel@gmail.com"
3. Enter password: "Password1@"
4. Click "Login" button

### Test Data
- Username: mindpixel@gmail.com
- Password: Password1@

### Expected Result
Clear error message "Epic sadface: Username and password do not match any user in this service" should be displayed.

### Actual Result
Error message is unclear/confusing to end users.

### Impact
Users may not understand why login failed, leading to poor user experience.

### Attachments
- Screenshot: bug_001_login_error.png

### Related Test Case
LOGIN_TC_01

---

## BUG_002
| Field | Description |
|-------|-------------|
| Bug ID | BUG_002 |
| Title | Verification code for password change not sent |
| Application | SauceDemo E-commerce |
| URL | https://www.saucedemo.com/signup |
| Module | User Registration |
| Environment | Chrome / Windows 11 |
| Severity | High |
| Priority | High |
| Status | Open |
| Reported Date | January 27, 2026 |
| Reported By | Anish Rajan Magar |
| Assigned to | Dev Team |

### Steps to Reproduce
- Go to login page
- Click forgot password
- Enter valid registered email
- Click send

### Expected Result
Verification code sent to user email.

### Actual Result
Verification code not sent.

### Impact
Creates issues in recovering account.

### Relates Test Cases
LOGIN_TC_002

## BUG_003

| Field | Description |
|-------|-------------|
| Bug ID | BUG_003 |
| Title | No validation error displayed for invalid email format on signup |
| Application | SauceDemo E-commerce |
| URL | https://www.saucedemo.com/signup |
| Module | User Registration |
| Environment | Chrome v120 / Windows 11 |
| Severity | Medium |
| Priority | High |
| Status | Open |
| Reported Date | January 28, 2026 |
| Reported By | Anish Rajan Magar |
| Assigned To | Dev Team |

### Steps to Reproduce
1. Navigate to SauceDemo signup page
2. Enter First name: "John"
3. Enter Last name: "Doe"
4. Enter email: "invalidemail" (without @ symbol)
5. Enter password: "Password123"
6. Click "Create Account" button

### Test Data
- First Name: John
- Last Name: Doe
- Email: invalidemail
- Password: Password123

### Expected Result
Validation error message "Please enter a valid email address" should be displayed below the email field.

### Actual Result
No error message displayed. Form may submit with invalid data or fail silently.

### Impact
Invalid email addresses may be registered, causing issues with password recovery and email notifications.

### Attachments
- Screenshot: bug_002_email_validation.png

### Related Test Case
SIGNUP_TC_02


