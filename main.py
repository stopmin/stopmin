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


## Currently Studying

`Spring`, `Kotlin`, `Java`

<div style="display: flex; align-items: flex-start;">
  <img src="https://techstack-generator.vercel.app/java-icon.svg" alt="icon" width="60" height="60" />
</div>

 
## Algorithm
[![Solved.ac Profile](http://mazassumnida.wtf/api/v2/generate_badge?boj=geemin2514)](https://solved.ac/geemin2514/)
  


<!-- <img src="https://techstack-generator.vercel.app/python-icon.svg" alt="icon" width="44" height="44" /> --!>
<!-- <img src="https://techstack-generator.vercel.app/js-icon.svg" alt="icon" width="60" height="60" /> &nbsp --!>


"""  # list of blog posts will be appended here

for idx, feed in enumerate(RSS_FEED['entries']):
    if idx > MAX_POST:
        break
    else:
        feed_date = feed['published_parsed']
        markdown_text += f"[{time.strftime('%Y/%m/%d', feed_date)} - {feed['title']}]({feed['link']}) <br/>\n"
        
f = open("README.md", mode="w", encoding="utf-8")
f.write(markdown_text)
f.close()