# Измените путь к файлу

path = 'dbase.txt'


class Grades(object):

    def __init__(self):
        self.name = None
        self.member = None
        self.num_member = None

    def app_member(self, name):
        with open(path, 'a') as f:
            self.name = f.write(f'{name}\n')

    def remove_member(self, member):
        with open(path) as f:
            c = f.readlines()
            aa = 0
            for x in range(len(c)):
                s = c[x].split('|')
                for y in range(len(s)):
                    if s[y] == member:
                        c.pop(x)
                        aa = 1
                if aa == 1:
                    break

        with open(path, 'w') as f:
            self.member = f.write(''.join(c))

    def edit(self, num_item, num_member, k):
        with open(path) as f:
            c = f.readlines()
            aa = 0
            for x in range(len(c)):
                lis = c[x].split('|')
                for y in range(len(lis)):
                    if lis[y] == num_member:
                        if k == '1':
                            lis[0] = num_item
                            aa = 1
                            c.remove(c[x])
                        elif k == '2':
                            lis[-1] = num_item
                            aa = 1
                            c.remove(c[x])
                        elif k == '3':
                            lis[y] = num_item
                            aa = 1
                            c.remove(c[x])
                if aa == 1:
                    lis = '|'.join(lis).replace('\n', '')
                    c.append(lis + '\n')
                    break
            with open(path, 'w') as f:
                self.num_member = f.write(''.join(c))


def print_grades():
    with open(path) as f:
        for x in f:
            print(x.replace('|', ' '))


if __name__ == '__main__':
    while True:
        print(
            '1. Добавить ученика(Вместе с предметом и оценкой)\n',
            '2 . Изменить данные ученика\n',
            '3. Удалить все данные ученика\n',
            '4. Показать табель\n'
        )
        num = input('Какую функцию выберите(Напишите указанной цифрой)? ')
        if num == '1':
            a = int(input('Сколько людей хотите добавить? '))

            while a != 0:
                item = input('По какому предмету? ') + '|'
                Grades().app_member(name=item + input('Введите ученика: ') + '|' + input('Введите оценки(через пробел): '))
                a -= 1
        elif num == '2':

            print(
                '1. Изменить предмет у ученика\n',
                '2. Изменить оценки у ученика\n',
                '3. Изменить ученика оставив предмет и оценки\n'
            )

            num_aa = input('Введите значения: ')
            k = num_aa
            if num_aa == '1':

                print_grades()
                num_member = input('Введите ученика ')
                num_item = input('На какой предмет? ')
                Grades().edit(num_item, num_member, k)
            elif num_aa == '2':

                print_grades()
                num_member = input('Введите ученика ')
                num_item = input('Введите будущие оценки ')
                Grades().edit(num_item, num_member, k)
            elif num_aa == '3':
                print_grades()
                num_member = input('Введите ученика ')
                num_item = input('Введите второго ученика ')
                Grades().edit(num_item, num_member, k)

            else: print('Введите корректное число!')

        elif num == '3':

            print_grades()
            member = input('Укажите того, кого хотите удалить:- ')
            Grades().remove_member(member)

        elif num == '4':
            print_grades()
        else:
            print('Введите допустимое число')