# notipier manual installation
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
    - To do this, you may use a text editor such as nano or Vim. 
    ```bash
    nano .env
    ```
    or

    ```bash
    vi .env
    ```
    - Be sure to save the edits to the file when complete
        - nano: `Ctrl+X, Y, Enter`
        - Vim: `:wq`
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
8. Deactivate the virtual environment.
    ```bash
    deactivate
    ```
9. Edit `notipier.service` and replace `/path/to/` with the path to the notipier.py file in the notipier directory. 
    - To do this, you can use the `pwd` command to find your current directory, then use a text editor such as nano or Vim. 
    ```bash
    nano notipier.service
    ```
    or

    ```bash
    vi notipier.service
    ```
    - Be sure to save the edits to the file when complete
        - nano: `Ctrl+X, Y, Enter`
        - Vim: `:wq`
10. Create a hard link of the service file to `/etc/systemd/system`.
    ```bash
    sudo ln notipier.service /etc/systemd/system/notipier.service
    ```
11. Enable the service to launch at startup and start the service. 
    ```bash
    sudo systemctl enable notipier.service && sudo systemctl start notipier.service
    ```
12. Reboot your system and view your **System Boot** message!
