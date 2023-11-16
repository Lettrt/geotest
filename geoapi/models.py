from django.db import models

class Query(models.Model):
    cadastre_number = models.CharField(max_length=255)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    # max_digits=9 - 3 цифры до точки для долготы (макс 3 цифры) и 6 цифр полсле точки
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Геоданные"
        verbose_name_plural = "Геоданные"
        ordering = ["-created_at"]

    def __str__(self):
        return f'{self.cadastre_number} создан {self.created_at}'

class QueryResult(models.Model):
    query = models.ForeignKey(Query, on_delete=models.CASCADE, related_name='results')
    result = models.BooleanField()
    processed_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Результат"
        verbose_name_plural = "Результаты"
        ordering = ["-processed_at"]

    def __str__(self):
        return f"{self.query.cadastre_number} - {'Успешно' if self.result else 'Ответ не получен'}"