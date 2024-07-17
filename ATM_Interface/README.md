# Python ATM Application

This project is a fully functional ATM application built with Python and KivyMD. It simulates basic banking operations such as checking balance, withdrawing cash, depositing cash, and viewing transaction history.

## Features

- **User Authentication:** Secure PIN-based login to access ATM functionalities.
- **Balance Check:** Check your account balance.
- **Withdraw Cash:** Withdraw specific amounts from your account.
- **Deposit Cash:** Deposit cash into your account.
- **Transaction History:** View the history of all transactions made.

## Technologies Used

- **Python:** Core programming language.
- **Kivy:** Framework for building the user interface and handling backend logic.
- **KivyMD:** Kivy Material Design library for creating a user-friendly interface.

## Getting Started

### Prerequisites

Ensure you have the following installed:

- Python 3.x
- pip (Python package installer)

### Installation

1. Clone the repository:

   ```sh
   git clone https://github.com/SyedAejazAhmed/python.git
   cd ATM_Interface
   ```
2. Install the required Python packages:

  ```sh
  pip install kivy kivymd
  ```
3. Running the Application
To run the ATM application, use the following command:

  ```sh
  python ATM.py
  ```
## Usage
1. **Insert Card:** Start the application and click on "Insert Card" to proceed.
2. **Enter PIN:** Input the PIN to authenticate.
3. **Choose Transaction:** Select from options like Check Balance, Withdraw Cash, Deposit Cash, or View Transaction History.
4. **Perform Transaction:** Follow the on-screen instructions to complete your transactions.

## Key Functions
- insert_card: Transitions to the welcome screen.
- update_pin_input: Updates the PIN input field with user input.
- clear_pin_input: Clears the PIN input field.
- enter_pin: Authenticates the user based on the entered PIN.
- go_to_balance: Displays the current account balance.
- go_to_withdraw: Transitions to the cash withdrawal screen.
- go_to_deposit: Transitions to the cash deposit screen.
- go_to_history: Displays the transaction history.
- withdraw_cash: Handles the cash withdrawal process.
- deposit_cash: Handles the cash deposit process.
- go_back_to_transaction: Returns to the main transaction screen.
- exit_to_welcome: Logs the user out and returns to the welcome screen.
- exit_app: Closes the application.
- _on_keyboard_down: Handles keyboard inputs for the PIN entry.

## Contributing
Contributions are welcome! If you find any issues or have suggestions for improvements, feel free to open an issue or create a pull request.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgements
Special thanks to the open-source community and everyone who provided support and guidance during the development of this project.

## Contact
If you have any questions, feel free to reach out:
