# Task Manager Web Application

This is a simple task manager web application built using Flask, a Python web framework.

## Features

- Add tasks to the task list
- Delete tasks from the task list

## Installation

1. Make sure you have Python installed on your system.
2. Clone this repository:

git clone <repository_url>
3. Install the required dependencies:


pip install -r requirements.txt
## Usage
1. Run the Flask development server:


python app.py
2. Open your web browser and go to `http://localhost:5000`.
3. Enter a task in the input field and click the "Add Task" button.
4. Tasks will be displayed as a list. To delete a task, click the "Delete" button next to it.

## Topology
```ASCII
+------------------+      HTTP GET         +-------------------+
|  Web Browser    | ---------------------> |  Flask Application|
+------------------+                       +-------------------+
        |                                          |
        | HTTP GET                                 |
        | /                                        |
        |                                          |
        |     +--------------------------+         |
        +---> |  index()                 |         |
        |     |  Render index.html       |         |
        |     |  Display tasks list      |         |
        |     +--------------------------+         |
        |                                          |
        |                                          |
        |                                          |
        |  HTTP POST                               |
        |  /add                                    |
        |                                          |
        |     +--------------------------+         |
        +---> |  add()                   |         |
        |     |  Extract task from form  |         |
        |     |  Append task to tasks    |         |
        |     |  Redirect to /           |         |
        |     +--------------------------+         |
        |                                          |
        |                                          |
        |  HTTP POST                               |
        |  /delete                                 |
        |                                          |
        |     +--------------------------+         |
        +---> |  delete()                |         |
        |     |  Extract task from form  |         |
        |     |  Remove task from tasks  |         |
        |     |  Redirect to /           |         |
        |     +--------------------------+         |
        |                                          |
        |                                          |
        |                                          |
        |                                          |
        |                                          |
        |      +-----------------------+           |
        +----> |  index.html           |           |
               |  Display tasks list   |           |
               +-----------------------+           |

```

## Contributing
Contributions are welcome! If you have any ideas, suggestions, or bug reports, please open an issue or submit a pull request.

## License
This project is licensed under the [MIT License](LICENSE).







