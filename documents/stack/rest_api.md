# REST API
* "Representational State Transfer"의 약자.
* HTTP를 이용하여 데이터를 주고받기 위한 방법 중 하나.

## 구성
* 자원 (Resource) - URI
* 행위 (Verb) - HTTP Method
* 표현 (Representations) - html 파일, json, xml 등등등...

### URI란?
* "Uniform Resource Identifier"의 약자.
* 쉽게 말하면 우리가 평소에 사용하는 인터넷 주소임.

```
URI는 아래와 같이 구성됨
scheme:[//[user[:password]@]host[:port]][/path][?query][#fragment]

scheme - 프로토콜을 의미함
user, password - 말 그대로 사용자의 이름과 비밀번호. (웹상에서는 보통 사용하지 않음)
host - 주소.
port - 포트. 생략하는경우 해당 프로토콜의 기본 포트를 이용.
path - 경로.
query - 쿼리스트링을 의미. 아래에서 추가로 설명함.
fragment - 서브리소스 식별자.
           나무위키 등에서 주소 끝에 #부제목 같은거 붙어있는 경우,
           해당 부제목으로 바로 이동하는것이 그 예시.


예시
https://github.com/jhchoi123/HUFS.OpenSourceSW.Team2 라는 URI가 있음
 -> https는 scheme에 해당함. https 프로토콜을 이용해서 통신한다는 의미.
 -> github.com는 host에 해당함. github.com에 접속한다는 의미.
 -> port는 생략되었기 때문에, https 프로토콜의 기본 포트인 443번 포트를 이용하게 됨.
    참고로 http의 기본 포트는 80번, https의 기본 포트는 443번임.
    더 자세히는 well-known port를 구글에 검색해보기.
 -> jhchoi123/HUFS.OpenSourceSW.Team2는 path를 의미함.
    github.com이라는 서버에 있는 jhchoi123/HUFS.OpenSourceSW.Team2 페이지로 이동한다는 의미.


쿼리스트링이란?
네이버나 구글에 검색을 하면, 프로토콜://호스트/경로 말고도,
뒤에 ?a=123&b=345&c=789 같은 이상한 문자열이 붙어있음.
우리가 검색을 할 때 서버측에 우리가 검색하고싶은 단어를 보내줘야 서버 측에서 검색 결과를 보내줄텐데,
이 단어를 서버측에 어떻게 보내줄까? 의 답이 바로 이 쿼리스트링임.
(쿼리스트링 말고도 request body를 이용하는 방법도 있지만 이건 지금은 필요 없음.
궁금하면 http request post body를 검색해볼것)

"?"는 쿼리스트링이 존재한다는것을 알리기 위한 접두사
"&"는 쿼리스트링이 여러개인 경우 쿼리스트링끼리 나누기 위한 접두사
이를 알고 ?a=123&b=345&c=789 를 봐보면
key=value 꼴인것을 확인할 수 있음.
위의 쿼리스트링을 분석하면
a의 값은 123, b의 값은 345, c의 값은 789 라는 뜻임.
```

### HTTP Method란?
우리가 웹 사이트에서 페이지를 이동할 때,    
사실은 그냥 이동하는것이 아닌 내부적으로 다른 방법으로 이동함.    
이 방법이 바로 HTTP Method임.    

HTTP Method에는 여러가지가 있지만, 우리가 알아야 하는 것은 아래의 5종류임.
* GET: 리소스를 "받아오기만" 할 때 이용
* POST: 서버로 데이터를 "전송" 할 때 이용
* PUT: 리소스를 "변경" 하거나 "생성" 할 때 이용
* PATCH: 리소스를 "부분적으로 변경" 할 때 이용
* DELETE: 리소스를 "삭제" 할 때 이용

그 중 우리가 실제로 이용하는것은 GET 하나뿐임.      
따라서 나머지는 스스로 찾아보시길.
참고로 우리가 일반적으로 사이트를 이동할 때,     
혹은 주소창에 주소를 쳐서 바로 이동할 때는 99% GET을 이용함.


### Representation?
그냥 우리가 URI로 HTTP Method를 이용하여 request를 보냈을 경우,     
그것에 대한 response가 Representation임.