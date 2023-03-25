## Plugin for Transmitting FQDN Addresses to Telegram
* This plugin has been developed with the purpose of transmitting provisional Fully Qualified Domain Name (FQDN) addresses, specifically those containing the phrase "gradio.live", to the messaging platform Telegram. Its main objective is to facilitate remote work in Stable Diffusion.

### README: Send Message Configuration
* To configure the message sending, please follow the instructions below:

+ Insert the Telegram token and chat ID into the config.ini file.
### Bot Functionality
* The bot performs the following functions:

+ The pyTelegramBotAPI library is installed and the necessary modules for the Telegram bot are imported. Configuration parameters are read from a file named config.ini.
+ The bot token and chat ID are extracted from the configuration file and used to create a bot instance.
+ Two functions are defined for sending text messages and public URLs to the Telegram chat using the telebot module.
+ The send_public_url function sends a public URL to the Telegram chat. If the URL is empty, it sends a default message instead.
+ The code checks if it is being executed as the main program and then sends a start message to the chat. A message is also printed to the console for testing purposes.