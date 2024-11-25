import requests
from selectolax.parser import HTMLParser
import os
from tqdm import tqdm
from dotenv import load_dotenv

load_dotenv()


cookie = os.environ["COOKIE"]
headers = {
    "cookie": str(cookie),
    "Referer": "https://training.talkpython.fm/courses/all",
}


def get_courses_url():
    url = "https://training.talkpython.fm/account/"

    response = requests.get(url, headers=headers)
    html = HTMLParser(response.text)
    courses = html.css("#courses table a")[1:]

    return courses


def get_video_info(video_url, video_title, module_tile, course_title):

    cwd = os.getcwd()
    path = os.path.join(cwd, "talk-python", course_title, module_tile, video_title)

    os.makedirs(path, exist_ok=True)

    response = requests.get(video_url, headers=headers, stream=True)

    if response.status_code == 200:
        with open(os.path.join(path, "video.webm"), "wb") as f:
            for chunk in tqdm(
                response.iter_content(chunk_size=1024),
                desc=f"module {module_tile} - lecture {video_title}",
                unit="KB",
                unit_scale=True,
            ):
                if chunk:
                    f.write(chunk)
    else:
        print(f"Erro ao baixar o vídeo: {response.status_code}")


def get_course_info(course_url):
    r = requests.get(course_url, headers=headers)
    html = HTMLParser(r.text)

    course_title = html.css_first(
        ".container.full-page-content.course-details-page div h1"
    ).text()
    module_title = None
    conter = 0
    for row in html.css("table.table.borderless tr"):
        if row.id:
            module_title = row.css_first("td a").text()
            continue

        lectureTitle = (
            f"{conter} - {row.css_first('td .lecture-title-column a span').text()}"
        )
        conter += 1

        lectureLink = row.css_first("td .lecture-title-column a").attrs["href"]
        lectureID = lectureLink.split("/")[-1]

        vidoe_url = f"https://training.talkpython.fm/player/video/{lectureID}?format=webm&resolution=720p"

        get_video_info(
            video_url=vidoe_url,
            video_title=lectureTitle,
            module_tile=module_title,
            course_title=course_title,
        )


def scrape():
    base_url = "https://training.talkpython.fm"
    courses = get_courses_url()

    for course in courses:
        course_link = course.attributes["href"]
        finalCourseURL = f"{base_url}{course_link}"
        get_course_info(finalCourseURL)


if __name__ == "__main__":
    scrape()
