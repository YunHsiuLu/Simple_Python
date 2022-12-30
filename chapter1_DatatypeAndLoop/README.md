# Data type and Loop
第一章節首先在描述有關python的資料型態<br>
跟其他程式很不一樣，python不只不用宣告變數的資料型態，還能自動將變數轉換型態。<br>
若有接觸過c/c++或是matlab這類程式語言，會發現當你想要宣告整數的變數時：<br>
```c
int a = 0;
int b = 0;
```
並且宣告完畢後，不能直接回傳不同資料型態給該變數，ex. 將字串型態回傳給整數型態（直接爆炸）：
```c
int a = 0;
a = 'abcde';
```
但在python裏面，完全沒有在管你什麼資料型態，通通幫你把屎把尿（這邊其實有點類似javascript，但js還需要宣告`auto`）：
```python
a = 0
print(a) #回傳0
a = 'abcde'
print(a) #回傳字串的abcde
```
這時你應該也有發現，python裡面並沒有像c/c++或是matlab或是java一樣的結尾符號`;`。<br>
沒錯！python是用“換行”作為結語的，若你想要換行但該行指令尚未結束，必須要在行尾加上反斜線`\`：
```python
a = 'abcdef'\
'ghijklmnop'\
'qrstuvwxyz'
print(a) #回傳a~z的字串
```

