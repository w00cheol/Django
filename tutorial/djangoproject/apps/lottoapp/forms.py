from django import forms
from .models import GuessNumbers

class PostForm(forms.ModelForm):
    class Meta:
        # 모델 명과 입력받을 데이터 필드 초기화
        model = GuessNumbers
        fields = ['name', 'text', 'num_lotto',]