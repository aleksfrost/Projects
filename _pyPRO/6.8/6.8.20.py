from collections import Counter


def print_bar_chart(data: [list[str], str], mark: str) -> None:
    max_len = len(max(data, key=len))
    res = sorted(Counter(data).items(), key=lambda x: x[1], reverse=True)
    for r in res:
        print(f'{r[0].ljust(max_len)} |{mark*r[1]}')


print_bar_chart('beegeek', '+')

languages = ['java', 'java', 'python', 'C++', 'assembler', 'java', 'C++', 'C', 'pascal', 'C++', 'pascal', 'java']

print_bar_chart(languages, '#')