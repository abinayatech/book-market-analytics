import sqlite3
import os

class CleanDataPipeline:
    def process_item(self, item, spider):
        # Clean price: remove '£' and convert to float
        if item.get('price'):
            item['price'] = float(item['price'].replace('£', ''))
        
        # Clean rating: convert text word to integer
        rating_map = {
            'One': 1, 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5
        }
        if item.get('rating'):
            item['rating'] = rating_map.get(item['rating'], 0)
            
        return item

class SaveToSQLitePipeline:
    def __init__(self):
        # Create DB in the parent directory (project root) so Dashboard can see it easily
        # Current dir: .../scraper/bookscraper/
        # DB dir: .../book_analytics_project/
        self.db_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), 'books.db')
        
    def open_spider(self, spider):
        self.conn = sqlite3.connect(self.db_path)
        self.curr = self.conn.cursor()
        self.curr.execute("""
            CREATE TABLE IF NOT EXISTS books (
                upc TEXT PRIMARY KEY,
                title TEXT,
                price REAL,
                rating INTEGER,
                category TEXT,
                description TEXT
            )
        """)
        self.conn.commit()

    def process_item(self, item, spider):
        try:
            self.curr.execute("""
                INSERT OR REPLACE INTO books (upc, title, price, rating, category, description)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (
                item.get('upc'),
                item.get('title'),
                item.get('price'),
                item.get('rating'),
                item.get('category'),
                item.get('description')
            ))
            self.conn.commit()
        except Exception as e:
            print(f"Error inserting item: {e}")
        return item

    def close_spider(self, spider):
        self.conn.close()
