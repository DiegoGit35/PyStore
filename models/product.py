from sqlmodel import SQLModel, Field


class Product(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    title: str
    description: str
    price: int
    discount_percentage: int
    rating: int
    stock: int
    brand: str
    thumbnail: str
    images: str
    is_published: bool
    created_at: str
    category_id: int | None = Field (default = None, foreign_key = "categories.id")


    class Config:
        schema_extra = {
            "schema": {
                'title': 'Smartphone XYZ',
                'description': 'A high-performance smartphone with advanced features.',
                'price': 7999,  # 79.99 units of currency
                'discount_percentage': 15,  # 15% discount
                'rating': 4,  # Rated 4 out of 5
                'stock': 50,  # 50 units in stock
                'brand': 'XYZ Electronics',
                'thumbnail': 'https://example.com/thumbnail.jpg',
                'images': 'https://example.com/image1.jpg,https://example.com/image2.jpg',
                'is_published': True,  # Product is published and visible
                'created_at': '2023-05-15T10:30:00Z',  # Created on May 15th, 2023 at 10:30 AM UTC
                'category_id': 1234
            }
        }

