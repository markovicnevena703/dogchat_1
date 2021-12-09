
import app

comment1={
    "Text": "What time are you going?",
    "Name":"Charlie",
    "Username":"chucky",
    "Picture": "chucky.jpg"

}
comment2={
    "Text": "I'm gonna go at 7pm tonight",
    "Name":"Melba",
    "Username":"melba",
    "Picture": "melba.png"

}
comment3={
    "Text": "I love naps too",
    "Name":"Melba",
    "Username":"melba",
    "Picture": "melba.png"

}
comment4={
    "Text": "Lucky you",
    "Name":"Chucky",
    "Username":"chucky",
    "Picture": "chucky.jpg"

}

post1= {
        "PostId":1,
        "Text":"Can't wait to go to the park today!",
        "Name":"Melba",
        "Username":"melba",
        "LikeCount":["chucky"],
        "CommentCount":[comment1, comment2],
        "Picture": "melba.png"
    }
post2= {
        "PostId":2,
        "Text":"Aren't naps the best?",
        "Name":"Melba",
        "Username":"melba",
        "LikeCount":[],
        "CommentCount":[],
        "Picture": "melba.png"
    } 
post3= {
        "PostId":3,
        "Text":"I could really use a treat right now.",
        "Name":"Charlie",
        "Username":"chucky",
        "LikeCount":["melba"],
        "CommentCount":[comment3],
        "Picture": "chucky.jpg"
    }
post4={
    "PostId":4,
    "Text": "Such a lovely day today!",
    "Name": "Fido",
    "Username":"fido",
    "LikeCount":["chucky", "melba"],
    "CommentCount":[comment4],
    "Picture":"fido.jpg"
}

user1={
    "Username": "melba",
    "Name":"Melba",
    "Bio": "Paul's dog",
    "Posts":[post1, post2]
}
user2={
    "Username": "chucky",
    "Name":"Charlie",
    "Bio": "White puddle",
    "Posts":[post3]
}
user3={
    "Username": "fido",
    "Name":"Fido",
    "Bio": "Black puppy",
    "Posts":[post4]
}

    
test_posts={
    1:post1,
    2:post2,
    3:post3,
    4:post4
}

test_users=[user1, user2, user3]

def insert_post():
    new_post=app.create()
    test_posts[len(test_posts) + 1] = new_post
    for user in test_users.values():
        if (user['Username']==new_post['Username']):
            post_name="post" + len(test_posts)
            user['Posts'].append(post_name)
    

