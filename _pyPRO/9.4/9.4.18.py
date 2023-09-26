def remove_marks(text, marks):
    remove_marks.__dict__.setdefault('count', 0)
    remove_marks.__dict__['count'] += 1
    res = ''.join([ch for ch in text if ch not in marks])
    return res



text = 'Hi! Will we go together?'

print(remove_marks(text, '!?'))
print(remove_marks.count)

marks = '.,!?'
text = 'Are you listening? Meet my family! There are my parents, my brother and me.'

for mark in marks:
    print(remove_marks(text, mark))

print(remove_marks.count)


