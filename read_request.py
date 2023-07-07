import json

def open_file():
    file_name = "test.txt"
    # file_name = "test_json.txt"
    r = open(file_name,"r",encoding="utf-8")
    request = r.read()
    r.close()
    re_list = request.split('\n')
    return re_list

#  获取区分header和body的行号
def get_num():
    re_list = open_file()
    for i in re_list:
        if i == '':
            return re_list.index(i)
    return -1


# 获取请求头部
def get_header():
    re_list = open_file()
    i = get_num()
    if i == -1:
        print("格式错误，header和body需要有空行分割")
    headers = {}
    for data in re_list[:i]:
        data = data.split("\n")
        if ":" not in data[0]:
            continue
        k_v_list = data[0].split(":",1)
        headers[k_v_list[0]]=k_v_list[1]
    return headers



# 判断是否为json数据
def is_json(text):
    try:
        json.loads(text)
        return True
    except ValueError:
        return False

# 获取请求体
def get_body():
    re_list = open_file()
    i = get_num()
    if i == -1:
        print("格式错误，header和body需要有空行分割")
    # bodys1 = {}
    # bodys2 = ""
    for data in re_list[i+1:]:
        if data == "":
            continue
        if is_json(data):
            return json.loads(data)
        else:
            return data

headers = get_header()
print(headers)
bodys = get_body()
print(bodys)




