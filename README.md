
# Django Recon

This project is a Django-based web application.

---

**This project is part of my 3rd semester coursework for the Bachelor of Computer Applications (BCA) program at BPPIMT, Salt Lake.**

---


# Project Structure

```
django-recon/
├── core/           # App: core business logic, models, views
│   ├── migrations/ # DB migrations
│   └── ...         # Other app files
├── demo/           # (Empty or for demo purposes)
├── django_recon/   # Project settings, URLs, WSGI/ASGI
├── static/         # Static files (CSS, JS, images)
│   ├── css/
│   ├── img/
│   └── js/
├── templates/      # HTML templates
├── db.sqlite3      # SQLite database file
├── manage.py       # Django management script
├── requirements.txt# Python dependencies
├── myenv/          # Python virtual environment
└── README.md       # Project documentation
```



## Demo

Below are example screenshots of the tool in action:

![Google Demo](demo/demo_google.png)


![Whois Demo](demo/whois_demo.png)

*Demo images are shown above.*

---

## Disclaimer

This project is a domain reconnaissance tool intended for educational and authorized security testing purposes only. The author is not responsible for any misuse or illegal activities performed using this tool. Use responsibly and always ensure you have proper authorization.

## Prerequisites
- Python 3.11+
- pip (Python package manager)
- (Recommended) Virtual environment tool: `venv`

## Setup Instructions


### 1. Clone the Repository

```sh
git clone https://github.com/DebaA17/django-recon.git
cd django-recon
```


### 2. Create and Activate Virtual Environment


#### On Linux/Mac:
```sh
python3 -m venv myenv
source myenv/bin/activate
```


#### On Windows:
```sh
python -m venv myenv
myenv\Scripts\activate
```


### 3. Install Dependencies
```sh
pip install -r requirements.txt
```


### 4. Apply Migrations
```sh
python manage.py migrate
```


### 5. Create a Superuser (Optional, for admin access)
```sh
python manage.py createsuperuser
```



### 6. Run the Development Server

#### On Linux/Mac:
```sh
python manage.py runserver 0.0.0.0:8000
```

#### On Windows:
```sh
python manage.py runserver
```


The server will start at http://127.0.0.1:8000/


## Additional Commands

- **Collect static files:**
  ```sh
  python manage.py collectstatic
  ```
- **Run tests:**
  ```sh
  python manage.py test
  ```



## Notes
- Always activate your virtual environment before running any Django commands.
- For production deployment, additional configuration is required (see Django documentation).

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
