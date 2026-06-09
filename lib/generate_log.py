from datetime import datetime


def generate_log(log_data):
    """
    Generates a timestamped log file from a list of log entries.

    Args:
        log_data (list): A list of log entry strings to write to the file.

    Returns:
        str: The filename that was created.

    Raises:
        ValueError: If log_data is not a list.
    """
    if not isinstance(log_data, list):
        raise ValueError("log_data must be a list.")

    filename = f"log_{datetime.now().strftime('%Y%m%d')}.txt"

    with open(filename, "w") as file:
        for entry in log_data:
            file.write(f"{entry}\n")

    print(f"Log written to {filename}")

    return filename


if __name__ == "__main__":
    log_data = ["User logged in", "User updated profile", "Report exported"]
    generate_log(log_data)