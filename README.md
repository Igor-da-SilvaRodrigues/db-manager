## Build/Run Project
### Navegue até a raiz do projeto em um terminal.
```shell
cd $PROJECT_PATH
```

### Create venv
```shell
python -m venv venv
```

### Activate venv
```shell
venv/Scripts/activate
```
### Install dependencies
```shell
pip install -r requirements.txt
```

### Start Server
```shell
python manage.py runserver
```

### Compile SASS
```shell
python manage.py sass app_auth/static/sass/main.scss app_auth/static/css/main.css -g
```
