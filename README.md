# Task Manager

## What is this?

This is a Django-based Task Manager application that allows users to create, update, delete, and view tasks. It also includes features for filtering and sorting tasks, as well as providing smart task suggestions based on existing tasks (smart suggestions is unfortunately not finished). It also has a simple UI to showcase the functionalities.

## How to run
1. **Install dependencies:**
    Make sure you have Python and pip installed. Then run:
    ```sh
    pip install -r requirements.txt
    ```

2. **Apply migrations:**
    ```sh
    python manage.py migrate
    ```

3. **Run the development server:**
    ```sh
    python manage.py runserver
    ```

4. **Access the application:**
    Open your web browser and go to `http://127.0.0.1:8000/`.

## How to use

1. **View Tasks:**
    - Navigate to the home page (`http://127.0.0.1:8000/`) to see the list of tasks.
    - Use the filter and sort options to customize the task list view.

2. **Create a Task:**
    - Click on the "Add a new item" button to open the task creation form.

3. **Update a Task:**
    - Click on a task title in the task list to open the task update form.

4. **Delete a Task:**
    - Click on a task title in the task list to open the task update form.
    - Click the "Delete task" button to delete the task.

5. **Smart Task Suggestions:**
    - Access the smart task suggestions endpoint at `http://127.0.0.1:8000/smart-suggestions/` to get suggestions for new tasks based on existing tasks.

## API Endpoints

- **View Tasks:** `GET /`
- **Create Task:** `GET /task/add/` (form), `POST /task/add/` (submit form)
- **Update Task:** `GET /task/<int:pk>/` (form), `POST /task/<int:pk>/` (submit form)
- **Delete Task:** `POST /task/<int:pk>/delete/`
- **Smart Task Suggestions:** `GET /smart-suggestions/`
