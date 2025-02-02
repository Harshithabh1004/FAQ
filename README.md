# FAQ Multilingual System

This is a Django-based FAQ system that supports multilingual content. The system allows users to manage Frequently Asked Questions (FAQs) in multiple languages, including automatic translation and a rich text editor interface. It integrates with CKEditor for WYSIWYG editing, Google Translate API for translations, and uses Redis for caching to improve performance.

## Features

- **Multilingual FAQ**: Supports multiple languages like English, Hindi, Bengali, Kannada, Telugu, and Tamil.
- **WYSIWYG Editor**: The system uses `django-ckeditor` for rich text editing.
- **Automatic Translation**: Translations are automatically provided for questions and answers using Google Translate API.
- **Caching**: Redis caching is used to store translated content for quick retrieval.
- **Admin Panel**: Easy-to-use admin interface to manage FAQs in different languages.
- **REST API**: Exposes an API to retrieve FAQs based on the selected language.
- **Testing**: Includes unit tests to ensure the functionality of the FAQ system.

## Requirements

- Python 3.x
- Django 3.x or higher
- Redis (for caching)
- Google Translate API key (optional, if using Google Translate for translations)
- CKEditor for Django

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/faq_proj.git
   cd faq_proj
2.pip install -r requirements.txt
3.python manage.py migrate
4.python manage.py createsuperuser
   username:harshithabh
   password:harshi10@
   ```

5. Configure Redis and Google Translate API (if using)
6. Run the development server: python manage.py runserver
7. Access the admin panel: http://localhost:8000/admin
8. Access the FAQ system: http://localhost:8000/faq
9.Access the FAQ system: http://localhost:8000/faq/?lang=hi
