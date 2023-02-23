# Social Media Blog Site App - Quadrant 

App developed by [Badhri Narayanan S]

Made  using HTML, Flask, Bootstrap, Basic Javascript
____


## Application Pics

## Home Page (All Users Posts gets displayed)
![image](https://user-images.githubusercontent.com/124488669/220835068-3f535f02-b35f-4074-b414-2e0046382e36.png)


## Add a Post
![image](https://user-images.githubusercontent.com/124488669/220835128-92a21fea-e883-43e9-b461-212dc8afc7b2.png)



## Post Details(User Engagement with liking and commenting on posts)
![image](https://user-images.githubusercontent.com/124488669/220835319-2faf309c-aec2-4829-9cf2-75e5683a25cd.png)



## User Dashboard & Post Updation & Deletion for Owner of Post
![image](https://user-images.githubusercontent.com/124488669/220835393-d19c27e1-c2bb-4c3e-b633-7a894494ab1f.png)



## Follow & unfollow Other Users
![image](https://user-images.githubusercontent.com/124488669/220835509-ad7b6f37-15a6-45ef-bba4-83ec14ccb30e.png)



## Dashboard has Followers and Following user
![image](https://user-images.githubusercontent.com/124488669/220835616-5d63943f-748a-4b92-b6bd-3139b01fa443.png)
![image](https://user-images.githubusercontent.com/124488669/220835724-6340f13c-9a0e-42a6-a19a-16b1fcf3f385.png)


## Followers Post displayed in Feeds page
![image](https://user-images.githubusercontent.com/124488669/220835806-065672bc-a9a1-4e8e-b708-45912581b4a4.png)


## Search for Users
![image](https://user-images.githubusercontent.com/124488669/220834537-f974f354-b65f-4ce7-bba7-77c49c43b018.png)


_______

## Steps to run this app
- Create a Virtual environment in the same directory
  - `python -m venv env` for Windows.
  - `virtualenv env` for Linux or MacOS.
- Activate the Virtual environment
  - `env\Scripts\activate` for Windows.
  - `source env/bin/activate` for Linux or MacOS.
- Run the app `python run.py`
- Don't forget to deactivate the Virtual environment when you're done exploring
  - `env\Scripts/deactivate` for Windows.
  - `source env/bin/deactivate` for Linux or MacOS.
___

## Folder Structure

- ### /static
  - [/main.css](static/main.css) - Stylesheet.
  - [/profile_pics](static/profile_pics) - Profile Pictures of Each User gets stored
  - [/meme_pics](static/meme_pics) - Image Upload by the User in their Blogs gets Uploaded
 
- ### /flaskblog
  - [/__init__.py](flaskblog/__init__.py) - Configuration of database.
  - [/models.py](flaskblog/models.py) - Contains Database schemas.
  - [/forms.py](flaskblog/forms.py) - Contains all user input forms of the app
  - [/routes.py](flaskblog/routes.py) - Routing Information of Functions defined 

  

- ### /templates
  - [/about.html](templates/about.html) - Template for About Us Page of APP
  - [/account.html](templates/account.html) - Template for Dashboard page.
  - [/create_post.html](templates/create_post.html) - Template for create_post page.
  - [/feed.html](templates/feed.html) - Template for feed of following user's posts will display
  - [/followers.html](templates/followers.html) - Template for followers page[Display their usernames].
  - [/following.html](templates/following.html) - Template for following page[Displays usernames followed by current_user].
  - [/home.html](templates/home.html) - Template for home page
  - [/layout.html](templates/layout.html) - Template for Layout page[Base Page contains Navbar]
  - [/login.html](templates/login.html) - Template for Login page.
  - [/post.html](templates/post.html) - Template for Post page[Particular User's Posts & Followers Count displayed]
  - [/register.html](templates/register.html) - Template for register page
  - [/search.html](templates/search.html) - Template for Search page [Displays Searched User]
  - [/user_posts.html](templates/user_posts.html) - Template for user_posts page.



- ## [/instance/site.db](/instance/site.db) - SqlLite DataBase Tables & Data
- ## [/README.md](README.md)
- ## [/requirements.txt](requirements.txt) - Packages required
- ## [/run.py](run.py) - Configuration of Application.
- ## [/CHECKLIST.md](CHECKLIST.md) - Checklist for Project Submission.



