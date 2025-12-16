# Django Recon

This project is a Django-based web application.

## Prerequisites
- Python 3.11+
- pip (Python package manager)
- (Recommended) Virtual environment tool: `venv`

## Setup Instructions

```
### 1. Clone the Repository
```
git clone https://github.com/DebaA17/django-recon.git
cd django-recon
```


### 2. Create and Activate Virtual Environment

#### On Linux/Mac:
```
python3 -m venv myenv
source myenv/bin/activate
```

#### On Windows:
```
python -m venv myenv
myenv\Scripts\activate
```

### 3. Install Dependencies
```
pip install -r requirements.txt
```

### 4. Apply Migrations
```
python manage.py migrate
```

### 5. Create a Superuser (Optional, for admin access)
```
python manage.py createsuperuser
```


### 6. Run the Development Server

#### On Linux/Mac:
```
python manage.py runserver 0.0.0.0:8000
```

#### On Windows:
```
python manage.py runserver
```

The server will start at http://127.0.0.1:8000/ 

## Additional Commands

- **Collect static files:**
  ```
  python manage.py collectstatic
  ```
- **Run tests:**
  ```
  python manage.py test
  ```

## Notes
- Always activate your virtual environment before running any Django commands.
- For production deployment, additional configuration is required (see Django documentation).
