"""
This class takes the corresponding PDF files and turns each page into an image for the OCR scan.
"""
import fitz
from PIL import Image, ImageOps
from src.abstractor.UserInput import UserInput
from logging import info
from src.abstractor.Config import Config

class PdfEditor():
    def __init__(self, pdf_path:str, usr:UserInput, config:Config):
        """
        Initializes the PdfEditor class.

        Args:
            pdf_path (str): The path to the PDF file.
            usr (UserInput): An instance of the UserInput class.
            config (Config): An instance of the Config class.
        """
        info("Initializing PdfEditor")
        self.user_input = usr.get_user_input()
        self.image_crop = config.get("pdf_image_crop")
        self.pdf_path = pdf_path
        self.pdf = fitz.open(pdf_path)
        self.pil_images = []

    def convert(self):
        """
        Converts each page of the PDF into an image.

        This method iterates over the specified range of pages and converts each page into an image.
        The images are stored in the `pil_images` list.
        """
        for page_num in range(self.user_input.get("start_index"), self.user_input.get("end_index")+1):
            try:
                page = self.pdf.load_page(page_num)
                pix = page.get_pixmap(dpi=self.image_crop.get("dpi"))
                img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
                self.pil_images.append(img)
            except:
                continue

    def crop_images(self):
        """
        Crops the images based on the specified threshold and margin.

        This method crops each image in the `pil_images` list based on the specified threshold and margin.
        The cropped images replace the original images in the list.
        """
        for index, pil_image in enumerate(self.pil_images):
            pil_image = pil_image.convert('L')
            pil_image = ImageOps.invert(pil_image)
            bbox = pil_image.convert('L').point(lambda x: 255 if x < self.image_crop.get("threshold") else 0).getbbox()
            # Expand the bounding box with the margin
            margin = self.image_crop.get("margin")
            bbox = (max(0, bbox[0] - margin),
                    max(0, bbox[1] - margin),
                    min(pil_image.width, bbox[2] + margin),
                    min(pil_image.height, bbox[3] + margin))
            trimmed_image = pil_image.crop(bbox)
            self.pil_images[index] = trimmed_image