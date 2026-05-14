from typing import List
from models import Book


class Stats:
    """Класс для расчёта статистики по книгам"""
    
    @staticmethod
    def calculate_average_rating(books: List[Book]) -> float:
        """Подсчёт средней оценки"""
        if not books:
            return 0.0
        ratings = [book.rating for book in books if book.rating > 0]
        return round(sum(ratings) / len(ratings), 2) if ratings else 0.0
    
    @staticmethod
    def books_by_author(books: List[Book]) -> dict:
        """Статистика книг по авторам"""
        from collections import Counter
        authors = [book.author for book in books]
        return dict(Counter(authors))
    
    @staticmethod
    def books_by_genre(books: List[Book]) -> dict:
        """Статистика книг по жанрам"""
        from collections import Counter
        genres = [book.genre for book in books if book.genre]
        return dict(Counter(genres))
    
    @staticmethod
    def get_books_by_year(books: List[Book], year: int) -> List[Book]:
        """Книги определённого года"""
        return [book for book in books if book.year == year]
    
    @staticmethod
    def print_stats(books: List[Book]):
        """Вывод красивой статистики"""
        if not books:
            print("📚 Библиотека пока пуста.")
            return
        
        print("\n" + "="*50)
        print("📊 СТАТИСТИКА ПРОЧИТАННЫХ КНИГ")
        print("="*50)
        print(f"Всего книг прочитано: {len(books)}")
        print(f"Средняя оценка: {Stats.calculate_average_rating(books)} ⭐")
        
        # По авторам
        authors = Stats.books_by_author(books)
        print(f"\n📖 Книги по авторам:")
        for author, count in sorted(authors.items(), key=lambda x: x[1], reverse=True):
            print(f"   • {author}: {count} книг")
        
        # По жанрам
        genres = Stats.books_by_genre(books)
        if genres:
            print(f"\n🎭 Книги по жанрам:")
            for genre, count in sorted(genres.items(), key=lambda x: x[1], reverse=True):
                print(f"   • {genre}: {count} книг")
        
        print("="*50)