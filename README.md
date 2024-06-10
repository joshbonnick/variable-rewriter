# Variable Rewriter

Python script designed to streamline the process of converting variable names in files to either camelCase or snake_case. This tool recursively scans files in a given directory or a specified file
path, parses the variables, and formats them according to your specified case style.

## Features

- **Recursive Parsing:** Scans through directories and files recursively.
- **Variable Formatting:** Converts variable names to either camelCase or snake_case.
- **PHP Support:** Currently supports only PHP files.
- **Git Integration:** Automatically creates and pushes a new Git branch with the changes.
- **Dry Run:** Option to preview changes without applying them.

## Usage

### Basic Command

```bash
python variable_rewriter.py <filepath_or_directory> <case_style> [--dry]
```

- `<filepath_or_directory>`: The path to the file or directory you want to process.
- `<case_style>`: The desired case style for the variables. Accepts `camel` or `snake`. Defaults to `camel` if not provided.
- `[--dry]`: Optional flag to perform a dry run, displaying the changes without applying them.

### Examples

1. **Convert variables in a single file to camelCase:**
    ```bash
    python case_formatter.py /path/to/file.php camel
    ```

2. **Convert variables in a directory to snake_case:**
    ```bash
    python case_formatter.py /path/to/directory snake
    ```

3. **Perform a dry run to see changes without applying them:**
    ```bash
    python case_formatter.py /path/to/directory camel --dry
    ```

## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes.