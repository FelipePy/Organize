import os
from so import So


class Organizer:

    def __init__(self):
        self.audios_ext = ['.mp3', '.wav', '.wma', '.ogg', '.aiff', '.pcm', '.flac']
        self.videos_ext = ['.mp4', '.m4v', '.mov', '.avi', '.mov', '.mpg', '.mpeg', '.wmv']
        self.images_ext = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.psd', '.exif', '.raw']
        self.documents_ext = ['.txt', '.log', '.pdf', '.docx', '.pptx', '.word', '.xlsx', '.ppt', '.psd', '.cdr', '.ai']
        self.programs_ext = ['.exe', '.py', '.c', '.cpp', '.js', '.zip', '.rar', '.bin', '.sh', '.ini', '.jar', '.java',
                             '.jav',
                             '.izh', '.msi']
        self.so = So()

    def organizer(self, directory):
        aud = [0, "Audios"]
        img = [0, "Imagens"]
        vid = [0, "Videos"]
        doc = [0, "Documentos"]
        pro = [0, "Programas"]
        out = [0, "Outros"]
        abrev = [aud, img, vid, doc, pro, out]
        folders = ["Audios", "Imagens", "Videos", "Documentos", "Programas", "Outros"]
        formats = [self.audios_ext, self.images_ext, self.videos_ext, self.documents_ext, self.programs_ext]
        self.create_folders = []
        counter = 0
        archives_names = os.listdir(directory)

        for archive in archives_names:
            new_folder = str(os.path.join(directory, folders[0]))
            if os.path.isfile(os.path.join(directory, archive)):
                counter += 1
                count = 0
                extension = self.get_extension(archive)

                for format in formats:
                    if extension in format:
                        new_folder = os.path.join(directory, folders[count])
                        if folders[count] == abrev[count][1]:
                            self.create_folder(new_folder)
                            abrev[count][0] += 1
                            break

                    count += 1
                    if folders[count] == "Outros":
                        self.create_folder(new_folder)
                        out[0] += 1
                    new_folder = os.path.join(directory, folders[-1])

                old = os.path.join(directory, archive)
                new = os.path.join(new_folder, archive)
                os.rename(old, new)

                index = new_folder.rfind('/')
                print(f"Moveu o \033[33m{archive}\033[0m de", directory, "->", new_folder[index:])

        print(f"\n\nSistema Operacional -> {self.so.get_so()}")
        print(f"\033[34mTotal de arquivos organizados -> \033[0m\033[31m{counter}\033[0m")

        if counter > 0:
            print("\n\033[34mArquivos em cada pasta\033[0m")
            for abv in abrev:
                if abv[0] > 0:
                    print(abv[1], "->", abv[0])

            print('\n\033[34mPastas criadas\033[0m')
            for folder in self.create_folders:
                index = folder.rfind('/')
                print(f"-> {folder[index + 1:]}")

    def create_folder(self, folder):
        folder = os.path.join(folder)
        if not os.path.isdir(folder):
            os.mkdir(folder)
            self.create_folders.append(folder)

    def check_arguments(self):
        print("Verificou os argumentos")
        pass

    def get_extension(self, archive):
        index = archive.rfind('.')
        return archive[index:]