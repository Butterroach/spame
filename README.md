# spame

## A discord.py bot for managing spam channels

Spame is a Discord bot written in discord.py that manages spam channels by removing messages that aren't the same as the current spam message.

### Features

-   Deletes messages that aren't equal to the currently set spam message
-   Toggleable .env option for case insensitive/sensitive matching
-   'Changer' permission that allows users with it to change the spam message through a bot command at any time
-   Allows for multiple spam channels with a prefix
-   Automatically pins announcements for new spam messages and deletes older pins to avoid reaching the pin limit

### **Notes**

-   **The bot will require the 'Manage Messages' permission, the 'Message Content' intent, the 'Server Members' intent, and the 'Bot' scope to work properly.**
-   **The bot is designed to be on one server only. If on multiple servers, the spam message will be set all across them, and settings will apply to every server. You can fork the bot and fix this for your own use if you'd like, but I will NOT be accepting any pull requests that fix this.**

### How to use

1. Get Python and Git.
2. Clone the repository with git.
3. Run `pip install -r requirements.txt`.
4. Set up a .env file by coping the .env.example file and editing it.
5. Now, run the bot.py program and enjoy! The bot will only run in channels that have names that start with the SPAM_CHANNEL_PREFIX value.
