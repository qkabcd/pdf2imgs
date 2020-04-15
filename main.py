import os
from pdf2image import convert_from_path

# 获取输入目录下的pdf路径
def file_name(file_dir):   
    L=[]     
    for root, dirs, files in os.walk(file_dir):  
        for file in files:  
            if os.path.splitext(file)[1].lower() == '.pdf':
                L.append(os.path.join(root, file))  
    return L

# 按文件名建立目录
def createDir(oneFileDir):
    if not os.path.exists(oneFileDir):
        os.makedirs(oneFileDir)

# 按pdf文件名转换为以该pdf文件名的目录，并把jpg文件保存到该目录下
def convertPdtToDir(pdf_file_name):
    filePath,newDirName=os.path.split(pdf_file_name)
    # 判断是否为pdf结尾，pdf结尾就进行处理
    if newDirName[-3:].lower()=='pdf':
        newDir=newDirName[0:-4]
        createDir(newDir)
        pages = convert_from_path(newDirName)
        count = 0
        for page in pages:
            targetPic =os.path.join(newDir, 'page-' + str(count+1) + '.jpg')
            page.save(targetPic, 'JPEG')
            print(targetPic)
            count = count + 1 

    
if __name__=='__main__':
    pdfFiles=file_name('.')
    
    for name in pdfFiles:
         convertPdtToDir(name)
    print('恭喜，完成pdf转为jpg')