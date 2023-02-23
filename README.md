# Social Media Blog Site App - Quadrant 

App developed by [Badhri Narayanan S]

Made  using HTML, Flask, Bootstrap, Basic Javascript
____


## Application Pics

## Home Page (All Users Posts gets displayed)
![image](https://user-images.githubusercontent.com/124488669/220834196-c76c43b2-eebe-4f62-9113-bd1b60f262dc.png)


## Add a Post
![image](https://user-images.githubusercontent.com/124488669/220834078-76f6ad4e-e519-49cb-84ef-6fad7e96e386.png)


## Post Details(User Engagement with liking and commenting on posts)
![image](https://user-images.githubusercontent.com/124488669/220833914-cf1983ff-a133-4447-81d1-90e26dd15ba3.png)


## User Dashboard & Post Updation & Deletion for Owner of Post
![image](https://user-images.githubusercontent.com/124488669/220833492-2d02395e-41c0-441d-882e-ad36798a038a.png)


## Follow & unfollow Other Users
![image](https://user-images.githubusercontent.com/124488669/220833285-dcd1abdb-7cdf-4b05-9d6a-f5efb5274fec.png)

## Dashboard has Followers and Following user
![image](https://user-images.githubusercontent.com/124488669/220832958-38c3ee67-22bf-40c1-8b7b-1ebc843efcc1.png)
![image](https://user-images.githubusercontent.com/124488669/220832983-1fcb43ab-28f6-4c91-9365-388d968a4365.png)

## Followers Post displayed in Feeds page
![image](https://user-images.githubusercontent.com/124488669/220832717-d98c57a4-0465-4b5d-8652-711c148e6050.png)

## Search for Users
![image](https://user-images.githubusercontent.com/124488669/220834389-b927dfab-2f8a-4459-8b1d-6c0a49391565.png)


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



