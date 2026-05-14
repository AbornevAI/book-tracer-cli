class Book:
    """Класс для представления книги"""
    
    def __init__(self, title: str, author: str, year: int, 
                 genre: str = "", rating: float = 0.0):
        self.title = title.strip()
        self.author = author.strip()
        self.year = int(year)
        self.genre = genre.strip()
        self.rating = float(rating)
    
    def to_dict(self) -> dict:
        """Преобразует объект книги в словарь для сохранения в JSON"""
        return {
            "title": self.title,
            "author": self.author,
            "year": self.year,
            "genre": self.genre,
            "rating": self.rating
        }
    
    @classmethod
    def from_dict(cls, data: dict):
        """Создает объект Book из словаря"""
        return cls(
            title=data.get("title", ""),
            author=data.get("author", ""),
            year=data.get("year", 0),
            genre=data.get("genre", ""),
            rating=data.get("rating", 0.0)
        )
    
    def __str__(self):
        return f'"{self.title}" — {self.author} ({self.year})'
    
    def __repr__(self):
        return f"Book(title='{self.title}', author='{self.author}', year={self.year})"