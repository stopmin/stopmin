import feedparser, time

URL = "https://stopmin.tistory.com/rss"
RSS_FEED = feedparser.parse(URL)
MAX_POST = 5

markdown_text = """
![waving](https://capsule-render.vercel.app/api?type=waving&height=200&text=Welcome%20to%20Stopmin%20Github👋&fontAlign=70&color=gradient&fontSize=30)

### 안녕하세요!
부산대학교 정보컴퓨터공학부 22학번 정지민입니다.

<!--[![Typing SVG](https://readme-typing-svg.demolab.com?font=Fira+Code&pause=1000&color=000000&repeat=false&width=435&height=50&lines=저는+정지민입니다😀)](https://git.io/typing-svg)
[![Top Langs](https://github-readme-stats.vercel.app/api/top-langs/?username=stopmin)](https://github.com/stopmin/github-readme-stats)-->


## GitHub Streak
[![GitHub Streak](https://streak-stats.demolab.com?user=Stopmin&theme=onedark-duo)](https://git.io/streak-stats)


## 📎 Currently Studying
`Spring`, `Kotlin`, `Java`
  
## 📝 Latest Posting
"""  # list of blog posts will be appended here

for idx, feed in enumerate(RSS_FEED['entries']):
    if idx >= MAX_POST:  # '>= MAX_POST' 사용하여 정확한 포스트 수를 맞춥니다.
        break
    else:
        feed_date = feed['published_parsed']
        # Markdown에서의 줄 바꿈 처리를 위해 라인 끝에 공백 두 개 추가
        markdown_text += f"[{time.strftime('%Y/%m/%d', feed_date)} - {feed['title']}]({feed['link']})  \n"
        
with open("README.md", "w", encoding="utf-8") as f:
    f.write(markdown_text)

