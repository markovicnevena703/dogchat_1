from flask import Flask, render_template, abort, request
from data import test_posts, test_users
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
auth = HTTPBasicAuth()


users = {
    "melba": generate_password_hash("melba123"),
    "chucky": generate_password_hash("chucky123"),
    "fido": generate_password_hash("fido123")
}

@auth.verify_password
def verify_password(username, password):
    if username in users and \
            check_password_hash(users.get(username), password):
        return username


@app.route("/")
@auth.login_required
def feed():
    title = "My Feed"
    return render_template('feed.html', posts=test_posts, title=title, user=auth.current_user())

@app.route("/comments/<int:post_id>")
def comments(post_id):
    post = test_posts[post_id]
    title = "Comments"
    return render_template('comments.html', title=title, post=post)

@app.route("/create", methods=['POST'])
def create():
    post_content=request.form['post-content']
    user=auth.current_user()
    image = user +'.png'

    new_post={
        "PostId": len(test_posts)+1,
        "Text": post_content,
        "Name": user,
        "Username": user,
        "LikeCount": [],
        "CommentCount":[],
        "Picture": image
        

    }

    return new_post


# @app.route('/submit', methods=['POST'])
# def submit():
#     return 'You entered: {}'.format(request.form['post-content'])





@app.route("/profile/<string:username>")
@auth.login_required
def profile(username):
    
    for user in test_users:
        if (user.get('Username') == username):
            posts = user.get('Posts')
            current_user=user
            break
        

    return render_template('profile.html', user=current_user, posts=posts)

@app.route("/logout")
def logout():
    return abort(401)

