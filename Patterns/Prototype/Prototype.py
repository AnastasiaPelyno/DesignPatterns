from abc import ABC, abstractmethod
import copy


class Prototype(ABC):
    @abstractmethod
    def clone(self):
        pass


class Chapter:
    def __init__(self, title: str, pages: int):
        self.title = title
        self.pages = pages

    def __str__(self):
        return f"«{self.title}» ({self.pages} стор.)"


class Book(Prototype):
    def __init__(self, title, author, genre, pages, isbn, chapters: list = None, cover="м'яка", price=0.0):
        self.title = title
        self.author = author
        self.genre = genre
        self.pages = pages
        self.cover = cover
        self.price = price
        self.chapters = chapters or []
        self.__isbn = isbn
        self.__editor_note = None

    def clone(self):
        return copy.deepcopy(self)

    def set_editor_note(self, note: str):
        self.__editor_note = note

    def get_editor_note(self):
        return self.__editor_note

    def get_isbn(self):
        return self.__isbn

    def set_isbn(self, isbn: str):
        self.__isbn = isbn

    def __str__(self):
        chapters_str = (
            "\n             ".join(str(c) for c in self.chapters)
            if self.chapters else "—"
        )
        return (
            f"  Назва      : {self.title}\n"
            f"  Автор      : {self.author}\n"
            f"  Жанр       : {self.genre}\n"
            f"  Сторінок   : {self.pages}\n"
            f"  Обкладинка : {self.cover}  |  Ціна: {self.price} грн\n"
            f"  ISBN       : {self.__isbn}\n"
            f"  Розділи    : {chapters_str}"
        )


chapters = [
    Chapter("Розділ 1", 50),
    Chapter("Розділ 2", 40),
    Chapter("Розділ 3", 120),
    Chapter("Розділ 4", 240),
]

book = Book(
    title="Дослідження операцій",
    author="Михайло Бартіш",
    genre="Наукова література",
    pages=450,
    isbn="123-4567890123",
    chapters=chapters,
    cover="м'яка",
    price=320.0,
)
book.set_editor_note("Перевірити формули у розділі 3")

# Клон 1 — тверда обкладинка
book_hardcover = book.clone()
book_hardcover.cover = "тверда"
book_hardcover.price = 480.0

# Клон 2
book_next = book.clone()
book_next.title = "Дослідження опреацій: Частина 2"
book_next.set_isbn("123-4567890456")
book_next.price = 340.0
book_next.chapters[0].title = "Розділ"
book_next.chapters.append(Chapter("Розділ 5", 18))
book_next.pages=468

separator = "─" * 44

print(f"\n{'═' * 44}")
print("Видавнича серія «Дослідження операцій»")
print(f"{'═' * 44}")

print(f"\nПРОТОТИП\n{separator}")
print(book)

print(f"\nКЛОН 1 — тверда обкладинка\n{separator}")
print(book_hardcover)

print(f"\n КЛОН 2 — продовження\n{separator}")
print(book_next)

