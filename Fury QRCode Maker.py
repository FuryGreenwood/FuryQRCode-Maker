"Fury QRCode Maker | Script-App"

"IMPORTANTE | CAUTION"
"(ES) Si va a trabajar dentro del script, se recomienda *NO GUARDAR* los cambios realizados en el script o al menos guardar sus diferentes configuraciones por separado."
"(EN) If you're going to work inside the script, it's recommended *NOT TO SAVE* the changes made to the script or at least to save your different configurations separately."


import qrcode
from PIL import Image


from qrcode.image.styledpil import StyledPilImage

# Estilos de los cuadrados - Square Styles
from qrcode.image.styles.moduledrawers import SquareModuleDrawer
from qrcode.image.styles.moduledrawers import GappedSquareModuleDrawer
from qrcode.image.styles.moduledrawers import CircleModuleDrawer
from qrcode.image.styles.moduledrawers import RoundedModuleDrawer
from qrcode.image.styles.moduledrawers import VerticalBarsDrawer
from qrcode.image.styles.moduledrawers import HorizontalBarsDrawer

# Estilos de colores - Color Styles
from qrcode.image.styles.colormasks import SolidFillColorMask            # color_mask = SolidFillColorMask(back_color = (255, 255, 255), front_color = (0, 0, 0))
from qrcode.image.styles.colormasks import RadialGradiantColorMask       # color_mask = RadialGradiantColorMask(back_color=(255, 255, 255), center_color=(0, 0, 0), edge_color=(0, 0, 255))
from qrcode.image.styles.colormasks import SquareGradiantColorMask       # color_mask = SquareGradiantColorMask(back_color=(255, 255, 255), center_color=(0, 0, 0), edge_color=(0, 0, 255))
from qrcode.image.styles.colormasks import HorizontalGradiantColorMask   # color_mask = HorizontalGradiantColorMask(back_color=(255, 255, 255), left_color=(0, 0, 0), right_color=(0, 0, 255))
from qrcode.image.styles.colormasks import VerticalGradiantColorMask     # color_mask = VerticalGradiantColorMask(back_color=(255, 255, 255), top_color=(0, 0, 0), bottom_color=(0, 0, 255))

"(ES) Borrar el '#' si necesita estas funciones | (EN) Delete the '#' if you need these functions"

"Logo"
#Logo_link = input('Nombre/dirección exacta del logo | Exact name/address of the logo (.jpg recommended): ')
#logo = Image.open(Logo_link)
#basewidth = 100
# Adjust logo size
#percent = (basewidth/float(logo.size[0]))
#hsize = int((float(logo.size[1])*float(wpercent)))
#logo = logo.resize((basewidth, hsize), Image.ANTIALIAS)

"User-Input"
data_input = input ('URL - Text: ')
box_size_input = int (input ('Tamaño del código | Code size (2 > +): ')) 
border_input = int (input ('Borde | Edge(0 > +): '))

"Core"
qr = qrcode.QRCode(error_correction = qrcode.constants.ERROR_CORRECT_L, box_size=box_size_input, border=border_input)
qr.add_data (data_input)
qr.make(fit = True)
# module_drawer = "Any Square Style (NAME)" - SolidFillColorMask(back_color=(x, x, x), front_color=(x, x, x)
img = qr.make_image(image_factory = StyledPilImage, module_drawer = SquareModuleDrawer(), color_mask = SolidFillColorMask(back_color = (255, 255, 255), front_color = (0, 0, 0))).convert('RGB')

"Embeded a Logo"
#pos = ((img.size[0] - logo.size[0]) // 2, (img.size[1] - logo.size[1]) // 2)
#img.paste(logo, pos)

img.save('qr.png')

"Console"
print('QR Generated!')