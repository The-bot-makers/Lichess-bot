# Lichess-bot

[![Python Build](https://github.com/The-bot-makers/Lichess-bot/actions/workflows/python-build.yml/badge.svg)](https://github.com/The-bot-makers/Lichess-bot/actions/workflows/python-build.yml)

The code template to make a Lichess Bot and deploy it to heroku server easily.

This is the code of [@master_bot](https://lichess.org/@/master_bot) in [lichess.org](https://lichess.org)

### Chess Engines

- Stockfish 13(dev) POPCNT + SSE41
- Fairy Stockfish 13 POPCNT + SSE41
- Multi-Variant Stockfish 13 POPCNT + SSE41

### Polyglot Opening Books

- [book.bin](https://github.com/The-bot-makers/Lichess-bot/blob/master/book.bin) for Standard Chess
- [bookchen.bin](https://github.com/The-bot-makers/Lichess-bot/blob/master/bookchen.bin) for Lichess Supported Variants(negligble size, antichess only. still in development.)

### Heroku Buildpack

- heroku/python

### Heroku Stack

- heroku-20 (allowing a maximum hash size of 512 mb)

### How to Use

- Fork this repository.
- Edit only your token in the config.yml file over [here](https://github.com/the-bot-makers/Lichess-bot/blob/master/config.yml#L1).
- Create a new heroku app.
- Go to the 'Deploy' tab and click 'Connect to GitHub'.
- Click on 'search' and then select your fork of this repository.
- Then 'Enable Automatic Deploys' and then select the 'master' branch (which is already done by default) and Click 'Deploy'.
- Once it has been deployed, go to 'Resources' tab on heroku and enable 'worker' (bash startbot.sh) dynos. (do note that if you don't see any dynos in the 'Resources' tab, then you must refresh your heroku page.)
- You're now connected to lichess and awaiting challenges! Your bot is up and ready!

**Note:** Incase of any errors during deploy of code to heroku, make sure to set the buildpack in the 'Settings' tab in heroku as given in the instructions [here](https://github.com/The-bot-makers/Lichess-bot#heroku-buildpack)

### Important Notes

- Make sure to disable/switch off the dyno once you are not monitoring your bot, for the bot used to crash in bullet often. In the recent very few games, this stopped happening, but until it is fully tested, switch off the dyno when you are monitoring your bot. If any error shows up in the logs, immediately restart all dynos by more-restart all dynos.
- Also swith off your bot when you are shutting your computer down, else it might crash. This happens due to the bot losing connection with heroku. To prevent this your internet has to be running smoothly and constantly connected to heroku.
- This bot uses 120 MB hash size with 5 threads. This is quite strong, but the downside is games at a time. Heroku's free dyno's limitations are crossed even with 2-3 games in one go. So make sure you don't play many games in one go. If you want multiple games at a time, reduce the values of threads and hash in the lichessbot.py and use multithreading to handle multiple games. This is mainly caused due to rate limiting from heroku or lichess. This can be prevented by increasing 'rate_limiting_delay' in the 'config.yml' file.
- Compared to other bots, this bot plays relatively fast, and the time taken is static. I am trying to figure out a way to have better time management.
