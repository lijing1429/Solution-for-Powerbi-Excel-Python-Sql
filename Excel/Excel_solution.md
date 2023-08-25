# Excel solution

All the solutions I encountered in different projects.

## 1. How to create dependent list via data validation?
[solution](https://trumpexcel.com/dependent-drop-down-list-in-excel/)
- create the related table - the list and dependent list
- create the dropdown list via `Data` - `Data validation`
- create the relationship between list and dependent list via `Formulas` - `Defined Names` - `Create from selection`
- check the relationship in the `Formulas` - `Defined Names` - `Name Manager`(**unselect 'left column' and check the name**)
- create the dependent dropdown list via `Data` - `Data validation` - `source: *=indirect(cell postion of list)*` (**change the absolute position to relatative**)

![ScreenShot](/Excel/Appendix_excel/1-1.PNG)
![ScreenShot](/Excel/Appendix_excel/1-2.PNG)
![ScreenShot](/Excel/Appendix_excel/1-3.PNG)
![ScreenShot](/Excel/Appendix_excel/1-4.PNG)

## 2. How to creat a totally blank sheet?
- unselect Gridlines via `View` - `Show`

![ScreenShot](/Excel/Appendix_excel/2-1.PNG)

## 3. How to define the chart title by the specific cell value?
- select chart title, then input `=cell`

![ScreenShot](/Excel/Appendix_excel/3-1.PNG)

## 4. Contiditional format cell based on the comparision with the other cell?
- `Conditional formatting` - `New rule` - `Format only cells that contain`

![ScreenShot](/Excel/Appendix_excel/4-1.PNG)
![ScreenShot](/Excel/Appendix_excel/4-2.PNG)

## 5. Sumifs using if to filter different information
- Using **blank range** and **blank column** to filter
![ScreenShot](/Excel/Appendix_excel/5-1.PNG)

## 6. Setting up/down arrow
- Home - **Conditional formatting** - Manage rules - New rule - Format style - icon sets - choose **type** as **number**
![ScreenShot](/Excel/Appendix_excel/6-1.PNG)

## 7. Add line above/inside the specific bar as targets
- **Change chart type** as **line** - Right click **Format Data Point** - change **Line** to **No line** - Change **Marker** as **Built in** - Change **Size**

[Reference](https://www.ablebits.com/office-addins-blog/add-line-excel-graph/)

![ScreenShot](/Excel/Appendix_excel/7-1.PNG)

## 8. Vlookup return multiple values vertically? 

- Also using it to create the **independent list**
- Find **D2** in range **A2:A11**, then return all the match rows in **B2:B11**

```
=IFERROR(INDEX($B$2:$B$11,SMALL(IF($D$2=$A$2:$A$11,ROW($A$2:$A$11)-ROW($A$2)+1),ROW(1:1))),"")
 ```

[Reference](https://www.statology.org/index-match-return-multiple-values-vertically/)

![ScreenShot](/Excel/Appendix_excel/8-1.PNG)

## 9. Vlookup return multiple values in same cells? 

- Find **D2** in range **A2:A20**
- Return all the match rows in **B2:B20**
- **TEXTJOIN** all the return values together

```
=TEXTJOIN(", ",TRUE,IF(D2=$A$2:$A$20,$B$2:$B$20,""))
```

[Reference](https://trumpexcel.com/multiple-lookup-values-single-cell-excel/)

![ScreenShot](/Excel/Appendix_excel/9-1.PNG)

## 10. How to add in Power Pivot in Excel?