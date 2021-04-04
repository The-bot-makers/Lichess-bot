# masterbotheroku - Lichess-bot

The code template to make a Lichess Bot and deploy it to heroku server easily.

This is the code of [@master_bot](https://lichess.org/@/master_bot) in [lichess.org](https://lichess.org)

### Chess Engines

- Stockfish 13 POPCNT + SSE41

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
- You're now connected to lishogi and awaiting challenges! Your bot is up and ready!
