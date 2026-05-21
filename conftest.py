import pytest
from main import BooksCollector

@pytest.fixture #фикстура, которая создаёт объект класса BooksCollector
def collection():
    return BooksCollector() 

@pytest.fixture
def ten_books_with_different_genres():
    collection = BooksCollector()
    # добавляем книги разных жанров
    collection.add_new_book('Оно') # ужасы
    collection.add_new_book('Незнакомцы в поезде') # детективы
    collection.add_new_book('Тайная история') # детективы
    collection.add_new_book('Дюна') # фантастика
    collection.add_new_book('1984') # фантастика
    collection.add_new_book('Человек-амфибия') # фантастика    
    collection.add_new_book('Чебурашка')    # мультфильмы
    collection.add_new_book('Артур и минипуты')   # мультфильмы
    collection.add_new_book('Буратино')     # мультфильмы
    collection.add_new_book('Маленький принц')     # мультфильмы
   
    # устанавливаем жанры
    collection.set_book_genre('Оно', 'Ужасы')
    collection.set_book_genre('Незнакомцы в поезде', 'Детективы')
    collection.set_book_genre('Тайная история', 'Детективы')
    collection.set_book_genre('Дюна', 'Фантастика')
    collection.set_book_genre('1984', 'Фантастика')
    collection.set_book_genre('Человек-амфибия', 'Фантастика')
    collection.set_book_genre('Чебурашка', 'Мультфильмы')
    collection.set_book_genre('Артур и минипуты', 'Мультфильмы')
    collection.set_book_genre('Буратино', 'Мультфильмы')
    collection.set_book_genre('Маленький принц', 'Мультфильмы')
    return collection
