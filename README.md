# Simple Python
這是2018年中央大學數學系教授 - 吳維漢老師與物理系教授 - 林宗泰老師合開的python課程<br>
目的是要讓理學院與工學院同學對於修習微積分課程有更直覺的思維。<br>

這是講義的封面<br>
![alt text](https://github.com/YunHsiuLu/Simple_Python/blob/main/book.jpg)

在講義裡，並沒有說明如何下載，以及在各個作業系統中如何操作<br>
所以我在底下先簡單扼要地說明：<br>
[Windows](#Windows); [MacOS](#MacOs); [Linux](#Linux)

# Windows
以在windows系統中來說，使用anaconda作為練習python語言是最方便的作法。<br>
當然，網路上也能查到很多很多的做法，像是使用vscode來做開發，或是用python原生的IDE進行撰寫。<br>
這邊就先以anaconda作為範例。
## Anaconda
Anaconda是一個虛擬環境，主要是為了python一系列套件而設計，而不管是用哪個作業系統，都可以用anaconda來操作python。<br>
安裝方法非常簡單，直接去google：anaconda windows即可。[官方網站](https://www.anaconda.com/)<br>
注意，anaconda非常肥大，需要3.7GB左右，如果電腦已經太撐了吃不下去了，請另尋安裝python的辦法。
![alt text](https://github.com/YunHsiuLu/Simple_Python/blob/main/windows1.jpg)

注意！有些電腦在安裝anaconda時，會出現"這不是你電腦信任的軟體"之類的警告語，這時候你得自己想辦法去設定裡面調整電腦設定，讓你的電腦可以安裝來自網路上的軟體。（設定->應用程式與功能->選擇要從中取得應用程式的位置->選單拉開->所有位置）<br>
![alt text](https://github.com/YunHsiuLu/Simple_Python/blob/main/windows2.jpg)

接下來就一直next、agree、next、agree......（中間有一步是問你安裝的位置，如果有要更改的，請不要next，拜託）。<br>
然後等他跑綠條......（時間還蠻久的，不如就來聽首歌[愛人錯過](https://www.youtube.com/watch?v=6D79CYTxvOM)）<br>

恭喜你，跑完綠條了！你打開"開始"會看到多出了一個anaconda的資料夾（由於開著"開始"就沒有辦法截圖）<br>
裡面有：


# MacOS
雖然anaconda適用於每個作業系統，又很簡單下載安裝，但內容物實在是過於繁雜（屁股有夠大），在mac中我習慣用終端機（terminal）下載比較乾淨的套件。<br>
[Homebrew](https://brew.sh/index_zh-tw)：專門用來下載macOS package的工具，只能在terminal中使用。剛買來電腦裡面應該是沒有homebrew這個套件，所以必須要先到上面Homebrew連結找如何安裝homebrew。<br>
## Homebrew
terminal中貼上<br>
`$ /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"`

安裝完成之後，安裝python。（這邊假設是要安裝python 3.10版本，如果未來要進行更多的版本測試，就是執行`brew install pythonX.XX`，意思是安裝python X.XX版）<br>
`$ brew install python3.10`<br>
大部分的package安裝，都會詢問你要不要安裝？然後你就要手動輸入yes or no<br>
而我們通常為了節省時間，會在brew install [package]後面加上一個參數`-y`<br>
ex. `$ brew install python3.10 -y`<br>
這個`-y`的意思是：不要問我了，我就是要安裝！當然，安全起見，初學者建議都不要加。<br>
安裝完成之後，在terminal裏面打`python3.10`後即可進入python的ide視窗。<br>
![alt text](https://github.com/YunHsiuLu/Simple_Python/blob/main/macOS_python-ide.png)
若要跳出python ide，在裡面打`exit()`即可。<br>
`>>> exit()`
在python ide裡面執行的任何指令，"等同於"自己新建立一個python file(副檔名.py)然後去執行之後的結果。差別只是"不能儲存成一個檔案"！所以通常我們都是把ide當成"測試工具"。（像是測試有沒有什麼套件、某些簡單的指令有沒有辦法成功之類的）<br>
當然，上面說要跳出python ide所執行的exit()，也是一個python的指令，做的事情就是跳出python ide。<br>

## Start your first python
### In python IDE
1. 打開terminal
2. 執行`python3.10`
3. 在IDE裡面打上`>>> print("Hello World!")`
4. IDE會回傳給你執行結果。
這邊先說，我的terminal有自己設計過，所以一定長得跟你們不一樣，可以先不用理會。
![alt text](https://github.com/YunHsiuLu/Simple_Python/blob/main/macOS_python-ide-test.png)

### First python file
這邊可能需要惡補一些terminal的指令集，我應該會再開另一個git來做terminal的各種教學吧....吧.....<br>
簡單幾個指令提供：<br>
1. `cd [路徑]`：移動到你指定的路徑。不用中括號。
2. `mkdir [資料夾名稱]`：新創建一個資料夾。不用中括號。
3. `touch [檔案名稱]`：新創建一個檔案。不用中括號。
4. `python3.10 [example.py]`：執行example.py。不用中括號。
5. `rm [檔案名稱]`：把檔案刪掉。不用中括號。
6. `rm -r [資料夾名稱]`：把資料夾刪掉。不用中括號。
如果要刪除東西刪不掉，可以加`-f`，force to remove。但要小心有沒有誤刪！<br>
**絕對不要打`rm -rf /`或是`rm *`**：*是all的意思，對你懂的。<br>
聰明的你肯定能夠把上面的東西結合起來，然後新創一個檔案->撰寫程式->執行他<br>



# Linux
