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