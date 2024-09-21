
# InstaTrackBot

InstaTrackBot is a Selenium-based automation tool designed to help you track and manage your Instagram followers and following. With this bot, you can identify users who follow you back, fetch lists of followers and followings, and automate data scraping.



## Features

1. Login Automation: Automatically logs into Instagram using your credentials.
2. Follower Tracking: Fetches your followers list.
3. Following Tracking: Fetches your following list.
4. Follow Back Check: Compares followers and following to identify who follows you back.
5. Scroll Automation: Automates scrolling through followers and following lists to load more data.


## Installation

1. Clone this repository:

```bash
  https://github.com/sulogno/InstaTrackBot.git

```
2. Navigate to the project directory:

```bash
  cd InstaTrackBot
```
3.  Install the required dependencies:
```bash
  pip install -r requirements.txt

```
4. Download ChromeDriver and ensure it's in your system's PATH or in the project directory.

## Usage
1. Run the bot by executing the script:
```bash
  python main.py
```
2. It will ask for:
```bash 
Enter your username:"username"
Enter your password:"password"
```
3. The bot will log in, navigate to your profile, fetch follower and following data, and display users who follow you back.








## Project Structure

- **`main.py`**: Main script to run InstaTrackBot.
- **`requirements.txt`**: Lists all dependencies.
- **`README.md`**: Documentation.

## How It Works

1. Login: The bot logs into Instagram using your credentials.
2. Profile Navigation: It navigates to your Instagram profile to access follower and following data.
3. Scroll Automation: The bot scrolls through your followers and following lists to load all the available data.
4. Follow Back Analysis: It compares your followers and following lists to identify who follows you back.
5. Results: The bot prints out the usernames of people who follow you back.


## Functions

- **`get_total_count(category)`**: Fetches the total count of followers or following users.
- **`scroll_and_fetch(scroll_box, max_count)`**: Scrolls through a list and fetches usernames.
- **`get_following_list()`**: Fetches and returns the list of accounts you are following.
- **`get_follower_list()`**: Fetches and returns the list of accounts that follow you.
- **`following_back()`**: Compares your followers and following lists to display users who follow you back.
- **`close_button()`**: Closes the Instagram dialog window.
## Possible Future Updates

Instagram's structure may change over time, which could affect the bot. If it stops working:

- Update the XPaths to match Instagram's new HTML structure.
- Handle new pop-ups or layout changes.
## Requirements

- Python 3.8+
- Selenium
- Google Chrome Browser
- ChromeDriver (compatible with your Chrome version)
## Contributing

Feel free to open issues or submit pull requests to improve InstaTrackBot!

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
