# from google_drive_downloader import GoogleDriveDownloader as gdd

# gdd.download_file_from_google_drive(file_id='1T0433HfRFYlfZaEoTBRazhREwuVcXh6H',
#                                     dest_path='D:\Python-Projects\NLP\File-validation\Resume\Try\mnist.zip',
#                                     unzip=True)

########################################################################################################################

import requests


def download_file_from_google_drive(id, destination):
    URL = "https://docs.google.com/uc?export=download"

    session = requests.Session()

    response = session.get(URL, params={'id': id, 'confirm': 1}, stream=True)
    token = get_confirm_token(response)

    if token:
        params = {'id': id, 'confirm': token}
        response = session.get(URL, params=params, stream=True)
    filename = response.headers['Content-Disposition'].split(';')[1]
    filename = filename.split('\"')[1]
    destination = destination + filename
    print(destination)
    save_response_content(response, destination)


def get_confirm_token(response):
    for key, value in response.cookies.items():
        if key.startswith('download_warning'):
            return value

    return None


def save_response_content(response, destination):
    CHUNK_SIZE = 32768

    with open(destination, "wb") as f:
        for chunk in response.iter_content(CHUNK_SIZE):
            if chunk: # filter out keep-alive new chunks
                f.write(chunk)


if __name__ == "__main__":
    file_id = '1T0433HfRFYlfZaEoTBRazhREwuVcXh6H'
    destination = r"D:\Python-Projects\NLP\File-validation\Resume\Try\\"
    download_file_from_google_drive(file_id, destination)

########################################################################################################################
''' import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# Define the SCOPES. If modifying it,
# delete the token.pickle file.
SCOPES = ['https://www.googleapis.com/auth/drive']


# Create a function getFileList with
# parameter N which is the length of
# the list of files.
def getFileList(N):
    # Variable creds will store the user access token.
    # If no valid token found, we will create one.
    creds = None

    # The file token.pickle stores the
    # user's access and refresh tokens. It is
    # created automatically when the authorization
    # flow completes for the first time.

    # Check if file token.pickle exists
    if os.path.exists('token.pickle'):
        # Read the token from the file and
        # store it in the variable creds
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)

    # If no valid credentials are available,
    # request the user to log in.
    if not creds or not creds.valid:

        # If token is expired, it will be refreshed,
        # else, we will request a new one.
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)

        # Save the access token in token.pickle
        # file for future usage
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    # Connect to the API service
    service = build('drive', 'v3', credentials=creds)

    # request a list of first N files or
    # folders with name and id from the API.
    resource = service.files()
    result = resource.list(pageSize=N, fields="files(id, name)").execute()

    # return the result dictionary containing
    # the information about the files
    return result


# Get list of first 5 files or
# folders from our Google Drive Storage
result_dict = getFileList(1)

# Extract the list from the dictionary
file_list = result_dict.get('files')

# Print every file's name
for file in file_list:
    print(file['name'])'''


'''import gdown

url = "https://docs.google.com/document/d/1T0433HfRFYlfZaEoTBRazhREwuVcXh6H/edit?usp=share_link&ouid=104676003970984958117&rtpof=true&sd=true"
output = "D:\\Python-Projects\\NLP\\File-validation\\Resume\\Try\\"
f = ""

Try:
    # a file
    f = gdown.download(url, quiet=False, fuzzy=True, output=output)

except Exception as e:
    Try:
        url_list = url.split('/')
        print(url_list)
        # same as the above, but with the file ID
        id = url_list[5]
        f = gdown.download(id=id, quiet=False, output=output)
    except Exception as e:
        print(f"cannot download the file{e}")

print(f)
if f is not None:
    f_list = f.split("\\")
    print(f_list[-1])
    print(str(f_list[-1]).split(".")[-1])
    print(len(f))
    print(type(f))'''

'''from __future__ import print_function

import io

import google.auth
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaIoBaseDownload


def download_file(real_file_id):
    """Downloads a file
    Args:
        real_file_id: ID of the file to download
    Returns : IO object with location.

    Load pre-authorized user credentials from the environment.
    TODO(developer) - See https://developers.google.com/identity
    for guides on implementing OAuth2 for the application.
    """
    creds, _ = google.auth.default()

    Try:
        # create drive api client
        service = build('drive', 'v3', credentials=creds)

        file_id = real_file_id

        # pylint: disable=maybe-no-member
        request = service.files().get_media(fileId=file_id)
        file = io.BytesIO()
        downloader = MediaIoBaseDownload(file, request)
        done = False
        while done is False:
            status, done = downloader.next_chunk()
            print(F'Download {int(status.progress() * 100)}.')

    except HttpError as error:
        print(F'An error occurred: {error}')
        file = None

    return file.getvalue()


if __name__ == '__main__':
    download_file(real_file_id='1T0433HfRFYlfZaEoTBRazhREwuVcXh6H')'''


########################################################################################################################
# import gdown
'''current_resume_directory = RESUME_DIRECTORY_PATH + "/" + str(candidate_id)
            if os.path.isdir(current_resume_directory):
                pass
            else:
                Try:
                    os.mkdir(current_resume_directory)
                except Exception as e:
                    logging.exception(f"Error creating parent directory {RESUME_DIRECTORY_PATH}: {e}")
                    continue

            resume_path = current_resume_directory + "/"
            f = ""
            Try:
                url_list = url.split('/')
                # same as the above, but with the file ID
                download_file_id = url_list[5]
                f = gdown.download(id=download_file_id, quiet=False, fuzzy=True, output=resume_path)
            except Exception as e:
                Try:
                    f = gdown.download(url, quiet=False, fuzzy=True, output=resume_path)
                except Exception as e:
                    logging.exception(f"cannot download the resume for candidate-id {candidate_id}: {e}")
            if f is not None:
                # f = f.replace("\\", "\\\\")
                # f_list = f.split("\\\\")
                f_list = f.split("/")'''
########################################################################################################################
