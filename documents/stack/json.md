# JSON이란?
* JavaScript Object Notation의 약자.
* 말 그대로 자바스크립트의 오브젝트를 나타내기 위한 형식임.
```json
{
  "key1": "string value!",
  "key2": 123,
  "key3": true,
  "key4": [
    "json",
    "has",
    "array",
    "type!"
  ],
  "key5": {
    "innerKey1": "json",
    "innerKey2": "also",
    "innerKey3": "has",
    "innerKey4": "object",
    "innerKey5": "type!"
  }
}
```
위의 json 예제를 보면, `"key": "value"` 형식이며, value의 타입에는 string, number, boolean, Array, Object 이렇게 5개의 타입이 존재한다.    
쉽게 말하면, 파이썬의 딕셔너리와 거의 같다!

## JSON의 타입에 대해서

### number
* 말 그대로 숫자를 의미한다.
* integer, float, double 같은 세부적인 타입 구분 없이 정수, 실수를 모두 포함한다.

### string
* 말 그대로 문자열을 의미한다.
* 다른 언어와 마찬가지로 `"가나다"` 형식 (큰 따옴표 사용)으로 나타낸다.
* \를 이용해서 이스케이프가 가능하다.
  * \b: 개행
  * \t: 탭
  * \": 큰따옴표
  * \\: 역슬래시

### boolean
* true 혹은 false

### Array
* 배열이다.
* 배열 내부에는 number, string, boolean 외에도 또 다른 배열이나 오브젝트가 들어갈 수 있다.
* 자바스크립트는 type checking이 weak한 언어이기 때문에, 배열 내부가 꼭 같은 타입만으로 이뤄지지 않아도 된다.
```json
[
  123,
  "not number!",
  [
    "another arr"
  ],
  {
    "key": "val"
  }
]
```
위와 같이 서로 다른 타입을 원소로 가진다고 해서 문제를 일으키지는 않는다.

### Object
* 객체이다.
* "{}" (중괄호)를 이용하여 표현한다.
* 애초에 json부터 object로 이루어져 있다.

## JSON in Python
파이썬에는 json을 다루기 위한 스탠다드 라이브러리가 존재한다.    
파이썬 내부에서 `import json`으로 이용하면 된다.     
저 위에서 말한것처럼 json과 파이썬 딕셔너리는 거의 같기 때문에 json을 파이썬 딕셔너리로, 딕셔너리를 json으로 손쉽게 변환할 수 있다.


### Read JSON
```python
import json     # json 라이브러리 로드

# json 형식의 string.
# 실제로는 http를 통해서 가져오거나, 파일을 읽어와서 사용하는 경우가 많을것이다.
json_string = '''
{
    "key": "value",
    "arr": [
        123,
        456,
        789
    ],
    "obj": {
        "bool": true
    }
}
'''

json_obj = json.loads(json_string)

print(json_obj["key"])              # this will be "value"
print(json_obj["arr"][0])           # this will be 123
print(json_obj["obj"]["bool"])      # this will be True

```
위와 같이 str 오브젝트 속에 들어있는 json 형식의 문자열을 json.loads 함수에 넣어주면 파이썬 딕셔너리로 변환해준다.

### Write JSON
```python
import json

# 파이썬 딕셔너리
py_dict = {
    "hello": "world!",
    "num": 123,
    "bool": False,
    "obj": {
        "key": "val"
    }
}

json_str = json.dumps(py_dict)
```

위와 같이 파이썬 딕셔너리를 json.dumps 함수에 넣어주면, json형식의 문자열로 바꿔준다.

### 주의!
json.dumps 함수와 json.loads 함수와 비슷한 json.dump / json.load 함수가 존재한다.    
json.dump 함수는 로컬에 저장되어있는 파일을 직접 불러와 변환하는 함수이고,    
json.load 함수는 파이선 딕셔너리를 json으로 변환하여 로컬에 파일로 저장하는 함수이다.