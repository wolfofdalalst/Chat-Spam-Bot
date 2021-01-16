## Chat-Spam-Bot
#### Programming Language : Python3 
Before running the program, make sure *pyautogui* and *keyboard* modules are installed.\
To install them, enter these commands in CMD :-
```
> pip install pyautogui 
> pip install keyboard
```
### How to execute the program?
STEP 1 : Execute the *SPAM.bat* file by either clicking it or executing it in CMD.\
STEP 2 : Within 10 seconds click the text-box where the messages will be entered.\
STEP 3 : The program will send 500 messages but incase you want to terminate the program before hand,\
press the key "q" on your keyboard or press *ctrl+c* in the application window and the program will terminate.\

To change the Fail Safe Key (which is "q" by default) of the program, open *bot.py* and change the following variable :-
```python
SAFE_KEY = "[input your key here]"
``` 
For example if one wants the Fail Safe Key to be "x", we make the following changes :-
```python
SAFE_KEY = "x"
```
