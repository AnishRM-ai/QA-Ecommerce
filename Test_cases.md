# Test Cases

## Login Test Case

### Global Pre-condition
- Browser is open
### Common Pre-Condition
- User is on login page
- User is registered 

| Test Case ID | Scenario | Pre-Condition | Test Steps | Expected Result | Actual Result| Status |
|--------------|----------|---------------|------------|-----------------|--------------|--------|
| LOGIN_TC_00 | Verify login with valid credentials |  | 1. Enter valid username<br> 2. Enter valid password<br> 3. Click login | User should login successfully | User logged in successfully | Pass |
| LOGIN_TC_01 | Verify login with invalid credentials |  | 1. Enter invalid username<br> 2. Enter valid password<br> 3. Click login | Error message "Invalid username or password" should be displayed | Unclear error message | Fail |
| LOGIN_TC_02 | Verify forgot password | User email is registered | 1. Clicks on forgot password<br> 2. Enters valid email<br> 3. Clicks on send confirmation code | Verification code should be sent to registered email| verification code not received. | Fail |
| LOGIN_TC_03 | Login with valid username and invalid password |  | 1. Enter valid email <br> 2. Enters invalid password<br> 3. Clicks on login | Error message "Invalid username or password" should be displayed | Clear Error message displayed | Pass |
| LOGIN_TC_04 | Login with empty username field  |  | 1. Enter valid password <br> 2. Click login | Error message "Please enter your username" should be displayed | Clear Error message displayed just below the field | Pass |
| LOGIN_TC_05 | Login with empty password field |  | 1. Enter valid email <br> 2. Click login | Error message "Please enter your password" should be displayed | Error message displayed just below the field | Pass |
| LOGIN_TC_06 | Login with both empty field | | 1. Leave the email and password field empty<br> 2. Click login | Validation Error message "Please enter email and password" should be displayed below the field | Validation error message displayed | Pass |
| LOGIN_TC_07 | Verify password field is masked | | Enter valid character on password field | Characters on password field should be masked | Characters on password field are masked | Pass |
| LOGIN_TC_08 | Verify session is maintained after page refresh | User is logged in | 1. Login with valid credential<br>2. Refresh the browser page | User should be logged in after page refresh | User is logged in after page refresh | Pass |
| LOGIN_TC_09 | Verify logout functionality | User is logged in | 1. Click logout button |  User should logged out and redirected to login page | User logged out and redirected to login page | Pass |



## SignUp Page Test Case

### Common Pre-condition
- User is on Registration Page.


| Test Case ID | Scenario | Pre-condition | Test Steps | Expected Result | Actual Result | Status |
|--------------|----------|---------------|------------|-----------------|---------------|--------|
| SIGNUP_TC_00 | Verify successful account registration | | 1. Enter required valid credentials such as First and Last Name, email, password<br> 2. Click on create button <br> | User account should register successfully and redirected to the homepage. | Account registered successfully, redirected to homepage. | Pass |
| SIGNUP_TC_01 | Register with all empty fields | | 1. Leave all the fields empty<br>2. Click create button | Error message"Please fill up all the required fields." should be displayed. | Error message displayed | Pass |
| SIGNUP_TC_02 | Sign up with invalid email format | | 1. Enter email in invalid format<br>2. Enter valid password<br>3. Enter First and last name<br>4. Click create | Error message"Please enter valid email" should be displayed | Error message did not display | Fail |
| SIGNUP_TC_03 | Sign up with insufficient character password | | 1. Enter First and Last name<br>2. Enter valid email<br>3. Enter insufficient character password<br>4. Click create | Validation error message"Password must be 8 or more than 8 character long" should be displayed | No Validation error shown | Fail |

## Product Inventory Test Case
### Common Pre-condition
- User is on product inventory page.

| Test Case ID | Scenario | Pre-condition | Test Steps | Expected Result | Actual Result | Status |
|--------------|----------|---------------|------------|-----------------|---------------|--------|
| PRODINV_TC_00 | Verify the product list loads | | 1. Open Product inventory page | Available product is displayed | Available product displayed | Pass |
| PRODINV_TC_01 | Verify the product name, price, image visible | | 1. Open Product inventory page | Product name, price, image is visible | Product name, price, image is visible | Pass |
| PRODINV_TC_02 | Verify the product search functionality | | 1. Enter product name on search bar<br> 2. Click search | The searched product should be listed if availabe if not then it should display error message | Searched product listed as it was available | Pass |



