posts = []

def analyze_post(data):
    word_count = len(data.content.split())

    if word_count < 5:
        category = "Short"
    elif word_count < 15:
        category = "Medium"
    else:
        category = "Long"

    post = {
        "id": len(posts) + 1,
        "title": data.title,
        "content": data.content,
        "word_count": word_count,
        "category": category
    }

    posts.append(post)
    return post


def get_posts():
    return posts