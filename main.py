import csv
f = open('seoul.csv', 'r', encoding='cp949')
data = csv.reader(f, delimiter=',')
for row in data:
    print(row)
f.close()

"""
github

echo "# main.py" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/pah0729/main.py.git
git push -u origin main

git remote add origin https://github.com/pah0729/main.py.git
git branch -M main
git push -u origin main
"""