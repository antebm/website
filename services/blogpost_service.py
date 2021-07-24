recent_blogposts = [
    {
        "title": "Title 1",
        "author": "Author 1",
        "content": "Content 1"
    },
    {
        "title": "Silly",
        "author": "Author 2",
        "content": "Content 2"
    },
    {
        "title": "However",
        "author": "Author 3",
        "content": "Content 3"
    },
    {
        "title": "Title 4",
        "author": "Author 4",
        "content": "Content 4"
    },
    {
        "title": "Title 5",
        "author": "Author 5",
        "content": "Content 5"
    }
]

def read_blogpost(post_id: str):
    for blogpost in recent_blogposts:
        if blogpost["title"] == post_id:
            return blogpost
        
    return {
            "title": "No content",
            "author": "unknown author",
            "content": "no content"
            }

def read_recent():
    return recent_blogposts