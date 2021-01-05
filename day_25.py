public_key_card = 5099500
public_key_door = 7648211
subject_number_card = public_key_card
subject_number_door = public_key_door


def loop(number, subject_number, maximum=20201227):
    return (number * subject_number) % maximum


def find_initial_subject_number(public_key):
    initial_subject_number = 7
    subject_number = 1
    loop_size = 0
    while subject_number != public_key:
        loop_size += 1
        subject_number = loop(subject_number, initial_subject_number)
    return initial_subject_number, loop_size


initial_subject_number_card, loop_size_card = find_initial_subject_number(public_key_card)
initial_subject_number_door, loop_size_door = find_initial_subject_number(public_key_door)

n = 1
for i in range(loop_size_door):
    n = loop(n, subject_number=public_key_card)
print(n)
