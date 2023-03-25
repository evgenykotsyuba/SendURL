import launch
import os

req_file = os.path.join(os.path.dirname(os.path.realpath(__file__)), "requirements.txt")

with open(req_file) as file:
    for lib in file:
        lib = lib.strip()
        if not launch.is_installed(lib):
            launch.run_pip(f"install {lib}", f"SendURL/ requirement: {lib}")


config_file = os.path.join(os.path.dirname(os.path.realpath(__file__)), "config.ini")


def check_config_exist():
    if not os.path.isfile(config_file):
        lines = '[telegram]\nbot_token = \nchat_id = \n'
        with open(config_file, 'w') as f:
            f.writelines(lines)
        print(f'File config.ini empty...\nPlease insert in to file token and chat_id.\n{ config_file }\n')


def inline_send_public_url():
    # Get the absolute path to the webui.py file
    file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'webui.py'))

    # Read webui.py file
    with open(file_path, 'r') as f:
        lines = f.readlines()

    # Check if the function exists in the file
    text_exists = False
    for line in lines:
        if 'send_public_url(share_url)' in line:
            text_exists = True
            break
            exit()

    # If the function already exists, write the script
    if not text_exists:
        print('Function SendURL already exists.\nWebUI SendURL Updated...\n')

        # Insert the code to send the public URL
        lines.insert(7, 'from extensions.SendURL.send_msg import send_public_url\n')
        lines.insert(268, '        # Send public URL to Telegram\n')
        lines.insert(269, '        try:\n')
        lines.insert(270, '            send_public_url(share_url)\n')
        lines.insert(271, '        except Exception as e:\n')
        lines.insert(272, '            print(f"Error plugin SendURL: {e}")\n')
        lines.insert(273, '\n')

    # Write updated content to webui.py file
    with open(file_path, 'w') as f:
        f.writelines(lines)


check_config_exist()
inline_send_public_url()
