from django.urls import path

from QRCodes.views import QRCodeView


urlpatterns = [
    path('qr_codes', QRCodeView.as_view()),
]