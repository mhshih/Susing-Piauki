from django.contrib import admin
from django.db import models
from django.forms.widgets import CheckboxSelectMultiple, Textarea
from django.utils.timezone import now
from 標記.models import 語料表
from 標記.管理.ReadOnlyAdminFields import ReadOnlyAdminFields


class 標記表(語料表):

    def save(self, *args, **kwargs):
        self.標記時間 = now()
        super().save(*args, **kwargs)

    class Meta:
        proxy = True
        verbose_name = "標記表"
        verbose_name_plural = verbose_name


class 標記表管理(ReadOnlyAdminFields, admin.ModelAdmin):
    # change list
    list_display = [
        'id', '狀況',
        '漢字', '羅馬字', '詞性',
        '備註',
        '標記者', '標記時間',
    ]
    ordering = ['標記者', 'id', ]
    list_filter = ['語料狀況', ]
    search_fields = [
        'id', '漢字', '羅馬字', '詞性', '備註',
    ]
    list_per_page = 20

    # change view
    # venv/lib/python3.5/site-packages/django/contrib/admin/templates/admin/
#     change_list_template = 'admin/gi2_liau7_khoo3/語料表/custom_change_list.html'
#     change_form_template = 'admin/gi2_liau7_khoo3/語料表/custom_change_form.html'
#     readonly_fields = ('音檔', '頭一版資料',)
    fieldsets = (
        ('漢字', {
            'fields': ('漢字', '羅馬字', '詞性', '備註', ),
            'classes': ['wide']
        }),
        ('語料狀況', {
            'fields': ('語料狀況', ),
            'classes': ['wide']
        }),
    )

    # 文字欄位顯示從textarea改成input
    # 多對多欄位改用複選
    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={
            'rows': 2,
            'column': 40,
            'style': 'resize: none; min-width: 80%; overflow:hidden;'})},
        models.ManyToManyField: {'widget': CheckboxSelectMultiple},
    }

    def save_model(self, request, obj, form, change):
        # 儲存標記者
        obj.標記者 = request.user
        super(標記表管理, self).save_model(request, obj, form, change)

    def has_add_permission(self, request):
        # 薛：只能由程式上傳音檔和語料
        # 薛：任何人都不能從後台新增
        return True
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    class Media:
        css = {
            "all": ("css/admin_gi2_liau7_pio2.css", "css/moedictFont.css")
        }
