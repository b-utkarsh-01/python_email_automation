import base64
from bs4 import BeautifulSoup

def parse_email(service, msg_id):
    msg = service.users().messages().get(
        userId="me",
        id=msg_id,
        format="full"
    ).execute()

    headers = msg["payload"]["headers"]

    data = {
        "From": "",
        "Subject": "",
        "Date": "",
        "Content": ""
    }

    for header in headers:
        name = header["name"]
        value = header["value"]

        if name == "From":
            data["From"] = value
        elif name == "Subject":
            data["Subject"] = value
        elif name == "Date":
            data["Date"] = value
    parts = msg["payload"].get("parts", [])

    for part in parts:
        mime_type = part.get("mimeType")

        if mime_type == "text/plain":
            body_data = part["body"].get("data")
            if body_data:
                decoded = base64.urlsafe_b64decode(body_data).decode("utf-8")
                data["Content"] = decoded
                break

        elif mime_type == "text/html":
            body_data = part["body"].get("data")
            if body_data:
                html = base64.urlsafe_b64decode(body_data).decode("utf-8")
                soup = BeautifulSoup(html, "html.parser")
                data["Content"] = soup.get_text()


    return data
