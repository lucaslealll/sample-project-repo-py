# Development Environment Setup

> [!NOTE]
> ### Prerequisites
> - **Python 3.10**

## Setup Steps

1. **Create a local virtual environment:**
    ```sh
    python3.10 -m venv .venv
    ```

2. **Activate the virtual environment:**

   Close the terminal and reopen it to ensure the virtual environment activates correctly. If you're using `VS Code`, it may prompt you to switch the interpreter to the newly created environment.

   *If the environment does not activate automatically, use the following command*:

   - Linux, macOS:
      ```sh
      source .venv/bin/activate
      ```
   - Windows:
      ```cmd
      .venv\Scripts\activate
      ```

3. **Install the required libraries:**
    ```sh
    pip install -r requirements.txt
    ```

4. **The directory is now ready for use.**

---

### Additional Notes

- To deactivate the virtual environment, you can use the command:
    ```sh
    deactivate
    ```
   - Every time you open this project in VS Code, the virtual environment should be automatically recognized and initialized.
- Make sure all dependencies are listed in the `requirements.txt` file to ensure that the environment sets up correctly.
