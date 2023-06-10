# 3. Написать регулярное выражения, для нахождения навыков программирования из данного списка слов
import re

titles = [
    "Middle JavaScript Developer",
    "Middleee JavaScript Developer (AngularJS 9)",
    "Middle JavaScript Developer (React)",
    "Seniorrr JavaScript Developer (Angular)",
    "middle JavaScript angularjs "
]

# Навыки которые мы должны найти: javascript, angularjs, react, node js, node.js, nodejs
# При этом регистр не имеет значения, то есть angularjs и Angularjs - должно рассматриваться одинаково

# 1. 
for key in titles: 
    print(re.findall(key, 'javascript, angularjs, react, node js, node.js, nodejs', flags=re.IGNORECASE)) 

