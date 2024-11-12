# Directory for Access Files

This folder is intended as a directory where access files should be stored.

- **These files are not modified!**
- They are stored here to be accessed by production code for data retrieval.
- File types include `.json`, `.pkl`, and similar formats.

## Naming Conventions

- Use lowercase letters only.
- Use snake case (e.g., `application_name.py`).
- For file names, include the client name, file type, platform name, function, and final page name (for cookies).
- For JSON credentials, include the client name, platform name, and project code.

### Cookies

**Format**: USER + TYPE + PLATFORM + FINAL PAGE

**Example:**

- User: ufc
- Type: cookie
- Platform: twitter
- Final Page: profile

**Final filename**: `ufc_cookie_twitter_profile.py`

### Credentials

**Format**: USER + PLATFORM + PROJECT CODE

**Example:**

- User: ufc
- Platform: aws
- Project Code: ufc-31294891

**Final filename**: `ufc_aws_31294891.py`
