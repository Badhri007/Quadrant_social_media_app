# Blog Site App

App developed by [Badhri Narayanan S](mailto:21f2000483@student.onlinedegree.iitm.ac.in) (21f2000483)

Made  using HTML, Flask, Bootstrap, Basic Javascript
____

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



- ### [/instance/site.db](/instance/site.db) - SqlLite DataBase Tables & Data
- ### [/README.md](README.md)
- ### [/requirements.txt](requirements.txt) - Packages required
- ### [/run.py](run.py) - Configuration of Application.
- ### [/CHECKLIST.md](CHECKLIST.md) - Checklist for Project Submission.
- ### [/Blog Site App Report.pdf](Blog%20Site%20App%20Report.pdf) - Project Report.


- ### [Video](https://drive.google.com/file/d/1boEqvONLUdexiOXHXMVIuSuTdxHLl67h/view?usp=share_link)-Presentation Demo of the Application