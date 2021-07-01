"""A video player class."""
import random
from .video_library import VideoLibrary


class VideoPlayer:
    """A class used to represent a Video Player."""

    def __init__(self):
        self._video_library = VideoLibrary()

    def number_of_videos(self):
        num_videos = len(self._video_library.get_all_videos())
        print(f"{num_videos} videos in the library")

    def show_all_videos(self):
        """Returns all videos."""
        print("Here's a list of all available videos:")
        videos = self._video_library.get_all_videos()

        for video in videos:
            vtag = " ".join(video.tags)
            print(f"{video.title} ({video.video_id}) [{vtag}]")

    def get_video_onstatus(self,videomode):
        """Returns video thats playing."""
        videos = self._video_library.get_all_videos()
        for video in videos:
            if video._video_status == videomode:
                return video
        return None

    def play_video(self, video_id):
        """Plays the respective video.

        Args:
            video_id: The video_id to be played.
        """
        video = self._video_library.get_video(video_id)
        if video is None:
            print(f"Cannot play video: Video does not exist")
        else:
            playvideo = self.get_video_onstatus(1)
            pausevideo = self.get_video_onstatus(2)
            if playvideo is None and pausevideo is None:
                print(f"Playing video: {video.title}")
                video._video_status = 1
            else:
                if pausevideo is not None:
                    print(f"Stopping video: {pausevideo.title}")
                    print(f"Playing video: {video.title}")
                    pausevideo._video_status = 0
                    video._video_status = 1

                else :
                    print(f"Stopping video: {playvideo.title}")
                    print(f"Playing video: {video.title}")
                    playvideo._video_status = 0
                    video._video_status = 1


    def stop_video(self):
        """Stops the current video."""
        playvideo = self.get_video_onstatus(1)
        pausevideo = self.get_video_onstatus(2)
        if playvideo is None and pausevideo is None:
            print("Cannot stop video: No video is currently playing")

        if playvideo is not None:
            print(f"Stopping video: {playvideo.title}")
            playvideo._video_status = 0

        if pausevideo is not None:
            print(f"Stopping video: {pausevideo.title}")
            pausevideo._video_status = 0

    def play_random_video(self):
        """Plays a random video from the video library."""
        randomvideo=random.choice(self._video_library.get_all_videos())
        playvideo = self.get_video_onstatus(1)
        if playvideo is None:
            print(f"Playing video: {randomvideo.title}")
            randomvideo._video_status = 1
        else:
            print(f"Stopping video: {playvideo.title}")
            print(f"Playing video: {randomvideo.title}")
            playvideo._video_status = 0
            randomvideo._video_status = 1

    def pause_video(self):
        """Pauses the current video."""
        pausevideo = self.get_video_onstatus(2)
        playvideo = self.get_video_onstatus(1)
        if pausevideo is None:
            if playvideo is None:
                 print("Cannot pause video: No video is currently playing")
            else:
                print(f"Pausing video: {playvideo.title}")
                playvideo._video_status = 2

        else:
            print(f"Video already paused: {pausevideo.title}")


    def continue_video(self):
        """Resumes playing the current video."""
        pausevideo = self.get_video_onstatus(2)
        playvideo = self.get_video_onstatus(1)
        if pausevideo is None and playvideo is None:
            print("Cannot continue video: No video is currently playing")
        if pausevideo is not None:
            print(f"Continuing video: {pausevideo.title}")
            pausevideo._video_status = 1
        if playvideo is not None:
            print(f"Cannot continue video: Video is not paused")

    def show_playing(self):
        """Displays video currently playing."""
        playvideo = self.get_video_onstatus(1)
        pausevideo = self.get_video_onstatus(2)
        if playvideo is not None:
            vtag = " ".join(playvideo.tags)
            print(f"Currently playing: {playvideo.title} ({playvideo.video_id}) [{vtag}]")
        if pausevideo is not None:
            vtag = " ".join(pausevideo.tags)
            print(f"Currently playing: {pausevideo.title} ({pausevideo.video_id}) [{vtag}] - PAUSED")
        if pausevideo is None and playvideo is None:
            print("No video is currently playing")

    def create_playlist(self, playlist_name):
        """Creates a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("create_playlist needs implementation")

    def add_to_playlist(self, playlist_name, video_id):
        """Adds a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be added.
        """
        print("add_to_playlist needs implementation")

    def show_all_playlists(self):
        """Display all playlists."""

        print("show_all_playlists needs implementation")

    def show_playlist(self, playlist_name):
        """Display all videos in a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("show_playlist needs implementation")

    def remove_from_playlist(self, playlist_name, video_id):
        """Removes a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be removed.
        """
        print("remove_from_playlist needs implementation")

    def clear_playlist(self, playlist_name):
        """Removes all videos from a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("clears_playlist needs implementation")

    def delete_playlist(self, playlist_name):
        """Deletes a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("deletes_playlist needs implementation")

    def search_videos(self, search_term):
        """Display all the videos whose titles contain the search_term.

        Args:
            search_term: The query to be used in search.
        """
        print("search_videos needs implementation")

    def search_videos_tag(self, video_tag):
        """Display all videos whose tags contains the provided tag.

        Args:
            video_tag: The video tag to be used in search.
        """
        print("search_videos_tag needs implementation")

    def flag_video(self, video_id, flag_reason=""):
        """Mark a video as flagged.

        Args:
            video_id: The video_id to be flagged.
            flag_reason: Reason for flagging the video.
        """
        print("flag_video needs implementation")

    def allow_video(self, video_id):
        """Removes a flag from a video.

        Args:
            video_id: The video_id to be allowed again.
        """
        print("allow_video needs implementation")
