# Autama Backend

## Explanation of Autama(what it is and does)
_Autama: Web Platform_  

* API
* DB
* Supporting infrastructure

Add description here. 


## Build and Run  

### To Run:
  * pip3 install -r requirements.txt
  * If this is the first run, create a DB, download a personality dataset, and create a Nucleus
  * python manage.py runserver
  * in a web browser go to: 127.0.0.1:8000 (This should be displayed during server startup)

### To Create the DB: 
  * python manage.py makemigrations accounts
  * python manage.py makemigrations AutamaProfiles
  * python manage.py migrate

### To Download a Personality Dataset: 
  * python dataset.py
  
### To Create a Nucleus: 
  * python build.py


## Bugs, Defects, Failing Tests, etc

Bugs, Defects, and Failing Test information goes here as needed.

  * If you get a transformers.activations error while talking with an Autama, just recreate a nucleus
  * 5/27/20 - Bugs needing solutions:
    - first and last name fields during creation at registration not inserted into new Autama
    - fix missing icons
    - auto-login at registration(no redirect to login again)
    - swipe card details are jumbled


## License

This program is licensed under the "MIT License".  Please
see the file `LICENSE` in the source distribution of this
software for license terms.  

## Acknowledgments  

Django tutorial references here

Hugging Face Inc. for ConvAI


