# -*- coding: utf-8 -*-


QUOTES = ('Atrás de um Homem bem-sucedido está uma mulher cansada', 'Unidos venceremos, sozinhos caíremos')


class QuotoModel(object):

    def get_quote(self, n):
        try:
            value = QUOTES[n]
        except IndexError as error:
            value = 'Not found'
        return value


class QuoteTerminalView(object):

    def show_quote(self, quote):
        print(f'And the quote is : {quote}')

    def error(self, message):
        print(f'Error : {message}')

    def select_quote(self):
        return input('Which quote number would you like to see ?:')


class QuoteTerminalController(object):

    def __init__(self):
        self._model = QuotoModel()
        self._view = QuoteTerminalView()

    def run(self):
        valid_input = False
        while not valid_input:
            n = self._view.select_quote()
            try:
                n = int(n)
            except ValueError as error:
                self._view.error('Incorrect index "{0}"'.format(n))
            else:
                valid_input = True
        quote = self._model.get_quote(n)
        self._view.show_quote(quote)


def main():
    controller = QuoteTerminalController()
    while True:
        controller.run()


if __name__ == '__main__':
    main()
