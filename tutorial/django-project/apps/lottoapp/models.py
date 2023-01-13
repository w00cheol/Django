from statistics import mode
from django.db import models

# Create your models here.
from django.utils import timezone
import random

# super class models의 하위클래스 Model 상속
class GuessNumbers(models.Model):
    # 데이터 정의
    name = models.CharField(max_length=24)
    lottos = models.CharField(max_length=255, default='[1,2,3,4,5,6]')
    text = models.CharField(max_length=255)
    num_lotto = models.IntegerField(default=5)
    update_date = models.DateTimeField()

    def __str__(self):
        return f'{self.name} - {self.text}\n{self.lottos}'

    # 메서드 정의
    def generate(self):
        nums = list(range(1, 46))
        self.lottos = ""

        for _ in range(self.num_lotto):
            random.shuffle(nums)
            guess = sorted(nums[:6])
            self.lottos += str(guess) + '\n'

        self.update_date = timezone.now()
        self.save()