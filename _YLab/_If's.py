my_age: int = 19
my_gender: str = 'male'
if all((
    my_age >= 18,
    my_gender == 'male'
)):
    print('Взрослый')
elif all((
    my_age >= 18,
    my_gender == 'female'
)):
    print('Взрослая')
else:
    print('В каком роде к вам обращаться?')