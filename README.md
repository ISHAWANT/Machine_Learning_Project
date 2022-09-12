## Start Machine Learning Project

### Software and account Requirements.

1. [Github Account](http://github.com)
2. [Heroku Account](https://dashboard.heroku.com/login)
3. [VS Code IDE](https://code.visualstudio.com/download)
4. [GIT CLI](https://git-scm.com/downloads)

creating conda enviroment
```
conda create -p venv python==3.7 -y

```
conda activate venv/

```
```
pip install -r requirements.txt

```
```
git add .
```
```
git add file name
```

>To igonre file or folder from git we can write name of  file or folder in .gitignore file

```
To check the git staus
```
git status
```
To check all version maintained by git
```
git log
```
to create version/commit all changes by git
```
git commit -m "message"
```
To send version/changes to github
```
git push origin main
```
to check remote url
```
git remote -v
```
To Setup  CI/CD pipeline in heroku we need 3 information

1. HEROKU_EMAIL = DFKD@GMAIL.COM
2. HEROKU_API_KEY =  f7695298-20ba-4d22-9112-b69db7f09e89
3. HEROKU_APP_NAME = demo-ishawant

BUILD DOCKER IMAGE
```
docker build -t <image_name>:<tagname> .
```
>Note: Image name for docker must be lowercase

To List docker image
```
doker images
```

Run docker image
```
docker run -p 5000:5000 -e PORT=5000 image_id(just like f8clkdfjdklei84)

```
To check running container in docker

```
docker ps
```
To stop docker container
```
docker stop <container_id>

```
```
python setup.py install 
```

Install ipynb kernal
```
pip install ipykernal
```

