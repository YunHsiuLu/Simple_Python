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



# MacOS
雖然anaconda適用於每個作業系統，又很簡單下載安裝，但內容物實在是過於繁雜（屁股有夠大），在mac中我習慣用終端機（terminal）下載比較乾淨的套件。<br>
[Homebrew](https://brew.sh/index_zh-tw)：專門用來下載macOS package的工具，只能在terminal中使用。剛買來電腦裡面應該是沒有homebrew這個套件，所以必須要先到上面Homebrew連結找如何安裝homebrew。<br>
## Homebrew
terminal中貼上<br>
`/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"`

安裝完成之後，安裝python。（這邊假設是要安裝python 3.10版本，如果未來要進行更多的版本測試，就是執行`brew install pythonX.XX`，意思是安裝python X.XX版）<br>
`brew install python3.10`<br>
大部分的package安裝，都會詢問你要不要安裝？然後你就要手動輸入yes or no<br>
而我們通常為了節省時間，會在brew install [package]後面加上一個參數`-y`<br>
ex. `brew install python3.10 -y`<br>
這個`-y`的意思是：不要問我了，我就是要安裝！

# Linux
