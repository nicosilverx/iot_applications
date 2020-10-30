if __name__=="__main__":
    file_to_read = open('original.txt.txt', 'r')
    file_to_write = open('copy.txt', 'w')

    file_content = file_to_read.read()
    print(file_content)

    file_to_write.write(f"The content of the original file is: {file_content}")

    file_to_read.close()
    file_to_write.close()
