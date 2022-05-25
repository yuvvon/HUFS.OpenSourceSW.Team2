# API SPEC

## API ROOT URL

http://{나중에_완성되면_서버에_올려줄게요}/

## Endpoints

### 1. GetColorCombi

#### Path: /api/color/combi

#### Method: GET

#### Query Strings

* loc: Cloth Location
  * Type: string 
  * Value: "TOP" or "BOTTOM"
* color: Cloth Color
  * Type: string
  * Value: Key of List combination

#### Response

* pickedColor: Picked Color
  * Type: string
* pickedLoc: Picked Location
  * Type: string
* colors: List of Colors
  * Type: Array\<string\> 
* colorCode: List of Color Code
  * Type: Array\<{name: string, code: string}\>
    * name: Color Name
    * code: Color RGB Code

### 2. GetCombiList

#### Path: /api/color/list

#### Method: GET

#### Response

* list: Color Combi List
  * Type: Array\<{top: string, bottom: string}\>
    * top: Top Color
    * bottom: Bottom Color
* colorCode: Color Code List
  * Type: Array\<name: string, code: string\>
    * name: Color Name
    * code: Color RGB Code