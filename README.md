#Simple Bank System Application

## Introduction

This Python application simulates a basic banking system. It allows users to create bank accounts, deposit and withdraw money, check account balances, and view transaction history. The application uses basic password encryption for security.

## Features

- **Bank Account Management:** Create checking or savings accounts with initial balances.
- **Secure Password Handling:** Passwords are hashed using SHA-256 for secure storage.
- **Deposit and Withdrawal:** Perform deposit and withdrawal operations with basic validation.
- **Transaction History:** View a history of all transactions performed on the account.
- **Account Balance:** Check the current balance of your account at any time.
- **User Interface:** Simple text-based interface for interacting with the bank system.

## Installation

No additional libraries are required as the script uses standard Python libraries (`hashlib` and `datetime`). Ensure that Python is installed on your machine.

## Usage

1. **Starting the Application:** Run the script to start the banking system interface.
2. **Creating an Account:** Choose to create an account, providing a name, password, account type, and initial balance.
3. **Accessing an Account:** Access your account using your name and password.
4. **Performing Transactions:** Deposit or withdraw money, and view your account balance and transaction history.
5. **Exiting the Application:** Exit the application or log out of the account to return to the main menu.

## Files

- `bank_system.py`: Contains the main logic for the bank system, account management, and user interface.

## Extending the Application

- **Enhanced Security:** Implement more robust authentication and encryption methods.
- **Database Integration:** Store account data in a database instead of in-memory for persistence.
- **Additional Features:** Add features like account-to-account transfers, loan management, etc.
- **User Interface:** Improve the user interface with a graphical user interface or web interface.

## Notes

- This application is for educational purposes and not for real-world banking usage.
- The application does not persist data after the program is closed.

## License

This project is open-source and free to use or modify.
