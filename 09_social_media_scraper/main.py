import csv
from pathlib import Path

from bs4 import BeautifulSoup


def load_html(file_path: str):
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()
    return content


def extract_posts(soup: BeautifulSoup):
    posts = []
    post_elements = soup.find_all("div", class_="post")
    for post_element in post_elements:
        username = post_element.find("h2", class_="username").text.strip()
        content = post_element.find("p", class_="content").text.strip()
        timestamp = post_element.find("span", class_="timestamp").text.strip()
        posts.append(
            {
                "username": username,
                "content": content,
                "timestamp": timestamp,
            }
        )
    return posts


def save_posts_to_csv(posts: list[dict], file_path: str):
    with open(file_path, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=["username", "content", "timestamp"])
        writer.writeheader()
        writer.writerows(posts)


def main():
    directory = Path(__file__).parent
    html = load_html(str(directory / "social_media.html"))
    soup = BeautifulSoup(html, "html.parser")
    posts = extract_posts(soup)
    for post in posts:
        print(f"Username: {post['username']}")
        print(f"Content: {post['content']}")
        print(f"Timestamp: {post['timestamp']}")
        print("-" * 20)
    save_posts_to_csv(posts, str(directory / "social_media.csv"))


if __name__ == "__main__":
    main()
