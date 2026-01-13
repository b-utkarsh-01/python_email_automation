import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from config import STATE_FILE


def load_state():
    if not os.path.exists(STATE_FILE):
        return set()

    with open(STATE_FILE, "r") as f:
        return set(f.read().splitlines())


def save_state(processed_ids):
    with open(STATE_FILE, "w") as f:
        for msg_id in processed_ids:
            f.write(msg_id + "\n")

from gmail_service import (
    get_gmail_service,
    fetch_unread_emails,
    mark_as_read
)

from sheets_service import (
    get_sheets_service,
    append_row
)

from email_parser import parse_email


def main():
    # Initialize services
    gmail_service = get_gmail_service()
    sheets_service = get_sheets_service()

    # Load already processed email IDs
    processed_ids = load_state()

    # Fetch unread emails
    messages = fetch_unread_emails(gmail_service)

    for msg in messages:
        msg_id = msg["id"]

        # Skip if already processed
        if msg_id in processed_ids:
            continue

        # Parse email
        email_data = parse_email(gmail_service, msg_id)

        # Append to Google Sheet
        append_row(sheets_service, email_data)

        # Mark email as read
        mark_as_read(gmail_service, msg_id)

        # Save state
        processed_ids.add(msg_id)

    # Persist state
    save_state(processed_ids)



if __name__ == "__main__":
    main()
