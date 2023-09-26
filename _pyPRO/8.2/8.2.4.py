def traffic(n):
    def run(start):
        if start > 0:
            print('Не парковаться')
            start -= 1
            run(start)

    run(n)


traffic(3)
