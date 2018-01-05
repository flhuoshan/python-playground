#! python3
# this program is used for operatrion file


def create_file(file_name):
    f = open(file_name,'w')
    f.close()


def read_file(file_name):
    f = open(file_name, 'r')
    lines = f.readlines()
    for line in lines:
        print(line,end='')
    f.close()


def add_file(file_name, content):
    f = open(file_name, 'a')
    f.writelines(content + '\n')
    print(f.tell())
    f.close()


def add_file_batch(file_name, content_list):
    f = open(file_name, 'a')
    for content in content_list:
        f.writelines(content + '\n')
    f.close()


def copy_single_file(src, dest):
    filesrc = None
    filedest = None
    try:
        filesrc = open(src, 'r')
        src_lines = filesrc.readlines()
        filedest = open(dest, 'w')
        filedest.writelines(src_lines)
        filesrc.close()
        filedest.close()
    except FileNotFoundError as e:
        if filesrc != None:
            filesrc.close()
        if filedest != None:
            filedest.close()
        print(e)


if __name__ == '__main__':
    create_file('1234.txt')
    content_list = ['abc','def','hij']
    add_file('1234.txt','2332443')
    add_file('1234.txt', '2332444')
    read_file('1234.txt')
    add_file_batch('1234.txt',content_list)
    read_file('1234.txt')
    copy_single_file('1234.txt', 'abc/4321.txt')
    print("abc")


