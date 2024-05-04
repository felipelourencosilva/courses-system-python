class Video:
    def __init__(video_url: str):
        self.__video_url = video_url

    @property
    def video_url(self) -> str:
        return self.__video_url

    @video_url.setter
    def video_url(self, video_url):
        if isinstance(video_url, str):
            self.__video_url = video_url
