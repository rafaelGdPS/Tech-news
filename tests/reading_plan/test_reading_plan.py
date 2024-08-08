import pytest
from tech_news.analyzer.reading_plan import ReadingPlanService  # noqa: F401, E261, E501
from unittest.mock import patch


mock_db_news = [
        {"title": "Noticia 1", "reading_time": 1},
        {"title": "Noticia 2", "reading_time": 5},
        {"title": "Noticia 3", "reading_time": 10},
        {"title": "Noticia 4", "reading_time": 25},
        {"title": "Noticia 5", "reading_time": 60},
    ]

result = {
    "readable": [
        {
            "unfilled_time": 4,
            "chosen_news": [
                (
                    "Noticia 1",
                    1,
                ),
                (
                    "Noticia 2",
                    5,
                ),
            ],
        },
        {
            "unfilled_time": 0,
            "chosen_news": [
                (
                    "Noticia 3",
                    10,
                )
            ],
        },
    ],
    "unreadable": [
        ("Noticia 4", 25),
        ("Noticia 5", 60),
    ],
}


@patch(
        "tech_news.analyzer.reading_plan.ReadingPlanService._db_news_proxy",
        return_value=mock_db_news
        )
def test_reading_plan_group_news(find_news):

    with pytest.raises(
        ValueError, match="Valor 'available_time' deve ser maior que zero"
    ):
        ReadingPlanService.group_news_for_available_time(0)

    reading_plan = ReadingPlanService.group_news_for_available_time(10)
    assert reading_plan == result
