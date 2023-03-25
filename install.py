import launch
import os

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
REQ_FILE = os.path.join(CURRENT_DIR, "requirements.txt")
CONFIG_FILE = os.path.join(CURRENT_DIR, "config.ini")
WEBUI_FILE = os.path.abspath(os.path.join(CURRENT_DIR, '..', '..', 'webui.py'))


def install_missing_libraries():
    with open(REQ_FILE) as file:
        for lib in file:
            lib = lib.strip()
            if not launch.is_installed(lib):
                launch.run_pip(f"install {lib}", f"SendURL/ requirement: {lib}")


def check_config_exist():
    if not os.path.isfile(CONFIG_FILE):
        lines = '[telegram]\nbot_token = \nchat_id = \n'
        with open(CONFIG_FILE, 'w') as f:
            f.writelines(lines)
        print(f'File config.ini empty...\nPlease insert token and chat_id into the file: {CONFIG_FILE}\n')


def inline_send_public_url():
    with open(WEBUI_FILE, 'r') as f:
        lines = f.readlines()

    # Check if the function exists in the file
    text_exists = False
    for line in lines:
        if 'send_public_url(share_url)' in line:
            text_exists = True

    # If the function already exists, exit
    if not text_exists:
        print('Function send_public_url already exists.\nWebUI send_public_url is already up to date.\n')

        # Insert the code to send the public URL
        lines.insert(7, 'from extensions.SendURL.send_msg import send_public_url\n')
        lines.insert(268, '        # Send public URL to Telegram\n')
        lines.insert(269, '        try:\n')
        lines.insert(270, '            send_public_url(share_url)\n')
        lines.insert(271, '        except Exception as e:\n')
        lines.insert(272, '            print(f"Error plugin SendURL: {e}")\n')
        lines.insert(273, '\n')

    # Write updated content to webui.py file
    with open(WEBUI_FILE, 'w') as f:
        f.writelines(lines)


if __name__ == '__main__':
    install_missing_libraries()
    check_config_exist()
    inline_send_public_url()