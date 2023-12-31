# notipier Manual Installation
1. Clone the GitHub repository using:
    ```bash
    git clone https://github.com/dekay7/notipier.git
    ```
2. Enter the notipier directory.
    ```bash
    cd notipier
    ```
3. Rename `example.env` to `.env`.
    ```bash
    mv example.env .env
    ```
4. Edit `.env` and replace `https://discord.com/api/webhooks//` with URL with your [Discord Webhook](https://support.discord.com/hc/en-us/articles/228383668-Intro-to-Webhooks) URL. 
    ```bash
    nano .env
    ```
5. Initialize the Python virtual environment. 
    ```bash
    python -m venv .
    ```
6. Activate the virtual environment.
    ```bash
    source bin/activate
    ```
7. Install the requirements via pip. 
    ```bash
    pip install -r requirements.txt
    ```
8. Create a hard link of the service file to `/etc/systemd/system`.
    ```bash
    ln notipier.service /etc/systemd/system/notipier.service
    ```
9. Enable the service to launch at startup and start the service. 
    ```bash
    sudo systemctl enable notipier.service && sudo systemctl start notipier.service
    ```