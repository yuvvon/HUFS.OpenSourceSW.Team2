# HUFS OpenSW Team 2 Project Repository

Demo Here: [http://hufsoss.rflxn.xyz/](http://hufsoss.rflxn.xyz/)

## 목표

* 의상 색 조합을 알려주는 사이트 구현

## 설계

### 페이지 구성

* 색을 선택하는 페이지
    * 색상 팔레트를 보여주고, 거기서 색을 선택하는 방식
* 선택한 색을 분석해서 색 조합을 알려주는 페이지

### 추가 기능

* 퍼스널 컬러 기능
* 상/하의 뿐만 아니라, 신발의 색상 조합도 알려줌

### 백엔드

#### 목표

* 색 조합 데이터를 코드로 구현
* 조합 데이터를 프론트로 보내주기 위한 REST API 구현
* html 파일 서빙 구현

#### flask 사용

```pip install flask```를 이용하여 flask 라이브러리 설치.    
해당 라이브러리를 이용하여 REST API 및 웹서버 구현

### 프론트엔드

#### 목표

* 색상 선택 페이지 구현
* 색상 조합 페이지 구현

#### bootstrap 사용

html 파일에 다음과 같은 메타 태그 추가

```html

<meta name="viewport" content="width=device-width, initial-scale=1">
<link href="css/bootstrap.min.css" rel="stylesheet">
```

html 파일의 body 태그 내에 다음과 같은 스크립트 추가

```html

<script src="js/bootstrap.min.js"></script>
```

## 일정

* 9주차: 기능 설계 및 구조 설계
* 10주차: 기술 스택 조사
* 11주차 ~ 13주차: 구현
* 14주차: 디버깅

## 개발 분담

* 프론트엔드: 최준혁, 박지영
* 백엔드: 김경식, 박윤서, 조유원

