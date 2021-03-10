from urllib.request import urlopen
import moviepy.editor as mp

class Genel():
    def __init__(self):
        pass

    def download_video(self, link, name):
        rsp = urlopen(link)
        with open(name, 'wb') as f:
            f.write(rsp.read())

    def mp4_to_mp3(self, mp4_path, mp3_path):
        clip = mp.VideoFileClip(mp4_path).subclip(0,20)
        clip.audio.write_audiofile(mp3_path)

#if __name__ =="__main__":
    #genel = Genel()
    
    #genel.download_video('https://vcdn.ensonhaber.com//flv/flvideo/v/2019/03/1552756840.mp4','kauai.mp4')
    #genel.mp4_to_mp3("kauai.mp4", "theaudio.mp3")