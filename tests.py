import pytest

from main import BooksCollector

# Создаем фикстуру для инициализации класса перед каждым тестом
@pytest.fixture
def books_collector():
    return BooksCollector()

# Тест на добавление новой книги
def test_add_new_book(books_collector):
    books_collector.add_new_book("Книга 1")
    assert "Книга 1" in books_collector.get_books_genre()

# Тест на добавление книги с неправильной длиной названия
def test_add_new_book_invalid_length(books_collector):
    books_collector.add_new_book("Книга с очень длинным названием, которое не влезает")
    assert "Книга с очень длинным названием, которое не влезает" not in books_collector.get_books_genre()

# Тест на установку жанра книги
def test_set_book_genre(books_collector):
    books_collector.add_new_book("Книга 2")
    books_collector.set_book_genre("Книга 2", "Фантастика")
    assert books_collector.get_book_genre("Книга 2") == "Фантастика"

# Тест на получение списка книг с определенным жанром
def test_get_books_with_specific_genre(books_collector):
    books_collector.add_new_book("Книга 3")
    books_collector.set_book_genre("Книга 3", "Ужасы")
    books_collector.add_new_book("Книга 4")
    books_collector.set_book_genre("Книга 4", "Ужасы")
    books_collector.add_new_book("Книга 5")
    books_collector.set_book_genre("Книга 5", "Комедии")
    assert books_collector.get_books_with_specific_genre("Ужасы") == ["Книга 3", "Книга 4"]

# Тест на получение книг для детей
def test_get_books_for_children(books_collector):
    books_collector.add_new_book("Книга 6")
    books_collector.set_book_genre("Книга 6", "Детективы")
    books_collector.add_new_book("Книга 7")
    books_collector.set_book_genre("Книга 7", "Фантастика")
    assert books_collector.get_books_for_children() == ["Книга 7"]

# Тест на добавление и удаление книги в избранное
def test_add_and_delete_book_in_favorites(books_collector):
    books_collector.add_new_book("Книга 8")
    books_collector.set_book_genre("Книга 8", "Фантастика")
    books_collector.add_book_in_favorites("Книга 8")
    assert "Книга 8" in books_collector.get_list_of_favorites_books()
    books_collector.delete_book_from_favorites("Книга 8")
    assert "Книга 8" not in books_collector.get_list_of_favorites_books()

# Параметризированный тест на добавление книги в избранное с неправильным жанром
@pytest.mark.parametrize("genre", ["Мультфильмы", "Комедии"])
def test_add_book_in_favorites_invalid_genre(books_collector, genre):
    books_collector.add_new_book("Книга 9")
    books_collector.set_book_genre("Книга 9", genre)
    books_collector.add_book_in_favorites("Книга 9")
    assert "Книга 9" in books_collector.get_list_of_favorites_books()

# Параметризированный тест на добавление книги с некорректным названием
@pytest.mark.parametrize("invalid_name", ["", "A" * 41])
def test_add_new_book_invalid_name(books_collector, invalid_name):
    books_collector.add_new_book(invalid_name)
    assert len(books_collector.get_books_genre()) == 0


# Тест на установку жанра для несуществующей книги
def test_set_genre_for_nonexistent_book(books_collector):
    books_collector.set_book_genre("Книга 10", "Фантастика")
    assert books_collector.get_book_genre("Книга 10") is None

# Тест на установку недопустимого жанра для книги
def test_set_invalid_genre(books_collector):
    books_collector.add_new_book("Книга 11")
    books_collector.set_book_genre("Книга 11", "Драма")
    assert books_collector.get_book_genre("Книга 11") == ''

# Тест на получение списка избранных книг
def test_get_list_of_favorites_books(books_collector):
    books_collector.add_new_book("Книга 12")
    books_collector.set_book_genre("Книга 12", "Фантастика")
    books_collector.add_new_book("Книга 13")
    books_collector.set_book_genre("Книга 13", "Ужасы")
    books_collector.add_book_in_favorites("Книга 12")
    books_collector.add_book_in_favorites("Книга 13")
    assert books_collector.get_list_of_favorites_books() == ["Книга 12", "Книга 13"]

# Тест на удаление несуществующей книги из избранного
def test_delete_nonexistent_book_from_favorites(books_collector):
    books_collector.delete_book_from_favorites("Книга 14")
    assert books_collector.get_list_of_favorites_books() == []

# Тест на добавление книги в избранное несколько раз
def test_add_book_in_favorites_multiple_times(books_collector):
    books_collector.add_new_book("Книга 15")
    books_collector.set_book_genre("Книга 15", "Фантастика")
    books_collector.add_book_in_favorites("Книга 15")
    books_collector.add_book_in_favorites("Книга 15")
    assert len(books_collector.get_list_of_favorites_books()) == 1

# Тест на получение списка книг для детей без установленных жанров
def test_get_books_for_children_no_genre(books_collector):
    books_collector.add_new_book("Книга 16")
    books_collector.add_new_book("Книга 17")
    books_for_children = books_collector.get_books_for_children()
    assert [] == books_for_children


# Тест на получение пустого списка книг для детей при наличии запрещенных жанров
def test_get_books_for_children_with_forbidden_genre(books_collector):
    books_collector.add_new_book("Книга 18")
    books_collector.set_book_genre("Книга 18", "Ужасы")
    books_for_children = books_collector.get_books_for_children()
    assert len(books_for_children) == 0
