# 这是我学习Python曾经练习的代码 #
5/10/2016 5:27:31 PM 
>CR回车 LF换行Windows/Dos CRLF \r\n
Linux/Unix LF \n
MacOS CR \r
解决方法是:打开命令行，进行设置，如果你是在Windows下开发，建议设置autocrlf为true。
2014/08/20 补充：如果你文件编码是UTF8并且包含中文文字，那还是把autocrlf设置为false，并且把所有文件转换为Linux编码（即LF\n），开启safecrlf检查

----------
### 5/10/2016 6:05:10 PM  ###
- AutoCRLF
*提交时转换为LF，检出时转换为CRLF*
    git config --global core.autocrlf true
*提交时转换为LF，检出时不转换*
    git config --global core.autocrlf input

----------

**提交检出均不转换**
    **git config --global core.autocrlf false** ***<Warning's Keyword!>***

----------

- SaFeCRLF
*拒绝提交包含混合换行符的文件*
    git config --global core.safecrlf true
*允许提交包含混合换行符的文件*
    git config --global core.safecrlf false
*提交包含混合换行符的文件时给出警告*
    git config --global core.safecrlf warn