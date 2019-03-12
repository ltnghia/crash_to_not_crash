import requests, os, shutil

def download_file_from_google_drive(id, destination):
    URL = "https://docs.google.com/uc?export=download"

    session = requests.Session()

    response = session.get(URL, params = { 'id' : id }, stream = True)
    token = get_confirm_token(response)

    if token:
        params = { 'id' : id, 'confirm' : token }
        response = session.get(URL, params = params, stream = True)

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

def mkdir(path):
    if not os.path.exists(path):
        os.makedirs(path)

def download_and_extract(file_id, dst, final_dst):
    print("downloading {}...".format(dst))
    download_file_from_google_drive(file_id, dst)
    print("download completed!")

    print("extracting...")
    mkdir(final_dst)
    mkdir("./datasets/temp")
    os.system("tar -xf {} --strip-components=1 -C ./datasets/temp".format(dst))
    files = os.listdir("./datasets/temp/")
    for f in files:
            shutil.move("./datasets/temp/"+f, final_dst)
    os.system("rm -r ./datasets/temp")
    print("extraction completed!")

    os.system("rm {}".format(dst))
    print("zip file removed")

if __name__ == "__main__":
    # # Accident Images Part 1
    # file_id = str("1xTqFxguYxvF8zf7_e_clAq2GTq1Wi3vC")
    # dst = str("./datasets/GTACrash_accident_images_part1.tar.gz")
    # final_dst = str("./datasets/GTACrash/accident")
    # download_and_extract(file_id, dst, final_dst)

    # Accident Labels Part 1
    file_id = str("1FRf8qBPDVMsbLVLa3LVzcffxLVC97MO9")
    dst = str("./datasets/GTACrash_accident_labels_part1.tar.gz")
    final_dst = str("./datasets/GTACrash/accident")
    download_and_extract(file_id, dst, final_dst)

    # # Accident Images Part 2
    # file_id = str("1K_wEYFvyqMI_Dq_Au8d97Fb23RgCzS40")
    # dst = str("./datasets/GTACrash_accident_images_part2.tar.gz")
    # final_dst = str("./datasets/GTACrash/accident")
    # download_and_extract(file_id, dst, final_dst)

    # Accident Labels Part 2
    file_id = str("15H9qwpXdw3MyagBIRdbR5xKVh0WSGemg")
    dst = str("./datasets/GTACrash_accident_labels_part2.tar.gz")
    final_dst = str("./datasets/GTACrash/accident")
    download_and_extract(file_id, dst, final_dst)

    # # Accident Images Part 3
    # file_id = str("1JjuJ-h670FWYsaZ5V7XMGPNg8QNertRU")
    # dst = str("./datasets/GTACrash_accident_images_part3.tar.gz")
    # final_dst = str("./datasets/GTACrash/accident")
    # download_and_extract(file_id, dst, final_dst)

    # # Accident Labels Part 3
    # file_id = str("1ORimytITwqxiK3QeLnKONZMVeVF-m1Qo")
    # dst = str("./datasets/GTACrash_accident_labels_part3.tar.gz")
    # final_dst = str("./datasets/GTACrash/accident")
    # download_and_extract(file_id, dst, final_dst)

    # # Nonaccident Images Part 1
    # file_id = str("1fSEqEvhDm-vKm4ZPSddn08w6NuV3Zm4l")
    # dst = str("./datasets/GTACrash_nonaccident_images_part1.tar.gz")
    # final_dst = str("./datasets/GTACrash/nonaccident")
    # download_and_extract(file_id, dst, final_dst)

    # # Nonaccident Labels Part 1
    # file_id = str("18-jLdiZ85bWVRDHwGAKBXdtXylx2xs5y")
    # dst = str("./datasets/GTACrash_nonaccident_labels_part1.tar.gz")
    # final_dst = str("./datasets/GTACrash/nonaccident")
    # download_and_extract(file_id, dst, final_dst)

    # # Nonaccident Images Part 2
    # file_id = str("1Q8xQMWrdbzSTjCa8Cr68Cnx1gN5DxTfP")
    # dst = str("./datasets/GTACrash_nonaccident_images_part2.tar.gz")
    # final_dst = str("./datasets/GTACrash/nonaccident")
    # download_and_extract(file_id, dst, final_dst)

    # # Nonaccident Labels Part 2
    # file_id = str("1DQzx--L41kdztYkJKExplYyXSyFawgdi")
    # dst = str("./datasets/GTACrash_nonaccident_labels_part2.tar.gz")
    # final_dst = str("./datasets/GTACrash/nonaccident")
    # download_and_extract(file_id, dst, final_dst)