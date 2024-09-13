# Keylogger Using pynput Library
This project is a simple keylogger built in Python using the pynput library to capture keyboard input. It logs keystrokes to a text file, handling common keys (alphanumeric and special keys like space, enter, etc.) and managing backspace deletions and shift key presses efficiently.

## Features
### Shift Key Handling:

The keylogger tracks when the shift key is pressed and ensures that it is logged only once, no matter how long it is held down.

### Backspace Key Handling:

When the backspace key is pressed, the logger removes the last character from the log file instead of logging the keypress itself. This makes the log more readable and accurate.
Date and Time Logging:

The logger records the date and time it starts running, helping to track when the keylogging session began.
Future Enhancements
Dynamic File Saving:
Currently, the keylog file is saved as keylog.txt in the specified directory. A planned enhancement will allow the keylogger to create unique filenames (with timestamps or counters) for each session to avoid overwriting old logs.
Installation
Clone the repository:

bash
Copy code
git clone https://github.com/yourusername/keylogger.git
Install dependencies:

bash
Copy code
pip install pynput

Update the log_dir variable in the script to specify where the log file should be saved.

## Usage
Run the keylogger:

bash
Copy code
python keylogger.py

The script will begin listening for keyboard input and log it to keylog.txt in the directory specified by log_dir.

The logged file will include:

Alphanumeric keys.
Special keys like space, enter, and shift.
Removal of characters when backspace is pressed.

## How It Works
Logging Alphanumeric and Special Keys:
### Alphanumeric keys: Captured via key.char and written directly to the log file.
### Special keys: Handled separately, logging them by name (e.g., [space], [enter]).
### Shift Key:
The shift key is tracked using a shift_pressed flag to ensure it's logged only once, even if held down for a long period.
### Backspace Key:
The logger handles the backspace key by removing the last character from the log file, making it behave like an actual backspace and cleaning up the logged content.
## Example
Here’s an example of the log output:

bash
2024-09-12 14:45:23
[shift] Hello [shift] World
[shift] This is a test message

## Future Enhancements
Dynamic Filename Creation:
Implement functionality to generate unique log filenames to prevent overwriting previous logs automatically.

Additional Key Exceptions:
Add more special key handling for other modifier keys (e.g., ctrl, alt, capslock, etc.).

Contributing
Contributions are welcome! Feel free to submit a pull request or open an issue to discuss further improvements or bug fixes.

License
This project is licensed under the MIT License.
