Importing Libraries:
The code begins by importing tkinter (as tk) for GUI creation and webbrowser to open URLs in a browser.

Loading Currency Data:

A file named currencydata.txt is opened, and each line is read into a dictionary, currencyDict, with currency names as keys and conversion rates as values.
Function Definitions:

open_net(): Opens a hardcoded URL (for currency rates) in the default browser when called.
display_result(result): Creates a new window displaying the conversion result. An image (currency icon) is set as the window icon.
deletion(): Destroys the result window when called, usually after closing.
convert_currency(): Converts the entered amount based on the selected currency and shows the result by calling display_result.
Setting up Main Window:

The main Tk window (window) is created, titled “CURRENCY CONVERTER,” with an icon and size set to 1920x1080.
GUI Components:

Amount Label and Entry: A label prompts the user to enter an amount in INR, followed by an entry field (amount_ent) for input.
Currency Selection: A dropdown menu (currency_menu) is created, letting users select from the currencyDict.
Buttons:
REFER HERE Button: Opens the URL with currency information by calling open_net.
CONVERT Button: Triggers the convert_currency function, performing the conversion.
CLOSE Button: Closes the result window by calling deletion.
Main Loop Execution:

The window.mainloop() call keeps the GUI window open and responsive to user inputs until closed manually.
