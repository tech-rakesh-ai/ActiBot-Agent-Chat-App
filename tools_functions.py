import requests
from requests.auth import HTTPBasicAuth
import streamlit as st


# Define tool for creating a website
def create_website_func(membershipType: str, name: str):
    """
    Create a website on Liferay.

    :param membershipType: Membership Type of the website like open, private.
    :param name: Website Name
    :return: Response
    """
    data = {
        "membershipType": membershipType,
        "name": name
    }
    # Function to call Liferay API based on intent
    auth = HTTPBasicAuth(st.secrets['USERNAME'], st.secrets['PASSWORD'])

    url = st.secrets['LIFERAY_BASE_URL'] + "headless-site/v1.0/sites"
    headers = {'accept': 'application/json', 'Content-Type': 'application/json'}

    response = requests.post(url, auth=auth, headers=headers, json=data)

    if response.status_code in [200, 201]:
        response_data = f"Website created successfully! Response: {response.json()}"
        print(response_data)
        return response_data
    else:
        response_data = f"Website creation failed! Response: {response.text}"
        print(response_data)
        return response_data


# Define tool for creating a user
def create_user_func(alternateName: str, emailAddress: str, familyName: str, givenName: str):
    """
    Create a user on Liferay.
    :param alternateName: User's name
    :param emailAddress: User's email address
    :param familyName: User's family name
    :param givenName: User's first name
    :return: Response
    """
    user_data = {
        "alternateName": alternateName,
        "emailAddress": emailAddress,
        "familyName": familyName,
        "givenName": givenName
    }
    auth = HTTPBasicAuth(st.secrets['USERNAME'], st.secrets['PASSWORD'])
    url = st.secrets['LIFERAY_BASE_URL'] + "headless-admin-user/v1.0/user-accounts"

    headers = {'accept': 'application/json', 'Content-Type': 'application/json'}

    response = requests.post(url, auth=auth, headers=headers, json=user_data)

    if response.status_code in [200, 201]:
        response_data = f"User created successfully! Response: {response.json()}"
        print(response_data)
        return response_data

    else:
        response_data = f"User creation failed! Response: {response.text}"
        print(response_data)
        return response_data


import requests
from requests.auth import HTTPBasicAuth
from typing import Optional


def get_user_list_func(
        page: Optional[int] = 1,
        pageSize: Optional[int] = 20,
        filter: Optional[str] = None,
        search: Optional[str] = None,
        sort: Optional[str] = None
):
    """
    Get users from Liferay with pagination, filtering, searching, and sorting.
    :param page: Page number to retrieve.
    :param pageSize: Number of users per page.
    :param filter: Filter condition for the query.
    :param search: Search term for the query.
    :param sort: Sort condition for the query.
    :return: Filtered response
    """
    auth = HTTPBasicAuth(st.secrets['USERNAME'], st.secrets['PASSWORD'])
    url = f"{st.secrets['LIFERAY_BASE_URL']}headless-admin-user/v1.0/user-accounts"

    headers = {'accept': 'application/json', 'Content-Type': 'application/json'}

    # Adding query parameters to the request
    params = {
        "page": page,
        "pageSize": pageSize,
        "filter": filter,
        "search": search,
        "sort": sort
    }

    # Removing None values from params
    params = {k: v for k, v in params.items() if v is not None}

    print("PARAMS-----------------------", params)

    response = requests.get(url, auth=auth, headers=headers, params=params)
    if response.status_code in [200, 201]:
        print("RESPONSE-----------------------", response.json())
        users = response.json().get('items', [])
        filtered_users = []

        for user in users:
            user_info = {
                "id": user.get('id'),
                "name": f"{user.get('givenName', '')} {user.get('familyName', '')}",
                "emailAddress": user.get('emailAddress'),
                "status": user.get('status'),
                "websites": len(user.get('siteBriefs', []))
            }
            filtered_users.append(user_info)

        response_data = f"Users list retrieved successfully! Filtered Response: {filtered_users}"
        print(response_data)
        return response_data
    else:
        response_data = f"Failed to retrieve user list: {response.text}"
        print(response_data)
        return response_data
