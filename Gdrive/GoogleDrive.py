from pydrive2.auth import GoogleAuth
from pydrive2.drive import GoogleDrive


def login():
    gauth = GoogleAuth()
    gauth.LoadCredentialsFile('credentials_module.json')
    if gauth.access_token_expired:
        gauth.Refresh()
    else:
        gauth.Authorize()
    return GoogleDrive(gauth)

def load_file(path_file, id_dir):
    creds = login()
    file = creds.CreateFile({'parents': [{'kind': 'drive#fileLink', 'id': id_dir}]})
    file['title'] = path_file.split('/')[-1]
    file.SetContentFile(path_file)
    file.Upload()
    print ('file uploaded')

# def create_dir(name_directory)

if __name__ == "__main__":
    id = '1-4hWvU7jA0e8kn3a70VCGKLXv3C8m1AM'
    load_file('aaa.jpeg', id)
