# SauceDemo E-commerce Manual Testing Project

## Project Overview
This project demonstrates comprehensive manual testing of the SauceDemo e-commerce application. The testing covers critical functionalities including user authentication, product management, shopping cart operations, and checkout processes.

**Application Under Test:** [SauceDemo](https://www.saucedemo.com)

## Testing Objectives

- Validate core e-commerce functionalities
- Identify bugs and usability issues
- Ensure data validation and error handling
- Document test cases following industry standards
- Create professional bug reports with detailed reproduction steps

## Test Summary

| Metric | Count |
|--------|-------|
| **Total Test Cases** | 28 |
| **Passed** | 23 |
| **Failed** | 5 |
| **Pass Rate** | 82% |
| **Bugs Found** | 4 |

##  Test Coverage

### Modules Tested

1. **Login Module** (10 test cases)
   - Valid/Invalid credentials
   - Empty field validation
   - Password masking
   - Session management
   - Logout functionality
   - Password recovery

2. **Signup Module** (4 test cases)
   - Successful registration
   - Field validation
   - Email format validation
   - Password strength validation

3. **Product Inventory** (3 test cases)
   - Product listing
   - Product details display
   - Search functionality

4. **Shopping Cart** (6 test cases)
   - Add to cart
   - Remove from cart
   - Update quantity
   - Cart persistence
   - Multiple items handling

5. **Checkout Process** (4 test cases)
   - Complete checkout flow
   - Address validation
   - Payment information validation
   - Order confirmation
## Test Case Documentation

All test cases are documented with the following structure:

- **Test Case ID**: Unique identifier
- **Scenario**: What is being tested
- **Pre-conditions**: Required setup
- **Test Steps**: Step-by-step instructions
- **Expected Result**: What should happen
- **Actual Result**: What actually happened
- **Status**: Pass/Fail

**View Test Cases:** [Test_cases.md](Test_cases.md)

## Bugs Identified

### Critical Bugs

| Bug ID | Severity | Module | Description | Status |
|--------|----------|--------|-------------|--------|
| BUG_001 | Medium | Login | Unclear error message on invalid login | Open |
| BUG_002 | High | Signup | Missing email format validation | Open |
| BUG_003 | High | Login | Password reset email not received | Open |
| BUG_004 | Medium | Signup | No password length validation | Open |

**Detailed Bug Reports:** [Bug_Reports.md](Bug_Reports.md)

## Testing Environment

- **Browser:** Chrome (Version 120)
- **Operating System:** Windows 11
- **Screen Resolution:** 1920x1080
- **Testing Period:** January 2026
- **Testing Type:** Manual, Black-box Testing

## Testing Methodologies Applied

- **Black Box Testing**: Testing without knowledge of internal code structure
- **Functional Testing**: Verifying each function works as expected
- **Positive Testing**: Valid input scenarios
- **Negative Testing**: Invalid input and edge cases
- **Boundary Value Analysis**: Testing limits of input fields
- **Regression Testing**: Ensuring existing features still work

## Test Metrics & Analysis

### Test Execution Summary

- **Total Execution Time**: ~8 hours
- **Average Test Case Execution Time**: ~15-20 minutes
- **Defect Density**: 4 bugs / 28 test cases = 14% defect rate
- **Critical/High Priority Bugs**: 2 (50% of total bugs)

### Module-wise Results

| Module | Test Cases | Pass | Fail | Pass % |
|--------|-----------|------|------|--------|
| Login | 10 | 8 | 2 | 80% |
| Signup | 4 | 2 | 2 | 50% |
| Product Inventory | 3 | 3 | 0 | 100% |
| Shopping Cart | 6 | 6 | 0 | 100% |
| Checkout | 4 | 4 | 0 | 100% |

### For Recruiters/Hiring Managers

1. Review [Test_cases.md](Test_cases.md) to see test case design skills
2. Check [Bug_Reports.md](Bug_Reports.md) to evaluate bug reporting quality
3. Examine this README to understand testing approach and documentation

### For Fellow QA Engineers

1. Clone this repository as a reference for test documentation
2. Use the test case template for your own projects
3. Adapt the bug report format for your testing workflow

## Key Learnings

1. **Test Case Design**: Learned to create clear, reproducible test cases with proper pre-conditions and expected results
2. **Bug Reporting**: Developed skills in writing detailed bug reports with severity classification and business impact
3. **Test Coverage**: Understood the importance of both positive and negative test scenarios
4. **Documentation**: Improved technical writing and documentation skills
5. **SDLC/STLC**: Applied Software Testing Life Cycle principles in a real-world scenario

## Tools & Technologies

- **Documentation**: Markdown
- **Version Control**: Git/GitHub
- **Browser**: Chrome DevTools for inspection
- **Test Management**: Manual tracking in Markdown tables

## Best Practices Followed

✅ Clear and concise test case descriptions  
✅ Unique test case IDs for traceability  
✅ Detailed steps for reproducibility  
✅ Proper severity and priority classification for bugs  
✅ Business impact analysis in bug reports  
✅ Professional documentation formatting  
✅ Version control for test artifacts  

## Future Enhancements

- [ ] Add automation test suite using Playwright
- [ ] Include API testing for backend validation
- [ ] Create visual regression tests
- [ ] Implement CI/CD pipeline for automated testing
- [ ] Add performance testing metrics
- [ ] Create test execution videos

## Contact

**Tester:** Anish Rajan Magar  
**Email:** magaranish880@gmail.com 

## License

This project is for educational and portfolio purposes.

## Acknowledgments

- SauceDemo team for providing a publicly accessible test application
- QA community for testing best practices and guidelines
