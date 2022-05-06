# Flask
* 파이썬 웹 프레임워크 중 하나.
* 파이썬으로 웹 애플리케이션이나 REST API 서버를 구현할 때 사용함.

## vs Django 
* 파이썬에는 Flask 말고도 Django("장고"라고 읽음)라는 웹 프레임워크가 존재함.
* 장고는 플라스크보다 기능들이 훨씬 많은 full-stack 프레임워크임.
* 반면 플라스크는 기능이 적은 마이크로 웹 프레임워크임.
* 파이썬으로 웹 애플리케이션을 구현하는 경우 "보통은" 장고를 사용함.
* 우리는 매우 간단한 REST API 구현을 목표로 하기 때문에, 훨씬 가벼운 플라스크를 이용함.

## 시작하기 전에
콘솔에 ```pip install flask```를 쳐서 flask를 다운로드 받을것.

## 기초 튜토리얼
라우트는 URI에서 path에 해당하는것을 말한다.

### 1. 기본적인 라우트 구현.
```python
from flask import Flask

app = Flask(__name__)           # flask 인스턴스 생성

@app.route("/")                 # URI가 인덱스 페이지를 가르키는 경우
def index():                    # 이 함수를 실행시키고
    return "INDEX PAGE HERE!"   # 이 리턴값을 표시한다.

if __name__ == "__main__":
    app.run()                   # flask 인스턴스를 이용하여 서버 실행
```
위의 소스코드를 실행시킨 후 http://localhost:5000로 접속하면   
INDEX PAGE HERE! 이 출력되는것을 확인할 수 있다.

### 2. html 파일 보내주기
```python
# 인스턴스 생성 생략

@app.route("/")
def index():
    with open("html_파일_경로", encoding="utf8", mode="r") as html_file:
        return html_file.read()

# 서버 실행 생략
```
위와 같이 하면 html_파일_경로 에 있는 html파일을 보내줄 수 있다.

### 3. 정적 파일 서빙
```python
app = Flask(__name__,
            static_url_path="",
            static_folder="정적_파일_폴더_위치")
```
인스턴스 생성을 위와 같이 (static_url_path="", static_folder="정적_파일_폴더_위치")로 설정하면,
정적_파일_폴더_위치 내의 파일을 자동으로 보내준다.     
아래와 같은 파일이 존재한다고 가정해보자
```
./static/test.html
./static/css/test.css
```
그리고 인스턴스 생성을 아래와 같이 했다고 가정해보자.
```python
app = Flask(__name__,
            static_url_path="",
            static_folder="./static")
```
이런 경우, 아래와 같이 된다.
```
If you send HTTP Request to "GET http://localhost:5000/test.html", 
Response will be file of "./static/test.html"

If you send HTTP Request to "GET http://localhost:5000/css/test.css", 
Response will be file of "./static/css/test.css"
```

### 4. 쿼리스트링 받아오기
```python
from flask import Flask, request

app = Flask(__name__)

@app.route("/query")
def qs_test():
    qs_a = request.args.get("a")
    qs_bc = request.args.get("bc")
    qs_def = request.args.get("def")
    
    return f"{qs_a} / {qs_bc} / {qs_def}"

# 서버 실행 생략
```
위와 같이 request를 import한 후, request.args.get 함수를 이용하면 쿼리스트링을 가져올 수 있다.    
결과는 아래와 같다.
```
If you send HTTP Request to "GET http://localhost:5000/query?a=1&bc=2&def=3",
Response will be "1 / 2 / 3"

If you send HTTP Request to "GET http://localhost:5000/query?a=ABC&bc=DEF&def=GHI",
Response will be "ABC / DEF / GHI"
```
