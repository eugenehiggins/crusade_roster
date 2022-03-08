# crusade roster

## Installation
- Install python and pip: https://docs.djangoproject.com/en/4.0/intro/install/
- create virtual environment -- lots of choices here
  - `python3 -m venv env` for example 
  - `. env/bin/activate` to activate
- install requirements
  - `pip install -r requirements.txt`
  - `requirements.txt` will likely change
- test with `python manage.py runserver`
  - look for errors in the terminal
  - if working looks like:
  ```zsh
  Watching for file changes with StatReloader
  System check identified no issues (0 silenced).
  March 08, 2022 - 17:12:03
  Django version 4.0.2, using settings 'crusade_roster.settings'
  Starting development server at http://127.0.0.1:8000/
  Quit the server with CONTROL-C.
  ```
- ~~create superuser~~ this is done
  - user and password are `admin`
  - ~~`python manage.py createsuperuser`~~
  - ~~follow prompts, you can skip everything except username and password~~
  - ~~password can be weak, but it will warn you~~
- go to http://127.0.0.1:8000/
  - there is no template for the home page yet so it will show an error
  - there might not ever be a template for the homepage
- go to `127.0.0.1:8000/admin`

## TODO: features

### battle
- on Order of Battle page, select units then hit "create battle"
- goes to battle edit page
  - edit battle page carries over units already selected
  - enter battle size, enemy name and crusade points
  - enter mission/map details
  - enter pre-battle flavor text
  - enter/pick agendas?
- during battle
  - tally agendas
  - tally kills
  - record out-of-action 
- after battle click "end battle"
  - records win/loss
  - records xp
  - records battle scars
