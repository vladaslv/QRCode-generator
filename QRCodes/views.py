from io import BytesIO
from django.views.decorators.csrf import csrf_exempt
from django.http import FileResponse
from django.http import HttpResponseBadRequest
import zipfile

from django.views.generic import View

from QRCodes.forms import QRCodeForm
from QRCodes.utils import generate_qr_code, prepare_logo


class QRCodeView(View):
    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request) -> FileResponse:
        form = QRCodeForm(request.POST, request.FILES)
        if not form.is_valid():
            return HttpResponseBadRequest("Invalid request")
        prefix = form.cleaned_data.get('prefix', '')
        suffix = form.cleaned_data.get('suffix', '')
        num_zeros = int(form.cleaned_data.get('zeros', 0) or 0)
        amount = int(form.cleaned_data.get('amount', 1) or 1)
        logo = form.cleaned_data.get('logo')    
        if logo:
            logo = prepare_logo(logo)

        zip_buffer = BytesIO()

        with zipfile.ZipFile(zip_buffer, 'w') as zip_file:
            for i in range(int(amount)):
                identifier = prefix + str(i).zfill(int(num_zeros)+1) + suffix
                buffer = generate_qr_code(identifier, logo)
                zip_file.writestr(f'qr_code_{identifier}.png', buffer.read())

        zip_buffer.seek(0)
        response = FileResponse(zip_buffer, content_type='application/zip')
        response['Content-Disposition'] = 'attachment; filename="qr_codes.zip"'
        return response
