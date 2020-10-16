"""Admin email handler."""
# Third-Party Libraries
import requests
from utils.message_handling import error_msg
from utils.settings import URL, auth


def generate_admin_email():
    """Generate an admin email for a specified live site domain."""
    domain_name = input("Please enter a live domain name: ")

    resp = requests.get(
        f"{URL}/api/generate-email-address/?domain={domain_name}",
        headers=auth,
    )
    try:
        resp.raise_for_status()
    except requests.exceptions.HTTPError as e:
        error_msg(str(e))
        return

    print(resp.json())
    return resp.json()
