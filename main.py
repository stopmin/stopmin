import feedparser, time

URL = "https://stopmin.tistory.com/rss"
RSS_FEED = feedparser.parse(URL)
MAX_POST = 5

markdown_text = """
## 안녕하세요!
부산대학교 정보컴퓨터공학부 22학번 정지민입니다.

## 📄 Resume
- [View My Resume on Rallit](https://www.rallit.com/resumes/65210@geemin0/%EC%A0%95%EC%A7%80%EB%AF%BC)

## GitHub Streak
[![GitHub Streak](https://streak-stats.demolab.com?user=Stopmin&theme=onedark-duo)](https://git.io/streak-stats)

## 📎 Currently Studying
- `Spring`, `Kotlin`, `Java`
- And I'm Currently Interested In Deploying

## 📝 Latest Posting
"""  # list of blog posts will be appended here

for idx, feed in enumerate(RSS_FEED['entries']):
    if idx >= MAX_POST:
        break
    else:
        feed_date = feed['published_parsed']
        markdown_text += f"- [{time.strftime('%Y/%m/%d', feed_date)} - {feed['title']}]({feed['link']})  \n"
        
with open("README.md", "w", encoding="utf-8") as f:
    f.write(markdown_text)
