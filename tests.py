import pytest

class TestBooksCollector:
    def test_add_new_book(self, books_collector):
        books_collector.add_new_book("Книга 1")
        assert "Книга 1" in books_collector.get_books_genre(), "Книга не добавлена"

    def test_add_new_book_invalid_length(self, books_collector):
        books_collector.add_new_book("Книга с очень длинным названием, которое не влезает")
        assert "Книга с очень длинным названием, которое не влезает" not in books_collector.get_books_genre(), "Книга с длинным наванием добавлена"

    def test_set_book_genre(self, books_collector):
        books_collector.add_new_book("Книга 2")
        books_collector.set_book_genre("Книга 2", "Фантастика")
        assert books_collector.get_book_genre("Книга 2") == "Фантастика", "Не удалось установить жанр книги"

    def test_get_books_with_specific_genre(self, books_collector):
        books_collector.add_new_book("Книга 3")
        books_collector.set_book_genre("Книга 3", "Ужасы")
        books_collector.add_new_book("Книга 4")
        books_collector.set_book_genre("Книга 4", "Ужасы")
        books_collector.add_new_book("Книга 5")
        books_collector.set_book_genre("Книга 5", "Комедии")
        assert books_collector.get_books_with_specific_genre("Ужасы") == ["Книга 3", "Книга 4"], "Не удалось получить книгу с определенным жанром"

    def test_get_books_for_children(self, books_collector):
        books_collector.add_new_book("Книга 6")
        books_collector.set_book_genre("Книга 6", "Детективы")
        books_collector.add_new_book("Книга 7")
        books_collector.set_book_genre("Книга 7", "Фантастика")
        assert books_collector.get_books_for_children() == ["Книга 7"], "Не удалось получить книгу для детей"

    def test_add_book_in_favorites(self, books_collector):
        books_collector.add_new_book("Книга 8")
        books_collector.set_book_genre("Книга 8", "Фантастика")
        books_collector.add_book_in_favorites("Книга 8")
        assert "Книга 8" in books_collector.get_list_of_favorites_books(), "Не удалось добавить книгу в избранное"

    def test_delete_book_from_favorites(self, books_collector):
        books_collector.add_new_book("Книга 8")
        books_collector.set_book_genre("Книга 8", "Фантастика")
        books_collector.add_book_in_favorites("Книга 8")
        books_collector.delete_book_from_favorites("Книга 8")
        assert "Книга 8" not in books_collector.get_list_of_favorites_books(), "Не удалось удалить книгу из избранного"

    @pytest.mark.parametrize("invalid_name", ["", "A" * 41])
    def test_add_new_book_invalid_name(self, books_collector, invalid_name):
        books_collector.add_new_book(invalid_name)
        assert len(books_collector.get_books_genre()) == 0, "Книга с некорректным названием добавлена в список"

    def test_set_invalid_genre(self, books_collector):
        books_collector.add_new_book("Книга 11")
        """Присваиваем книге несуществующий жанр"""
        books_collector.set_book_genre("Книга 11", "Драма")
        assert books_collector.get_book_genre("Книга 11") == '', "Удалось установить жанр для книги"

    def test_get_list_of_favorites_books(self, books_collector):
        books_collector.add_new_book("Книга 12")
        books_collector.set_book_genre("Книга 12", "Фантастика")
        books_collector.add_new_book("Книга 13")
        books_collector.set_book_genre("Книга 13", "Ужасы")
        books_collector.add_book_in_favorites("Книга 12")
        books_collector.add_book_in_favorites("Книга 13")
        assert books_collector.get_list_of_favorites_books() == ["Книга 12", "Книга 13"], "Не удалось получить список избранных книг"

    def test_add_book_in_favorites_multiple_times(self, books_collector):
        books_collector.add_new_book("Книга 15")
        books_collector.set_book_genre("Книга 15", "Фантастика")
        books_collector.add_book_in_favorites("Книга 15")
        """Добавление книги в избранное второй раз"""
        books_collector.add_book_in_favorites("Книга 15")
        assert len(books_collector.get_list_of_favorites_books()) == 1, "Добавили книгу в избранное несколько раз"


    def test_get_books_for_children_with_forbidden_genre(self, books_collector):
        books_collector.add_new_book("Книга 18")
        """Присваиваем запрещенный для детей жанр для книги"""
        books_collector.set_book_genre("Книга 18", "Ужасы")
        books_for_children = books_collector.get_books_for_children()
        assert len(books_for_children) == 0, "В книгах для детей находится запрещенный жанр"
