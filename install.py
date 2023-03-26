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
    # Read file contents into memory
    with open(WEBUI_FILE, 'r') as f:
        lines = f.readlines()

    # Find index of specific block of text
    text_exists = False
    for i, line in enumerate(lines):
        if 'send_public_url(share_url)' in line:
            text_exists = True
            # print(f'line: {i} send_public_url exists')
            break

    if not text_exists:
        # Add missing text to file contents
        insert_index = None
        for i, line in enumerate(lines):
            if 'app, local_url, share_url' in line:
                preceding_whitespace = line[:len(line) - len(line.lstrip())]
                insert_index = i + 11
                new_lines = [
                    f"{preceding_whitespace}# Send public URL to Telegram\n",
                    f"{preceding_whitespace}try:\n",
                    f"{preceding_whitespace}    from extensions.SendURL.send_msg import send_public_url\n",
                    f"{preceding_whitespace}    send_public_url(share_url)\n",
                    f"{preceding_whitespace}except Exception as e:\n",
                    f"{preceding_whitespace}    print(f'Error plugin SendURL: {{e}}')\n",
                    "\n"
                ]
                lines = lines[:insert_index] + new_lines + lines[insert_index:]
                break

        if insert_index is None:
            # The expected block of text was not found, so don't modify the file contents
            print("send_public_url not found in expected location\n")
        else:
            # Write modified file contents back to file
            with open(WEBUI_FILE, 'w') as f:
                f.writelines(lines)

    return "Plugin SendURL ready..."


if __name__ == '__main__':
    install_missing_libraries()
    check_config_exist()
    inline_send_public_url()