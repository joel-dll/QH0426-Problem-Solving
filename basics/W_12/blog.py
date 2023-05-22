blog_posts = [{"Photos":3, "Likes":21, "Comments":2}, {"Likes":13, "Comments":2, "Shares":1},{"Photos":5, "Likes":33, "Comments":8, "Shares":3}, {"Shares":2, "Comments":4}, {"Photos":3, "Likes":19, "Comments":7}]

total_photos = 0

for post in blog_posts:
    try:
        total_photos = total_photos + post["Photos"]
    except KeyError:
        print("Exception occured")
        pass
