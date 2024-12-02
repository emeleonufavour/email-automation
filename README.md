# TechFam Email Automation

A Python tool to automate email sending to multiple recipients.
It allows scheduling emails at regular intervals or for specific times.

## Dependencies

- schedule
- email-validator
- python-dotenv

## Prerequisites

- Python 3.8 or higher.
- A Gmail account.

## Installation and Setup

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/your-username/email-automation.git
   cd email-automation
   ```

2. **Setup a virtual environment**:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install the dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Environment Variables**:

   ```bash
   EMAIL=your_email@gmail.com
   EMAIL_PASSWORD=your_app_password
   ```

5. **Run the script**:
   ```bash
   python email_automation.py
   ```

## Usage

1. **Customize variables**:

   ```bash
   recipients = ["recipient1@example.com", "recipient2@example.com"]
   subject = "Scheduled Email"
   body = "Hello, this is an automated email!"
   ```

2. **Set time interval**:
   ```bash
   schedule.every(2).weeks.at("10:00").do(job)
   ```

## Contribution

Feel free to fork the repository, create a feature branch, and submit a pull request. Contributions are welcome!
