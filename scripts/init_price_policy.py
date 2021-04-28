import base
from web import models


def run():
    exists = models.PricePolicy.objects.filter(category=1, title="免费版").exists()
    if not exists:
        models.PricePolicy.objects.create(
            category=1,
            title="免费版",
            price=0,
            project_num=5,
            project_space=8,
            per_file_size=1
        )


if __name__ == '__main__':
    run()
