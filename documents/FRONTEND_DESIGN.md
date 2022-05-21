# Front-End Design

## File Structure
* index.html: Index Page (Color Palate Page)
* color.html: Color Combination Page
* favicon.ico: Favicon Image File
* css/: CSS File Directory
  * bootstrap.min.css: Minimized Bootstrap CSS File
* js/: Javascript File Directory
  * bootstrap.min.js: Minimized Bootstrap JS File
  * index.js: Index Page JS File
  * color.js: Color File JS File

## Page Layout

### Shared
* Navigation Header on Page Top
* Footer on Page Bottom

### Index Page
1. Users are Looking Loc Picker First
2. If User Pick Loc, Color Palate will be Printed

### Color Combination Page
* Print Picked Loc
* Print Picked Color
* Print Combinations Under the Picked Loc and Color

## HTML Code Structure

## Shared
* Page Meta Data in <head> Tag
  * <meta name="viewport"> Tag for Bootstrap CSS
  * <link rel="stylesheet"> Tag for Load Bootstrap CSS File
  * <link rel="favicon"> Tag for Load Favicon File 
  * <title> Tag for Page Title
* Shared <header> Tag
* Shared <footer> Tag
* Load Bootstrap JS and index.js File with <script> Tag

### index.html
* Main Contents in <main> Tag

### color.html
* Main Contents in <main> Tag

## JS Code Structure

### api.js
* function - isCorrectLoc(loc: string): boolean
  * check loc is correct.
  * loc must be "TOP" or "BOTTOM"
* function - fetchColorCombi(color: string, loc: string): Promise<ColorCombiData>
  * fetch color combi data from "/api/color/combi"
* type - ColorCombiData
  * JSON Object
  * {pickedColor: string, pickedLoc: string, color: Array<string>, colorCode: Array<{name: string, code: string}>}
* function - fetchColorList(): Promise<ColorListData>
  * fetch color list data from "/api/color/list"
* type - ColorListData
  * JSON Object
  * {list: Array<{top: string, bottom: string}>, colorCode: Array<{name: string, code: string}>}

### index.js

### color.js

* function - getCurrentUrl(): string
  * return current url
* function - extractQuery(url: string): Map<string, string>
  * extract query string from url
* function - isValidParam(color: string, loc: string): boolean
  * check params for fetchColor


