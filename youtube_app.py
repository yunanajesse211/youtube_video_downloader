import streamlit as st
from pytube import YouTube

class YouTubeDownloader:
    def __init__(self):
        st.title("YouTube Video Downloader")
        self.url = st.text_input("Enter YouTube Video URL:")
        self.resolutions = ["2160p","1440p","1080p","720p", "360p", "240p"]
        self.resolution = st.selectbox("Select Resolution:", self.resolutions)
        self.download_button = st.button("Download Video")
        self.progress_bar = st.progress(0.0)

    def download_video(self):
        try:
            if self.url:
                yt = YouTube(self.url)
                video = yt.streams.filter(res=self.resolution).first()
                if video:
                    st.success(f"Downloading: {yt.title} ({self.resolution})")
                    video.download()
                    st.success("Download completed successfully!")
                else:
                    st.error("No video with the specified resolution found.")
            else:
                st.warning("Please enter a valid YouTube Video URL.")
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")

    def on_progress(self, stream, chunk, remaining):
        total_size = stream.filesize
        bytes_downloaded = total_size - remaining
        percentage = (bytes_downloaded / total_size) * 100.0
        self.progress_bar.progress(percentage)

    def run(self):
        if self.download_button:
            # Clear progress bar
            self.progress_bar.empty()
            with st.spinner("Downloading in progress..."):
                self.download_video()

if __name__ == "__main__":
    downloader = YouTubeDownloader()
    downloader.run()
