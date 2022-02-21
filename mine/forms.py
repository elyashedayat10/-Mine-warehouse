from django import forms
from .models import Mine


class MineForm(forms.ModelForm):
    class Meta:
        model = Mine
        fields = (
            'name',
            'stone_type',
            'discovery_license_number',
            'date_of_issuance_of_the_discovery_license_number',
            'operating_license_number',
            'date_of_issuance_of_operating_license_number',
            'minimum_operating_tonnage',
            'government_law',
            'province',
            'city',
            'village',
            'image',
            'description',
            'address',
            'summary',
            'bold',
            'sub_bold'
        )
        labels = {
            'name': "نام معدن",
            'stone_type': "نو ع سنگ",
            'discovery_license_number': "شماره مجوز کشف",
            'date_of_issuance_of_the_discovery_license_number': "تاریخ صدور پروانه کشف",
            'operating_license_number': "شماره پروانه بهره برذاری",
            'date_of_issuance_of_operating_license_number': "تاریخ صدور پروانه عملیاتی",
            'minimum_operating_tonnage': "حداقل تناژ بهره برداری",
            'government_law': "حقوق دولتی(تومان/تن)",
            'province': "استان",
            'city': "شهرستان",
            'village': "روستا",
            'image': "تصویر",
            'description': "توضیحات",
            'address': "آدرس دقیق",
            'summary':"خلاصه",
            'bold':'متن بولد',
            'sub_bold':'متن پایین'
        }
