# Skiptify

An applet running in the background to learn from what music you skip when you play a playlist, so that if you skip many similar songs it will automatically skip that kind of songs.

## Discord

Click this link https://discord.gg/8vs5a2Nk to koin our discord.

## Project structure

- backend
  - src
  - db: all about the db mangement
  - model: all about the decision model
- utils:
  - api_interface: all about interfacing with the API
  - frontend : all about the frontend
  - test : tests
  - req.txt : environment

`conda config --append channels conda-forge`
`conda create --name ./envs --file requirements.yml`
