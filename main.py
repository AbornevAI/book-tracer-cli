from models import Book
from storage import Storage
from stats import Stats


def main():
    storage = Storage("books.json")
    
    while True:
        print("\n" + "="*50)
        print("📚 ТРЕКЕР ПРОЧИТАННЫХ КНИГ")
        print("="*50)
        print("1. Добавить книгу")
        print("2. Показать все книги")
        print("3. Поиск книги")
        print("4. Удалить книгу")
        print("5. Показать статистику")
        print("6. Выход")
        print("="*50)
        
        choice = input("\nВыберите действие (1-6): ").strip()
        
        if choice == "1":
            add_book_menu(storage)
        elif choice == "2":
            show_all_books(storage)
        elif choice == "3":
            search_book_menu(storage)
        elif choice == "4":
            delete_book_menu(storage)
        elif choice == "5":
            Stats.print_stats(storage.get_all_books())
        elif choice == "6":
            print("👋 До свидания! Хорошего чтения!")
            break
        else:
            print("❌ Неверный выбор. Попробуйте ещё раз.")


def add_book_menu(storage):
    print("\n--- Добавление новой книги ---")
    title = input("Название книги: ").strip()
    author = input("Автор: ").strip()
    year = input("Год издания: ").strip()
    genre = input("Жанр (можно оставить пустым): ").strip()
    rating = input("Оценка от 1 до 10 (можно оставить пустым): ").strip()
    
    try:
        book = Book(
            title=title,
            author=author,
            year=int(year),
            genre=genre,
            rating=float(rating) if rating else 0.0
        )
        storage.add_book(book)
        print(f"✅ Книга '{title}' успешно добавлена!")
    except ValueError:
        print("❌ Ошибка: год должен быть числом, оценка — числом.")


def show_all_books(storage):
    books = storage.get_all_books()
    if not books:
        print("📭 Библиотека пока пуста.")
        return
    
    print(f"\n📚 Всего книг: {len(books)}\n")
    for i, book in enumerate(books, 1):
        print(f"{i}. {book} — оценка: {book.rating if book.rating > 0 else '—'}")
        if book.genre:
            print(f"   Жанр: {book.genre}")


def search_book_menu(storage):
    print("\n--- Поиск книги ---")
    print("1. По названию")
    print("2. По автору")
    subchoice = input("Выберите (1-2): ").strip()
    
    if subchoice == "1":
        title = input("Введите название (или часть): ").strip()
        results = storage.find_book(title=title)
    elif subchoice == "2":
        author = input("Введите автора (или часть): ").strip()
        results = storage.find_book(author=author)
    else:
        print("❌ Неверный выбор.")
        return
    
    if results:
        print(f"\n✅ Найдено книг: {len(results)}")
        for book in results:
            print(f"   • {book}")
    else:
        print("❌ Книги не найдены.")


def delete_book_menu(storage):
    title = input("\nВведите точное название книги для удаления: ").strip()
    if storage.delete_book(title):
        print(f"✅ Книга '{title}' успешно удалена.")
    else:
        print("❌ Книга с таким названием не найдена.")


if __name__ == "__main__":
    main()