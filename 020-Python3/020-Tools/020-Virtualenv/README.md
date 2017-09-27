# Viratualenv Example

Prerequisit
* Pip

## Create a new Viratualenv Project
```
virtualenv env
```

## Install Libraries
```
env\Scripts\pip install request
```

## Generate dependencies
```
env\Scripts\pip freeze > requiremenets.txt
```

## Install Dependenecies
```
env\Scripts\pip install -r requiremenets.txt
```