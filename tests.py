from main import BooksCollector
import pytest

class TestBooksCollector:

    def test_add_new_book_with_empty_name(self):
        collector = BooksCollector()
        collector.add_new_book('')
        assert len(collector.get_books_genre()) == 0

    def test_add_new_book_with_name_longer_40(self):
        collector = BooksCollector()
        collector.add_new_book("x" * 50)
        assert len(collector.get_books_genre()) == 0


    def test_add_new_book_with_one_simbol(self):
        collector = BooksCollector()
        collector.add_new_book("Книга")
        assert "Книга" in collector.get_books_genre()


    def test_set_book_genre_valid(self):
        collector = BooksCollector()
        collector.add_new_book('Книга')
        collector.set_book_genre('Книга', "Ужасы")
        assert collector.get_book_genre('Книга') == "Ужасы"


    def test_set_book_genre_invalid_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Книга')
        collector.set_book_genre('Книга', 'Драма')
        assert collector.get_book_genre('Книга') == ''


    def test_get_book_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Книга')
        collector.set_book_genre('Книга', 'Ужасы')
        assert collector.get_book_genre("Книга") == 'Ужасы'

    @pytest.mark.parametrize(
        "name, genre, genre_check, expected",
        [
            ('Книга', 'Комедии', 'Комедии',
             ['Книга']),
            ('Книга', 'Ужасы', 'Детективы', []),
        ]
    )
    def test_get_books_with_specific_genre(self, name, genre, genre_check, expected):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert collector.get_books_with_specific_genre(genre_check) == expected



    @pytest.mark.parametrize("book_name, book_genre, expected", [
        (
        'Книга', 'Комедии', {'Книга': 'Комедии'}),
        ('Книга1', 'Ужасы', {'Книга1': 'Ужасы'}),
    ])
    def test_get_books_genre(self, book_name, book_genre, expected):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, book_genre)
        assert collector.get_books_genre() == expected


    def test_get_books_for_children_with_valid_books(self):
        collector = BooksCollector()
        collector.add_new_book('Книга')
        collector.set_book_genre('Книга', 'Мультфильмы')
        expected = ['Книга']
        assert collector.get_books_for_children() == expected

    def test_get_books_for_children_with_all_age_restricted_genres(self):
        collector = BooksCollector()
        collector.add_new_book('Книга')
        collector.set_book_genre('Книга', 'Ужасы')
        expected = []
        assert collector.get_books_for_children() == expected

    @pytest.mark.parametrize(
        "books_genre, book_name, expected",
        [
            (['Книга'], 'Книга', ['Книга']),
            ([], "Книга", []),
        ]
    )
    def test_add_book_in_favorites(self, books_genre, book_name, expected):
        collector = BooksCollector()
        for book in books_genre:
            collector.add_new_book(book)
        collector.add_book_in_favorites(book_name)
        assert collector.get_list_of_favorites_books() == expected

    @pytest.mark.parametrize(
        "initial_favorites, book_name_to_delete, expected_favorites",
        [
            (['Книга1', 'Книга2'], 'Книга1', ['Книга2']),
            (['Книга1'], 'Книга2', ['Книга1']),
        ]
    )
    def test_delete_book_from_favorites(self, initial_favorites, book_name_to_delete, expected_favorites):
        collector = BooksCollector()
        collector.favorites = initial_favorites
        collector.delete_book_from_favorites(book_name_to_delete)
        assert collector.get_list_of_favorites_books() == expected_favorites














