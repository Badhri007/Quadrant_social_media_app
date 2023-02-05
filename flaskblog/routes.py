import os
import secrets
from xml.etree.ElementTree import Comment
from PIL import Image
from flask import render_template, url_for, flash, redirect, request,abort
from flaskblog import app, db, bcrypt
from flaskblog.forms import RegistrationForm, LoginForm, UpdateProfileForm,PostForm,SearchForm
from flaskblog.models import User, Post,Comment,Like,Follow
from flask_login import login_user, current_user, logout_user, login_required



@app.before_first_request
def create_tables():
     db.create_all()



@app.route("/")
@app.route("/home")
def home():
    page=request.args.get('page',1,type=int)
    posts=Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=4)
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/account/followers")
def followers():
    followers=Follow.query.filter_by(UserName=current_user.username).all()
    followers_list=[each.FollowedBy for each in followers]
    print(current_user)
    return render_template('followers.html', title='Followers',followers_list=followers_list)

@app.route("/account/following")
def following():
    following=Follow.query.filter_by(FollowedBy=current_user.username).all()
    followers_list=[each.UserName for each in following]
    print(current_user)
    return render_template('following.html', title='Following',followers_list=followers_list)




@app.route("/feed")
def feed():
    following=Follow.query.filter_by(FollowedBy=current_user.username).all()
    followers_list=[each.UserName for each in following]
    posts=Post.query.order_by(Post.date_posted.desc())
    return render_template('feed.html', title='Feed',followers_list=followers_list,posts=posts)



@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))


def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path, 'static/profile_pics', picture_fn)

    output_size = (125, 125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)

    print("picture saved")
    return picture_fn


@app.route("/account", methods=['GET', 'POST'])
@login_required
def account():
    form = UpdateProfileForm()
   
    if form.validate_on_submit():
        print(form.picture.data)
        if form.picture.data:
            picture_file = save_picture(form.picture.data)
            current_user.image_file = picture_file
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash('Your account has been updated!', 'success')
        return redirect(url_for('account'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
    image_file = url_for('static', filename='profile_pics/' + current_user.image_file)
    return render_template('account.html', title='Account',
                           image_file=image_file, form=form)






def save_meme(form_meme):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_meme.filename)
    meme_fn = random_hex + f_ext
    meme_path = os.path.join(app.root_path, 'static/meme_pics', meme_fn)
    output_size = (500,500)
    i = Image.open(form_meme)
    i.thumbnail(output_size)
    i.save(meme_path)
    return meme_fn


@app.route("/post/new", methods=['GET', 'POST'])
@login_required
def new_post():
    form=PostForm()
    if form.validate_on_submit():
        print("-----------")
        print(form.meme_file.data)
        if form.meme_file.data:
            meme_file = save_meme(form.meme_file.data)
            post=Post(title=form.title.data,content=form.content.data,meme_file=meme_file,author=current_user)
            db.session.add(post)
            db.session.commit()
            flash('Your Post is added to Blogs','success')
            return redirect(url_for('home'))
        else:
            post=Post(title=form.title.data,content=form.content.data,author=current_user)
            db.session.add(post)
            db.session.commit()
            flash('Your Post is added to Blogs','success')
            return redirect(url_for('home'))

    return render_template('create_post.html', title='Add a Post',form=form,legend='Add a Post')



@app.route("/post/<int:post_id>",methods=['GET', 'POST'])
def post(post_id):
    post=Post.query.get_or_404(post_id)
    return render_template('post.html',title=post.title,post=post)


@app.route("/post/<int:post_id>/update",methods=['GET', 'POST'])
@login_required
def update_post(post_id):
    post=Post.query.get_or_404(post_id)
    if post.author == current_user or (current_user.username=='admin' and current_user.email=='admin@blog.com'): 
        form=PostForm()
        if form.validate_on_submit():
            post.title=form.title.data
            post.content=form.content.data
            if form.meme_file.data:
                post.meme_file = save_meme(form.meme_file.data)
            db.session.commit()
            flash('Your Blog gets updated','success')
            return redirect(url_for('post',post_id=post.id))
        elif request.method =='GET':
            form.title.data=post.title
            form.content.data=post.content

    elif post.author != current_user:
            abort(403)
    return render_template('create_post.html', title='Update Post',form=form,legend='Update Post')

@app.route("/post/<int:post_id>/delete", methods=['POST'])
@login_required
def delete_post(post_id):
    
    post = Post.query.get_or_404(post_id)
    likes=Like.query.filter_by(author=current_user.id,post_id=post.id).all()
    comments=Comment.query.filter_by(id=post.id).all()

    if post.author == current_user or (current_user.username=='admin' and current_user.email=='admin@blog.com'):
    
        db.session.delete(post)

        for comment in comments:
            db.session.delete(comment)

        for like in likes:
            db.session.delete(like)
       
       
       
        db.session.commit()
        flash('Your Blog has deleted successfully!', 'success')
        return redirect(url_for('home'))

    else:
        abort(403)
    
    


@app.context_processor
def layout():
    form=SearchForm()
    
    return dict(form=form)

 
# @app.route('/search',methods=["POST"])
# def search():
#     form=SearchForm()
    
#     if form.validate_on_submit():
#         post.searched=form.searched.data

#         posts=Post.query.filter(Post.content.like('%'+ post.searched +'%'))
#         t_posts=Post.query.filter(Post.title.like('%'+ post.searched +'%'))
#         t_posts=t_posts.order_by(Post.title).all()
        
#         posts=posts.order_by(Post.title).all()
#         return render_template("search.html",title='Search',form=form,searched=post.searched,posts=posts,t_posts=t_posts)
        


 
@app.route('/search',methods=["POST"])
def search():
    form=SearchForm()
    
    if form.validate_on_submit():
       searched=form.searched.data
       users = User.query.filter(User.username.like('%'+ searched +'%'))
        # users=User.query.filter(User.username.like('%'+ searched +'%'))
        # t_posts=Post.query.filter(Post.title.like('%'+ searched +'%'))
        # t_posts=t_posts.order_by(Post.title).all()
        
       users=users.order_by(User.username).all()
       return render_template("search.html",title='Search',form=form,searched=searched,users=users)






@app.route("/user/<username>")
def user_posts(username):
    page=request.args.get('page',1,type=int)
    user=User.query.filter_by(username=username).first_or_404()
    posts=Post.query.filter_by(author=user).order_by(Post.date_posted.desc()).paginate(page=page, per_page=4)
    followers=Follow.query.filter_by(UserName=username).all()
    follow_list=[]
    for each in followers:
        follow_list.append(each.FollowedBy)
    return render_template('user_posts.html', posts=posts,user=user,followers=follow_list)

@app.route("/follow/<username1>/<username2>")
def follow_user(username1,username2):
    try:
        flo=Follow(UserName=username1,FollowedBy=username2)
        db.session.add(flo)
        db.session.commit()
        return {"status":True}
    except:
        return {"status":False}

@app.route("/unfollow/<username1>/<username2>")
def unfollow_user(username1,username2):
    rows=Follow.query.filter(Follow.UserName==username1,Follow.FollowedBy==username2).all()
    print(rows)
    for row in rows:
        db.session.delete(row)
    db.session.commit()
    return {"status":True}
    
@app.route("/create-comment/<post_id>",methods=['GET','POST'])
@login_required
def create_comment(post_id):
    text=request.form.get('text')

    if text:
        post=Post.query.filter_by(id=post_id).first()
        if post:
            comment=Comment(text=text,author=current_user.id,post_id=post.id)
            db.session.add(comment)
            db.session.commit()
            flash("Successfully added comment","success")
            
        else:
            flash("Post does not exist",category="error")
    return redirect(url_for('post',post_id=post_id))




@app.route("/delete-comment/<comment_id>",methods=['GET','POST'])
@login_required
def delete_comment(comment_id):
    comment=Comment.query.filter_by(id=comment_id).first()
  
    if current_user.id ==comment.author:
            # comment=Comment(author=current_user.id,comment_id=comment.id)
            db.session.delete(comment)
            db.session.commit()
            flash(" Comment deleted Successfully ","success")
    elif  current_user.id !=comment.author :
            flash("You do not have permissions to delete this comment","danger")
    else:
            flash('Comment does not exists',"danger") 
    
    return redirect(url_for('home',comment_id=comment))



@app.route("/like-post/<post_id>",methods=['GET'])
@login_required
def like_post(post_id):
    post=Post.query.filter_by(id=post_id).first()
    like=Like.query.filter_by(author=current_user.id,post_id=post.id).first()

    if like:
            
            db.session.delete(like)
            db.session.commit()
   
    elif not like:
           like=Like(author=current_user.id,post_id=post.id)
           db.session.add(like)
           db.session.commit()
   
    else:
        flash("Post does not exist","danger")
            
        
    return redirect(url_for('post',post_id=post_id))