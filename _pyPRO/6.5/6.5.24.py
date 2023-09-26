from collections import defaultdict


def best_sender(messages, senders):
    half_res = defaultdict(int)
    for m, s in zip(messages, senders):
        half_res[s] += len(m.split())
    res = sorted(half_res.items(), key=lambda x: (x[1], x[0]))[-1]
    return res[0]


messages = ['Hi, Linda', 'Hi, Sam', 'How are you doing?']
senders = ['Sam Fisher', 'Linda', 'Sam Fisher']

print(best_sender(messages, senders))

messages = ['How is Stepik for everyone', 'Stepik is useful for practice']
senders = ['Bob', 'Charlie']

print(best_sender(messages, senders))
