import json
from typing import List, Optional
from models import Book


class Storage:
    """Класс для работы с хранилищем книг (JSON-файл)"""
    
    def __init__(self, filename: str = "books.json"):
        self.filename = filename
        self.books: List[Book] = []
        self.load_books()
    
    def load_books(self):
        """Загружает книги из JSON-файла"""
        try:
            with open(self.filename, 'r', encoding='utf-8') as f:
                data = json.load(f)
                self.books = [Book.from_dict(book) for book in data]
        except (FileNotFoundError, json.JSONDecodeError):
            self.books = []
            self.save_books()  # создаём пустой файл
    
    def save_books(self):
        """Сохраняет книги в JSON-файл"""
        with open(self.filename, 'w', encoding='utf-8') as f:
            data = [book.to_dict() for book in self.books]
            json.dump(data, f, ensure_ascii=False, indent=4)
    
    def add_book(self, book: Book):
        """Добавляет новую книгу"""
        self.books.append(book)
        self.save_books()
        return book
    
    def get_all_books(self) -> List[Book]:
        """Возвращает список всех книг"""
        return self.books.copy()
    
    def find_book(self, title: str = None, author: str = None) -> List[Book]:
        """Поиск книг по названию или автору"""
        result = self.books
        if title:
            result = [b for b in result if title.lower() in b.title.lower()]
        if author:
            result = [b for b in result if author.lower() in b.author.lower()]
        return result
    
    def delete_book(self, title: str) -> bool:
        """Удаляет книгу по названию (точное совпадение)"""
        initial_count = len(self.books)
        self.books = [b for b in self.books if b.title.lower() != title.lower()]
        if len(self.books) < initial_count:
            self.save_books()
            return True
        return False