""" A python script to update the #song section (My latest song addiction) in index.html """

from datetime import datetime
from sys import argv

TEMPLATE: str = """<article id="song" class="block">
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
    </article>"""


def main() -> None:

    # Get the timestamp of right now
    time: datetime = datetime.now()
    timezone: str = "UTC+8" # Replace this if needed
    timestamp: str = time.strftime("%Y, %B %d (%H:%M)") + f" {timezone}"

    # Get url
    url: str
    if len(argv) != 2:
        # URL not found in args
        url = input("Song URL:    ")
    else:
        # URL is in args
        url = argv[1]
    url = convert_url(url)

    # Prompt for other data
    artist: str = input("Artist Name: ").strip()
    title:  str = input("Song Title:  ").strip()

    # Create the new html code for the #song section
    html_block: str = TEMPLATE.format(url=url, timestamp=timestamp)

    # Overwrite index.html
    with open("index.html", "r+", encoding="utf8") as f:
        text: str = f.read()
        new_text: str = overwrite_songs_block(text, html_block)

        f.seek(0)
        f.write(new_text)
        f.truncate()

    print(f"Updated index.html! - {timestamp}")
    print(f"Update song addiction to {artist} [ {title} ]")


def convert_url(url: str) -> str:
    """ Converts a youtu.be url to an embed url """

    SHARE_LINK: str = "https://youtu.be/"
    EMBED_LINK: str = "https://www.youtube.com/embed/"
    if url.startswith(SHARE_LINK):
        url = url.replace(SHARE_LINK, "")
        url = EMBED_LINK + url
        return url

    elif url.startswith(EMBED_LINK):
        return url

    else:
        raise ValueError("To ensure no errors, please use YouTube's Share button to get the URL of the video.")


def overwrite_songs_block(html: str, new_songs_block: str) -> str:

    start: int = html.find('<article id="song" class="block">')
    end:   int = html.find("</article>", start) + len("</article>")

    return html[0:start] + new_songs_block + html[end:]


if __name__ == "__main__":
    main()
