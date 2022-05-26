## CSC 4530 Project - Milestone 1
Heroku Deployed link: https://vast-springs-24079.herokuapp.com

## Table of Contents
* [Overview](#overview)
* [APIs Frameworks and Libraries](apis-frameworks-and-libraries)
* [Installation Info](#installation-info)
* [Setup](#setup)
* [API Instruction Documents](#api-instruction-documnets)
* [Technical Issues and Fix](#technical-issues-and-fix)
* [Unresolved Issues and Improvements](#unresolved-issues-and-improvements)

## Overview
Project milestone 1 used API's from The Movie Data Base (TMDB) and Wikipedia.

TMDB api: used to fetch movie information

Wikipedia api: used to fetch the wikipedia url searched using tmdb api's title information. 

## APIs Frameworks and Libraries 
API Used: Wikipedia, The Movie Data Base

Framework: Flask

Library: OS, Requests, JSON, Random 
    
    - OS: Provides functions for interacting with operating system 
    
    - Requests: Allow user to send HTTP request 
    
    - JSON: Converts the python dictionary into a JSON string 
    
    - Random: Generate pseudo-random numbers

## Installation Info
VS Code: 
    - Setup Overview Documnethttps://code.visualstudio.com/docs/setup/setup-overview
    - VS Code Python Extension: https://code.visualstudio.com/docs/python/python-tutorial
    - Pylint installation document: https://code.visualstudio.com/docs/python/linting

requests: pip3 install requests (run this command to install requests)


homebrew:  
(MacOS and Linux only) 
    - heombrew can be installed using: /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)" 
    - Homebrew Document: https://docs.brew.sh

heroku: 
    - For MacOS: brew tap heroku/brew && brew install heroku
    - Heroku Install Instruction: https://devcenter.heroku.com/articles/heroku-cli

## Setup
Authentication:
For the users forking the program will require to have .gitignore and .env file.
.gitignore can be specified to ignore .env file. 
.env file contains the api-key (api-key can be obtained through tmdb website)

App.py:
Contains the list of movie ids. User can create a list of movie ids.
Movie ID can be found in TMDB website url for a specific movie.
ex. "https://www.themoviedb.org/movie/438631-dune?language=en-US"
    "438631" right before is the movie ID. 
By adding movie ids, when running the program movies in the list will be randomly generated with the information

tmdb.py: 
Takes the tmdb movie ids to generate information from the api. 
Program includes poster image, title, tagline, genre and genre.
Poster Image takes the poster_path from the api and appended into the default url.
Title and taglines are the informations are fetched through movie ids.
Genre takes movie id's genre id and find that id in the dictionary and output the name of the genre. 


wikipedia.py:
Generates the URL using the title fetched from tmdb.py
Nothing needs to be done in this file, as long as the movie information is shown on the page, 
program will take care of generating the url. 

If user wants to add extra features using wikipedia api, 
user can check the instruction documents and API sandbox provided in the mediawiki. 


## API Instruction Documents
The Movie Data Base: 
Get Movie Details: https://developers.themoviedb.org/3/movies/get-movie-details 
Images: https://developers.themoviedb.org/3/getting-started/images

Wikipedia (MediaWiki): 
Main Page: https://www.mediawiki.org/wiki/API:Main_page
API Sandbox: https://www.mediawiki.org/wiki/Special:ApiSandbox

## Technical Issues and Fix
1. Homebrew: 
    When installing homebrew in terminal, it may disappear after a session. 
    During the process of installing homebrew, terminal will show two commands user can run. 
    Using the command given, homebrew can be automatically be called when opening temrinal.
2. Wikipedia API (Media Action API):
    "https://en.wikipedia.org/wiki/Special:ApiSandbox#action=query&format=json&prop=info&generator=search&formatversion=2&inprop=url&gsrsearch=Spider-Man%3A%20No%20Way%20Home"
    API Sandbox was utilized. Take the information required to generate path for generating required pages.

    Used mediawiki instructions and searches to try different types of parameter that API sandbox takes to generate differnet types of information until finding matching instructions from mediawiki page. 
    gsrsearch is replaced with response which passes the gsrsearch information and the title fetched from tmdb api. 

## Unresolved Issues and Improvements 
pylint: linting issues have not been resolved.
Black extension in VS code could be used to resolve the linting errors. 
There are other extensions available for solving linting errors. 
Autopep8 is also provided as default for VS Code

Installation of required tools and maintaining the tools.
Aside from the fixed issues, installation of tools and configuration can be tough. 
If user can take care of this in advance (unless the tools are needed later and was not aware)
it will save time and less errors to deal with. 

