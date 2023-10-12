from django.urls import path

from games.views import (
    AnagramHuntView,
    GameScoreView,
    GameScoreDetailView,
    MathFactsPlayView,
    MathFactsView,
    record_score,
)

app_name = "games"
urlpatterns = [
    path("anagram-hunt/", AnagramHuntView.as_view(), name="anagram-hunt"),
    path("math-facts/", MathFactsView.as_view(), name="math-facts"),
    path("math-facts/play/", MathFactsPlayView.as_view(), name="math-facts-play"),
    path("record-score/", record_score, name="record-score"),
    path("game-scores/", GameScoreView.as_view(), name="game-scores"),
    path(
        "score-details/<int:pk>/", GameScoreDetailView.as_view(), name="score-details"
    ),
]
