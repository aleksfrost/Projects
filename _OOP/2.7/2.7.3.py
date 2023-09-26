class Notebook:
    def __init__(self, notes: list):
        self._notes = notes

    @property
    def notes_list(self):
        i = 0
        for note in self._notes:
            i += 1
            print(f'{i}.{note}')



note = Notebook(['Buy Potato', 'Buy Carrot', 'Wash car'])
note.notes_list