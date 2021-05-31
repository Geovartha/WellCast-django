from django.urls import path

from las_viewer.views import (
    one_base_page,
    two_las_upload,
    threea_data_cleaning,
    threeb_preview_cleaned,
    four_model_output,
)

urlpatterns = [
    path("", one_base_page, name="base_page"),
    path("two", two_las_upload, name="upload_las"),
    path("threea", threea_data_cleaning, name="las_cleaning"),
    path("threeb", threeb_preview_cleaned, name="las_cleaned_preview"),
    path("four", four_model_output, name="model_output"),
]
