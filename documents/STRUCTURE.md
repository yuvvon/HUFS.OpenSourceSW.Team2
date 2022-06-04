# File Structure

* main.py: REST API 구현을 위한 Flask Router Python 메인 파일
* color.py: 색 조합 DB/함수 파일
* web/: 프론트엔드 (웹) 폴더
  * static/: Flask Static File Serving을 위한 폴더
    * index.html: 인덱스 페이지 HTML 파일 (색상 선택 페이지)
    * color.html: 색 조합 페이지 HTML 파일
    * favicon.ico: 파비콘 파일
    * css/: CSS 파일 폴더
      * bootstrap.min.css: Minimize 된 Bootstrap CSS 파일
      * shared.css: 전 페이지 공용 CSS 파일
    * js/: 자바스크립트 파일 폴더
      * bootstrap.min.js: Minimize 된 Bootstrap JS 파일
      * shared.js: 전 페이지 공용 JS 파일
      * api.js: REST API 호출을 위한 JS 파일
      * index.js: 인덱스 페이지 (index.html) JS 파일
      * color.js: 색 조합 페이지 (color.html) JS 파일
    * icons/: Bootstrap 아이콘 사용을 위한 폴더
      * bootstrap-icons.css: Bootstrap 아이콘 CSS 파일

# Back-End Code Structure

## main.py

* index_page(): "/" (인덱스 페이지)를 위한 Flask 라우터 함수
* color_page(): "/color" (색 조합 페이지)를 위한 Flask 라우터 함수
* color_combi(): REST API "/api/color/combi"를 위한 Flask 라우터 함수
* color_list(): REST API "/api/color/list"를 위한 Flask 라우터 함수
* rgb_to_hex(r, g, b): 10진수 RGB 코드를 16진수로 바꿔주는 유틸리티 함수
* make_2len_hex(hex_code): 16진수를 2글자 문자열로 formatting 해주는 유틸리티 함수

## color.py

* ColorCombination: 색 조합 정보를 전달하기 위한 Data Object Class
* combinations: 색 조합 정보를 저장하는 리스트
* check_letters(): combinations 내부의 데이터에 존재할지도 모르는 공백, 소문자를 제거해주는 함수
* compare_data(): combinations 내부에 중복되는 값을 없애주는 함수
* color_code_map: 10진수 RGB 코드를 저장해놓는 dictionary
* get_combi(where, color): 해당하는 값에 어울리는 색 조합 리스트를 가져오는 함수
* get_color_code(color): RGB 코드를 가져오기 위한 함수

# Front-End Code Structure

## index.html

* head: 뷰포트 설정, 문자코드 설정, CSS 파일 로딩 등
* body: 페이지 본체
  * header: 페이지 네비게이션 헤더
  * main: 페이지 메인 컨텐츠
    * div[id="choose-part-div"]: TOP/BOTTOM 선택
    * div[id="main-part-color-palette-div"]: 색상 선택을 위한 컬러팔레트 출력    
      -> 기본적으로는 비어있고, display="none" 상태로 출력되지 않음    
      -> index.js에서 TOP/BOTTOM 버튼 클릭시 컬러 팔레트를 생성해서 출력함
  * footer: 페이지 푸터
  * script: JS 파일 로딩

## color.html

* head: index와 동일
* body: 페이지 본체
  * header: index와 동일
  * h1[id="main-picked-title"] ~ div[id="picked-color-div"]: 선택한 색상 출력    
    -> html 파일 내부에는 색상 출력이 비어있음    
    -> color.js에서 ajax를 이용하여 API로부터 컬러코드를 fetch 후 출력함
  * div[id="combi-color-set-div"]: 색 조합 출력
    -> html 파일 내부에는 색상 출력이 비어있음    
    -> color.js에서 ajax를 이용하여 API로부터 색 조합 정보를 fetch 후 출력함
  * footer: index와 동일
  * script: JS 파일 로딩

## js/shared.js

* getElem(querySelector): document.querySelector 함수 간략화 (HTML Element 가져오는 함수)
* hideElem(elem): css display 속성을 "none"으로 바꿔 화면에서 HTML Element를 숨기는 함수
* showElem(elem): css display 속성을 "block"으로 바꿔 숨긴 HTML Element를 다시 출력하는 함수
* createSquareDiv(colorCode): 정사각형 div HTML Element를 생성하는 함수

## js/api.js

* API_ROOT: API Root URL
* API_URL: API Endpoint Path를 저장하는 Object
* fetchColorCombi(color, loc): 어울리는 색 조합을 API로부터 fetch 해오는 함수
* fetchColorList(): 전채 색 조합을 API로부터 fetch 해오는 함수

# 전체 Flow

## 인덱스 페이지
1. (프론트) 웹 브라우저에서 index 페이지 요청
2. (백엔드) main.py 에서 index_page() 함수를 통해 index 페이지 반환
3. (프론트) 받은 index 페이지 출력
4. (프론트) index.js 에서 "/api/color/list" API 호출
5. (백엔드) main.py 에서 color_list() 함수 실행
6. (백엔드) color_list() 함수 내부에서 color.py의 combinations 리스트를 불러와 전체 색 조합 반환
7. (프론트) 받은 전체 색 조합을 통해 컬러 팔레트 출력

## 색 조합 페이지
1. (프론트) 웹 브라우저에서 color 페이지 요청
2. (백엔드) main.py 에서 color_page() 함수를 통해 color 페이지 반환
3. (프론트) 받은 color 페이지 출력
4. (프론트) color.js 에서 "/api/color/combi" API 호출
5. (백엔드) main.py 에서 color_combi() 함수 실행
6. (백엔드) color_combi() 함수 내부에서 get_combi(where, color) 함수를 실행하여 맞는 색 조합 반환
7. (프론트) 받은 색 조합을 통해 색 조합 컬러 팔레트 출력