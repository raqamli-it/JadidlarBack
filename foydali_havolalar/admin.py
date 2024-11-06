from django.contrib import admin
from django.utils.html import format_html
from foydali_havolalar.models import Foydali_havolalar, Foydali_havolalarImage


class Foydali_havolalarImageInline(admin.TabularInline):
    model = Foydali_havolalarImage
    fields = ('image',)
    max_num = 10
    min_num = 1
    can_delete = False
    show_change_link = True
    show_add_button = True
    verbose_name = 'Rasm'
    verbose_name_plural = 'Rasmlar'
    list_display = ('image',)
    ordering = ('image',)
    extra = 0


@admin.register(Foydali_havolalar)
class Foydali_havolalarAdmin(admin.ModelAdmin):
    inlines = [Foydali_havolalarImageInline]
    list_display = ('title', 'display_admin_photo', 'display_images',)
    fields = ('title_uz', 'title_ru', 'title_en', 'link', 'logo_image',)
    list_display_links = ('title',)
    search_fields = ('title',)
    list_filter = ('title',)
    list_per_page = 25
    list_max_show_all = 100
    save_as = False
    save_as_continue = True
    save_on_top = False
    readonly_fields = ('display_admin_photo', 'display_images', )

    def display_admin_photo(self, obj):
        if obj.logo_image:
            return format_html('<img src="{0}" width="100" height="100" />'.format(obj.logo_image.url))
        return ''

    display_admin_photo.short_description = 'Rasm'
    display_admin_photo.allow_tags = True

    def display_images(self, obj):
        images = obj.foydali_havola_images.all()  # Adjust the related name accordingly
        return format_html(''.join('<img src="{0}" width="100" height="100" style="margin-right: 10px;" />'.format(img.image.url) for img in images))

    display_images.short_description = 'Rasmlar'
    display_images.allow_tags = True

