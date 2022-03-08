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
- ~~create superuser~~ this is done
  - user and password are `admin`
  - ~~`python manage.py createsuperuser`~~
  - ~~follow prompts, you can skip everything except username and password~~
  - ~~password can be weak, but it will warn you~~
- there is no template for the home page yet so it will show an error
- `127.0.0.1/admin`

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
