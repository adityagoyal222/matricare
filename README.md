# MatriCare

MatriCare is an webapp enabled discussion forum for new and expecting mothers. Questions can be asked to the community of other mothers and experts of related field
![HomePage](https://github.com/adityagoyal222/matricare/blob/master/home-screen.png?raw=true)

## Main Features
<ul>
  <li>Create new posts for your queries.</li>
  *forum.png*
  <li>'Like' and comment on others' posts.</li>
  <li>Keep a personal journal, and if needed, share them with your doctors for easier and more accurate diagnosis.</li>
  <li>Get wonderful advice from verified doctors</li>
  </ul>

## Installation

Create a new Python virtual environment 

```
python -m venv venv
```

Activate virtual environment

```
venv\Scripts\activate
```

Install all the dependencies from matricare/requirements.txt

```
pip install -r requirments.txt
```

Execute all migrations in the matricare/matriCare directory

```
python manage.py migrate
python manage.py maekmigrations
python manage.py migrate
```

## Usage

After the installation is complete, the web app is ready to launch. Go to matricare/matriCare directory where manage.py is located.
```
python manage.py runserver
```
Finally, launch 127.0.0.1:8000 in your browser to view the web app

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
