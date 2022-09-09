import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token
        
    def upload_file(self, file_from, file_to):
        """Upload a file to dropbox using API v2 """
        dbx = dropbox.Dropbox(self.access_token)
        
        with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(), file_to)
            

def main():
    access_token = 'sl.BO2VVrZGpBDyF_fEcinF0qtzJ61EF8yylYVHfazwtPG7K0prO9hVyb4i3JOhxB8kp8PcaATzMBcQsokwpWSbfjbhCOfjw06Ko-iOWI0331Y3Nj9ZuD6kXdZl7WxTo_CUKKpqajp3DW9N'
    transferData = TransferData(access_token)

    file_from = 'test.txt'
    file_to = '/personal/test.txt'  # The full path to upload the file to, including the file name

    # API v2
    transferData.upload_file(file_from, file_to)

if __name__ == '__main__':
    main()