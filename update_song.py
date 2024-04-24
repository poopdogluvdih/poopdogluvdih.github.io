from datetime import datetime
from sys import argv

TEMPLATE: str = """
      <article id="song" class="block">
      <h1>My latest song addiction</h1>
      <br />
      <div style="display: flex; justify-content: center">
        <iframe
          width="560"
          height="315"
          src="{url}"
          title="YouTube video player"
          frameborder="0"
          allow="accelerometer; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
          referrerpolicy="strict-origin-when-cross-origin"
          allowfullscreen
        ></iframe>
      </div>
      <p style="text-align: center; color: #d1d1d1; font-style: italic">
        Last Update: {timestamp}
      </p>
    </article>
"""

def main() -> None:

    # Get the timestamp of right now
    time: datetime = datetime.now()
    timestamp: str = time.strftime("%Y, %B %d (%H:%M) %z")

    # Get url
    url: str
    if len(argv) != 2:
        # URL not found in args
        url = input("Song URL: ")
    else:
        # URL is in args
        url = argv[1]
    url = convert_url(url)

    html_block: str = TEMPLATE.format(url=url, timestamp=timestamp)
    print(html_block)


def convert_url(url: str) -> str:
    """ Converts a youtu.be url to an embed url """

    SHARE_LINK: str = "https://youtu.be/"
    EMBED_LINK: str = "https://www.youtube.com/embed/"
    if url.startswith(SHARE_LINK):
        url = url.replace(SHARE_LINK, "")
        url = EMBED_LINK + url
        return url

    else:
        raise ValueError("To ensure no errors, please use YouTube's Share button to get the URL of the video.")


if __name__ == "__main__":
    main()
