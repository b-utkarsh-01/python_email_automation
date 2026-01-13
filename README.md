## 1️⃣ Clone the Repository

```jsx
git clone <your-repository-url>
cd gmail-to-sheets
```

### 2️⃣ Create Required Folders

Inside the project root, make sure this folder exists:

```
gmail-to-sheets/
 └── credentials/
```

⚠️ The `credentials` folder is mandatory.

OAuth credentials **must be placed inside this folder**.

---

### 3️⃣ Create a Google Sheet

1. Go to https://sheets.google.com
2. Create a **new blank Google Sheet**
3. Add the following headers in the first row:

| From | Subject | Date | Content |

1. Copy the **Spreadsheet ID** from the URL
    
    Example:
    
    ```
    https://docs.google.com/spreadsheets/d/SPREADSHEET_ID/edit
    ```
    
2. Paste this ID in `config.py`:

```python
SPREADSHEET_ID ="PASTE_YOUR_SHEET_ID_HERE"
```

---

### 4️⃣ Google Cloud Console Setup (Mandatory)

Each user must configure their **own Google Cloud project**:

1. Go to [https://console.cloud.google.com](https://console.cloud.google.com/)
2. Create a new project
3. Enable the following APIs:
    - Gmail API
    - Google Sheets API
4. Configure **OAuth Consent Screen**
    - User type: External
    - Add your Gmail as a Test User
5. Create **OAuth Client ID**
    - Application type: Desktop App
6. Download the OAuth credentials file

---

### 5️⃣ Place OAuth Credentials File

After downloading the OAuth file:

1. Rename the downloaded file to:

```
credentials.json
```

1. Place it inside the following folder:

```
gmail-to-sheets/credentials/credentials.json
```

⚠️ This file must **never be committed** to GitHub.

It is already excluded using `.gitignore`.

---

### 6️⃣ Install Python Dependencies

Make sure **Python 3.9 or higher** is installed.

Install required libraries:

```bash
pip install -r requirements.txt
```

---

### 7️⃣ Run the Project

From the **project root directory**:

```bash
python src/main.py
```

### First Run:

- Browser opens for Google OAuth
- Gmail & Sheets permissions are granted
- Unread emails are logged into the Google Sheet

### Re-run:

- No duplicate entries
- Already processed emails are skipped