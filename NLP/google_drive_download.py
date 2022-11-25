import gdown

try:
    # a file
    url = '''https://docs.google.com/document/d/1T0433HfRFYlfZaEoTBRazhREwuVcXh6H/edit?usp=share_link&ouid=104676003970984958117&rtpof=true&sd=true'''
    # share_url = '''https://drive.google.com/file/d/0B_Mf-2xGgrgISzBkNmlSdnY5b09OUFNmdC1NYVF5UUwxbGE0/view?usp=sharing&resourcekey=0--3ncBrR-9ViDobbpbVwgDg'''
    # link_url = '''https://docs.google.com/document/d/1T0433HfRFYlfZaEoTBRazhREwuVcXh6H/edit?usp=share_link&ouid=104676003970984958117&rtpof=true&sd=true'''
    output = "resume.docx"
    f = gdown.download(url, quiet=False, fuzzy=True)
    print(f)
    print(type(f))
except Exception as e:
    try:
        url_list = url.split('/')
        print(url_list)
        # same as the above, but with the file ID
        id = url_list[5]
        gdown.download(id=id, quiet=False)
    except Exception as e:
        print(f"cannot download the file{e}")
