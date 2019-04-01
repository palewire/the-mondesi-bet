from django.db import models


class SeasonTotal(models.Model):
    """
    Mondesi's season totals from his Baseball Reference profile page.
    """
    datetime = models.DateTimeField(auto_now_add=True)
    json = models.TextField()

    class Meta:
        ordering = ("-datetime",)
        get_latest_by = "datetime"

    def __str__(self):
        return f"{self.datetime}"


class GameLog(models.Model):
    """
    Mondesi's daily game logs from his Baseball Reference profile page.
    """
    datetime = models.DateTimeField(auto_now_add=True)
    json = models.TextField()

    class Meta:
        ordering = ("-datetime",)
        get_latest_by = "datetime"

    def __str__(self):
        return f"{self.datetime}"


class Projection(models.Model):
    """
    Mondesi's projected season totals from FanGraphs.
    """
    datetime = models.DateTimeField(auto_now_add=True)
    json = models.TextField()

    class Meta:
        ordering = ("-datetime",)
        get_latest_by = "datetime"

    def __str__(self):
        return f"{self.datetime}"
