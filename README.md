# XeroApiWorkshop
A workshop given by Xero in collaboration with Women Who Code 

## Introduction

Hi! We're really glad to have you learning with us. This repository will be the starting place for this workshop. Fork this repository to create your own copy. Then, clone that using your terminal. You'll also want to set up the link between your local version and remote repositories so that any changes you make can be pushed to your version of the master. We recommend using this as a starting point and developing your API further to suit your own needs or learn further from the project. We have also created a repository with more endpoints here https://github.com/erikacheyenne/XeroApiWorkshopCompleted.git . Take this project further by adding even more endpoints, creating a frontend that connects with your work, and add a database. 

Please read the getting started secion below so you can get this code running on your computer after you've set up your repositories. 

### What is an API?
An API is an application programming interace. An API is an engine that takes the request for another program, and sends the response back after you've interacted with it. 

### What are API's used for?
* Connecting services to each other
* Linking frontend and backend components together 

### How does Xero use APIs?
* Connecting various parts of our platform to each other 
* Allow customers to access their bank data
* Enable connections with other services in our ecosystem
* Combine backend and frontend components
* Enforce authentication and authorization

### How do I build an API?
We'll be going over how to build an API in this workshop. An API will need various methods, and those methods will define what kind of request is sent out, and what kind of response is received. 

This workshop will focus specifically on REST APIs, but you may build a SOAP API in your career. SOAP APIS rely on XML for making requests, while REST APIs rely on URLs. You may find that some REST APIs require more details, like a token for authentication, but overall they rely on URLs. 

## Getting Started
### Set Up Repo
* Fork this repository
* Clone your fork to your computer using your terminal

If you need help doing this, follow this tutorial: https://www.digitalocean.com/community/tutorials/fork-clone-make-changes-push-to-github .
### How to get the code running - Mac 
Run these commands in this order.

* pip install flask - this is to install it specifically on your computer 
* python3 -m venv venv
* virtualenv venv
* source venv/bin/activate - use this anytime you want to be in the virtual environment
* pip install flask - this is to install it to your virtual environment 
* Python 
* import flask - this is to check that the install worked 
* CONTROL + Z - to exit the python command line
* export FLASK_APP=storeapi.py - so flask can see our app for the first time
* flask run - run our app, we will keep doing this part over and over 


### How to get the code running - Windows 
If you are using Windows, you'll want to install Gitbash to run these commands. You can download Gitbash here: https://gitforwindows.org/ .

You'll also want to install Pip specifically for Windows, the guide to doing that is here: 
https://github.com/BurntSushi/nfldb/wiki/Python-&-pip-Windows-installation .

Run these commands in this order.

* pip install flask - this is to install it specifically on your computer 
* python3 -m venv venv
* virtualenv venv
* venv\Scripts\activate - use this anytime you want to be in the virtual environment
* pip install flask - this is to install it to your virtual environment 
* Python 
* import flask - this is to check that the install worked 
* CONTROL + Z - to exit the python command line
* export FLASK_APP=storeapi.py - so flask can see our app for the first time
* flask run - run our app, we will keep doing this part over and over 

### How is the repository organized

This repository has all of the files organized based on what is being done in that file. There is a file specifically for the routes, a file for the application being run, and a file for the environmental variables for flask. 
