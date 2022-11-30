import gdown

url = '''https://docs.google.com/document/d/1T0433HfRFYlfZaEoTBRazhREwuVcXh6H/edit?usp=share_link&ouid=104676003970984958117&rtpof=true&sd=true'''
# share_url = '''https://drive.google.com/file/d/0B_Mf-2xGgrgISzBkNmlSdnY5b09OUFNmdC1NYVF5UUwxbGE0/view?usp=sharing&resourcekey=0--3ncBrR-9ViDobbpbVwgDg'''
# link_url = '''https://docs.google.com/document/d/1T0433HfRFYlfZaEoTBRazhREwuVcXh6H/edit?usp=share_link&ouid=104676003970984958117&rtpof=true&sd=true'''

output = "D:\\Python-Projects\\NLP\\File-validation\\"
f = ""

try:
    # a file
    f = gdown.download(url, quiet=False, fuzzy=True, output=output)

except Exception as e:
    try:
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
    print(type(f))
