def copy_file(source, dest, buffer_size=2048):


        with open(source, 'rb') as source_file,\
                open(dest, 'wb') as dest_file:
            while True:
                data = source_file.read(buffer_size)
                if not data:
                    break
                dest_file.write(data)
                print(f"{len(data)} copied successfully ")




source_path = 'source.txt'
dest_path = 'dest.txt.txt'

copy_file(source_path, dest_path)