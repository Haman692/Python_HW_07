verse = input('Стих винипуха: ')
verseList = verse.lower().split()
function = lambda x: sum(1 for i in x if i in 'аеёиоуыэюя') 
count = function(verseList[0])
if all([function(i) == count for i in verseList]):
    print('Парам пам-пам')
else:
    print('Пам парам')