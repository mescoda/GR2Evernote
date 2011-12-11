# coding:utf-8

# for shared-items.json with title_num

import json,os
from HTMLParser import HTMLParser

directory = 'D:\gr'

if not os.path.exists(directory):
    os.mkdir(directory)

def write_withcontent_bycontenttag():
    try:
        title = str(num_title)+'. '+item['title'].replace(':','_')
        url = item['alternate'][0]['href']
        content = item['content']['content'].encode('utf-8')
        with open(directory+'/'+title+'.html', 'w') as output:
            output.write('<h1>'+title.encode('utf-8')+'</h1>')
            output.write('<a href="'+url+'">'+url+'</a>')
            output.write(content)
    except:
        title = str(num_title)+'. '+'Tweet'+str(num)
        url = item['alternate'][0]['href']
        content = item['content']['content'].encode('utf-8')
        with open(directory+'/'+title+'.html', 'w') as output:
            output.write('<h1>'+title.encode('utf-8')+'</h1>')
            output.write('<a href="'+url+'">'+url+'</a>')
            output.write(content)

def write_withcontent_bysummarytag():
    try:    #标题正常解析
        title = str(num_title)+'. '+item['title'].replace(':','_')
        url = item['alternate'][0]['href']
        content = item['summary']['content'].encode('utf-8')
        with open(directory+'/'+title+'.html', 'w') as output:
            output.write('<h1>'+title.encode('utf-8')+'</h1>')
            output.write('<a href="'+url+'">'+url+'</a>')
            output.write(content)
    except:     #标题极长无法正常解析 通常为分享的tweet
        title = str(num_title)+'. '+'Tweet'+str(num)
        url = item['alternate'][0]['href']
        content = item['summary']['content'].encode('utf-8')
        with open(directory+'/'+title+'.html', 'w') as output:
            output.write('<h1>'+title.encode('utf-8')+'</h1>')
            output.write('<a href="'+url+'">'+url+'</a>')
            output.write(content)

def write_withoutcontent():
    try:
        title = str(num_title)+'. '+item['title'].replace(':','_')
        url = item['alternate'][0]['href']
        with open(directory+'/'+title+'.html', 'w') as output:
            output.write('<h1>'+title.encode('utf-8')+'</h1>')
            output.write('<a href="'+url+'">'+url+'</a>')
    except:
        title = str(num_title)+'. '+'Tweet'+str(num)
        url = item['alternate'][0]['href']
        with open(directory+'/'+title+'.html', 'w') as output:
            output.write('<h1>'+title.encode('utf-8')+'</h1>')
            output.write('<a href="'+url+'">'+url+'</a>')

num = 0

with open('shared-items.json','r') as json_file:
    json_base = json.load(json_file,'utf-8')
    parser = HTMLParser()

    for item in json_base['items']:
        num = num + 1
        num_title = '%04d'%( num )
        try:    #分享时有内容
            try:    #json中有两种标记内容的tag 通过content提取内容
                write_withcontent_bycontenttag()
            except:     #通过summary提取内容
                write_withcontent_bysummarytag()
        except:     #分享时通过工具栏或其他插件导致json中没有内容只有链接或简介
            write_withoutcontent()