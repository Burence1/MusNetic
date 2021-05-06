# MusNetic

## Authors
 [Burens Omondi](https://github.com/Burence1)
 [Alvynah Wabwoba](https://github.com/alvynah)
 [Paul Ngigi](https://github.com/Paul-Ngigi)
 [Evance Barracks]()
 


# Description
This is a flask application that allows users to search and listen to their favourite music previews.
Users are granted permissions to save their favourite songs to a playlist after signing in to the site.



## User Story

1. As a user, I would like to search for music tracks of my choice.
2. As a user, I would like to listen to a preview a the song of my choice.
3. As a user, I would like to view the top songs.
4. As a user, I would like to add songs to my playlist.
5. As a user, I would like sign up for an account successfully.
6. As a writer, I would also like to get a welcome email after signing up.
7. As a writer, I would like to sign in to the page.


## Behaviour Driven Development (BDD)

### WRITERS

1. Sign Up

|Behaviour 	           |    Input 	                 |       Output          |
|----------------------------------------------|:-----------------------------------:|-----------------------------:|       
| Select sign up from the navigation bar    | Email, Username, Password|   Writer is redirected to log in page   |  


2. Log in

|Behaviour 	           |    Input 	                 |       Output          |
|----------------------------------------------|:-----------------------------------:|-----------------------------:|       
| Select login from the navigation bar / actions that redirect to login    | Email, password |  Writer is authenticated and redirected to landing page|  


3. Search for a song

|Behaviour 	           |    Input 	                 |       Output          |
|----------------------------------------------|:-----------------------------------:|-----------------------------:|       
| User search for a song in the search form    | Title, Preview| User is redirected to the song or songs they have searched for  |  


4. Play song review

|Behaviour 	           |    Input 	                 |       Output          |
|----------------------------------------------|:-----------------------------------:|-----------------------------:|       
| Click on the play icon to play the preview  | play preview|  The song preview is played in an iframe   |  

5. Edit Post

|Behaviour 	           |    Input 	                 |       Output          |
|----------------------------------------------|:-----------------------------------:|-----------------------------:|       
| Click on the like icon to like songs   | like| The songs liked are added to your playlist   |  




## Setup/Installation Requirements
### Getting the code
1. clone repository
    https://github.com/Burence1/MusNetic.git
    
2. Move to the folder and install requirements
    cd MusNetic
    python3.9 -m venv virtual
    source virtual/bin/activate
    pip install -r requirements.txt
### Running the Application
1. Run main application
   * Change in manage.py create_app('development')
   * python3.9 manage.py server
   * Run http://127.0.0.1:5000/
2. Run tests
    * Change in manage.py create_app('test')
   * python3.9 manage.py test

## Technologies Used

* PostgreSQL
* Flask framework
* Python3.9
* Bootstrap
* CSS
* HTML

## Contact Information
For any further inquiries or contributions or comments, reach us at musnetic65@gmail.com
### License
[MIT License]
