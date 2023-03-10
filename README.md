# Film Crew todolist

This is the final resubmission of the project found here https://github.com/Tylerdevries/ToDoApp, please refer to this repository for user stories and commits outlining the progression of the main project. 
This repository houses an augmented version with changes made to failed criteria. 
Changes made include crediting the walkthrough used for the basis of the project, having a fixed focus for the use of the project and an updated readme to match new version of project. No changes were made to passing criteria.

The goal of this site is to allow individual users working on a film crew to sign in as their role to create a fully amendable todolist where they can track tasks working on a given film project. 

Users of this site will be able to register their role from the login page. Once registered they can sign in and view their own data which will be saved via a postgresql database.

The site is targeting towards use for individuals working on a film project in college or for broader production.

![director tasks](https://user-images.githubusercontent.com/93283135/216874880-b783a051-6cb3-40f5-92c0-d04a6f4d6d80.PNG)



## Features:


### General Navigation:

I Designed the site with UX in mind.

Users are initially directed to a login page where they can sign in using a username(which would be a role in the production of the film) and password or use a register redirect to sign up for the app.

New users will be directed to a register page where there will be three fields for them to fill out, Username, password and password confirmation. 

Users that have either logged in or registered will be directed to the home page. Here they will have a multitude of options including logout, create task and search.

Returning users can delete or update alreaady created tasks.

The site has been styled using CSS in a main.html file which in pulled from in all other template files. 

![film login](https://user-images.githubusercontent.com/93283135/216874903-120f81c3-e96c-408d-80e7-b5bded8cfe9d.PNG)

![login view](https://user-images.githubusercontent.com/93283135/192444694-a841206d-cc1b-4fa8-9dad-c5098230c10c.PNG)


### The Login Page:

The login page is the first page shown to a user that isn't logged in.

It asks the user for a username and password. Djangos built in class for login authorization will validate the information given through the database.

Below the login button, users can register for the app by follow the link titled register. 

A screenshot of the view for this page is shown above. This view is called on within the urls.py file and is tested on in the test.py file. 

![Register role](https://user-images.githubusercontent.com/93283135/216874931-69401fda-a763-4dcc-ae67-cbcb5116b872.PNG)
![registerview](https://user-images.githubusercontent.com/93283135/216874953-aafa2a7b-77e5-4626-a6da-8c7477aa3302.PNG)




### Register Page:

Here the user can sign up for the app.

Upon sign up completion the user is redirect to the home page.

The view used here is displayed above. This confirms authorisation and adds the user to the database. 

This view is called on within the urls.py file and is tested on in the test.py file. 

![task list](https://user-images.githubusercontent.com/93283135/192447656-8253d6d1-f0a1-434c-943f-5071d2153a83.PNG)


### The Home Page:

The home page shows all available features to the user in a comprehensive list.

Here the user can logout using the link in the top right corner of the app. This link will redirect the user back to the login page. 

The header at the top of the page is styled to welcome the user by their role in the production and tell them how many incomplete tasks they remaining in their todo list.

The search bar is below this and uses the django search feature to search the users todo list. The view interprets strings typing into the search and searches for tasks contains these strings within their name.

To the right of the search bar is a plus button which when pressed will redirect the user to an empty form where the user can create a new task.

Below these two features is the list of todos. Here the user can see what todos are completed and what are pending via the styling. 

If the user clicks on the task from the shown list it will redirect them to the form with the task information. 

The X button features on the task will redirect the user to a delete confirmation page. 

Above is the view for the functioning of this page.

This view is called on within the urls.py file and is tested on in the test.py file. 

![task descriptioin](https://user-images.githubusercontent.com/93283135/216875971-aae5ebcc-423e-4e36-a16a-9c48ce2813a5.PNG)

### The Task Creation Form:

This is the page the user is directed to when clicking on the plus symbol on the home page.

Here the user can title their task and leave a description that can be seen when the task is opened. 

Upon submitting the information the task is added to the home page and the user is returned to it.

The user can return to the home page by clicking the back link at the top left of the page. 

Above is the view for the functioning of this page.

![dop screen](https://user-images.githubusercontent.com/93283135/216877117-fb70324e-fc53-40b7-815b-f2dd0e307c02.PNG)

![delete screen](https://user-images.githubusercontent.com/93283135/216875979-a05bd43a-bb4b-4708-b090-392b03fd555d.PNG)
![task updates and delete](https://user-images.githubusercontent.com/93283135/216875990-9fbc3c0b-8830-4f2d-a738-a595267cd6e6.PNG)



### Delete and Update Task: 

The delete page shown above appears when the user clicks on the X icon alongside a task.

Here the user is prompted to confirm that they wish to delete the task. 

I added a confirmation page as a new user could accidentally press this button and this could lead to poor user experience.

The edit page shown above is shown when the user clicks on the name portion of a task.

Here the user is shown what was previously filled out in these fields including and can make changes which will reflect on the home page. 

Above is the views for the functioning of these pages.

## Testing

![testing the views](https://user-images.githubusercontent.com/93283135/216876166-13caa104-96bd-41e8-8d58-8f106e8e4265.PNG)


I used the included django testing functions to test my views.

I tested the responses of each of the major views as seen above. 

## Major Errors in Development

### Solved Bugs

An initial issue I ran into with working with the most recent build of django was a crsf token issue when loading the homepage.

I fixed this by amending the setting.py file and adding CSRF_TRUSTED_ORIGINS = [
    (https://tylertodo.herokuapp.com)
]

I also ran into an issue when deploying my app to heroku. The issue was that the push to heroku main would failed due to the organising of my files and folders.

I solved this by moving all files and folders to the root directory of the main repo and adding a Procfile prior to pushing.

I also reverted to python-3.9.14 to solve this issue. 

### Unfixed Bugs

No unfixed bugs

## Deployment

The site was deployed through Heroku. 

I used the following steps to deploy my page:
1. I moved all files and folders to the main root.
2. I installed gunicorn and dj-database-url.
3. I logged into my installed heroku within the repo terminal.
4. I created a new heroku app linking the repo to my heroku account.
5. I created a new ElephantSQL Database and linked it and cloudinary to my repo for use.
6. I pushed all these changes to github and made my first deployment to heroku
7. Created the Environment Variables within setting.py and env.py, gitpod workspaces and heroku.
8. Hid the SECRET_KEY

The livelink can be found here https://filmcrewtodo.herokuapp.com/

## Credits

The prior two walkthroughs in this module of the course. 

I used the following sites as sources and tutorials for django components.

https://stackoverflow.com/

https://ccbv.co.uk/projects/Django/4.0/

https://www.youtube.com/watch?v=llbtoQTt4qw&t=3511s

