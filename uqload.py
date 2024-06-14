from validations.input_validations import is_uqload_url, is_string_empty
from video_downloader import VideoDownloader
from bs4 import BeautifulSoup
import requests, re, colorama, datetime

class UQLoad:
    def __init__(self, url: str) -> None:
        self.video_url = None
        self.url = self.__validate_url(url)
    
    def __validate_url(self, url: str) -> str:
        if is_string_empty(url):
            raise ValueError("URL must be a non-empty string")
        
        
        if not is_uqload_url(url):
            raise ValueError(
                "Invalid uqload URL. Example: https://uqload.co/xxxxxxxxxxxx.html"
                )
        return url.strip()
    
    def download(self, video_name: str) -> None:
        self.__get_video()
        if self.video_url is not None:
            if video_name is None:
                video_name = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
            downloader = VideoDownloader(url=self.video_url, filename=video_name)
            downloader.download()
    
    
    def __get_video(self) -> None:
        response = requests.get(url=self.url, stream=True)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')
        
        scripts = soup.find_all('script')
        
        if scripts:
            video_regex = r'https?://.*?v\.mp4'
            match = re.search(video_regex, str(scripts))
            if match:
                self.video_url = match.group(0)
                print(f"\n{colorama.Fore.LIGHTGREEN_EX}Video trouvée: {self.video_url}")
                print(f"{colorama.Fore.LIGHTGREEN_EX}Discord: Senko.bin\n")
            else:
                raise Exception("Video Not Found! :(")
        else:
            raise Exception(f"{response.text} :(")