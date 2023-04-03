from api_handlers.checker import all_comments
from db.get_keywords import get_keywords_list


def main():
    keyword_lst = get_keywords_list()
    comments = all_comments()
    for keyword in keyword_lst:
        for comment in comments:
            if keyword in comment[0]:
                print(keyword, comment)


if __name__ == "__main__":
    main()
