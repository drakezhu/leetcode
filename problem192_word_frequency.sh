
#tr 用来重新输出单词，-cs指的是用换行符来替代非字母的字符
#uniq用来把（相邻）重复的合并并且计数
#sort -nr是按数字大小反向排序
tr -cs '[a-z]' "\n" < words.txt | sort | uniq -c | sort -nr | awk '{print $2, $1}'
