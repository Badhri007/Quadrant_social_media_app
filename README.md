# Social Media Blog Site App - Quadrant 

App developed by [Badhri Narayanan S]

Made  using HTML, Flask, Bootstrap, Basic Javascript
____


Application Pics

## Home Page (All Users Posts gets displayed)
![image](https://user-images.githubusercontent.com/124488669/220830686-a2743f3f-9102-4cdb-813d-76329ebd7b74.png)

##Add a Post
![image](https://user-images.githubusercontent.com/124488669/220830839-12010427-ee2c-498b-b11f-cbe3b1bdb7b9.png)

##Post Details(User Engagement)
![image](https://user-images.githubusercontent.com/124488669/220830946-5bb0fc41-1170-4af7-a562-71c16b7c8b3e.png)

##User Dashboard & Post Updation & Deletion for Owner of Post
![image](https://user-images.githubusercontent.com/124488669/220831178-b6dd140c-6011-4a5b-9015-84f525fd1747.png)

##Follow & unfollow Other Users
![image](https://user-images.githubusercontent.com/124488669/220831285-d3eeb04f-4869-4b4e-a6ff-b8f710e7a2b2.png)

##Dashboard has Followers and Following user
![image](https://user-images.githubusercontent.com/124488669/220831438-5650b8f4-e391-4a89-9e4c-5140331760ce.png)
![image](https://user-images.githubusercontent.com/124488669/220831744-e20ccd12-dbe0-4d2e-a572-1ce11c0bd721.png)

##Followers Post displayed in Feeds page
![image](https://user-images.githubusercontent.com/124488669/220831894-baddc128-f29d-4f5d-8653-d5e0f0dce04f.png)

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



