import qrcode
from PIL import Image
from io import BytesIO


def prepare_logo(file) -> Image:
    try:
        logo = Image.open(file)
    except (IOError, ValueError) as error:
        raise ValueError(f"Invalid image format: {error}")
    base_width = 100
    width_percent = (base_width / float(logo.size[0]))
    height_size = int((float(logo.size[1]) * float(width_percent)))
    logo = logo.resize((base_width, height_size), Image.ANTIALIAS)
    return logo


def generate_qr_code(identifier: str, logo: Image=None) -> BytesIO:
    qr = qrcode.QRCode(version=8, error_correction=qrcode.constants.ERROR_CORRECT_H)
    qr.add_data(identifier)
    qr.make(fit=True)
    img = qr.make_image(fill_color='Black', back_color='white').convert('RGB')
    
    if logo:
        pos = ((img.size[0] - logo.size[0]) // 2,
        (img.size[1] - logo.size[1]) // 2)
        img.paste(logo, pos)
    
    buffer = BytesIO()
    img.save(buffer, 'PNG')
    buffer.seek(0)
    return buffer