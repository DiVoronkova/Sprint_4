import pytest
from main import BooksCollector


class TestBooksCollector:


    # Проверка добавления книг (с названием, длина которых от 1 до 40 символов) в books_genre
    def test_add_new_book_three_correct_books_added(self, collection):
        list_of_books = ['а', 'Дом в котором', 'а'*40]
        for book in list_of_books:
            collection.add_new_book(book)
        assert len(collection.get_books_genre()) == 3

    # Негативная проверка, что книги (с названием, длина которых 0 или более 40 символов) не добавляются в books_genre
    @pytest.mark.parametrize('incorrect_book_name', ['', 'а'*41, 'a'*42, 'а'*50])
    def test_add_new_book_incorrect_input_not_added(self, collection, incorrect_book_name):
        collection.add_new_book(incorrect_book_name)
        assert len(collection.get_books_genre()) == 0

    @pytest.mark.parametrize(
        'book_name, genre',
        [
            ['1984', 'Фантастика'],
            ['Оно', 'Ужасы'],
            ['Вечный сон', 'Детективы'],
            ['Незнайка на луне', 'Мультфильмы'],
            ['Тревожные люди', 'Комедии']
        ]
    )
    # Проверка устанавления книге (из books_genre) жанра (из списка genre)
    def test_set_book_genre_genre_added(self, collection, book_name, genre):
        collection.add_new_book(book_name)
        collection.set_book_genre(book_name, genre)
        assert collection.get_book_genre(book_name) == genre

    # Негативная проверка получения пустой строки вместо устанавленного книге жанра (НЕ из списка genre) по её имени (из books_genre) 
    def test_get_book_genre_incorrect_genre_not_added(self, collection): 
        collection.add_new_book('Sapiens')
        collection.set_book_genre('Sapiens', 'Научпоп')
        assert collection.get_book_genre('Sapiens') == ''

    @pytest.mark.parametrize(
        'specific_genre, result',
        [
            ['Фантастика', 3],
            ['Ужасы', 1],
            ['Детективы', 2],
            ['Мультфильмы', 4],
            ['Комедии', 0]
        ]
    )
    # Проверка вывода списка книг (из books_genre) с определённым жанром (из списка genre)
    def test_get_books_with_specific_genre_true(self, ten_books_with_different_genres, specific_genre, result):
        assert len(ten_books_with_different_genres.get_books_with_specific_genre(specific_genre)) == result
       
    # Проверка получения словаря books_genre (книги и жанры) 
    def test_get_books_genre_true(self, collection):
        collection.add_new_book('Тревожные люди')
        collection.set_book_genre('Тревожные люди', 'Комедии')
        assert collection.get_books_genre() == {'Тревожные люди': 'Комедии'}
        
    # Проверка получения списка книг, подходящих детям (исключая книги с жанром из genre_age_rating)
    def test_get_books_for_children_books_with_age_rating_excluded(self, ten_books_with_different_genres):
        children_books = ten_books_with_different_genres.get_books_for_children()
        for book in children_books:
          genre = ten_books_with_different_genres.get_book_genre(book)
          assert genre not in ten_books_with_different_genres.genre_age_rating

    # Проверка добавления книги в Избранное (favorites)
    def test_add_book_in_favorites_book_added(self, collection):
        book_name = 'Приключения Шерлока Холмса'
        collection.add_new_book(book_name)
        collection.add_book_in_favorites(book_name)
        assert book_name in collection.get_list_of_favorites_books()

    # Проверка удаления книги из Избранного (favorites)
    def test_delete_book_from_favorites_book_deleted(self, collection):
        book_name = 'Приключения Шерлока Холмса'
        collection.add_new_book(book_name)
        collection.add_book_in_favorites(book_name)
        collection.delete_book_from_favorites(book_name)
        assert book_name not in collection.get_list_of_favorites_books()

    # Проверка получения списка всех книг, добавленных в Избранное (favorites)
    def test_get_list_of_favorites_books_correct_list(self, collection):
        list_of_books = ['Матильда', 'Дом в котором', 'Вторая жизнь Уве']
        for book in list_of_books:
            collection.add_new_book(book)
            collection.add_book_in_favorites(book)
        collection.add_new_book('Оно')
        assert collection.get_list_of_favorites_books() == ['Матильда', 'Дом в котором', 'Вторая жизнь Уве']