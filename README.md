## Django E-Commerce Project

### Project Description:

This project is an e-commerce website built using Django, a high-level Python web framework. The website allows users to browse products, add them to the cart, and place orders. It includes features such as user authentication, product search, order management, and payment processing.

### Getting Started:

1. Clone the repository:

```bash
git clone  git@github.com:FazlulAyanKoushik/e-commerce-project-v2.git
```

2. Create a virtual environment:

```bash
python3 -m venv env
```

3. Activate the virtual environment:

on Windows:
```bash
venv\Scripts\activate
```

on macOS and Linux:
```bash
source venv/bin/activate
```

4. Install the project dependencies:

```bash
pip install -r requirements.txt
```

### Database Setup:

1. Create the database tables:

```bash
python manage.py migrate
```

2. Create a superuser account:

```bash
python manage.py createsuperuser
```

3. Start the development server:

```bash
python manage.py runserver
```

### Project Structure:

The project is organized into the following Django apps:

- **accounts**: Manages user authentication and profile management.
- **cart**: Handles cart management and order processing.
- **core**: Contains common utilities and settings for the project.
- **orders**: Manages order creation, processing, and tracking.
- **products**: Handles product management and browsing.
- **payment**: Integrates payment processing using Stripe.
- **search**: Implements product search functionality.
- **staticfiles**: Contains static files such as CSS, JavaScript, and images.


## Tools for Testing:

### pytest

- **Simplicity and Readability**: pytest provides a simple and intuitive syntax for writing tests, making it easy to understand and maintain test suites.
- **Powerful Features**: With fixtures, parametrization, and plugins support, pytest offers powerful features to write comprehensive and efficient test cases.

### pytest-django

- **Seamless Django Integration**: pytest-django seamlessly integrates pytest with Django's testing framework, allowing us to leverage Django's testing utilities and database fixtures while writing pytest-style tests.
- **Improved Test Performance**: With transactional database handling and Django-specific fixtures support, pytest-django helps in improving test performance and reliability.

### pytest-selenium

- **End-to-End Testing**: pytest-selenium enables us to perform end-to-end testing of web applications by automating browser interactions.
- **Cross-Browser Compatibility**: By supporting multiple browsers, pytest-selenium ensures that our web application works consistently across different browser environments.
- **Integration with pytest**: Integrated seamlessly with pytest, pytest-selenium allows us to write and execute Selenium tests using pytest's flexible testing framework.

### pytest-factoryboy

- **Efficient Test Data Setup**: pytest-factoryboy provides utilities for creating and managing test data using Factory Boy, simplifying the process of setting up test fixtures.
- **Dynamic Test Data Generation**: With pytest-factoryboy, we can dynamically generate test data with complex relationships, reducing the boilerplate code and improving test readability.
- **Integration with pytest Fixtures**: pytest-factoryboy seamlessly integrates with pytest fixtures, enabling us to create and use factory instances within our test functions easily.
