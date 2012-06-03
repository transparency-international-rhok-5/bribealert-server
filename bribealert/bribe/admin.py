from django.contrib import admin

from models import Bribe, NationalChapter

class BribeAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'chat_link',)
    exclude = ('country', 'secure_token')
    
    def queryset(self, request):
        qs = super(BribeAdmin, self).queryset(request)
        
        chapters = filter(lambda chapter: request.user in chapter.user_set.all(), NationalChapter.objects.all())
        return qs.filter(country__in=map(lambda chapter: chapter.country, chapters))

admin.site.register(Bribe, BribeAdmin)