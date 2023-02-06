# To Do App

This is the final resubmission of the project found here https://github.com/Tylerdevries/ToDoApp, please refer to this repository for user stories and commits outlining the progression of the main project. 
This repository houses an augmented version with changes made to failed criteria. 
Changes made include crediting the walkthrough used for the basis of the project, having a fixed focus for the use of the project and an updated readme to match new version of project. No changes were made to passing criteria.

The goal of this site is to allow individual users working on a film crew to sign in as their role to create a fully amendable todolist where they can track tasks working on a given film project. 

Users of this site will be able to register their role from the login page. Once registered they can sign in and view their own data which will be saved via a postgresql database.

The site is targeting towards use for individuals working on a film project in college or for broader production.

![film home](https://user-images.githubusercontent.com/93283135/216871039-d850d8f5-6ce7-49ac-a7aa-0927a4a901c0.PNG)


## Features:


### General Navigation:

I Designed the site with UX in mind.

Users are initially directed to a login page where they can sign in using a username(which would be a role in the production of the film) and password or use a register redirect to sign up for the app.

New users will be directed to a register page where there will be three fields for them to fill out, Username, password and password confirmation. 

Users that have either logged in or registered will be directed to the home page. Here they will have a multitude of options including logout, create task and search.

Returning users can delete or update alreaady created tasks.

The site has been styled using CSS in a main.html file which in pulled from in all other template files. 

![login screen](https://user-images.githubusercontent.com/93283135/192444712-e37a3582-106e-45c1-8c30-dc1ccbf2cf81.PNG)
![login view](https://user-images.githubusercontent.com/93283135/192444694-a841206d-cc1b-4fa8-9dad-c5098230c10c.PNG)


### The Login Page:

The login page is the first page shown to a user that isn't logged in.

It asks the user for a username and password. Djangos built in class for login authorization will validate the information given through the database.

Below the login button, users can register for the app by follow the link titled register. 

A screenshot of the view for this page is shown above. This view is called on within the urls.py file and is tested on in the test.py file. 

![image](https://user-images.githubusercontent.com/93283135/192445925-ff257c1b-cc91-4ac5-b761-237a9ca46e64.png)
![register code](https://user-images.githubusercontent.com/93283135/192446140-d917bbd2-f44a-48ce-b3bd-8433d7693f74.PNG)


### Register Page:

Here the user can sign up for the app.

Upon sign up completion the user is redirect to the home page.

The view used here is displayed above. This confirms authorisation and adds the user to the database. 

This view is called on within the urls.py file and is tested on in the test.py file. 

![home page](https://user-images.githubusercontent.com/93283135/192447633-f21076f7-2951-464b-96e4-5c333a9efd7b.PNG)
![task list](https://user-images.githubusercontent.com/93283135/192447656-8253d6d1-f0a1-434c-943f-5071d2153a83.PNG)


### The Home Page:

The home page shows all available features to the user in a comprehensive list.

Here the user can logout using the link in the top right corner of the app. This link will redirect the user back to the login page. 

The header at the top of the page is styled to welcome the user by their username and tell them how many incomplete tasks they remaining in their todo list.

The search bar is below this and uses the django search feature to search the users the todo list. The view interprets strings typing into the search and searches for tasks contains these strings within their name.

To the right of the search bar is a plus button which when pressed will redirect the user to an empty form where the user can create a new task.

Below these two features is the list of todos. Here the user can see what todos are completed and what are pending via the styling. 

If the user clicks on the task from the shown list it will redirect them to the form with the task information. 

The X button features on the task will redirect the user to a delete confirmation page. 

The three dots on the far right can be held and dragged to drag the tasks to rearrange the order of the list. 

Above is the view for the functioning of this page.

This view is called on within the urls.py file and is tested on in the test.py file. 


![create task](https://user-images.githubusercontent.com/93283135/192454054-921d4d9a-10ee-4966-ac9a-4ee524968424.PNG)
![create tasks](https://user-images.githubusercontent.com/93283135/192454110-8c193a54-4e95-48bb-a111-d86142cab263.PNG)


### The Task Creation Form:

This is the page the user is directed to when clicking on the plus symbol on the home page.

Here the user can title their task and leave a description that can be seen when the task is opened. 

Upon submitting the information the task is added to the home page and the user is returned to it.

The user can return to the home page by clicking the back link at the top left of the page. 

Above is the view for the functioning of this page.

This view is called on within the urls.py file and is tested on in the test.py file. 

![update](https://user-images.githubusercontent.com/93283135/192455937-e84c61f4-666a-4a06-ae0a-823c990505b7.PNG)
![update and delete](https://user-images.githubusercontent.com/93283135/192455887-9599e91d-e743-4622-a20c-162bac7c7ccc.PNG)
![delete](https://user-images.githubusercontent.com/93283135/192455952-1df19229-44a7-4a14-b6d9-ffc87c65f0da.PNG)


### Delete and Update Task: 

The delete page shown above appears when the user clicks on the X icon alongside a task.

Here the user is prompted to confirm that they wish to delete the task. 

I added a confirmation page as a new user could accidentally press this button and this could lead to poor user experience.

The edit page shown above is shown when the user clicks on the name portion of a task.

Here the user is shown what was previously filled out in these fields including and can make changes which will reflect on the home page. 

Above is the views for the functioning of these pages.

## Testing


![testing](https://user-images.githubusercontent.com/93283135/192486724-42b0fb0b-b4de-4b20-84bc-96279331ddf6.PNG)


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

I also reverted to heroku stack 20 and python-3.9.14 to solve this issue. 

### Unfixed Bugs

No unfixed bugs

## Deployment

The site was deployed through Heroku. 

I used the following steps to deploy my page:
1. I moved all files and folders to the main root.
2. I installed gunicorn and dj-database-url.
3. I logged into my installed heroku within the repo terminal.
4. I created a new heroku app linking the repo to my heroku account.
5. I created a new postgresql database on heroku and linked it to my repo for use instead of sqlite.
6. I pushed all these changes to github and made my first deployment to heroku
7. Created the Environment Variables within setting.py, gitpod workspaces and heroku.
8. Hid the SECRET_KEY

The livelink can be found here https://tylertodo.herokuapp.com/

## Credits

The prior two walkthroughs in this module of the course. 

I used the following sites as sources and tutorials for django components.

https://stackoverflow.com/

https://getbootstrap.com/

https://ccbv.co.uk/projects/Django/4.0/

https://www.youtube.com/watch?v=llbtoQTt4qw&t=3511s

