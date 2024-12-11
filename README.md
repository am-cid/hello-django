# hello-django
simple crud in django. simple marketplace with users and listings.

# Setup
## Prerequisites: Install `uv`
`uv` is a python package and project manager. [Installation steps](https://docs.astral.sh/uv/getting-started/installation/)

## Setup
1. Create and activate virutal environment

    Windows
    ```bash
    uv venv
    .venv/scripts/activate
    ```
    Linux
    ```bash
    uv venv
    source .venv/bin/activate
    ```

2. Download dependencies

    ```bash
    uv sync
    ```

3. Take the `.env.example` and rename it to `.env`. You only really need to
assign `SECRET_KEY` since others have sensible defaults. It can be any string
    ```bash
    SECRET_KEY=your-super-secret-key-here
    ```
    For production:
    ```bash
    DEBUG=False
    ALLOWED_HOST=www.where-I-am-deploying-to.com,api.somewhere-else.com
    DATABASE_URL=postgres://username:password@hostname:5432/dbname
    ```
    `ALLOWED_HOST` is a csv. You usually can just leave `DATABASE_URL` blank
    so it uses sqlite but only if where you are deploying to supports it.

4. Run migrations to create tables
    ```bash
    cd simple_crud
    python manage.py migrate
    ```

4. Run server
    ```bash
    python manage.py runserver
    ```

---

Go to [localhost:8000/](localhost:8000/) to view all listings
